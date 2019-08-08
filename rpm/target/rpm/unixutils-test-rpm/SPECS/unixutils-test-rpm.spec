Name: unixutils-test-rpm
Version: 1.0.0
Release: 1.0.0
Summary: unixutils-test-rpm
License: 2019, UnixUtils
Group: Development/Tools
autoprov: yes
autoreq: yes
BuildRoot: /Task3/rpm/target/rpm/unixutils-test-rpm/buildroot

%description

%files

%attr(755,root,root) /tmp/rpm

%pre
#! /bin/bash

package=httpd

rpm -q $package

if [ $? -eq 0 ]
then
	echo "httpd is installed"
else
	 echo "please install httpd package"
fi


%post
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



