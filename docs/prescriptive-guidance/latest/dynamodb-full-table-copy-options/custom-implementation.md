---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-full-table-copy-options/custom-implementation.html
---

# Using a custom implementation in .NET or Java with AWS SDKs
<a name="custom-implementation"></a>

Instead of relying on other AWS services to perform cross-account table copy, you can build a custom solution using .NET, Java, Python, or another supported programming language. AWS provides SDKs, which allow programmatic access to AWS services or APIs, in multiple languages. This solution requires hands-on development experience in the language that you use.

You can create a console app (or a new API endpoint, if you work on a web API) that can be invoked to perform full table copy. The custom solution should perform the following steps:

1. Delete the DynamoDB table in the target account.

1. Create the DynamoDB table (with on-demand capacity) and indexes in the target account. Alternatively, you can use the provisioned capacity mode and set the RCUs and WCUs according to your needs.

1. Copy data from the source account to the target account, using the DynamoDB batch write operation in AWS SDK to reduce the number of service calls to DynamoDB.

![The custom implementation uses security tokens to access the IAM policies that provide access to the source and target accounts.](http://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-full-table-copy-options/images/guide-img/b39c4f99-8119-4c72-9813-d6420f64f36c/images/8f905e4f-ab6f-449c-96bd-0770b9ac2155.png)

This solution best suits DynamoDB tables that are small in size (less than 500 MB).

For a DynamoDB table with 200 K items (average item size 30 KB and table size of 250 MB), this solution, including table creation and data population, takes about 5 minutes:
+ Capacity mode – Provisioned, with 4000 RCUs and 4000 WCUs
+ Capacity units consumed – 30 K RCUs and approximately 400 K WCUs

## Advantages
<a name="advantages.c81d244e-4190-501e-819b-702d56792579"></a>
+ The solution doesn't depend on any AWS service other than DynamoDB, so there is less maintenance overhead.
+ The solution can be made serverless by using an  AWS Lambda function to run it. However, the runtime must be 15 minutes or less.

## Drawbacks
<a name="drawbacks.a8ee07d1-ca21-54fd-b982-fc0697e7b136"></a>
+ The solution consumes more RCUs and WCUs.
+ It might not be a good solution for large datasets, because the  solution requires active connections with two different DynamoDB tables in two different accounts (using two different security tokens). If the table copy for a large dataset takes a long time, there might be connection disruptions or security token expiry, so you must implement logic to handle those possibilities. You must also implement logic to continue the copy from where it failed.
