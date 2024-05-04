import json
from customer.models import Product
from django.contrib import messages
from django.core.mail import send_mail



def registrationMail(email):
    msg=f'Thank you for Registering with us. \n Exlplore our new products at lowest rate and best service in the Town.\n\nbest regards,\nEtech Team'
    send_mail("Welcome to Etech-Family",
                  msg,
                  "jp2112003@gmail.com",
                  [email],
                  fail_silently=False)
    
    
def confirmationMail(email,orderid):
    link=f'http://127.0.0.1:8000/customer/ordertrack/{orderid}'
    msg=f'Your order has been confirmed for order id {orderid}' + f'\nClick on this link to track your order {link}'
    send_mail("Etech order confirmed",
                  msg,
                  "jp2112003@gmail.com",
                  [email],
                  fail_silently=False)    


def updateCart(request,productDetails):
    products=json.loads(productDetails)
    for item in products:
        name = products[item][0]
        allProducts = Product.objects.get(name=name)
        qty = allProducts.qty
        qty = qty -products[item][2]
        if qty < 0 :
            msg=f'Sorrry but we can\'t able to satisfy your request for {name}. We have only {allProducts.qty} items in our stock.'
            messages.warning(request,msg)
            return False
        else :
            allProducts.qty = qty        
            allProducts.save()
            return True
        
    
def prodDetail(prodDetail):
    products=json.loads(prodDetail)
    data=''
    for item in products:
        str=f'{products[item][0]} ({products[item][1]} * {products[item][2]})\n'
        data+=str
    return data
    