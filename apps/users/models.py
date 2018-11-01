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
        if form['birth_date'] == "":
            errors.append('Date of birth must be selected')
        return errors

    def create_user(self, user_data):
        pw_hash = bcrypt.hashpw(user_data['password'].encode(), bcrypt.gensalt())

        user = self.create(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            user_name=user_data['user_name'],
            email=user_data['email'],
            pw_hash=pw_hash,
            birth_date=user_data['birth_date'],
            total_pokes=0
        )
        return user

    def login(self, form):
        user_list = self.filter(email=form['email'])
        if len(user_list) > 0:
            user = user_list[0]
            if bcrypt.checkpw(form['password'].encode(), user.pw_hash.encode()):
                return (True, user.id)
            else:
                return (False, "Incorrect Email and Password combination")
        else:
            return (False, "Incorrect Email and Password combination")

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw_hash = models.CharField(max_length=500)
    birth_date = models.DateField()
    total_pokes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()