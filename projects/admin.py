from django.contrib import admin
from django.forms import Textarea
from django.utils.html import format_html  # For escaping malicious HTML
from django.core import urlresolvers

from projects.models import *

class ProjectsInLine(admin.TabularInline):
    model = Project.team.through
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(
                            attrs={'rows':3,
                                   'cols':80,
                            })
        }
    }
    readonly_fields = ('project_link',)
    search_fields = ('title',)
    list_display = ('title', 'start_date', 'end_date')

    inlines = [
        ProjectsInLine,
    ]
    exclude = ('team', )

    def project_link(self, obj):
        url = urlresolvers.reverse('project', args=(obj.id, ))
        return format_html('<a href={}>Project Link</a>'.format(url))

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

admin.site.register(Project, ProjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Mentor, MentorAdmin)
