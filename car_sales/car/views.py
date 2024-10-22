from django.shortcuts import render,redirect
from django.views.generic import DetailView,DeleteView,UpdateView,CreateView
from .import models
from .import forms 
from django.urls import reverse_lazy
from user.models import OrderCarUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self,request,*args,**kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment= comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request,*args,**kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object # Car model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    

