from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import random

class TestUser():
    def __init__(self):
        self.username = 'userEx'
        self.location = ''
        self.perish = False

def dashboard(request):
    packages = []
    bins = ['A', 'B', 'C', 'D', 'Floor']

    for i in xrange(0, random.randint(5,10)):
        u = TestUser()
        u.username += str(i)
        u.location = bins[random.randint(0, (len(bins) - 1))]
        if random.randint(0,5) == 5:
            u.perish = True
        packages.append(u)

    payload = {'packages': packages}

    return render_to_response('desk/dashboard.html', payload, context_instance = RequestContext(request))