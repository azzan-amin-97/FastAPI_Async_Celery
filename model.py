from pydantic import BaseModel

# Pydantic BaseModel
# Order class model for request body
class Order(BaseModel):
    customer_name: str
    order_quantity: int