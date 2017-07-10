#!/bin/sh
value=$(curl https://phitr-us-002.firebaseio.com/beacons/kitchen.json)  
echo $value
