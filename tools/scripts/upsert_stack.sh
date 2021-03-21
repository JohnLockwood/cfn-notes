#!/bin/bash 
##########################################################################
# Name:         scripts/upsert_stack.sh
# Description:  Ensures local CloudFormation directory is synced to an S3
#               location because CloudFormation.  Then updates the given
#               stack from the given cloudformation script.  Note that the 
#               region will be the AWS config default.
# Usage:        $1 stack-name 
#               $2 filename  - You should run this script from the tools/cfn
#                 directory and specify a relative path to the file.  For
#                 example ../scripts/upsert_stack.sh database prod/db.yml
#               $3 remaining options to be passed to create-stack
#                 (NOTE:  this sample not matched  db example above)
#                   --parameters \
#                   ParameterKey=Password,ParameterValue=DoubleSecretPr0bat10n \
#                   --capabilities CAPABILITY_IAM
#               Example:
#               ./upsert_stack.sh testing-is-good IAMAppRole.cfn \
#                   --parameters \
#                   ParameterKey=Password,ParameterValue=DoubleSecretPr0bat10n \ 
#                   --capabilities CAPABILITY_IAM               
#               JCL todo note there is more usage for editing bucket
#               and local path -- document!
# Hat tip:      Thanks to https://bit.ly/3dWs82F for some modified parts.
#               
##########################################################################

stack=$1
cfn_file=$2
opts=${@:3}

# JCL todo input checking

get_abs_dirname() {
  relative_directory=$1 
  pushd $relative_directory > /dev/null;
  pwd;
  popd > /dev/null;
}


S3_BUCKET=brownbag-api-deployment
DIRECTORY=cloudformation
SYNC_URL=s3://$S3_BUCKET/$DIRECTORY
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
LOCAL_DIR="${SCRIPT_DIR}/../cfn"
DIR=$(get_abs_dirname $LOCAL_DIR)


echo "Syncing $DIR to $SYNC_URL"

aws s3 sync "$DIR" "$SYNC_URL"

if ! $(aws cloudformation describe-stacks --stack-name $stack > /dev/null 2>&1)
then
    echo "Stack $stack does not exist, creating...";
    aws cloudformation create-stack --stack-name $stack --template-url $(aws s3 presign "${SYNC_URL}/${cfn_file}") $opts
else
    echo "Stack $stack exists, updating...";
    aws cloudformation update-stack --stack-name $stack --template-url $(aws s3 presign "${SYNC_URL}/${cfn_file}") $opts
fi

