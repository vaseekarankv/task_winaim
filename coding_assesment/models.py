from pydantic import BaseModel

# Define Product Model
class Product(BaseModel):
    name: str
    description: str
    price: float

# Define Supplier Model
class Supplier(BaseModel):
    name: str
    contact_email: str

# Define Warehouse Model
class Warehouse(BaseModel):
    name: str
    location: str

# Define Stock Level Model
class StockLevel(BaseModel):
    product_id: int
    warehouse_id: int
    quantity: int
