from django.contrib import admin
from django.forms import Textarea
from django.utils.html import format_html  # For escaping malicious HTML
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.shortcuts import render

from projects.models import *

def to_panel(modeladmin, request, queryset):
    if request.method == "POST":
        context = {}
        projects = []
        seleted = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        for project in seleted:
            projects.append(Project.objects.get(pk=project))
        panels = Panel.objects.all()
        context['projects'] = projects
        context['panels'] = panels
        return render(request, 'topanel.html', context)

class ProjectsInLine(admin.TabularInline):
    model = Project.team.through
    extra = 0

class PanelInLine(admin.TabularInline):
    model = Panel.projects.through
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    actions = [to_panel]
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                            attrs={'rows':3,
                                   'cols':80,
                            })
        }
    }
    readonly_fields = ('project_link',)
    search_fields = ('title',)
    list_display = ('title','get_panel', 'start_date', 'end_date')

    inlines = [
        ProjectsInLine,
        PanelInLine,
    ]
    exclude = ('team', )

    def project_link(self, obj):
        url = urlresolvers.reverse('project', args=(obj.id, ))
        return format_html('<a href={}>Project Link</a>'.format(url))

    def get_panel(self, obj):
        panels = obj.panel_set.all()
        if panels:
            return panels[0].name

    get_panel.short_description = 'Panel(s)'

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'department', 'contact',)
    search_fields = ('name', 'roll_no',)

    inlines = [
        ProjectsInLine,
    ]

class MentorAdmin(admin.ModelAdmin):
    readonly_fields = ('projects_list',)
    list_display = ('name', 'department', 'projects')

    def projects(self, obj):
        return format_html("<br>".join([k.title for k in obj.project_set.all()]))

    def projects_list(self, obj):
        projects = Project.objects.filter(mentor=obj)
        if projects.count() == 0:
            return '(None)'
        projects_links = []
        for project in projects:
            url = urlresolvers.reverse('admin:projects_project_change', args=(project.id, ))
            print url
            projects_links.append('<li><a href="{}">{}</a></li>'.format(url, unicode(project)))
        return format_html('<ol>{}</ol>'.format('<br>'.join(projects_links)))
    projects_list.short_description = 'Project(s)'

class PanelAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )
    exclude = ('projects', )
    inlines = [
        PanelInLine,
    ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Mentor, MentorAdmin)
admin.site.register(Panel, PanelAdmin)
