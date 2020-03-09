from miscellaneous import get_csrf_token
import json


class Marks():

    base_url = "http://merlindiary.ru/teacher/students-in-lesson?id="

    def set_all(s, lesson_id):
        r1 = s.get(Marks.base_url + str(lesson_id))
        r2 = Marks.set_one(s, get_csrf_token(r1), lesson_id, 37, 1, "mark_homework", 3)
        return r2


    def set_one(s, csrf_token, lesson_id, student_id, index_of_student_to_edit, attribute_to_edit, mark):
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
                "lesson_id": lesson_id,
                "student_id": student_id
            }, separators=(",", ":")),
            "editableAttribute": attribute_to_edit,
            "StudentsInLesson[" + str(index_of_student_to_edit) + "][" + str(attribute_to_edit) + "]": mark
        }

        return s.post(Marks.base_url + str(lesson_id), data = data, headers = headers)
