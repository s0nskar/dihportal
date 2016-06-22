from django.shortcuts import render
from django.http import HttpResponse

import csv

from .models import *

# For filling database of the csv
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
                mentor = row[10].strip().lower()
                mentor_department = row[11].strip().lower()

                stu = Student.objects.get_or_create(
                            name=name,
                            roll_no=roll_no,
                            department=department,
                            email=email,
                            contact=phone,
                            summer_course=summer_course
                        )
                if stu[1]:
                    project = Project.objects.get_or_create(title=project_name)

                    if project[1]:
                        mentor = Mentor.objects.get_or_create(name=mentor)
                        if mentor[1]:
                            mentor[0].department = mentor_department
                            mentor[0].save()
                        project[0].mentor = mentor[0]
                        project[0].start_date = date_start
                        project[0].end_date = date_end
                        project[0].save()
                    project[0].team.add(stu[0])
                print rownum
            rownum += 1
    return HttpResponse("Done")

def secondfill(request):
    with open('teamleader.csv') as f:
        reader = csv.reader(f)
        rownum = 0
        for row in reader:
            if rownum != 0:
                title = row[1].strip().lower()
                team_leader_roll = row[3]
                plan_first_second = row[14]
                plan_third_fourth = row[15]
                plan_fifth_sixth = row[16]
                plan_seventh_eight = row[17]
                plan_after_eight = row[18]

                try:
                    project = Project.objects.get(title=title)
                    project.plan_first_second = plan_first_second
                    project.plan_third_fourth = plan_third_fourth
                    project.plan_fifth_sixth = plan_fifth_sixth
                    project.plan_seventh_eight = plan_seventh_eight
                    project.plan_after_eight = plan_after_eight
                    project.save()
                    try:
                        team_leader = Student.objects.get(roll_no=team_leader_roll)
                        project.team_leader = team_leader
                        project.save()
                    except:
                        print roll_no
                except:
                    print title
            rownum += 1
        return HttpResponse("Done")



# Making evalution
def evaluation(request):
    context = {}
    p = Project.objects.all()
    context['projects'] = p

    return render(request, 'evaluation.html', context)

def projects(request):
    context = {}
    p = Project.objects.all()
    context['projects'] = p
    return render(request, 'projects.html', context)
