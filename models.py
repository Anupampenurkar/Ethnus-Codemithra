from . import db

class ProductTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    dateOfSale = db.Column(db.Date, nullable=False)
    category = db.Column(db.String(255), nullable=False)
    sold = db.Column(db.Boolean, nullable=False)

