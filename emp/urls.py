from django.urls import path

from emp.views import *

urlpatterns = [
    path('home/', emp_home),
    path('add-emp/', add_emp),
    path('emp-delete/<int:emp_id>',emp_delete),
    path('emp-update/<int:emp_id>',emp_update),
    path('do-update/<int:emp_id>',do_emp_update),

]
