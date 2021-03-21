# CloudFormation Notes

## Needs:

* Can use cfn_nag (https://github.com/stelligent/cfn_nag)
* Best practices doc is here: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html

CLI:
```
aws cloudformation
alias cfn='aws cloudformation'
```

## Some examples in ../tools/cfn/ and children

## To validate template:

Locally:
```
cfn validate-template --template-body file://somefile.yml
```

## To create a change-set for a stack that doesn't exist:

```
cfn create-change-set --change-set-name test --change-set-type CREATE --stack-name test --template-body file://ec2_ecs_optimized_ami.yml
{
    "Id": "arn:aws:cloudformation:us-east-1:363498436337:changeSet/test/6b08572d-41b7-4756-85ed-bc7ae199c3a7",
    "StackId": "arn:aws:cloudformation:us-east-1:363498436337:stack/test/026146c0-88c0-11eb-b59e-12eb925008c9"
}

# Can then do
cfn describe-change-set --change-set-name "arn:aws:cloudformation:us-east-1:363498436337:changeSet/test/6b08572d-41b7-4756-85ed-bc7ae199c3a7" > change-set-info.json

```

## Create a bucket and copy a file

```
aws s3 mb s3://codesolid-cfn-delme
aws s3 cp somefile.yml s3://codesolid-cfn-delme
```
