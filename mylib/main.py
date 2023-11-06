from pyspark.sql import SparkSession
from pyspark.sql.functions import col, unix_timestamp

# Initialize SparkSession
spark = SparkSession.builder.appName('nyc_taxi_data_processing').getOrCreate()

# Load the dataset
df = spark.read.csv('../data/train.csv', inferSchema=True, header=True)

# Data exploration
df.show()
df.printSchema()

# Data transformation
timeFmt = "yyyy-MM-dd HH:mm:ss"
df = df.withColumn('pickup_time', unix_timestamp(col('pickup_datetime'), timeFmt))
df = df.withColumn('dropoff_time', unix_timestamp(col('dropoff_datetime'), timeFmt))

# Data analysis
df = df.withColumn('actual_duration', (col('dropoff_time') - col('pickup_time')) / 60)
result = df.select('id', 'trip_duration', 'actual_duration')

# Display the first few rows of the result
result.show()

# Save the results
result.coalesce(1).write.option('header', 'true').csv('nyc_taxi_durations.csv')