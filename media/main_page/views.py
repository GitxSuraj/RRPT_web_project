from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Contact, Order, OrderUpdate, JobApplication, Trousers, TShirts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from math import ceil
from django.contrib import messages
import json
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext

from PayTm import Checksum
MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'


def index(request):
    allProds = []
    catprods = Product.objects.values('category', 'product_id')
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
        # print(prod)
        # print(allProds)

    params = {'allProds': allProds}
    return render(request, "main_page/index.html", params)


def tshirt(request):
    Tshirts = []
    cat_tshirt = TShirts.objects.values('category', 'product_id')
    tshirt_cats = {item["category"] for item in cat_tshirt}
    for tshirt_cat in tshirt_cats:
        prod = TShirts.objects.filter(category=tshirt_cat)
        Tshirts.append(prod)

    params = {'Tshirts': Tshirts}
    print(prod)
    print(Tshirts)
    return render(request, "main_page/t-shirts.html", params)


def trouser(request):
    Trouser = []
    cat_trousers = Trousers.objects.values('category', 'product_id')
    trouser_cats = {item["category"] for item in cat_trousers}
    for trouser_cat in trouser_cats:
        prod = Trousers.objects.filter(category=trouser_cat)
        Trouser.append(prod)

    params = {'Trouser': Trouser}
    return render(request, "main_page/trousers.html", params)


def productView(request, myid):
    product = Product.objects.filter(product_id=myid)
    print(product)
    return render(request, "main_page/products.html", {'product': product[0]})


def tshirtView(request, myid):
    tshirt = TShirts.objects.filter(product_id=myid)
    print(tshirt)
    return render(request, "main_page/tshirt_view.html", {'tshirt': tshirt[0]})


def trouserView(request, myid):
    trouser = Trousers.objects.filter(product_id=myid)
    print(trouser)
    return render(request, "main_page/trousers_view.html", {'trouser': trouser[0]})


def searchMatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.subcategory.lower() or query in item.category.lower():
        return True
    elif query in item.desc.upper() or query in item.product_name.upper() or query in item.subcategory.upper() or query in item.category.upper():
        return True
    elif query in item.desc or query in item.product_name or query in item.subcategory or query in item.category:
        return True
    elif query in item.desc.capitalize() or query in item.product_name.capitalize() or query in item.subcategory.capitalize() or query in item.category.capitalize():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'product_id')
    cats = {item["category"] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if n != 0:
            allProds.append([prod, range(1, nSlides), nSlides])

    catTshirts = TShirts.objects.values('category', 'product_id')
    tshirt_cat = {item["category"] for item in catTshirts}
    for cat in tshirt_cat:
        prodtemp = TShirts.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if n != 0:
            allProds.append([prod, range(1, nSlides), nSlides])

    catTrouser = Trousers.objects.values('category', 'product_id')
    trouser_cat = {item["category"] for item in catTrouser}
    for cat in trouser_cat:
        prodtemp = Trousers.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if n != 0:
            allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds': allProds, "msg": "", "query": query}
    print(params)
    if len(query) == 0:
        params = {'msg': "Please enter something in Search box"}
        print("Searched for blank")
    if len(allProds) == 0:
        params = {'msg': "No result found for " + query}
        print(f"Searched for", query)

    return render(request, "main_page/search.html", params)


def about(request):
    return render(request, 'main_page/about.html')


def contact(request):
    if request.method == "POST":
        user_name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        desc_type = request.POST.get('desc_type', '')
        desc = request.POST.get('desc', '')
        print(user_name, email, desc_type, desc)
        contact = Contact(user_name=user_name, email=email,
                          desc_type=desc_type, desc=desc)
        contact.save()
    return render(request, 'main_page/contact.html')


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '0')
        email = request.POST.get('email', '')
        address = request.POST.get(
            'address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '0')
        phone = request.POST.get('phone', '0')
        quantity = request.POST.get('quantity', '0')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city, state=state,
                      zip_code=zip_code, phone=phone, amount=amount, quantity=quantity)
        order.save()
        update = OrderUpdate(order_id=order.order_id,
                             update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        print(order.order_id)
        # Request paytm to transfer the amount to your account after payment by user
        param_dict = {
            'MID': 'mid',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(
            param_dict, MERCHANT_KEY)
        return render(request, 'main_page/paytm.html', {'param_dict': param_dict})

    return render(request, 'main_page/checkout.html')


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append(
                        {'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(
                        {"status": "success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'main_page/tracker.html')


def custom_design(request):
    return HttpResponse("Sorry ,we are not accepting any coustom disegins order")


def job_application(request):
    if request.method == "POST":
        name = request.POST.get('name', ''),
        email = request.POST.get('email', ''),
        phone = request.POST.get('phone', '0'),
        address = request.POST.get('address', ''),
        work = request.POST.get('work', ''),
        jobapplication = JobApplication(
            name=name, email=email, phone=phone, work=work, address=address)
        jobapplication.save()

    return render(request, 'main_page/job-application.html')


def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['SignUPemail']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) < 10:
            messages.error(
                request, "Your user name must be under 10 characters")
            return redirect('/')

        if not username.isalnum():
            messages.error(
                request, "User name should only contain letters and numbers")
            return redirect('/')
        if (pass1 != pass2):
            messages.error(request, "Passwords do not match")
            return redirect('/')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, "Your RRPT has been successfully created! Now login with your Username and Password to continue.")
        return redirect('/')

    else:
        return render(request, 'main_page/notfound.html')


def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(
                request, "Invalid credentials! Please try again")
            return redirect("/")

    return render(request, 'main_page/notfound.html')


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(
        response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('Order was not successful because ' +
                  response_dict['RESPMSG'])
    return render(request, 'main_page/paymentstatus.html', {'response': response_dict})


def error_404(request, exception):
    data = {}
    return render(request, 'main_page/404.html', data)


def error_500(request, *args, **argv):
    data = {}
    return render(request, 'main_page/500.html', data)
