from django.shortcuts import render
from .models import Cart


# Create your views here.

# 1) Get cart session - number associated to database
# 2) Check if cart exists if not create new and set it to the session
# 3)

def cart_home(request):
    # get cart session
    cart_id = request.session.get("cart_id", None)
    # check if cart_id doesnt exist
    # If cart already exists check for sure it is
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() == 1:
        print("Cart Id exists")
        cart_obj = qs.first()

        # Save user to cart when user log in
        if request.user.is_authenticated() and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
    else:
        cart_obj = Cart.objects.new_cart(user=request.user)
        # set new cart to the session
        request.session['cart_id'] = cart_obj.id
    # print(dir(request.session)) dir(request.session) prints all possible session methods
    return render(request, "cart/home.html", {})

# users=None no users logged in
# users=request.user handles all users
