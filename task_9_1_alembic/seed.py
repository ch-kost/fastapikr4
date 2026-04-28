from database import SessionLocal
from models import Product

items = [
    Product(title="Keyboard", price=2500.0, count=10, description="Mechanical keyboard"),
    Product(title="Monitor", price=18500.0, count=3, description="Full HD monitor"),
]

with SessionLocal() as db:
    for item in items:
        exists = db.query(Product).filter(Product.title == item.title).first()
        if exists is None:
            db.add(item)
    db.commit()
