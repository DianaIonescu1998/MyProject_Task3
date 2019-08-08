#! /bin/bash

cp /tmp/rpm/index.html /var/www/html

http_page="http://192.168.33.12/index.html"



curl -s -o - $http_page | grep "ERROR 404"
response=$?
if [ $response -eq 0 ]
then 
	echo page is loaded
else 
	echo page is not loaded
fi



