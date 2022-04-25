# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://cdn.eleflow.com.br/ef-web/wp-content/uploads/2016/08/21181642/Eleflow.png" alt="Eleflow BigData" width="200"/>
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC # SQL DB

# COMMAND ----------

### IMPORTING CONNECTOR MODULE ###

from sql_db import DB

# COMMAND ----------

### SET TEST PARAMETERS REQUIRED ###

DB_TYPE = "TYPE_OF_DATABASE"        # Examples: "mysql" or "sqlserver"
DB_DOMAIN = "DATABASE_DOAMIN_URL"   # Example: "myhost1"
DB_NAME = "DATABASE_NAME"           # Example: "master"

USERNAME = "DATABASE_LOGIN_USERNAME"
PASSWORD = "DATABASE_LOGIN_PASSWORD"

QUERY = "SELECT * FROM table WHERE column='value'"

TABLE = "DATABASE_TABLE"

# COMMAND ----------

### SETTING CONNECTION PARAMETERS ###

db_obj = DB(DB_TYPE, DB_DOMAIN, DB_NAME, USERNAME, PASSWORD)

# COMMAND ----------

### QUERYING TEST ###

db_obj.read_query(QUERY)

# COMMAND ----------

### GETTING TABLE TEST ###

db_obj.get_full_table(TABLE)
