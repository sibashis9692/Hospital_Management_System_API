from django.contrib import admin
from django.urls import path,include
from Home_app.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("register/", userRegisterViews.as_view(), name="registerViews"),
    path("login/", loginViews.as_view(), name = "loginViews"),


    path("doctors/", allDoctorsViews.as_view(), name="allDoctorsViews"),
    path("doctor/<int:pk>/", one_doctorViews.as_view(), name="one_doctorViews"),


    path("patients/", allPatientsViews.as_view(), name="allPatientsViews"),
    path("patient/<int:pk>/", one_patientViews.as_view(), name="one_patientViews"),
    # path("department/", adding_departmentViews.as_view(), name="departmentViews")

    path("patientsRecords/", allPatientsRecordsViews.as_view(), name="allPatientsRecordsViews"),
    path("patientsRecords/<int:pk>/", One_PatientRecordsViews.as_view(), name="PatientRecordsViews"),

    path("departments/", departmentViews.as_view(), name="departments")
]
