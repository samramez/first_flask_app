from flask import Flask, render_template, request, redirect, url_for

# Making instance of the class
app = Flask(__name__)

# Import from database_setup (Lesson One)
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB ##
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()



# If a path from the browser with /hello get executed, this function would  run
@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)

    return render_template('menu.html', restaurant = restaurant, items = items)

    # output = ''
    # for i in items:
    #     output += i.name
    #     output += "</br>"
    #     output += i.price
    #     output += "</br>"
    #     output += i.description
    #     output += "</br></br>"
    #
    # return output


# Task 1: Create route for newMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET','POST'])
def newMenuItem(restaurant_id):

    # It looks if there was any POST requests
    if request.method == 'POST':
        newItem = MenuItem(name = request.form['name'],restaurant_id = restaurant_id)
        session.add(newItem)
        session.commit()

        # To redirect user back to main page
        return redirect(url_for('restaurantMenu', restaurant_id= restaurant_id))

    # If server receives GET request
    else:
        return render_template('newmenuitem.html', restaurant_id = restaurant_id)


# Task 2: Create route for editMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:MenuID>/edit/', methods = ['GET', 'POST'])
def editMenuItem(restaurant_id, MenuID):

    editedItem = session.query(MenuItem).filter_by(id = MenuID).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('restaurantMenu', restaurant_id = restaurant_id))

    else:
        # USE THE RENDER_TEMPLATE FUNCTION BELOW TO SEE THE VARIABLES YOU SHOULD USE IN YOUR EDITMENUITEM TEMPLATE
        return render_template('editmenuitem.html', restaurant_id = restaurant_id, MenuID = MenuID, item = editedItem)

# Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "page to delete a menu item. Task 3 complete!"



if __name__ == '__main__':

    # True means we don't have to restart the server every time I modify the code
    app.debug = True

    # Running a local server on our system
    # 0.0.0.0 means all public ip addresses can access my server
    app.run(host='0.0.0.0', port = 5000)