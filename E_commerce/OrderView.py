from django.shortcuts import render, redirect
from django.contrib import messages
# from django.urls import reverse
from Order.models import Order

def order_view(request):
    orderData = Order.objects.all()
    data = {
        "orderData": orderData
    }
    return render(request, 'order/index.html', data)


def view_order(request, id):
    orderData = Order.objects.filter(id=id)
    data = {
        "orderData": orderData,
        "id": int(id),
    }
    return render(request, 'order/view.html', data)


def edit_order(request, id):
    orderData = Order.objects.get(id=int(id))

    if request.method == 'GET':
        data = {
            "orderData": orderData
        }
        return render(request, "order/edit.html", data)

    else:
        
        customer_name = request.POST.get("customer_name", orderData.customer_name)
        customer_email = request.POST.get("customer_email", orderData.customer_email)
        order_date = request.POST.get("order_date", orderData.order_date)
        status = request.POST.get("status", orderData.status)
        total_amount = request.POST.get("total_amount", orderData.total_amount)

        
        orderData.customer_name = customer_name
        orderData.customer_email = customer_email
        orderData.order_date = order_date
        orderData.status = status
        orderData.total_amount = total_amount
        orderData.save()

  
        return redirect('order_view')  


def delete_order(request, id):
    orderData = Order.objects.get(id=int(id))
    orderData.delete()
    messages.success(request, "Order deleted successfully!")
    return redirect(order_view)



def add_order(request):
     if request.method == 'GET':
        return render(request, "order/add.html")
     else:
        customer_name = request.POST.get("customer_name")
        customer_email = request.POST.get("customer_email")
        phone_number = request.POST.get("phone_number")
        order_date = request.POST.get("order_date")
        status = request.POST.get("status")
        quantity=request.POST.get("quantity")
        price=request.POST.get("price")
        total_amount = request.POST.get("total_amount")
        payment_method=request.POST.get("payment_method")
       
        save_data = Order(
            customer_name=customer_name,
            customer_email=customer_email,
            phone_number=phone_number,
            order_date=order_date,
            status=status,
            quantity=quantity,
            price=price,
            total_amount=total_amount,
            payment_method=payment_method,
        )
        save_data.save()
       
        return redirect(order_view)
