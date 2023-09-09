from rest_framework import serializers
from Home_app.models import *
from rest_framework import status

# Register serilaizers
class userRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'Role', 'Department_name', 'password']
        extra_kwargs = (
            {
                'first_name' : {'required': True},
                'last_name' : {'required': True},
                'email' : {'required': True},
                'Role' : {'required': True},
                'Department_name' : {'required' : True},
                'password' : {'required' : True}
            }
        )

    def create(self, validated_data):
        data = User.objects.create_user(**validated_data)
        return data

# Login serilaizer
class loginSerilaizers(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        extra_kwargs = (
            {
                "password" : {"required": True}
            }
        )

    
    def validate(self, data):
        data = User.objects.filter(email = data["email"]).first()
        if(not data):
            raise serializers.ValidationError({"Error": "User is Not Found"},status.HTTP_400_BAD_REQUEST)
        return data
    

class Patient_or_doctorsSerilaizers(serializers.ModelSerializer):
    Department_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'Department_name']
        extra_kwargs = (
            {
                'first_name' : {'required': True},
                'last_name' : {'required': True},
                'email' : {'required': True},
                'Role' : {'required': True},
                'Department_name' : {'required' : True},
                'password' : {'required' : True}
            }
        )
    def get_Department_name(self, user):
        return user.Department_name.Name  


class updatePatient_or_DoctorSerilaizers(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'Role', 'Department_name', 'password']

    def update(self, instance, validated_data):
        # Update instance fields with the provided data
        for field_name, field_value in validated_data.items():
            setattr(instance, field_name, field_value)

        print(validated_data)
        instance.set_password(validated_data["password"])
        # Save the changes to the instance
        instance.save()

        # Return the updated instance
        return instance


class patinets_recordsSerilaizers(serializers.ModelSerializer):
    Patient_name = serializers.SerializerMethodField()

    class Meta:
        model = Patient_Records
        fields= ['Patient_name', 'Diagnostics', 'Observations', 'Treatments']

    def get_Patient_name(self, user):
        return user.Patient_name.username 

    
class patinetRecordsInsertSerilaizers(serializers.ModelSerializer):
    # Patient_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Patient_Records
        fields = ['Patient_name', 'Created_date', 'Diagnostics', 'Observations', 'Treatments']
        
        extra_kwargs=(
            {
                'Patient_name' : {'required' : True}
            }
        )
    def create_user(self, validated_data):
        data = Patient_Records.objects.create_user(**validated_data)
        return data
    
    # def get_Patient_name(self, user):
    #     return user.Patient_name.username 


class update_Patient_record_Serilaizers(serializers.ModelSerializer):

    class Meta:
        model = Patient_Records
        fields = ['Diagnostics', 'Observations', 'Treatments']

    def update(self, instance, validated_data):
        # Update instance fields with the provided data
        for field_name, field_value in validated_data.items():
            setattr(instance, field_name, field_value)
        # Save the changes to the instance
        instance.save()

        # Return the updated instance
        return instance
    

    # class departmentsSerializers(serializers.ModelSerializer):


class departmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = "__all__"