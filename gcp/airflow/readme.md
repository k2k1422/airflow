
# Airflow in linux

create all the table and metadata
```
airflow db init
```

create a user name
```
airflow users create --username admin --firstname admin --lastname admin --role Admin --email admin@gmail.com
```

load .env to the cuurent bash
```
set -o allexport; source .env; set +o allexport
```

