from django.shortcuts import render
from Home_app.serializers import *
from Home_app.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import *
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Register views
class userRegisterViews(APIView):
    serializer_class = userRegisterSerializers

    def post(self, request):
        serializer = userRegisterSerializers(data = request.data)
        if(serializer.is_valid(raise_exception=True)):
            serializer.save()

            return Response({"Status": f"A new {serializer.data['Role']} Creat Sucessfully"}, status.HTTP_201_CREATED)


# Login views
class loginViews(APIView):
    serializer_class = loginSerilaizers
    
    def post(self, request):
        serilaizer = loginSerilaizers(data = request.data)
        if(serilaizer.is_valid(raise_exception=True)):
            user = User.objects.filter(username = serilaizer.data.get("username"), email = serilaizer.data.get("email"), password = serilaizer.data.get("password")).first()
            if(user is not None):
                token = get_tokens_for_user(user)
                return Response({"Status":f"{user.Role} Sucessfully Login", "Token" : token})
            else:
                return Response({"Error": "User password or Email or Username is not correct"})


# Getting all Doctors data
class allDoctorsViews(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = userRegisterSerializers

    def get(self, request):
        if(request.user.Role == "Doctor"):
            doctors = User.objects.filter(Role = "Doctor").all()
            serilaizer = Patient_or_doctorsSerilaizers(doctors, many=True)
            return Response({"Meg": serilaizer.data})
        else:
            return Response({"Warnning": "AccessDenied"})

    def post(self, request):
        if(request.user.Role == "Doctor"):
            serializer = userRegisterSerializers(data = request.data)
            if(serializer.is_valid(raise_exception=True)):
                user = serializer.save()
                token = get_tokens_for_user(user)
                return Response({"Status": f"A new {serializer.data['Role']} Creat Sucessfully", "Token": token}, status.HTTP_201_CREATED)
        else:
            return Response({"Warnning": "AccessDenied"})


# Getting One doctor views
class one_doctorViews(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = updatePatient_or_DoctorSerilaizers
    
    def get(self, request, pk):
        if(request.user.Role == "Doctor"):
            if(request.user.id == pk):
                serilaizer = Patient_or_doctorsSerilaizers(request.user)
                return Response({"Meg": serilaizer.data})
        return Response({"Warnning": "AccessDenied"})

    def put(self, request, pk):
        if(request.user.Role == "Doctor"):
            if(request.user.id == pk):
                doctor = User.objects.filter(id = pk).first()
                serializer = updatePatient_or_DoctorSerilaizers(doctor, data = request.data, partial=True)
                if(serializer.is_valid(raise_exception=True)):
                    user = serializer.save()
                    token = get_tokens_for_user(user)
                    return Response({"Status": f"{serializer.data['Role']} Update Sucessfully", "New_Token": token}, status.HTTP_201_CREATED)
        return Response({"Warnning": "AccessDenied"})


# Getting all Patients data
class allPatientsViews(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = userRegisterSerializers

    def get(self, request):
        if(request.user.Role == "Doctor"):
            patients = User.objects.filter(Role = "Patient").all()
            serilaizer = Patient_or_doctorsSerilaizers(patients, many=True)
            return Response({"Meg": serilaizer.data})
        else:
            return Response({"Warnning": "AccessDenied"})


    def post(self, request):
        if(request.user.Role == "Doctor"):
            serializer = userRegisterSerializers(data = request.data)
            if(serializer.is_valid(raise_exception=True)):
                user = serializer.save()
                token = get_tokens_for_user(user)
                return Response({"Status": f"A new {serializer.data['Role']} Creat Sucessfully", "Token": token}, status.HTTP_201_CREATED)
        else:
            return Response({"Warnning": "AccessDenied"})


# Getting One doctor views
class one_patientViews(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = updatePatient_or_DoctorSerilaizers

    def get(self, request, pk):
        if(request.user.Role == "Doctor"):
            patient = User.objects.filter(id = pk, Role = "Patient", Department_name = request.user.Department_name).first()
            if(patient):
                serilaizer = Patient_or_doctorsSerilaizers(patient)
                return Response({"Meg": serilaizer.data})
            else:
                return Response({"Error" : f"No Patients in your Department on Id {pk}"})

        elif(request.user.Role == "Patient"):
            if(request.user.id == pk):
                serilaizer = Patient_or_doctorsSerilaizers(request.user)
                return Response({"Meg": serilaizer.data})
            
        return Response({"Warnning": "AccessDenied"})

    def put(self, request, pk):
        if(request.user.Role == "Doctor"):
            patient_department = User.objects.filter(id = pk).first().Department_name
            if(request.user.Department_name == patient_department):
                patient = User.objects.filter(id = pk).first()
                serializer = updatePatient_or_DoctorSerilaizers(patient, data = request.data, partial=True)
                if(serializer.is_valid(raise_exception=True)):
                    user = serializer.save()
                    token = get_tokens_for_user(user)
                    return Response({"Status": f"{serializer.data['Role']} Update Sucessfully", "Token": token}, status.HTTP_201_CREATED)

        elif(request.user.Role == "Patient"):
            if(request.user.id == pk):
                patient = User.objects.filter(id = pk).first()
                serializer = updatePatient_or_DoctorSerilaizers(patient, data = request.data, partial=True)
                if(serializer.is_valid(raise_exception=True)):
                    user = serializer.save()
                    token = get_tokens_for_user(user)
                    return Response({"Status": f"{serializer.data['Role']} Update Sucessfully", "Token": token}, status.HTTP_201_CREATED)
        return Response({"Warnning": "AccessDenied"})



# Getting Patients Records
class allPatientsRecordsViews(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request):
        if(request.user.Role == "Doctor"):
            patient_records = Patient_Records.objects.filter(Patient_name__Department_name = request.user.Department_name).all()
            if(patient_records):
                serilaizer = patinets_recordsSerilaizers(patient_records, many=True)
                return Response({"Meg": serilaizer.data})
            else:
                return Response({"Error" : f"No Patients in your Department"})
            
    serializer_class = patinetRecordsInsertSerilaizers

    def post(self, request):
        if(request.user.Role == "Doctor"):
            if(request.user.Department_name == User.objects.filter(id = request.data["Patient_name"]).first().Department_name):
                serialize = patinetRecordsInsertSerilaizers(data = request.data)
                if(serialize.is_valid(raise_exception=True)):
                    serialize.save()
                    return Response({"Mes" : "Patients Record sucessfully saved"})

        return Response({"Mes" : "AcessDenied"})



class One_PatientRecordsViews(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = update_Patient_record_Serilaizers

    def get(self, request, pk):
        if(request.user.Role == "Doctor"):
            patient = User.objects.filter(id = pk, Role = "Patient", Department_name = request.user.Department_name)
            if(patient):
                patient_record = Patient_Records.objects.filter(Patient_name__id = pk).first()
                serilaizer = patinets_recordsSerilaizers(patient_record)
                return Response({"Mes" : serilaizer.data})
        elif(request.user.Role == "Patient"):
            if(request.user.id == pk):
                patient_record = Patient_Records.objects.filter(Patient_name__id = pk).first()
                serilaizer = patinets_recordsSerilaizers(patient_record)
                return Response({"Mes" : serilaizer.data})
            
        return Response({"Error" : "AcessDenied"})

    def put(self, request, pk):
        if(request.user.Role == "Doctor"):
            patient = User.objects.filter(id = pk, Role = "Patient", Department_name = request.user.Department_name)
            if(patient):
                patient_record = Patient_Records.objects.filter(Patient_name__id = pk).first()
                serilaizer = update_Patient_record_Serilaizers(patient_record, data = request.data)
                if(serilaizer.is_valid()):
                    user = serilaizer.save()
                    token = get_tokens_for_user(user)
                    return Response({"Status": "Patient Record Update Sucessfully", "Token": token}, status.HTTP_201_CREATED)
        elif(request.user.Role == "Patient"):
            if(request.user.id == pk):
                patient_record = Patient_Records.objects.filter(Patient_name__id = pk).first()
                serilaizer = update_Patient_record_Serilaizers(patient_record, data = request.data)
                if(serilaizer.is_valid()):
                    user = serilaizer.save()
                    token = get_tokens_for_user(user)
                    return Response({"Status": "Patient Record Update Sucessfully", "Token": token}, status.HTTP_201_CREATED)
        return Response({"Error" : "AcessDenied"})


class departmentViews(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = departmentsSerializer

    def get(self, request):
        departments = Departments.object.all()
        serializer = departmentsSerializer(departments, many = True)
        return Response({"Mes" : serializer.data})

    def post(self, request):
        if(request.user.Role == "Doctor"):
            serializer = departmentsSerializer(data = request.data)
            if(serializer.is_valid(raise_exception=True)):
                serializer.save()
                return Response({"Mes" : "Sucessfully Added New Departments"})
        else:
            return Response({"Mes" : "AcessDenied"})





# # Department views
# class adding_departmentViews(APIView):
#     serializer_class = departmentsSerializers
    
#     def post(self, request):
#         serilaizer = departmentsSerializers(data = request.data)
#         if(serilaizer.is_valid(raise_exception=True)):
#             serilaizer.save()
#             return Response({"Status":"Congratulation"})
#         else:
#             return Response({"Status":"Error"})
