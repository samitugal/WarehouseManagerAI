import os


from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from typing import List

from .DatabaseBase import DatabaseBase
from src.config_defs.database_config_defs import DatabaseTag, DatabaseConfig, DatabaseMainConfig
from .data_models import Product

class Postgres(DatabaseBase):
    def __init__(self, config: DatabaseConfig):
        if config.db.database_tag != DatabaseTag.POSTGRESQL:
            raise ValueError("PostgreSQLConfig can only be used with PostgreSQL.")
        if config.db is None:
            raise ValueError("PostgreSQL requires PostgreSQL Config.")
        
        load_dotenv()
        self.config = config

        self.connection_string = f"postgresql://{config.postgresql.user}:{config.postgresql.password}@{config.postgresql.host}:{config.postgresql.port}/{config.postgresql.database_name}"
        
        self.engine = create_engine(self.connection_string)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def disconnect(self):
        self.session.close()

    def fetch_product_table(self, product_name: str) -> List[Product]:
        query = """
            SELECT
                p.product_id,
                p.product_name,
                s.company_name AS supplier_name,
                c.category_name,
                p.quantity_per_unit,
                p.unit_price,
                p.units_in_stock,
                p.units_on_order,
                p.reorder_level,
                p.discontinued
            FROM
                products p
            JOIN
                suppliers s ON p.supplier_id = s.supplier_id
            JOIN
                categories c ON p.category_id = c.category_id
            WHERE
                p.product_name ILIKE :product_name
            ORDER BY
                p.product_name;
        """

        result = self.session.execute(text(query), {'product_name': self.clean_input_from_agent(self.fetch_product_table, product_name)}).fetchall()
        print(result)
        products = [Product(**row._asdict()) for row in result]
        return products


    