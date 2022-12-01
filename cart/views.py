from django.shortcuts import render, redirect, get_object_or_404
from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def cart_details(request,tot=0,count=0,ct_items=None):
    try:
        ct=cart_list.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot+=(i.prod.price*i.quantity)
            count+=i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart1.html',{'ci':ct_items,'t':tot,'cn':count,'tt':tot+10})

def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def add_cart(request,product_id):
    prodt=product.objects.get(id=product_id)
    try:
        ct=cart_list.objects.get(cart_id=c_id(request))
    except cart_list.DoesNotExist:
        ct=cart_list.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(prod=prodt,cart=ct)
        if c_items.quantity < c_items.prod.stock:
            c_items.quantity+=1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prod=prodt,quantity=1,cart=ct)
        c_items.save()
    return redirect('CartDetails')



def min_cart(request,product_id):
    ct=cart_list.objects.get(cart_id=c_id(request))
    prodt=get_object_or_404(product,id=product_id)
    c_items=items.objects.get(prod=prodt,cart=ct)
    if c_items.quantity>1:
        c_items.quantity-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('CartDetails')


def remove_cart(request,product_id):
    ct = cart_list.objects.get(cart_id=c_id(request))
    prodt = get_object_or_404(product, id=product_id)
    c_items = items.objects.get(prod=prodt,cart=ct)
    c_items.delete()
    return redirect('CartDetails')