Nginx uWSGI Flask Stack
=======================

Lightweight web app stack:

React - Nginx - uWSGI - Flask - PostgreSQL

Flask used to serve ``/api``
Nginx used to serve static content at ``/``

Containerised:

- Nginx
- Flask with uWSGI server
- PostgreSQL
- Adminer for managing db

``./shared`` is used to share a UNIX socket between the Nginx and uWSGI container.

Usage
-----

Start service

```bash
$ docker-compose up
```

Database
--------

The PostgreSQL database can be access via Adminer:
localhost:8080

System: PostgresSQL
Server: db
Username: postgres
Password: docker

Volume ./db mounts to /var/lib/postgresql/data to allow for persistence.

Password
--------
Use ``printf 'docker' > password`` in ./devsecrets to set password


TODO:
-----

- Handling permissions - https://denibertovic.com/posts/handling-permissions-with-docker-volumes/

Related links:
--------------
Stack: https://www.patricksoftwareblog.com/using-docker-for-flask-application-development-not-just-production/
