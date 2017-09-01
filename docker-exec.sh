#!/bin/bash
# Ask the user for container ID or name
echo Please Enter the container ID or Name?
read varid
echo Dispaching container
exec docker exec -it $varid sh