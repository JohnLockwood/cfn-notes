#!/bin/bash 
##########################################################################
# Name:         makevol.sh
# Description:  Creates a volume in us-east-1b
# Usage:        ./makevol.sh
##########################################################################

count_existing=$(aws ec2 describe-volumes --filters Name=tag:Name,Values=BrownbagEC2Volume | jq '.Volumes | length')
if [ "$count_existing" != "0" ]
then
    echo Volume  BrownbagEC2Volume already exists -- exiting!;
    exit 1;
fi

aws ec2 create-volume --encrypted --volume-type "gp3" --availability-zone "us-east-1b"  \
    --tag-specifications 'ResourceType=volume,Tags=[{Key=Name,Value=BrownbagEC2Volume}]' \
     --size 10 > volume_info.txt;
echo Volume details stored in volume_info.txt
cat volume_info.txt