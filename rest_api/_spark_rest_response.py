import requests
from pyspark.sql.types import *
from pyspark.sql import SparkSession

class SparkRestResponse:
    
    def __init__(self, response: requests.Response) -> None:
        self.response = response
        
    def to_spark_dataframe(self, key = None, schema = None):
        _SPARK = SparkSession.builder.getOrCreate()
        json = self.response.json().get(key) if key else self.response.json()
        if type(json) is not list:
            json = [json]
        schema = self._create_schema_from_json(json)
        return _SPARK.createDataFrame(_SPARK.sparkContext.parallelize(json), schema)

    def _create_schema_from_json(self, obj):
        struct_types = []
        for key, value in obj[0].items():
            try:
                if type(value) is int:
                    struct_types.append(StructField(key.lower().replace(' ', '_'), IntegerType(), True))
                elif type(value) is float:
                    struct_types.append(StructField(key.lower().replace(' ', '_'), FloatType(), True))
                elif type(value) is bool:
                    struct_types.append(StructField(key.lower().replace(' ', '_'), BooleanType(), True))
                else:
                    struct_types.append(StructField(key.lower().replace(' ', '_'), StringType(), True))
            except IndexError as ie:
                struct_types.append(StructField(key.lower().replace(' ', '_'), StringType(), True))

        return StructType(struct_types)
    
    def to_json(self):
        return self.response.json()
    
    def to_text(self):
        return self.response.text
