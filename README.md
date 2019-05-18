Nginx uWSGI Flask Stack
=======================

Simple stack for serving apis

Flask is used to serve ``/api``
Nginx is used to serve static content at ``/``

Containerised:

- Nginx
- Flask uWSGI server


``./shared`` is used to share a UNIX socket between the Nginx and uWSGI container.


Related link: https://www.patricksoftwareblog.com/using-docker-for-flask-application-development-not-just-production/
