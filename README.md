# python-docker

A simple Python app for [Docker's Python Language Guide](https://docs.docker.com/language/python).

# DFF Copied Over

- I copied over some of the scripts from the website to make easier to cut and paste.

## Run a simple test.

```
# This is not necessary becaise I am in the directory
# cd /path/to/python-docker

# Create a virtual environment. https://docs.python.org/3/library/venv.html
python3 -m venv .venv

# Activate the virtual environment.
source .venv/bin/activate

# Install dependencies. This is an example of one of the 12 Factor Rules --> Declare dependencies.
(.venv) $ python3 -m pip install -r requirements.txt

# Run the application and access from a browser
(.venv) $ python3 -m flask run

# CNTL-C to end application

# Exit virtual environment.
deactivate
```

## Docker

- The command example is in beta and I am not using that version of Docker.


- So, I went old school and wrote the files following a different example.  https://medium.com/geekculture/how-to-dockerize-your-flask-application-2d0487ecefb8

- Commands:
  - ```docker build -t donff2j/e6156-flask .```
  - ```docker images``` (I have a lot of images)
  - ```docker run -p 5001:5001 donff2j/e6156-flask```
  - ```docker push donff2j/e6156-flask``` (This step pushed an image for your architecture)

- I committed and pushed the project. 

## EC2

- I used an Amazon Linux instance.


- I followed this example: https://medium.com/appgambit/part-1-running-docker-on-aws-ec2-cbcf0ec7c3f8
  - ```sudo yum update -y```
  - ```sudo service docker start```
  - ```sudo usermod -a -G docker ec2-user```


- I cloned the project instead of pulling the container because my Mac is ARM.


- There is a way to "build" on ARM for an Intel chipset. I am lazy.


- I built the Dockerfile and then used ```curl localhost:5001```


- I now need to modify the service group to get to port 5001. Go through the instance to security group and add a rule.


- Go into the console and get the EC2 instances public IP address. You can now access the app on 5001.


- Pull the Docker container ```docker pull donff2/e6156-flask```


- I used an Amazon Linux instance.
- 

## Some Helpful Commands

- Kill a process on a port (MacOS): ```lsof -i tcp:3000```