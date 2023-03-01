


#Importing SparkSession
from  pyspark.sql import SparkSession
from  pyspark.
#Creating Spark Session Object
spark = SparkSession.builder.appName('data manipulation').getOrCreate()
#Reading csv dataset
df_sales = spark.read.csv('C:\\Users\\sm3873\\Downloads\\Products\\Products\\sales.csv')
df_sales.show(10)
df_sales=spark.read.option('header','TRUE').csv('C:\\Users\\sm3873\\Downloads\\Products\\Products\\sales.csv',inferSchema='TRUE')
df_sales.show()
df_sales.createOrReplaceTempView("df_sales")
df_products = spark.read.csv('C:\\Users\\sm3873\\Downloads\\Products\\Products\\products.csv')
df_products.show(10)
df_products=spark.read.option('header','TRUE').csv('C:\\Users\\sm3873\\Downloads\\Products\\Products\\products.csv',inferSchema='TRUE')
df_products.show(10)
df_products.createOrReplaceTempView("df_products")
df_sellers=spark.read.csv('C:\\Users\\sm3873\\Downloads\\Products\\Products\\sellers.csv')
df_sellers=spark.read.option('header','TRUE').csv('C:\\Users\\sm3873\\Downloads\\Products\\Products\\sellers.csv',inferSchema='TRUE')
df_sellers.show(10)
df_sellers.createOrReplaceTempView("df_sellers")
# when ever we have a data first we need to load the data and look into its columns along with its schema etc...

from pyspark.sql.functions import max
a=df_sales.join(df_products,df_sales.product_id == df_products.product_id, "inner").groupby([df_products.product_name,df_products.product_id]).agg(sum(df_sales.num_pieces_sold).alias("sales"))
a.show()
#gives us the product wise sales
highest_sales = a.select("product_id","sales").orderBy(desc("sales")).first()
highest_sales
#gives us the product with highest sales






