### AWS Lambda Function - using arguments

- Python 3.11 as Runtime

`def lambda_handler(event, context):`

**lambda_handler** 

- is the entry point for your function. 
- It's a specific function within your code that Lambda invokes when the function is triggered. 
- It require 2 argument

**event**  

- The input data that triggers your Lambda function. 
- It can come from various sources, such as API Gateway requests, S3 bucket changes, or scheduled events from CloudWatch. 
- The event data is passed to your Lambda handler as an argument, typically in a JSON format.

**context** 

- The context object provides information about the execution environment and allows your Lambda function to interact with AWS services. 

--------------------------------------------------------------------------------------------------------------------------------------------------


### Event JSON Test Key-Values

`{
  "stockUnits": "10",
  "stockPrice": "200"
}`

--------------------------------------------------------------------------------------------------------------------------------------------------
