#
# Author: Team 10
# Course: CIS*3760
# Date: 7 Feb 2022
# Description: a library to search for courses that match a description
#

import json

courses = []

code = ""
year = ""
weight = ""
semester = ""

# search_course, looks for courses that match a certain criteria
# given course_code, course_year, course_weight, course_semester
# returns -1 (error), 0 (no results), list (of courses)
def search_course(args_list):
    open_courses()
    
    # case where the only argument is the program name
    if len(args_list) < 4 or len(args_list) > 4:
        return -1
    else:
        global code, year, weight, semester
        code = args_list[0].lower()
        year = args_list[1].lower()
        weight = args_list[2].lower()
        semester = args_list[3].lower()

        # Filtering course list
        filtered_courses = courses
        # code
        if code != "x":
            filtered_courses = filter_code(check_code, filtered_courses)
        # Year
        if year != "x":
            filtered_courses = filter_year(check_year, filtered_courses)
        
        # Weight
        if weight != "x":
            filtered_courses = filter_weight(check_weight, filtered_courses)
        
        # Semester
        if semester != "x":
            filtered_courses = filter_semester(check_semester, filtered_courses)

        if not filtered_courses:
            # no courses matching the description found
            return None
        else:
            # return matching courses
            filtered_courses = sorted(filtered_courses, key=lambda x : x['cc'])
            return filtered_courses


# checks if a course matches the described course code
def check_code(course):    
    if code.lower() in course['cc'].lower():
        return True
    else:
        return False

# checks if a course matches the described course year
def check_year(course):
    course_year = (course['cc'].split("*", 1)[1])
    
    if year == course_year[0]:
        return True
    else:
        return False

# checks if a course matches the described course weight
def check_weight(course):
    if weight in course['cred']:
        return True
    else:
        return False

# checks if a course matches the described course semester
def check_semester(course):
    sem = semester.lower()
    
    #  if in USER REQUEST and COURSE
    if ("winter" in sem or "w" in sem) and ("Winter" in course['off']):
        return True
    elif ("summer" in sem or "s" in sem) and ("Summer" in course['off']):
        return True
    elif ("fall" in sem or "f" in sem) and ("Fall" in course['off']):
        return True
    else:
        return False
    
    
# filters out courses that don't match a certain course code
def filter_code(check_code, filtered_courses):
    courses_iterator = filter(check_code, filtered_courses)
    filtered_courses = list(courses_iterator)
    return filtered_courses

# filters out courses that don't match a certain course year
def filter_year(check_year, filtered_courses):
    courses_iterator = filter(check_year, filtered_courses)
    filtered_courses = list(courses_iterator)
    return filtered_courses

# filters out courses that don't match a certain course weight
def filter_weight(check_weight, filtered_courses):
    courses_iterator = filter(check_weight, filtered_courses)
    filtered_courses = list(courses_iterator)
    return filtered_courses

# filters out courses that don't match a certain course semester
def filter_semester(check_semester, filtered_courses):
    courses_iterator = filter(check_semester, filtered_courses)
    filtered_courses = list(courses_iterator)
    return filtered_courses


# This function opens the courses.json file and takes its contents
def open_courses():
    global courses
    courses = []
    
    with open("courses.json", "r") as file:
        json_data = json.load(file)

    for i in json_data:
        courses.append(i)