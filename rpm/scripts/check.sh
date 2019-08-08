#! /bin/bash

package=httpd

rpm -q $package

if [ $? -eq 0 ]
then
	echo "httpd is installed"
else
	 echo "please install httpd package"
fi

