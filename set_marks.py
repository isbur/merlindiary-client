from login import Merlin
from miscellaneous import beautify, get_csrf_token
from constants import names_shortcuts

from fuzzysearch import find_near_matches
from fuzzywuzzy import process
import json
import re


class Marks(Merlin):
    '''Set marks for _one_ lesson    '''

    base_url = "http://merlindiary.ru/teacher/students-in-lesson?id="
    keywords = (
        "mark_work_at_lesson",
        "mark_homework",
        "mark_dictation"
    )

    lesson_id = -1
    lesson_soup = ""
    lesson_RR_object = {}
    marks_dict = {}
    students_data = []

    
    def __init__(self, lesson_id):
        Merlin.__init__(self)
        self.login()
        self.lesson_id = lesson_id
        self.lesson_RR_object = self.s.get(Marks.base_url + str(self.lesson_id))
        self.lesson_soup = beautify(self.lesson_RR_object)
        self.get_students_from_page()
        self.get_marks()


    def get_marks(self):
        input_file = open("marks.input", "r")
        S = input_file.readlines()
        input_file.close()
        D = {}
        for string in S:
            L = string.split()
            D[L[0]] = list(map(int, L[1:]))
        self.marks_dict = D


    def get_students_from_page(self):
        html_rows = self.lesson_soup.find_all(name="tr", attrs={"data-key":re.compile(".+")})
        D = []
        for i, row in enumerate(html_rows):
            student = {}
            student['index'] = i
            student['student_id'] = json.loads(
                row["data-key"]
            )['student_id']
            cell = row.find(attrs={"data-col-seq":"1"})
            student['name'] = cell.string
            D.append(student)
        self.students_data = D


    def get_student_by_name(self, name):
        #print(name)
        choices = [student['name'] for student in self.students_data]
        #print(choices)
        res = process.extractOne(name, choices)
        #print(res)
        # Кажется, для библиотеки fuzzywuzzy условие на длину результата бессмысленно - оно всегда что-нибудь да найдёт
        if len(res) == 0 or res[1] < 90:
            #print("Deeper...")
            key = process.extractOne(name, names_shortcuts.keys())[0]
            another_name = names_shortcuts[key]
            res = process.extractOne(another_name, choices)
            if len(res) == 0 or res[1] < 90:
                raise Exception("name \"" + name + "\" was not found.")
        return [student for student in self.students_data if student['name'] == res[0]][0]


    def set_all(self):
        print(self.marks_dict)
        for name, marks in self.marks_dict.items():
            print(name, marks)
            student = self.get_student_by_name(name)
            for i, mark in enumerate(marks):
                csrf_token = get_csrf_token(self.lesson_RR_object)
                self.set_one(
                    csrf_token, 
                    student['student_id'], 
                    student['index'], 
                    Marks.keywords[i], 
                    mark
                )



    def set_one(self, csrf_token, student_id, index_of_student_to_edit, attribute_to_edit, mark):
        """
        :param attribute_to_edit(str): mark_homework, mark_lesson(?) ot mark_test(?)
        """
        headers = {
            "X_CSRF_TOKEN": csrf_token
        }
        data = {
            "_csrf": csrf_token,
            "hasEditable": 1,
            "editableIndex": index_of_student_to_edit,
            "editableKey": json.dumps({
                "lesson_id": self.lesson_id,
                "student_id": student_id
            }, separators=(",", ":")),
            "editableAttribute": attribute_to_edit,
            "StudentsInLesson[" + str(index_of_student_to_edit) + "][" + str(attribute_to_edit) + "]": mark
        }

        return self.s.post(Marks.base_url + str(self.lesson_id), data = data, headers = headers)
