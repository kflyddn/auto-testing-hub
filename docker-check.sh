#!/bin/bash

while true

do

result=`docker-compose ps`
echo $result | grep -i up

if [ $? == 0 ]; then

   sleep 10

else

   echo $result | grep -i "exit 0"

      if [ $? == 0 ]; then
         i=0
         cat testcode/reports/*.html |grep Failure
             if [ $? == 0 ]; then
                echo "Test not pass"
                echo "failed" > stat
             else 
                echo "Test pass"
                echo "pass" > stat
             fi
         break
      else 
               i=1
               break
      fi
fi
done


if [ $i == 0 ]; then
   echo "Test run finished"
   exit 0
else
   echo "Test run error"
   exit 1
fi