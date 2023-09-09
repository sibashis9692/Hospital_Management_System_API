from django.contrib.auth.models import BaseUserManager

class userManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password = None, **extra_fields):
        if(not email):
            return ValueError("Email is Required")
        
        email = self.normalize_email(email)

        user = self.model(username = username, email = email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)

        return user
    
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_admin', False)

        if(extra_fields.get('is_staff') is None):
            raise ValueError("Superuser must be staff")
        
        if(extra_fields.get('is_admin') is None):
            raise ValueError("Superuser must be admin")
        
        return self.create_user(username, email, password, **extra_fields)