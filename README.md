# BackEnd

## Set Up the Authentification

### Set Up the user model
There is a user model in the models folder. You can add more fields to the user model and use it.
This is why I used it for the sunglasses to add the user who created the sunglasses.

### Set Up the views!

You have 3 functions to configure in the views folder:
- `signup` to create a new user and connect it directly
- `login` to connect a user with the proper username
- `logout` to disconnect the user

### Set Up the routes
There is a base.html that verify whether the user is connected or not. If the user is connected, it will display the username and a logout button. If the user is not connected, it will display a login and a signup button.
![Firefox_Screenshot_2023-04-04T11-45-42 037Z](image/image1.png)

Moreover, if the user is not connected, he is not able to buy ne sunglasses.
