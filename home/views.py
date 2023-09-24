from django.shortcuts import render,redirect
from .models import BookTable,Testimonial,Offer,Menu
from django.contrib import messages

# Create your views here.
# Create your views here.
def index(request):
    alltest=Testimonial.objects.all()
    alloffer=Offer.objects.all()
    context={'alltest':alltest,'alloffer':alloffer}
    return render(request,'index.html',context)


def about(request):

    return render(request,'about.html')
def profile(request):

    return render(request,'profile.html')


def book(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login to book table if you are a new user create one account")
        return redirect('/auth/login')
    if request.method=="POST":
        fname=request.POST.get('name')
        fphonenum=request.POST.get('phonenum')
        femail=request.POST.get('email')
        fpersons=request.POST.get('persons')
        fdate=request.POST.get('date')
        person=BookTable(name=fname,phone_number=fphonenum,email=femail,persons=fpersons,date=fdate)
        person.save()
    return render(request,'book.html')


def menu(request):
    allmenu=Menu.objects.all()
    context={'allmenu':allmenu}
    return render(request,'menu.html',context)
    

def testimonial(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login to Write a review, if you are a new user create one account")
        return redirect('/auth/login')
    if request.method=="POST":
        fname=request.POST.get('name')
        fimage=request.POST.get('image')
        fproduct=request.POST.get('product')
        fdesc=request.POST.get('desc')
        review=Testimonial(name=fname,img=fimage,product=fproduct,desc=fdesc)
        review.save()
        
    return render(request,'testimonial.html')

def search(request):
    query = request.GET.get('search', '')  # Get the 'search' parameter from the URL
    allpost = Menu.objects.none()  # Initialize an empty queryset

    if len(query) < 100:
        allMenuName = Menu.objects.filter(title__icontains=query)
        allMenuDesc = Menu.objects.filter(desc__icontains=query)
        allpost = allMenuName.union(allMenuDesc)

    if not allpost:
        messages.warning(request, "No post available")

    params = {'allpost': allpost, 'query': query}
    return render(request, 'search.html', params)