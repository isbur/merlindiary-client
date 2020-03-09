# from get_last_lessons import get_last_lessons
from login import login
from miscellaneous import beautify
from miscellaneous import sprint
from miscellaneous import get_properties
from set_marks import Marks

import json
# import re
import requests
from urllib.parse import unquote

s = requests.Session()
login(s)
r = Marks.set_all(s, 1155)
soup = beautify(r)
# sprint(r.request)

a = json.dumps({
    "lesson_id": 1155,
    "student_id": 37
}, separators=(",", ":"))

s2 = unquote(r.request.body)

s1 = "_csrf=56AktvpDvKmMdGPfD-aWfuesvTPG5kXZWHjuZpuibuLe92P_sBvp6LoxNLxAj8wd0Pv0Aa-QFrwUJ7RQ6u8rsg%3D%3D&hasEditable=1&editableIndex=1&editableKey=%7B%22lesson_id%22%3A1155%2C%22student_id%22%3A37%7D&editableAttribute=mark_homework&StudentsInLesson%5B1%5D%5Bmark_homework%5D=4"
s1 = unquote(s1)


import difflib
d = difflib.Differ()
diff = d.compare(s1, s2)
print("".join(diff))