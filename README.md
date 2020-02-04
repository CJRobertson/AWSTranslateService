# Introduction
This service provides an interface for having text translated by Amazon Web Services 'Translate' service. Behind a Gunicorn web server is a
flask application. The flask application accepts a JSON formatted POST request and returns a JSON formatted response containing the translated text.


# Requirements
1. Python installed on a Linux based server.

2. The following packages to be installed in the Python environment:
   - boto3 (the SDK for AWS services)
   - flask (provides the web framework for handling HTTP requests)
   - gunicorn (provides the web server)
   - cerberus (error handling)

# Usage
There are two ways to go about using this application. You can either run the Gunicorn web server directly on something like an EC2 instance from Amazon, or you can run it in a container system like Kubernetes. Both of these will require environment variables for the application to run correctly.

## Environment Variables
```
export AWS_ACCESS_KEY_ID="KEY ID"
export AWS_SECRET_ACCESS_KEY="ACCESS KEY"
export APP_SETTINGS="development" (or can be switched to production)
```

The same enviornment variables should be used if you are wanting to use containerzation, but the format should look like the following before creating the docker image.
```
AWS_ACCESS_KEY_ID=KEY ID
AWS_SECRET_ACCESS_KEY=ACCESS KEY
APP_SETTINGS=development
```

## Starting Gunicorn
You can use the following command if you're just wanting to run this application on a single server without containerization. This command assumes you have navigated to the root directory of the translate service. Note that you must have enviroment variables setup otherwise it'll error out.
```
gunicorn -b :5000 --access-logfile - --error-logfile - app:app
```

## Docker
Running a docker image consists of using the below command if not utilizing something like Kubernetes. By default, the IP address is 0.0.0.0 which points to the local host. The :8000 port routes incoming request to the Gunicorn web server on port :5000. Both of these can be changed as needed.
```
docker run --env-file=.env -p 0.0.0.0:8000:5000 -d *image ID*
```
