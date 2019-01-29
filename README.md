# Pre-requirements

* docker
* heroku cli

# Deploy
* `heroku container:login`
* `heroku container:push web -a <APP_NAME>`
* `heroku container:release web -a <APP_NAME>`

## Running localy
* `docker build -t sl-time:latest .`
* `docker run -e PORT=5000 -it -p 5000:5000 sl-time:latest`
