from fastapi import FastAPI, HTTPException
from typing import List
from database import execute_query, close_connection
from models import Product, Supplier, Warehouse, StockLevel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Update this with your frontend URL
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Products endpoints
@app.post("/products/")
async def create_product(product: Product):
    query = "INSERT INTO products (name, description, price) VALUES (%s, %s, %s)"
    data = (product.name, product.description, product.price)
    execute_query(query, data)
    return {"message": "Product created successfully"}

@app.get("/products/")
async def get_products(skip: int = 0, limit: int = 10):
    query = "SELECT * FROM products LIMIT %s OFFSET %s"
    data = (limit, skip)
    return execute_query(query, data, fetchall=True)

@app.get("/products/search/")
async def search_products(name: str):
    query = "SELECT * FROM products WHERE name LIKE %s"
    data = ("%" + name + "%",)
    return execute_query(query, data, fetchall=True)

@app.put("/products/{product_id}")
async def update_product(product_id: int, product: Product):
    query = "UPDATE products SET name = %s, description = %s, price = %s WHERE id = %s"
    data = (product.name, product.description, product.price, product_id)
    execute_query(query, data)
    return {"message": "Product updated successfully"}

@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    query = "DELETE FROM products WHERE id = %s"
    data = (product_id,)
    execute_query(query, data)
    return {"message": "Product deleted successfully"}

# Suppliers endpoints
@app.post("/suppliers/")
async def create_supplier(supplier: Supplier):
    query = "INSERT INTO suppliers (name, contact_email) VALUES (%s, %s)"
    data = (supplier.name, supplier.contact_email)
    execute_query(query, data)
    return {"message": "Supplier created successfully"}

@app.get("/suppliers/")
async def get_suppliers(skip: int = 0, limit: int = 10):
    query = "SELECT * FROM suppliers LIMIT %s OFFSET %s"
    data = (limit, skip)
    return execute_query(query, data, fetchall=True)

@app.get("/suppliers/search/")
async def search_suppliers(name: str):
    query = "SELECT * FROM suppliers WHERE name LIKE %s"
    data = ("%" + name + "%",)
    return execute_query(query, data, fetchall=True)

@app.put("/suppliers/{supplier_id}")
async def update_supplier(supplier_id: int, supplier: Supplier):
    query = "UPDATE suppliers SET name = %s, contact_email = %s WHERE id = %s"
    data = (supplier.name, supplier.contact_email, supplier_id)
    execute_query(query, data)
    return {"message": "Supplier updated successfully"}

@app.delete("/suppliers/{supplier_id}")
async def delete_supplier(supplier_id: int):
    query = "DELETE FROM suppliers WHERE id = %s"
    data = (supplier_id,)
    execute_query(query, data)
    return {"message": "Supplier deleted successfully"}

# Warehouses endpoints
@app.post("/warehouses/")
async def create_warehouse(warehouse: Warehouse):
    query = "INSERT INTO warehouses (name, location) VALUES (%s, %s)"
    data = (warehouse.name, warehouse.location)
    execute_query(query, data)
    return {"message": "Warehouse created successfully"}

@app.get("/warehouses/")
async def get_warehouses(skip: int = 0, limit: int = 10):
    query = "SELECT * FROM warehouses LIMIT %s OFFSET %s"
    data = (limit, skip)
    return execute_query(query, data, fetchall=True)

@app.get("/warehouses/search/")
async def search_warehouses(name: str):
    query = "SELECT * FROM warehouses WHERE name LIKE %s"
    data = ("%" + name + "%",)
    return execute_query(query, data, fetchall=True)

@app.put("/warehouses/{warehouse_id}")
async def update_warehouse(warehouse_id: int, warehouse: Warehouse):
    query = "UPDATE warehouses SET name = %s, location = %s WHERE id = %s"
    data = (warehouse.name, warehouse.location, warehouse_id)
    execute_query(query, data)
    return {"message": "Warehouse updated successfully"}

@app.delete("/warehouses/{warehouse_id}")
async def delete_warehouse(warehouse_id: int):
    query = "DELETE FROM warehouses WHERE id = %s"
    data = (warehouse_id,)
    execute_query(query, data)
    return {"message": "Warehouse deleted successfully"}

# Stock levels endpoints
@app.post("/stock-levels/")
async def create_stock_level(stock_level: StockLevel):
    query = "INSERT INTO stock_levels (product_id, warehouse_id, quantity) VALUES (%s, %s, %s)"
    data = (stock_level.product_id, stock_level.warehouse_id, stock_level.quantity)
    execute_query(query, data)
    return {"message": "Stock level created successfully"}

@app.get("/stock-levels/")
async def get_stock_levels(skip: int = 0, limit: int = 10):
    query = "SELECT * FROM stock_levels LIMIT %s OFFSET %s"
    data = (limit, skip)
    return execute_query(query, data, fetchall=True)

@app.get("/stock-levels/search/")
async def search_stock_levels(product_id: int):
    query = "SELECT * FROM stock_levels WHERE product_id = %s"
    data = (product_id,)
    return execute_query(query, data, fetchall=True)

@app.put("/stock-levels/{stock_level_id}")
async def update_stock_level(stock_level_id: int, stock_level: StockLevel):
    query = "UPDATE stock_levels SET product_id = %s, warehouse_id = %s, quantity = %s WHERE id = %s"
    data = (stock_level.product_id, stock_level.warehouse_id, stock_level.quantity, stock_level_id)
    execute_query(query, data)
    return {"message": "Stock level updated successfully"}

@app.delete("/stock-levels/{stock_level_id}")
async def delete_stock_level(stock_level_id: int):
    query = "DELETE FROM stock_levels WHERE id = %s"
    data = (stock_level_id,)
    execute_query(query, data)
    return {"message": "Stock level deleted successfully"}

# Event handler to close database connection when the FastAPI application shuts down
@app.on_event("shutdown")
async def shutdown_event():
    close_connection()
