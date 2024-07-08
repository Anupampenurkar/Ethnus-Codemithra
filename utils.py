import requests
from .models import ProductTransaction
from . import db
import datetime

def fetch_and_initialize_data():
    url = "https://s3.amazonaws.com/roxiler.com/product_transaction.json"
    response = requests.get(url)
    data = response.json()

    for item in data:
        transaction = ProductTransaction(
            title=item['title'],
            description=item.get('description', ''),
            price=item['price'],
            dateOfSale=datetime.datetime.strptime(item['dateOfSale'], '%Y-%m-%d'),
            category=item['category'],
            sold=item['sold']
        )
        db.session.add(transaction)

    db.session.commit()

