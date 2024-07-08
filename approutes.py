from flask import request, jsonify
from .models import ProductTransaction
from . import db
from sqlalchemy import func, extract

def fetch_transactions(month):
    return ProductTransaction.query.filter(extract('month', ProductTransaction.dateOfSale) == month).all()

def paginate(query, page, per_page):
    return query.paginate(page, per_page, False).items

@app.route('/initialize', methods=['GET'])
def initialize():
    fetch_and_initialize_data()
    return jsonify({"message": "Database initialized"}), 200

@app.route('/transactions', methods=['GET'])
def list_transactions():
    month = request.args.get('month')
    search = request.args.get('search', '')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    query = ProductTransaction.query.filter(extract('month', ProductTransaction.dateOfSale) == int(month))

    if search:
        search = f"%{search}%"
        query = query.filter(
            ProductTransaction.title.like(search) | 
            ProductTransaction.description.like(search) | 
            ProductTransaction.price.like(search)
        )

    transactions = paginate(query, page, per_page)

    return jsonify([t.to_dict() for t in transactions])

@app.route('/statistics', methods=['GET'])
def statistics():
    month = int(request.args.get('month'))
    total_sales = db.session.query(func.sum(ProductTransaction.price)).filter(
        extract('month', ProductTransaction.dateOfSale) == month
    ).scalar()
    sold_items = ProductTransaction.query.filter(
        extract('month', ProductTransaction.dateOfSale) == month,
        ProductTransaction.sold == True
    ).count()
    not_sold_items = ProductTransaction.query.filter(
        extract('month', ProductTransaction.dateOfSale) == month,
        ProductTransaction.sold == False
    ).count()

    return jsonify({
        "total_sales": total_sales,
        "sold_items": sold_items,
        "not_sold_items": not_sold_items
    })

@app.route('/barchart', methods=['GET'])
def bar_chart():
    month = int(request.args.get('month'))
    price_ranges = {
        '0-100': 0,
        '101-200': 0,
        '201-300': 0,
        '301-400': 0,
        '401-500': 0,
        '501-600': 0,
        '601-700': 0,
        '701-800': 0,
        '801-900': 0,
        '901-above': 0
    }

    transactions = ProductTransaction.query.filter(extract('month', ProductTransaction.dateOfSale) == month).all()
    
    for t in transactions:
        if t.price <= 100:
            price_ranges['0-100'] += 1
        elif t.price <= 200:
            price_ranges['101-200'] += 1
        elif t.price <= 300:
            price_ranges['201-300'] += 1
        elif t.price <= 400:
            price_ranges['301-400'] += 1
        elif t.price <= 500:
            price_ranges['401-500'] += 1
        elif t.price <= 600:
            price_ranges['501-600'] += 1
        elif t.price <= 700:
            price_ranges['601-700'] += 1
        elif t.price <= 800:
            price_ranges['701-800'] += 1
        elif t.price <= 900:
            price_ranges['801-900'] += 1
        else:
            price_ranges['901-above'] += 1

    return jsonify(price_ranges)

@app.route('/piechart', methods=['GET'])
def pie_chart():
    month = int(request.args.get('month'))
    categories = db.session.query(ProductTransaction.category, func.count(ProductTransaction.id)).filter(
        extract('month', ProductTransaction.dateOfSale) == month
    ).group_by(ProductTransaction.category).all()

    result = {category: count for category, count in categories}
    return jsonify(result)

@app.route('/combined', methods=['GET'])
def combined():
    month = request.args.get('month')
    transactions_response = list_transactions()
    statistics_response = statistics()
    barchart_response = bar_chart()
    piechart_response = pie_chart()

    combined_response = {
        "transactions": transactions_response.json,
        "statistics": statistics_response.json,
        "barchart": barchart_response.json,
        "piechart": piechart_response.json
    }

    return jsonify(combined_response)

