from login import Merlin
from miscellaneous import beautify, get_csrf_token
import json


class Marks(Merlin):
    '''Set marks for _one_ lesson    '''

    base_url = "http://merlindiary.ru/teacher/students-in-lesson?id="
    lesson_id = -1

    
    def __init__(self, lesson_id):
        Merlin.__init__(self)
        self.lesson_id = lesson_id


    def get_students(r):
        soup = beautify(r)
        return soup


    def set_all(self):
        r1 = self.s.get(Marks.base_url + str(self.lesson_id))
        r2 = self.set_one(get_csrf_token(r1), 37, 1, "mark_homework", -1)
        return r2


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
