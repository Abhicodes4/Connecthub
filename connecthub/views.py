from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post,Profile
from .forms import Postform
from .forms import Profileform

@login_required(login_url='/connecthub')

def home(request):
                p=Post.objects.all()
                a=User.objects.all()
                return render(request,'feed.html',{'posts':p,'usnames':a})  
def loginfn(request):
     if request.method == 'POST':
            u=request.POST['a']
            pa=request.POST['b']

            c=auth.authenticate(username=u,password=pa)

            if c:
                auth.login(request,c)
                return redirect('/')
            
            else:
                messages.error(request,"Sorry, your password was incorrect. Please double-check your password")
                return redirect('/connecthub/')
    
     else:
        return render(request,'connecthub.html')
     


def logoutfnhub(request):
        auth.logout(request)
        return redirect('/connecthub')
      

def signuppagefn(request):
        return render(request,'signup.html')

def signupfn(request):
    un=request.POST['uname']
    na=request.POST['fname']
    em=request.POST['email']
    pa1=request.POST['pass1']
    pa2=request.POST['pass2']


    if pa1==pa2 :
      
      if User.objects.filter(username=un).exists():
              
             messages.error(request,"Username taken")
             return redirect('/signup')
      
      elif User.objects.filter(email=em).exists():
              
              messages.error(request,"Email already in use")
              return redirect('/signup')
      
       
      else:
          
          User.objects.create_user(username=un,email=em,first_name=na,password=pa1)
          messages.success(request,"Account created succesfully")
          return redirect('/connecthub')
      
        
    else :
        return redirect('/signup')
    
def searchpagefn(request): 
    return render(request,'search.html') 

def searchfn(request):
    items=request.GET['l']
    profiles=User.objects.filter(username__icontains=items)
    return render(request,'search.html',{'pros':profiles})    



def createpostfn(request):

    if request.method=="POST":
         p=Postform(request.POST,request.FILES)
         if p.is_valid():
            pca=p.save(commit=False)
            pca.us=request.user
            pca.save()

            return redirect('/connecthub')
    else:     
        p=Postform()
        return render(request,'createpost.html',{'pof':p})
    
def addprofilefn(request):

    if request.method=="POST":
        pr=Profileform(request.POST,request.FILES)
        if pr.is_valid():
            pcb=pr.save(commit=False)
            pcb.user=request.user
            pcb.save()

            return redirect('/userview')

    else:     
        pr=Profileform()
        return render(request,'addprofile.html',{'prf':pr})    
    

def userviewfn(request):
    posts = Post.objects.filter(us=request.user)
    return render(request,'userview.html',{'posts':posts})


def editprofilefn(request): 
    if request.method=="POST":
         a=Profile.objects.get(user=request.user_id)

         if a.user==request.user:    

            p=Profileform(request.POST,request.FILES,instance=a)
            if p.is_valid():
                p.save()  

                return redirect('/userview')
         else:
              return HttpResponse("<h1>sorry</h1>")   

    else:
        a=Profile.objects.get(user=request.user)     
        p=Profileform(instance=a)
        return render(request,'editprofile.html',{'pe':p})
    
def editpostpgfn(request):
    psts=Post.objects.filter(us=request.user)
    return render(request,'editpost.html',{'posts':psts})

def editpostfn(request,pr_id): 
    if request.method=="POST":
         a=Post.objects.get(id=pr_id) 

         if a.us==request.user:    

            c=Postform(request.POST,request.FILES,instance=a)
            if c.is_valid():
                c.save()  

                return redirect('/userview')
         else:
              return HttpResponse("<h1>sorry</h1>")   

    else:
        a=Post.objects.get(id=pr_id)     
        c=Postform(instance=a)
        return render(request,'editformpost.html',{'cf':c})   
    


def dltpostfn(request,pr_id): 
     a=Post.objects.get(id=pr_id) 
     a.delete()
     return redirect('/connecthub')
    
@login_required(login_url='/connecthub')
def proviewfn(request,id):
    pro=Post.objects.filter(us=id)
    pro2=Profile.objects.get(user=id)
    return render(request,'proview.html',{'prof':pro,'prof1':pro2})