from django.shortcuts import render,get_object_or_404
from django import forms
from django.http import HttpResponseRedirect
from .models import Post, Choice,SignUp
from django.utils import timezone
from .forms import PostForm,SignForm,MyRegistrationForm
from django.shortcuts import redirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Cars/post_list.html', {'posts':posts})

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    try:
        choice = Choice.objects.get(title=post)
    except:
        choice = Choice.objects.create(title=post)
    return render(request, 'Cars/post_detail.html', {'post': post, 'choice':choice})

def post_new(request):
    if request.method == "POST":
        print request.POST
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.image = request.POST["image"]
            post.published_date = timezone.now()
            post.save()
            Choice.objects.create(title=post)
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'Cars/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'Cars/post_edit.html', {'form': form})
        



def vote(request, pk):
    post =  get_object_or_404(Post, pk=pk)
    try:
        try:
            choice = Choice.objects.get(title=post)
        except:
            Choice.objects.create(title=post)
            choice = Choice.objects.get(title=post)
        print choice
        print choice.votes
        choice.votes +=1
        choice.save()
        return redirect('post_detail', pk=post.pk)
    except Exception, e:
        print e

def sign_page(request):
    if request.method == "POST":
        c=SignUp.objects.create(name=request.POST["name"], email_id=request.POST["email_id"])
        c.save()
        return render(request,'Cars/thank.html',{'o':c})
    else:
        form=SignForm()
        return render(request, 'Cars/sign_up.html', {'form': form})   

def register_user(request):
    if request.method=='POST' :
        form=MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'Cars/register_success.html')
    args={}
    args.update(csrf(request))
    args['form']=MyRegistrationForm()
    return render(request,'Cars/register.html',args)
            
def register_success(request):
    return render(request,'Cars/register_success.html')

    
            






    