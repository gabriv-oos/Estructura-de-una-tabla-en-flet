from fastapi import FastAPI

app = FastAPI()

base_de_datos = {
    "1": {"id": "1", "nombre": "Laptop", "precio": 15000, "stock": 10},
    "2": {"id": "2", "nombre": "Mouse", "precio": 300, "stock": 50}
}

# Obtener todos los productos 
@app.get("/products/")
def read_products(limit: int = 20, offset: int = 0):
    # Convertimos el diccionario a una lista para enviarla
    productos = list(base_de_datos.values())
    return productos[offset : offset + limit]

# Obtener un producto por ID 
@app.get("/products/{product_id}")
def read_product(product_id: str):
    return base_de_datos.get(product_id, {"error": "Producto no encontrado"})

# Crear un producto nuevo 
@app.post("/products/")
def create_product(data: dict):
    nuevo_id = str(len(base_de_datos) + 1)
    base_de_datos[nuevo_id] = data
    return {"mensaje": "Producto creado con éxito", "producto": data}

# Actualizar un producto 
@app.put("/products/{product_id}")
def update_product(product_id: str, data: dict):
    base_de_datos[product_id] = data
    return {"mensaje": f"Producto {product_id} actualizado"}

# Borrar un producto 
@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    if product_id in base_de_datos:
        del base_de_datos[product_id]
        return {"mensaje": "Producto eliminado"}
    return {"error": "Producto no encontrado"}