# python-microservice-fastapi
Learn to build your own microservice using Python and FastAPI

## How to run??
 - Make sure you have installed `docker` and `docker-compose`
 - Run `docker-compose up -d`
 - Head over to http://localhost:8080/api/v1/movies/docs for movie service docs 
   and http://localhost:8080/api/v1/casts/docs for cast service docs
   and http://localhost:8080/api/v1/reports/sales_funnel_summary/docs
   and http://localhost:8080/api/v1/reports/docs

## in your /etc/hosts set following


127.0.0.1       reports_service
127.0.0.1       movie_service
127.0.0.1       cast_service
127.0.0.1       reports_dev.ripe.ai

## reference -

https://dev.to/paurakhsharma/microservice-in-python-using-fastapi-24cc

https://towardsdatascience.com/how-to-contain-your-first-django-in-docker-and-access-it-from-aws-fdb0081bdf1d


https://djangoforbeginners.com/hello-world/

SQLITE info
https://www.sqlitetutorial.net/sqlite-tutorial/sqlite-show-tables/
