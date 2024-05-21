import stripe
from config import settings

stripe.api_key = settings.STRIP_KEY


def create_product(product):
    stripe_product = stripe.Product.create(name=product.name)
    return stripe_product


def create_product(product):
    stripe_product = stripe.Product.create(name=product.name)
    return stripe_product


def create_price(price, product):
    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=int(price) * 100,
        product_data={"name": product.get("id")},
    )
    return stripe_price


def create_session(session):
    stripe_session = stripe.checkout.Session.create(
        success_url="http://http://127.0.0.1:8000/",
        line_items=[{"price": session.get("id"), "quantity": 1}],
        mode="payment",
    )
    id = stripe_session.get("id")
    url = stripe_session.get("url")
    status = stripe_session.get("status")
    return id, url, status
