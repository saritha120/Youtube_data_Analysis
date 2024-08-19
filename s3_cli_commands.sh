## Using command line interface to upload data to S3
## To copy files from local machine to s3 recursively which exclude everything other than files whose type is json.
aws s3 cp . s3://saritha-de-youtube-raw-data/youtube/raw_statistics_reference_data/ --recursive --exclude "*" --include "*.json"

##To copy files from local machine to s3 in their own locations
aws s3 cp CAvideos.csv s3://saritha-de-youtube-raw-data/youtube/raw_statistics/region=ca/
aws s3 cp DEvideos.csv s3://saritha-de-youtube-raw-data/youtube/raw_statistics/region=de/
aws s3 cp FRvideos.csv s3://saritha-de-youtube-raw-data/youtube/raw_statistics/region=fr/
aws s3 cp GBvideos.csv s3://saritha-de-youtube-raw-data/youtube/raw_statistics/region=gb/
aws s3 cp INvideos.csv s3://saritha-de-youtube-raw-data/youtube/raw_statistics/region=in/
aws s3 cp JPvideos.csv s3://saritha-de-youtube-raw-data/youtube/raw_statistics/region=jp/
aws s3 cp KRvideos.csv s3://saritha-de-youtube-raw-data/youtube/raw_statistics/region=kr/
aws s3 cp MXvideos.csv s3://saritha-de-youtube-raw-data/youtube/raw_statistics/region=mx/
aws s3 cp RUvideos.csv s3://saritha-de-youtube-raw-data/youtube/raw_statistics/region=ru/
aws s3 cp USvideos.csv s3://saritha-de-youtube-raw-data/youtube/raw_statistics/region=us/
