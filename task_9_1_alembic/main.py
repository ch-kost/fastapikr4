from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models import Product
from schemas import ProductCreate, ProductOut

app = FastAPI(title="Products API")


@app.post("/products", response_model=ProductOut, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    item = Product(**product.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@app.get("/products", response_model=list[ProductOut])
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@app.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    item = db.get(Product, product_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return item
