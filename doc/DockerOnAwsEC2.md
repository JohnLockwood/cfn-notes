# Docker on EC2 Experiment

Installing and running Docker and Docker-Compose on AWS Amaazon Linux 2 instances works fine.

Instructions are [here](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html) for Docker and [here](https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9) for Docker-Compose.  In a nutshell:

```
sudo yum update -y
sudo amazon-linux-extras install docker
sudo yum install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
# Log-out / log-in to refresh user permissions
docker info
docker run --rm hello-world

# Install the latest Docker Compose
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose version
```