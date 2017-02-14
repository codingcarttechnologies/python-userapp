from django.shortcuts import render
import sys
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.template import Context
from models import SiteUser
import random
from datetime import datetime, date

#######################Home View##################################
def home(request):
	users_data = SiteUser.objects.all()
	ctx = RequestContext(request, {'users':users_data})   
	return render_to_response('home.html', 
						{
						}, context_instance=ctx)

#####################Crete User##################################
def createUser(request):
	if request.method=='POST':
		username=request.POST['username']
		birthday=request.POST['birthday']
		dob = checkdob(birthday)
		age = calculate_age(dob)
		if age>13:
			eligible = 'allowed'
		else:
			eligible = 'blocked'
		random_number=random.randint(0,100)
		if (random_number%3==0):
			bizz_fuzz ='Bizz'
		elif (random_number%5==0):
			bizz_fuzz ='Fuzz'
		elif (random_number%3==0) and (random_number%5==0):
			bizz_fuzz = 'Bizz_Fuzz'
		else:
			bizz_fuzz = random_number

		
		SiteUser.objects.create(username=username,birthday=birthday,eligible=eligible,random_number=random_number,bizz_fuzz=bizz_fuzz)
		return HttpResponseRedirect('/')
	else:
		ctx = RequestContext(request, {})  
		return render_to_response('create.html',{}, context_instance=ctx)

#########################Edit User###########################
def editUser(request):
	if request.method=='POST':
		userid = request.POST['userid']
		username=request.POST['username']
		birthday=request.POST['birthday']
		dob = checkdob(birthday)
		age = calculate_age(dob)
		if age>13:
			eligible = 'allowed'
		else:
			eligible = 'blocked'

		SiteUser.objects.filter(id=userid).update(username=username,birthday=birthday,eligible=eligible)
		return HttpResponseRedirect('/')

	else:
		userid = request.GET['userid']
		user = SiteUser.objects.get(id=userid)
		ctx = RequestContext(request, {'user_data':user})  
		return render_to_response('edit.html',{}, context_instance=ctx)

################################Delete User###########################
def deleteUser(request):
	userid = request.GET['userid']
	SiteUser.objects.filter(id=userid).delete()
	return HttpResponseRedirect('/')


################################View User###########################
def viewUser(request):
	userid = request.GET['userid']
	user=SiteUser.objects.get(id=userid)
	user_list=[]
	user_dict={'id':'','username':'','birthday':'','eligible':'','random_number':'','BizzFuzz':''}
	user_dict['id']=userid
	user_dict['username']=user.username
	user_dict['birthday']=user.birthday
	user_dict['eligible']= user.eligible
	user_dict['random_number']= user.random_number
	user_dict['BizzFuzz']= user.bizz_fuzz
	user_list.append(user_dict)
	request.session['user'] = user_list
	return HttpResponseRedirect('/user-info')

#######################View User###################################
def userInfo(request):
    user_data = request.session['user']
    ctx = RequestContext(request, {'user_data': user_data})   
    return render_to_response('view.html', 
                              {
                              }, context_instance=ctx)
#######################Function to check DOB##########################
def checkdob(date_text):
	try:
		return datetime.strptime(date_text,'%m/%d/%Y')
	except ValueError:
		raise ValueError("Incorrect data format")

######################Age Calcuation Function#########################
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


