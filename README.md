# dbfiles
Compile database files into makeself archive


## Developer environment

```bash
# task runner for python
sudo pip3 install invoke
```

## Запуск скрипта из корня проекта

```bash
PYTHONPATH=$PWD python3 ./dbfiles/main.py  --schema <schema.yaml> --name <name>
```

## schema.yaml

```yaml
before:
  - schema.yaml
  - schema2.yaml

main:
  - =#: CREATE SCHEMA IF NOT EXISTS test
  - sql: table.sql
  - yaml: file.yaml =# INSERT INTO test(name, value) VALUES('{file}', '{value}')
  - yaml: file.yaml =# INSERT INTO test(key, value) VALUES('key1', '{value}'->>'key1', 'key2', '{value}'->> key2)
  - json: file.json =# INSERT INTO test(name, value) VALUES('{file}', '{value}')
  - json: file.json =# INSERT INTO test(key, value) VALUES('key1', '{value}'->>'key1', 'key2', '{value}'->> key2)
  - csv: file.csv =# COPY TO test(col1, col2, col3) FROM '{file}' WITH CSV HEADER
  - csv: file.csv =# COPY TO test(col1, col2, col3) FROM '{file}' WITH CSV

after:
  - schema3.yaml
  - schema4.yaml

```

 * **=#** - execute inline sql query
 * **sql** - execute sql file
 * **yaml** - load yaml file then execute query. {file} - yaml file path, {value} - loaded data
 * **json** - load json file then execute query. {file} - json file path, {value} - loaded data
 * **csv** - define csv file path then execute query. {file} - defined csv file path
