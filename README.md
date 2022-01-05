# Django-email-automation
A django app to collect data from Api( weather ) and send the formatted data over email

For front-end this app use inbuilt admin dashboard of django.
and for database it uses sqlite.

Working:-
 --> admin creates record of user(name,email,city)
 --> a signal is triggerd when the creating instance of model for user.
 --> triggered signal calls on to a fucntion (say read_db)
 --> read_db does the following:-
      --> gets the current temperature at user's city via 'openweather' API
      --> sends mail to the user with temperature and appropiate emoji.
