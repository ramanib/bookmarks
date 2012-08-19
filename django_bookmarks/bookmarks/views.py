# Create your views here.

from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from bookmarks.forms import *
#from django.core.urlresolvers import reverse
#from django.contrib.auth.decorators import login_required



def main_page(request):
    return render_to_response('main_page.html',RequestContext(request))
 
 
#def user_page(request, username):
#    try:
#        user = User.objects.get(username=username)
#    except:
#        raise Http404('Requested user not found.')
#    bookmarks = user.bookmark_set.all()
#    template = get_template('user_page.html')
#    variables = Context({'username': username,'bookmarks': bookmarks})
#    output = template.render(variables)
#    return HttpResponse(output)


#@login_required
def user_page(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        raise Http404('Requested user not found.')
    bookmarks = user.bookmark_set.all()
    c = RequestContext(request, {'username': username,'bookmarks': bookmarks})
    return render_to_response('user_page.html', c )
    #return HttpResponseRedirect(reverse(user_page.html,args=[request.user.username]))
  
    
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.clean_data['username'],password=form.clean_data['password1'],email=form.clean_data['email'])
        return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
        variables = RequestContext(request, {'form': form})
        return render_to_response('registration/register.html', variables)


