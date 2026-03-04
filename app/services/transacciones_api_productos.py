import requests

BASE = "http://localhost:8000/products"
TIME_OUT = 10

# Obtiene la lista de productos de FastAPI
def list_products(limit: int = 20, offset: int = 0) -> dict:
    try:
        r = requests.get(f"{BASE}/", params={"limit": limit, "offset": offset}, timeout=TIME_OUT)
        if 200 <= r.status_code < 300:
            return r.json() if r.content else {}
        raise ValueError(f"Error {r.status_code}", r.status_code, r.text)
    except requests.exceptions.RequestException as e:
        raise ValueError("Error de conexión", None, str(e))

# Obtiene el producto con el id que se le pasa como parámetro
def get_product(product_id: str) -> dict:
    try:
        r = requests.get(f"{BASE}/{product_id}", timeout=TIME_OUT)
        if 200 <= r.status_code < 300:
            return r.json() if r.content else {}
        raise ValueError(f"Error {r.status_code}", r.status_code, r.text)
    except requests.exceptions.RequestException as e:
        raise ValueError("Error de conexión", None, str(e))

# Crea un producto nuevo
def create_product(data: dict) -> dict:
    try:
        r = requests.post(f"{BASE}/", json=data, timeout=TIME_OUT)
        if 200 <= r.status_code < 300:
            return r.json() if r.content else {}
        raise ValueError(f"Error {r.status_code}", r.status_code, r.text)
    except requests.exceptions.RequestException as e:
        raise ValueError("Error de conexión", None, str(e))

# Actualiza el producto indicado
def update_product(product_id: str, data: dict) -> dict:
    try:
        r = requests.put(f"{BASE}/{product_id}", json=data, timeout=TIME_OUT)
        if 200 <= r.status_code < 300:
            return r.json() if r.content else {}
        raise ValueError(f"Error {r.status_code}", r.status_code, r.text)
    except requests.exceptions.RequestException as e:
        raise ValueError("Error de conexión", None, str(e))

# Borra el producto indicado
def delete_product(product_id: str):
    try:
        r = requests.delete(f"{BASE}/{product_id}", timeout=TIME_OUT)
        if 200 <= r.status_code < 300:
            return r.json() if r.content else {}
        raise ValueError(f"Error {r.status_code}", r.status_code, r.text)
    except requests.exceptions.RequestException as e:
        raise ValueError("Error de conexión", None, str(e))

# --- Linea de pueba ---
if __name__ == "__main__":
    try:
        print("Consultando productos...")
        print(list_products())
    except Exception as error:
        print(f"No se pudo conectar: {error}")