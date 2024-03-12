from django.shortcuts import render,redirect
from . models import Item
from . forms import ItemForm
from django.http import HttpResponseRedirect

# Create your views here..
def index(request):
    item_list=Item.objects.all()
    return render(request,"food/index.html",{
        'item_list':item_list
    })

def detail(request,item_id):
    item=Item.objects.get(id=item_id)
    return render(request,"food/detail.html",{
        'item':item,
    })

def create_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return  render(request,'food/Item-form.html',{
        'form':form
    })
def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request,'food/Item-form.html',{
        'form':form,'item':item
    })

def delete_item(request,id):
    item=Item.objects.get(id=id)
    if request.method =="POST":
        item.delete()
        return redirect('food:index')
    return render(request,'food/item_delete.html',{
        'item':item
    })

