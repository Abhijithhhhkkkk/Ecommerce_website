from django.shortcuts import get_object_or_404, redirect, render

from django.conf import settings
from .models import Homepage,logo,details,order_details
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


# Create your views here.
def home(request):
        categories = [
        {"title":"Shirts","products":details.objects.filter(category='shirt')},
        {"title":"Pants","products":details.objects.filter(category='pant')},
        {"title":"Linen Co-ord Set","products":details.objects.filter(category='linen Co-ord Set')},
        {"title":"Modern Kurta","products":details.objects.filter(category='Modern Kurta')},
        {"title":"Slip Dress","products":details.objects.filter(category='slip Dress')},
    ]

        context = {
        'home': Homepage.objects.order_by('-id').first(),
        'logo': logo.objects.order_by('-id').first(),
        'categories': categories,
    }

        return render(request,'home.html',context)
def post_list(request,pk):
     
        
        detail=get_object_or_404(details,pk=pk)

        return render(request,'post_detail.html',{'detail':detail})

@login_required(login_url='login')
def process_order(request, pk):

    product = get_object_or_404(details, pk=pk)

    if request.method == 'POST':
        order_details.objects.create(
            product=product,
            buyer=request.user
        )
        return render(request, 'post-order.html', {
            'product': product
        })

    return redirect('post-list', pk=pk)