from django.test import TestCase
from communitymanager.models import *
from django.contrib.auth.models import User

# Create your tests here.

user1 = User(username='bb', password='toto')
user1.first_name = 'barbie'
user1.last_name = 'chaite'
print(user1)

