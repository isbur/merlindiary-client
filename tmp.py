# from get_last_lessons import get_last_lessons
from miscellaneous import beautify
from miscellaneous import sprint
from miscellaneous import get_properties
from set_marks import Marks

#import json
## import re
#import requests
#from urllib.parse import unquote

M = Marks(1155)
M.login()
r = M.set_all()
soup = beautify(r)
# sprint(r.request)

