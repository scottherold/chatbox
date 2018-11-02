from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

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