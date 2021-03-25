# Benchmarking different methods in PostgreSQL

* used psycopg2 library to connect to database via python
* comparing bulk loading with individual INSERT statements wrt time-taken
* using CURSORS to reduce fetch time of bulk queries