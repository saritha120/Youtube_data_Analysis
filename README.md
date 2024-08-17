End-to-End Data Engineering Project on YouTube Data

Project Description:
This project involves creating an end-to-end Data Engineering solution focused on YouTube data. The goal is to gain a deeper understanding of the ETL process and Data Visulization by utilizing Python, PySpark, basic SQL, and AWS tools such as S3, Glue, Lambda, Athena, QuickSight and Redshift. The project is designed to build practical, hands-on experience in data engineering.

Project Overview:
This project is about securely organizing and analyzing structured and semi-structured YouTube data, based on video categories and trending metrics.

DataSet:
https://www.kaggle.com/datasets/datasnaek/youtube-new

This Kaggle dataset is collected using Youtube API. This dataset contains several months of youtube daily trending data for various regions. Each regions data is in a seperate file.Data includes the video title, channel title, publish time, tags, views, likes and dislikes, description, and comment count.The data also includes a category_id field, which varies between regions.

AWS Services used:

Aws IAM   :- AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources.
Amazon S3 :- S3(Simple Storage Service) is an object storage service offering industry-leading scalability, data availability, security, and              performance. We are using S3 to store our raw and Cleansed data in our project.
AWS Glue  :- AWS Glue is a scalable, serverless data integration service that makes it easy to discover, prepare, and combine data for                    analytics, machine learning, and application development.
Aws Lambda:- With AWS Lambda, you can run code without provisioning or managing servers.
Aws Athena:- Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL.
QuickSight:- Amazon QuickSight is a fast business analytics service to build visualizations, perform ad hoc analysis, and quickly get                     business insights from your data

Project Goals:

Data Ingestion — Process of moving data from multiple sources into a storage medium.
ETL System — Process of Extracting raw data and transforming into desired format and storing the data in target source.
Data lake — Central Repositary to store our raw data or data from multiple sources which is S3 in our project.
Scalability — As the size of our data increases, we need to make sure our system scales with it.
Cloud — We can’t process vast amounts of data on our local computer so we need to use the cloud, in this case, we will use AWS.
Reporting — Build a dashboard to get answers to the question we asked earlier


References: https://youtu.be/yZKJFKu49Dk
