# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://cdn.eleflow.com.br/ef-web/wp-content/uploads/2016/08/21181642/Eleflow.png" alt="Eleflow BigData" width="200"/>
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC # RestAPI

# COMMAND ----------

from rest_api import RestApiRequest

# COMMAND ----------

headers = {
    "Api-Token": "YOUR_TOKEN"
}

# COMMAND ----------

req = RestApiRequest.build('https://symphony-of-destruction.free.beeceptor.com', headers=headers)

# COMMAND ----------

## * args -> Monta rota da url
## url + /api/v2/albuns
## ** kwargs -> ?param=name&color=blue
resp = req.get(*('api','v2','albuns'), **{'user':'caio.araujo@eleflow.com.br', "color":"red"})

# COMMAND ----------



# COMMAND ----------

display(
    resp.to_spark_dataframe('data').orderBy('publication')
)
