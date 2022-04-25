# Databricks notebook source
# MAGIC %md
# MAGIC <img src="https://cdn.eleflow.com.br/ef-web/wp-content/uploads/2016/08/21181642/Eleflow.png" alt="Eleflow BigData" width="200"/>
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC # PipeDrive

# COMMAND ----------

## Importing required modules
from pipe_drive import PipeDriveConnection

# COMMAND ----------

## Creating connection with token API
connection = PipeDriveConnection.v1_from_token_api('coloque_o_token_aqui')

# COMMAND ----------

## Getting Service Client that will provides all available service clients
service_client = connection.get_service_client()

# COMMAND ----------

## Getting all deals from DealsService
deals = service_client.deals_service.get_all_deals()

# COMMAND ----------

## Showing deals as DataFrame 
display(
    deals.to_spark_dataframe('data')
)
