from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    product_id: int
    product_name: str
    supplier_name: str
    category_name: str
    quantity_per_unit: str
    unit_price: float
    units_in_stock: int
    units_on_order: int
    reorder_level: int
    discontinued: bool