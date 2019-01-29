heroku container:login
heroku container:push web -a slio
heroku container:release web -a slio
