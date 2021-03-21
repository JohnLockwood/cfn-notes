stack=brownbag-ec2
file="prod/ec2.yml"
PARAMETERS=""

# count_existing=$(aws ec2 describe-volumes --filters Name=tag:Name,Values=BrownbagEC2Volume | jq '.Volumes | length')
VolumeId=$(aws ec2 describe-volumes --filters Name=tag:Name,Values=BrownbagEC2Volume | jq -r ".Volumes[0].VolumeId")
PARAMETERS="--parameters ParameterKey=VolumeId,ParameterValue=$VolumeId"
echo $PARAMETERS
echo deleting stack if it exists:  "${stack}"
aws cloudformation delete-stack --stack-name "${stack}"

echo waiting for stack to be deleted
aws cloudformation wait stack-delete-complete --stack-name "${stack}"

echo creating stack
./upsert_stack.sh "${stack}" "${file}" "--capabilities CAPABILITY_IAM $PARAMETERS"

