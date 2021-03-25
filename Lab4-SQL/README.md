# Benchmarking different methods in PostgreSQL

* used psycopg2 library to connect to database via python
* comparing bulk loading with individual INSERT statements wrt time-taken
* using CURSORS to reduce fetch time of bulk queries

## Requirements
1. [PostgreSQL](https://www.postgresql.org/)
2. Python
3. [psycopg2](https://pypi.org/project/psycopg2/) - Python library
