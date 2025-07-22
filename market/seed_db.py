from market import app, db, Item

with app.app_context():
    if not Item.query.filter_by(name="IPhone10"):
        item1 = Item(name="IPhone10", price=500, barcode="3457842378", description="desc")
        db.session.add(item1)

    if not Item.query.filter_by(name="MacBook"):
        item2 = Item(name="MacBook", price=1200, barcode="123456789012", description="Laptop desc")
        db.session.add(item2)
    
    db.session.commit()
    
    for item in Item.query.all():
        print(f"{item.name}: {item.price}, {item.barcode}, {item.description}")
    
    # for item in Item.query.filter_by(price=500):
    #     print(item.name)
        
    
    # print(Item.query.all())  #gives as a list