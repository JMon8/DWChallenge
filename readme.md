## Running the Application

### Prerequisites
* Python3 must be installed
  
The main files to run this demo are ```main.py``` and ```requirements.txt```

* Navigate to this folder from the command line and run
  * ```pip install requirements.txt```
* Then run the following command
  * ```python main.py```
* The resulting csvs will be written to the ```outputs/``` directory

## Architecture Overview
Using python and pandas, we will call the API, page through the results, then start processing

For AWS, 
* to keep things simple, I'd place this code in an AWS Lambda that we can schedule to run using serverless
* Utilize AWS Redshift and write the resulting dataframes to tables using the "pandas.DataFrame.to_sql" function
  * *Note: For bigger datasets, we may want to write the csvs to S3 first*  
* To leverage Databricks instead of redshift
  * Import the databricks-connect python package
  * Write the dataframes as delta tables
  