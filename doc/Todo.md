# December tasks:

## Goal:

* Try to get to completed EC2 container with Postgres and back end for now.  Really end to end you have until March, 
and I've now added tasks so relax if can't get this done in December.

## Tasks:

* [] Domain is now hosted at AWS with named hosted zone.  Need to see AWS::Route53::RecordSet -- can wire this into 
ec2.yml stack, this will allow dynamic setup all the way down to DockerCompose -- but no build yet!  We do have a 
buildspec.yml but this was for the lambda function.  Same is true for makefile apparently.   See next two points  
* [] Short term: Get all the lambda-specific stuff into a branch to get it out of the way.  Make sure branch is pushed.  
Note that We have a corresponding manual CodeBuild project, BrownbagLambdaBuild.  We should point that project
at the newly created branch.  
* [] Long term:  Work that branch to stabilize and test the lambda-specific stuff as part of brownbag.

## Tasks completed

* [x] tools/scritps/ec2.sh - Gets DockerCompose installed on an EC2 instance.  Does not yet pull container

* [x] Test stack without key. Works!
* [x] Test ECS optimized EC2 instance.  Got it working but note that I don't see a way to wire this up to ECS trivially, since ECS wants to manage instances itself.  Also note that by default one cannot connect to such an instance.

## Notes for ECS Cluster:

AWS::ECS::Cluster
    AWS::AWS::ECS::CapacityProvider
        - AutoScalingGroupProvider
            AutoScalingGroupArn --> See below AWS::AutoScaling::AutoScalingGroup
        - ManagedScaling

AWS::AutoScaling::AutoScalingGroup
    AWS::EC2::LaunchTemplate (https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html)
        Image ID goes here.  See EC2.yml
        AWS::EC2::LaunchTemplate LaunchTemplateData
    AWS::AutoScaling::AutoScalingGroup MixedInstancesPolicy - This and instances distribution determine # of on-demand, spot, reserved, etc.
        - AWS::AutoScaling::AutoScalingGroup InstancesDistribution