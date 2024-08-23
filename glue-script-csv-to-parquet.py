import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Define and parse script arguments
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Define schema
schema = StructType([
    StructField("video_id", StringType(), True),
    StructField("trending_date", StringType(), True),
    StructField("title", StringType(), True),
    StructField("channel_title", StringType(), True),
    StructField("category_id", IntegerType(), True),
    StructField("publish_time", StringType(), True),
    StructField("tags", StringType(), True),
    StructField("views", IntegerType(), True),
    StructField("likes", IntegerType(), True),
    StructField("dislikes", IntegerType(), True),
    StructField("comment_count", IntegerType(), True),
    StructField("thumbnail_link", StringType(), True),
    StructField("comments_disabled", StringType(), True),
    StructField("ratings_disabled", StringType(), True),
    StructField("video_error_or_removed", StringType(), True),
    StructField("description", StringType(), True),
    StructField("region", StringType(), True)
])

try:
    # Step 1: Read raw CSV data from S3
    raw_df = spark.read.option("header", "true").schema(schema).csv(
        "s3://saritha-de-youtube-raw-data/youtube/raw_statistics/"
    )

    # Extract region information from the file path and add it as a column
    clean_df = raw_df.withColumn("region", F.regexp_extract(F.input_file_name(), r'youtube/raw_statistics/region=([^/]+)', 1))

    # Drop rows with any null values
    clean_df = clean_df.dropna()

    # Convert the DataFrame to a Glue DynamicFrame
    dynamic_frame = DynamicFrame.fromDF(clean_df, glueContext, "dynamic_frame")

    # Step 3: Write the DynamicFrame to S3 in Parquet format with partitioning by region and category_id
    glueContext.write_dynamic_frame.from_options(
        frame=dynamic_frame,
        connection_type="s3",
        format="glueparquet",
        connection_options={"path": "s3://saritha-de-youtube-cleansed-data/youtube1/cleansed_statistics/", "partitionKeys": ["region", "category_id"]},
        format_options={"compression": "snappy"},
        transformation_ctx="dynamic_frame"
    )

    # Commit the job
    job.commit()

except Exception as e:
    sys.exit(1)  # Exit with a non-zero status to indicate failure
