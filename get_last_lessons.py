from miscellaneous import beautify
import re

#
# @param s - requests Session() object
#
def get_last_lessons(s):
    r = s.get("http://merlindiary.ru/teacher/lessons/index?sort=-datetime")
    soup = beautify(r)
    tables = soup.find_all(attrs={"data-key":re.compile("\d+")})
    dates = [table.find_all('td')[1].string for table in tables]
    return dates