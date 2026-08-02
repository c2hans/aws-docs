---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_cloudformation_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# CloudFormation examples using SDK for Python (Boto3)
<a name="python_3_cloudformation_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with CloudFormation.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Scenarios](#scenarios)

## Scenarios
<a name="scenarios"></a>

### Create a REST API to track COVID-19 data
<a name="cross_ApiGatewayDataTracker_python_3_topic"></a>

The following code example shows how to create a REST API that simulates a system to track daily cases of COVID-19 in the United States, using fictional data.

**SDK for Python (Boto3)**
 Shows how to use AWS Chalice with the AWS SDK for Python (Boto3) to create a serverless REST API that uses Amazon API Gateway, AWS Lambda, and Amazon DynamoDB. The REST API simulates a system that tracks daily cases of COVID-19 in the United States, using fictional data. Learn how to:
+ Use AWS Chalice to define routes in Lambda functions that are called to handle REST requests that come through API Gateway.
+ Use Lambda functions to retrieve and store data in a DynamoDB table to serve REST requests.
+ Define table structure and security role resources in an AWS CloudFormation template.
+ Use AWS Chalice and CloudFormation to package and deploy all necessary resources.
+ Use CloudFormation to clean up all created resources.
 For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/cross_service/apigateway_covid-19_tracker).

**Services used in this example**
+ API Gateway
+ CloudFormation
+ DynamoDB
+ Lambda
