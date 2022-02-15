# Home Automation using Jetson Nano 
Home Automation using Jetson Nano triggerd by Google Assistant on Android Device

## Approach
Sign up on https://ifttt.com and create Applet
1. The Trigger [This]:
+ look for Google assistant and connect the website to your google account
2. Send Webhook [That]:
+ look for Webhook and Choose Post Method 

For Further information:
* Explore the code in basic-flask-app/app.py

## on Jetson Nano
* You need to install apache server " Don't forget to allow it throught the firewall"
* Add a rule in your router for Port Forwarding to the jetson
* Get a Static Public IP address for the jetson /or set a DNS
Finally Here is the Flask App with GPIO Control:
1. move basic-flask-app directory to [/var/www/basic-flask-app]
2. move the config file to [/etc/apache2/sites-available]

** Final Note **
Don't forget to give the appropriate permission for gpio control to apache 
