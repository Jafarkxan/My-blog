from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Post, Contact
from .forms import PostForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings    

def aloqa(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # ✅ DB-ga saqlash
        contact = Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        # ✅ Emailga yuborish (console backend ishlatilsa console ga chiqadi)
        send_mail(
            subject=f"Yangi xabar: {name}",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            fail_silently=False
        )

        messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi!')
        return redirect('aloqa')
    
    return render(request, 'posts/aloqa.html')

# ✅ Admin-only decorator
def admin_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser)(view_func)
    return decorated_view_func


# 📌 Barcha postlarni chiqarish (READ - List)
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # eng so‘nggi post tepada
    return render(request, 'posts/post_list.html', {'posts': posts})


# 📌 Bitta postni ko‘rish (READ - Detail)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


# 📌 Yangi post qo‘shish (CREATE) → faqat admin
@admin_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user   # post muallifi → admin user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})


# 📌 Postni tahrirlash (UPDATE) → faqat admin
@admin_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form})


# 📌 Postni o‘chirish (DELETE) → faqat admin
@admin_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})

def aloqa(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Bu yerda xabarni saqlash yoki email yuborish funksiyasi qo‘shish mumkin
        messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi!')
        return render(request, 'posts/aloqa.html')
    
    return render(request, 'posts/aloqa.html')

def about(request):
    return render(request, 'posts/about_us.html')