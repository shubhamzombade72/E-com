from django.shortcuts import render, redirect
# from django.urls import reverse
from E_com_app.models import Product
from django.contrib import messages

def product1(request):
    productData = Product.objects.all()
    data = {
        "productData": productData
    }
    return render(request, 'productt/index.html', data)


def product_view(request, id):
    productData = Product.objects.all()
    data = {
        "productData": productData,
        "id": int(id),
    }
    return render(request, 'productt/view.html', data)


def edit_product(request, id):
    productData = Product.objects.get(id=int(id))
    
    if request.method == 'GET':
        data = {
            "productData": productData
        }
        return render(request, "productt/edit.html", data)
    
    else:
        c_img = request.FILES.get("c_img")
        pname = request.POST.get("pname")
        discription = request.POST.get("discription")
        price = request.POST.get("price")
        stock = request.POST.get("stock")

        productData.c_img = c_img
        productData.pname = pname
        productData.discription = discription
        productData.price = price
        productData.stock = stock
        productData.save()
        return redirect(product1)


def delete_product(request, id):
    productData = Product.objects.get(id=int(id))
    productData.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect(product1)



def add_product(request):
     if request.method == 'GET':
        return render(request, "productt/index.html")
     else:
        c_img = request.FILES.get("c_img")
        pname = request.POST.get("pname")
        discription = request.POST.get("discription")
        price = request.POST.get("price")
        stock = request.POST.get("stock")

       
        save_data = Product(
            c_img=c_img,
            pname=pname,
            discription=discription,
            price=price,
            stock=stock,
        )
        save_data.save()
       
        return redirect(product1)
