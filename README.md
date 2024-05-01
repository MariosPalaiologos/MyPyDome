# MyPyDome
 Django


Project named MyPyDome in development using the Django framework for Python.
It's an online shop where you can place orders for various products.
Currently working in localhost enviroment.

You can create an account to log in the website. There are 2 types of accounts. First one is for a user who can order products and the second one is for companies who can make their products available for sale in the platform.
You need to apply in order for your account to change type.

#######################################################################################################################

Depending on your account type, you have access to different pages in the website and can interracte in different ways.

Available Pages:
-Home
-Products For Sale
-Profile:
    -Account Info
    -My Dashboard
    -My Orders
    -Contact Us

#######################

Database in SQLite.
Tables currently used:
-auth_user
-products_wishlist
-products_order
-products_contactform

#######################

Run INFO:
- Download as ZIP, unzip and load the folder on VSCode
- Open VSCode terminal and run:
- python manage.py runserver 192.168.x.x:8000 
- 192.168.x.x is your local IP
- When the server is running, go to http://192.168.x.x:8000 on any device connected to your network

#######################
