from django.http import HttpResponse
#from django.http.response import HttpResponse
from django.shortcuts import render , redirect
from .models import Contact,User,Product

def index(request):
	try:
		user=User.objects.get(email=request.session['email'])
		return render(request,'index.html',{'user':user})
	except:
		return render(request,'index.html')
def contact(request):
	if request.method=="POST":
		Contact.objects.create(
			fname=request.POST['fname'],
			lname=request.POST['lname'],
			mobile=request.POST['mobile'],
			email=request.POST['email'],
			address=request.POST['address'],
			message=request.POST['message']
			)
		msg='Your Massage Has Been Send And Save Successfully'
		return render(request,'contact.html',{'msg':msg})
	else:
		return render(request,'contact.html')


def sign_up(request):
	if request.method=='POST':
		try:
			user=User.objects.get(email=request.POST['email'])
			msg='Your Email Id Is All Ready Registered, Please Login'
			return render(request, 'sign-up.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					name=request.POST['name'],
					mobile=request.POST['mobile'],
					email=request.POST['email'],
					password=request.POST['password'],
					address=request.POST['address'],
					profile_picture=request.POST['profile_picture']
					)
				msg='Your Data Has Been Save Successfully Now You Are Login'
				return render(request, 'sign-up.html',{'msg':msg})
			else:
				alert = True
				msg='Your Conform Password And Password Dose Not Match Please Try Again'
				return render(request, 'sign-up.html',{'msg':msg,"alert":alert})
	else:
		return render(request, 'sign-up.html')

def login(request):
	if request.method=='POST':
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['name']=user.name
				request.session['profile_picture']=user.profile_picture.url
				contact=Contact.objects.all()
				return render(request,'index.html',{'user':user})
			else:
				alert = True
				msg= 'Wrong Password Please Try Again'
				return render(request,'login.html',{'msg':msg,"alert":alert})
		except:
			alert = True
			msg='Your Email Id Not Registered'
			return render(request,'sign-up.html',{'msg':msg,"alert":alert})
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['name']
		del request.session['profile_picture']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def change_password(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		if user.password==request.POST['oldpassword']:
			if request.POST['npassword']==request.POST['cnpassword']:
				user.password = request.POST['npassword']
				user.save()
				msg='Your Password Change Successfully'
				del request.session['email']
				del request.session['name']
				del request.session['profile_picture']
				return render(request,'login.html',{'msg':msg})
			else:
				msg=msg='Your NewPassword And Conform New Password Not Same Please Try Again'
				return render(request,'change_password.html',{'msg':msg})
		else:
				msg=msg='Your OldPassword Not Correct, Please Try Again'
				return render(request,'change_password.html',{'msg':msg})
	else:
		return render(request,'change_password.html')

def profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=='POST':
		user.name=request.POST['name']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		try:
			user.profile_picture=request.FILES['profile_picture']
		except Exception as e:
			print(e)
			pass
		user.save()
		msg='Your Password Change Successfully'
		return render(request,'profile.html',{'msg':msg ,'user':user})

	else:
		return render(request,'profile.html',{'user':user})


def add_product(request):
	if request.method=='POST':
		Product.objects.create(
			proname=request.POST['proname'],
			protype=request.POST['protype'],
			qty=request.POST['qty'],
			price=request.POST['price'],
			prodetail=request.POST['prodetail'],
			pro_picture=request.POST['pro_picture']
			)
		msg='Your Product Has Been Save Successfully'
		return render(request,'add_product.html',{'msg':msg})
	else:
		return render(request,'add_product.html')

def show_product(request):
	products=Product.objects.all()
	return render(request,'show_product.html',{'products':products})

def edit_product(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.proname = request.POST['proname']
        product.protype = request.POST['protype']
        product.price = request.POST['price']
        product.save()
        msg = "Product updated successfully"
        return render(request, 'edit_product.html', {'product': product, 'msg': msg})
    else:
        return render(request, 'edit_product.html', {'product': product})

def delete(request,pk):
	product=Product.objects.get(pk=pk)
	product.delete()
	return redirect(request,'show_product')
	
def back(request):
	return redirect(request,'show_product')

def customer(request):
	contact=Contact.objects.all()
	return render(request,'customer.html',{'contact':contact})
def quot(request,pk):
	contact = Contact.objects.get(pk=pk)
	products=Product.objects.all()
	if request.method=='post':
		return render(request, 'quotation.html', {'contact': contact,'products':products})
	else:
		return render(request, 'quotation.html', {'contact': contact,'products':products})
