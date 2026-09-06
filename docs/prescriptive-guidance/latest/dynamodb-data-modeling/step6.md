---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-data-modeling/step6.html
---

# Step 6. Create the data queries
<a name="step6"></a>

## Objective
<a name="obj6"></a>
+ Create the main queries to validate the data model.

## Process
<a name="proc6"></a>
+ Database engineer manually creates a DynamoDB table in the AWS Region or on their computer (DynamoDB Local).
+ Database engineer adds sample data to the DynamoDB table.
+ Database engineer builds facets using the NoSQL Workbench for Amazon DynamoDB or the AWS SDK for Java or Python to build sample queries (see [blog post](https://medium.com/@synchrophoto/facets-in-nosql-workbench-for-amazon-dynamodb-dadc8267523b)).

  Facets are like a view of the DynamoDB table.
+ Database engineer and cloud developer build sample queries by using the AWS Command Line Interface (AWS CLI) or AWS SDK for the preferred language.

## Tools and resources
<a name="tools6"></a>
+ An active AWS account, to gain access to the DynamoDB console
+ [DynamoDB Local](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html) (optional), if you want to build the database on your computer without accessing the DynamoDB web service
+ [NoSQL Workbench for Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.settingup.html) (download and documentation)
+ [AWS SDK](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.html) in your choice of language (JavaScript, Python, PHP, .NET, Ruby, Java, Go, Node.js, C\+\+, and SAP ABAP)

## RACI
<a name="raci6"></a>

|
|
| Business user | Business analyst | Solutions architect | Database engineer | Application developer | DevOps engineer |
| --- |--- |--- |--- |--- |--- |
| I | I | I | R/A | R |   |

## Outputs
<a name="outputs6"></a>
+ Code to query the DynamoDB table

## Examples
<a name="sample6"></a>
+ [DynamoDB examples using the AWS SDK for Java](https://docs.aws.amazon.com/sdk-for-java/v2/developer-guide/examples-dynamodb.html)
+ [Python examples](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html)
+ [JavaScript examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/dynamodb-examples.html)
