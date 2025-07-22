from market import app, db
from market.models import Item, User

with app.app_context():
    
    if not User.query.filter_by(username = "John").first():
        u1 = User(username = "John", password_hash = '123456', email_address = 'john@gmail.com')
        db.session.add(u1)


    if not Item.query.filter_by(name="IPhone10").first():
        item1 = Item(name="IPhone10", price=500, barcode="111222333444", description="iPhone 10 description")
        db.session.add(item1)

    if not Item.query.filter_by(name="MacBook").first():
        item2 = Item(name="MacBook", price=1200, barcode="555666777888", description="Laptop desc")
        db.session.add(item2)

    if not Item.query.filter_by(name="Tablet").first():
        item3 = Item(name="Tablet", price=1100, barcode="579305222278", description="Tablet is good!")
        db.session.add(item3)
    
    db.session.commit()   # Commit here so user exists before setting as owner
    
    
    item1.owner = User.query.filter_by(username = "John").first().id
    db.session.add(item1)
    db.session.commit()
    
    

    for item in Item.query.all():
        print(f"{item.name}: {item.price}, {item.barcode}, {item.description}")
        
    
    print(item1.owner)  #Gives id of the owner
    
    i = Item.query.filter_by(name = "IPhone10").first()
    print(i.owned_user)
    
    
    print(User.query.all())
    print(Item.query.all())  #gives as a list
    
    
    

    # for item in Item.query.filter_by(price=500):
    #     print(item.name)
        
    
    # print(Item.query.all())  #gives as a list
    
    # db.session.rollback()   #makes previous changes not applicable 






