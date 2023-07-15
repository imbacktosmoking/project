from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .models import Comments

# Create your views here.

#def homepage(request):
    #return render(request, 'homepage.html')

class Homepage(ListView):
    model = Post 
    template_name = 'homepage.html'

class Post_details(DetailView):
    model = Post
    template_name = 'post_details.html'

class Submit_post(CreateView):
    model = Post
    template_name = "submit_post.html"
    fields = '__all__'

class Post_comments(CreateView):
    model = Comments
    template_name = "post_comments.html"
    fields = "__all__"

class About(ListView):
    model = Post
    template_name = "about.html"
    fields = "__all__"


