from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
UpperCasePassword_REGEX=re.compile(r'^(?=.*?[A-Z])')
NumericValue_REGEX=re.compile(r'^(?=.*?[0-9])')

# Create your models here.

class UserManager(models.Manager):
    def validate(self, form):
        errors = []
        if len(form['first_name']) < 3:
            errors.append('First name must be at least three characters long')
        if len(form['last_name']) < 3:
            errors.append('Last name must be at least three characters long')
        try:
            self.get(user_name=form['user_name'])
            errors.append('Username already taken, please choose a different one!')
        except:
            pass
        if len(form['user_name']) < 3:
            errors.append('User name must be at least three characters long')
        if not EMAIL_REGEX.match(form['email']):
            errors.append('Email address must be valid') 
        try:
            self.get(email=form['email'])
            errors.append('Email address already in use, please choose a different one!')
        except:
            pass
        if len(form['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        if form['password'] != form['password_confirm']:
            errors.append('Password confirmation must match password')

        if len(form['birth_date'])<1:
            errors.append('Date of birth must be selected')
        return errors

    def create_user(self, user_data):
        pw_hash = bcrypt.hashpw(user_data['password'].encode(), bcrypt.gensalt()).decode()

        user = self.create(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            user_name=user_data['user_name'],
            email=user_data['email'],
            pw_hash=pw_hash,
            birth_date=user_data['birth_date'],
            total_pokes=0,
            description="I am ......"
        )
        return user

    def login(self, form):
        errors=[]
        try:
            User=self.get(email=form['email'])
        except:
            errors.append("invalid email or password")
            return (False,errors)
        
        if bcrypt.checkpw(form['password'].encode(),User.pw_hash.encode()):
            return (True,User.id)
        else:
            errors.append("invalid email or password")
            return (False,errors)

    def EditUser(self,form,user_id):
        error=[]
        
        # checking it the password is being updated......
        try:
            form["password"]
            passwordEdit=True
        except:
            passwordEdit=False

        if passwordEdit==True:
            
            #password validation
            if len(form["password"])>0 and len(form["confirmpassword"])>0:

                if len(form['password'])<8:
                    error.append("password is too short. Should be atleast 8 characters")
                if not UpperCasePassword_REGEX.match(form['password']) :
                    error.append("at least one uppercase letter")
                if not NumericValue_REGEX.match(form['password']) :
                    error.append("at least one number")
                # confirm password validation
                if form["confirmpassword"]!=form["password"]:
                    error.append("Password does not match")

                # if there is no errors in the password format, we can update it......
                if len(error)<1:
                    EditUser=User.objects.get(id=user_id)
                    hashPassword=bcrypt.hashpw(form['password'].encode(),bcrypt.gensalt())
                    EditUser.pw_hash=hashPassword
                    EditUser.save()
                    print("password updated")
                    
        else:
            # check if email already taken
            if self.get(id=user_id).email !=form["email"] :
                if len(form["email"])<0:
                    error.append("Email cannot be blank")
                if self.filter(email=form['email']):
                    error.append("Email already used")
                    return (False,error)
                if not EMAIL_REGEX.match(form['email']):
                    error.append("Invalid Email Address!")
            
            
            # first name validation
            if  len(form['first_name'])<0:
                error.append("first name cannot be blank")
            if form['first_name'].isalpha()==False:
                error.append("Only letters in the first name")
            if len(form['first_name'])<2:
                error.append("First name should be atleast 2 characters")
            

            # last name validation
            if len(form['last_name'])<0:
                error.append("last name cannot be blank")
            if len(form['last_name'])<3:
                error.append("Last name should be atleast 2 characters")
            if form['last_name'].isalpha()==False:
                error.append("Only letters in the last name")

            # user name validation
            if len(form['user_name'])<0:
                error.append("user name cannot be blank")
            if len(form['user_name'])<3:
                error.append("User name should be atleast 2 characters")
    

            # description validation
            if len(form['description'])<5:
                error.append("Come on that's too short!!")

        if error:
            return(error)
        else:
            user=User.objects.get(id=user_id)
            user.first_name=form['first_name']
            user.last_name=form['last_name']
            user.email=form['email']
            user.user_name=form['user_name']
            user.description=form['description']
            user.save()
            print("infomation saved")
            return(error)


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=500)
    birth_date = models.DateField()
    total_pokes = models.IntegerField()
    description=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()