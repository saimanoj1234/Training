
#Creating Spark Session Object
spark = SparkSession.builder.appName('data manipulation').getOrCreate()





df_sales=spark.read.option('header','TRUE').csv('C:\\Users\\sm3873\\Downloads\\Products\\Products\\sales.csv',inferSchema='TRUE')
df_sales.show()
df_sales.createOrReplaceTempView("sales")





df_products=spark.read.option('header','TRUE').csv('C:\\Users\\sm3873\\Downloads\\Products\\Products\\products.csv',inferSchema='TRUE')
df_products.show()
df_products.createOrReplaceTempView("products")


#FOR PRODUCT WISE SALES


product_sales = spark.sql(""" SELECT sales.product_id,SUM(sales.num_pieces_sold * products.price) AS product_wise_sales 
                               FROM sales 
                               JOIN products ON sales.product_id = products.product_id 
                               GROUP BY sales.product_id""")






product_sales.createOrReplaceTempView("psales")
product_sales.show()


# FOR HIGHEST PRODUCT WISE SALE

#1.
highest_sales = product_sales.select("product_id","product_wise_sales").orderBy(desc("product_wise_sales")).first()
highest_sales




#2.
highest_sales = spark.sql(""" SELECT MAX(product_wise_sales) 
                              FROM psales
                              """)
highest_sales.show()




#3.
highest_sales2 = product_sales.select("product_id","product_wise_sales").orderBy(desc("product_wise_sales")).limit(5)
highest_sales2.show()
highest_sales3 = spark.sql(""" SELECT * 
                                FROM psales 
                                ORDER BY psales.product_wise_sales DESC 
                                LIMIT 5""")
highest_sales3.show()







