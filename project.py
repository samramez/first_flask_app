from flask import Flask

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
@app.route('/hello')
def hello_world():
    restaurant = session.query(Restaurant).first()
    items = session.query(MenuItem).filter_by(restaurant_id = restaurant.id)
    output = ''
    for i in items:
        output += i.name
        output += "</br>"
        output += i.price
        output += "</br>"
        output += i.description
        output += "</br></br>"

    return output


if __name__ == '__main__':

    # True means we don't have to restart the server every time I modify the code
    app.debug = True

    # Running a local server on our system
    # 0.0.0.0 means all public ip addresses can access my server
    app.run(host='0.0.0.0', port = 5000)