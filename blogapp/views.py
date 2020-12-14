from django.http.response import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from blogapp.models import Post, Category
from blogapp.forms import PostCreateForm

# Create your views here.
class PostListView(ListView):
    template_name = 'index.html'
    model = Post

    def get_context_data(self, **kwargs ):
        context = super().get_context_data(**kwargs)
        page = int(self.request.GET.get("page") or 0)
        print(page)
        context['object_list'] = Post.objects.order_by('-created')[page*4:page*4+4]
        context['page'] = page +1
        return context

class DailyListView(ListView):
    template_name = 'index.html'
    model = Post

    def get_context_data(self, **kwargs ):
        context = super().get_context_data(**kwargs)
        page = int(self.request.GET.get("page") or 0)
        post_list = Post.objects.filter(category='01')
        context['object_list'] = post_list.order_by('-created')[page*4:page*4+4]
        context['page'] = page +1
        return context


class SkillsListView(ListView):
    template_name = 'index.html'
    model = Post

    def get_context_data(self, **kwargs ):
        context = super().get_context_data(**kwargs)
        page = int(self.request.GET.get("page") or 0)
        post_list = Post.objects.filter(category='02')
        context['object_list'] = post_list.order_by('-created')[page*4:page*4+4]
        context['page'] = page +1
        return context        


class TipsListView(ListView):
    template_name = 'index.html'
    model = Post

    def get_context_data(self, **kwargs ):
        context = super().get_context_data(**kwargs)
        page = int(self.request.GET.get("page") or 0)
        post_list = Post.objects.filter(category='03')
        context['object_list'] = post_list.order_by('-created')[page*4:page*4+4]
        context['page'] = page +1
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = context['object'].pk
        context['object'] = Post.objects.get(pk=pk)
        return context

def savePost(request):

    pk = int(request.POST.get('pk', None))
    if pk :
        content = request.POST.get('data', None)
        print(content)
        if content :
            post_obj = Post.objects.get(pk=pk)
            post_obj.content = content
            post_obj.save()
        else : 
            json_data = {"msg" : "저장에 실패하였습니다."}
            return JsonResponse(json_data)
    else :
        json_data = {"msg" : "저장에 실패하였습니다."}
        return JsonResponse(json_data)
    json_data = {"msg" : "저장되었습니다."}
    return JsonResponse(json_data)


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'blogapp/create.html'
    success_url = reverse_lazy("blogs:home")

    def get_context_data(self, **kwargs) :
        print(self.request.path)
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        print("여긴 오냐 ")
        temp_post = form.save(commit=False)
        temp_post.writer = self.request.user
        temp_post.save()
        return super().form_valid(form)