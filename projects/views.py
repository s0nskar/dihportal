from django.shortcuts import render
from django.http import HttpResponse

import csv

from .models import *

def fill(request):
    with open('projects.csv') as f:
        print "Read"
        reader = csv.reader(f)
        rownum = 0
        for row in reader:
            if rownum != 0:
                project_name = row[1].strip().lower()
                date_start = row[7].strip()
                date_end = row[8].strip()
                name = row[2].strip()
                roll_no = row[3].strip()
                department = row[4].strip()
                email = row[5].strip()
                phone = row[6].strip()
                summer_course = row[9].strip()
                mentor = row[10].strip()
                mentor_department = row[11].strip()

                stu = Student.objects.create(name=name, roll_no=roll_no, department=department, email=email, contact=phone, summer_course=summer_course, mentor=mentor, mentor_department=mentor_department)
                project = Project.objects.get_or_create(title=project_name)
                project[0].start_date = date_start
                project[0].end_date = date_end
                project[0].save()
                project[0].team.add(stu)
                print rownum
            rownum += 1
    return HttpResponse("Done")
