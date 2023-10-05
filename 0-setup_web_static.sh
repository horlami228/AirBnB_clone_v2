#!/usr/bin/env bash
# This bash scripts sets up a web server for deployment of web_static

# install nginx if not there already
sudo apt-get update -y
sudo apt-get install nginx -y

# create the folder data
sudo mkdir -p /data/

# give ownership of data folder to user and make it recursive
sudo chown -R "$USER":"$USER" /data/

# create the sub directories needed
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/current/
# add an index.html file to the test it
content=" 
<html> 

	<head>
	Web Static
	</head>

	<body>
	This is a static page created
	</body>
</html>
"

echo "$content" | sudo tee /data/web_static/releases/test/index.html

# create a symbolic link for the index.html and force a new file if it already exist
ln -sf /data/web_static/releases/test/ /data/web_static/current/


# configure nginx with a new location for index.html with /hbnb_static/ as the endpoint

echo '	location = /hbnb_static {' > temp_config
echo '    	alias /data/web_static/current/;' >> temp_config
echo '	}' >> temp_config

# add this file to the configuration file for nginx
sudo sed -i '/listen 80 default_server;/r temp_config'  /etc/nginx/sites-available/default
sudo rm temp_config
# restart nginx
sudo service nginx restart

