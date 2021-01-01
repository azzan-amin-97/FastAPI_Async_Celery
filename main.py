from fastapi import FastAPI
from celery_worker import create_order
from model import Order

# Create FastAPI app
app = FastAPI()


# Create order endpoint
@app.post('/order')
def add_order(order: Order):
    # use delay() method to call the celery task
    create_order.delay(order.customer_name, order.order_quantity)
    return {"message": "Order Received! Thank you for your patience."}
