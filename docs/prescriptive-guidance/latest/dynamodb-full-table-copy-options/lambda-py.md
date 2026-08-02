---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-full-table-copy-options/lambda-py.html
---

# Using AWS Lambda and Python
<a name="lambda-py"></a>

This solution is similar to the .NET custom implementation solution. However, because this approach uses AWS Lambda, it's a serverless solution. The solution can read directly from the source DynamoDB table and write directly to the target DynamoDB table, or it can use the DynamoDB export feature. Using the export feature requires converting the data so that you can use the DynamoDB API BatchWriteItem operation to write that data to the target table.

This solution works best for DynamoDB tables that are smaller than 500 MB.

## Advantages
<a name="advantages.855d17dc-f66e-5a16-8b17-4fae42e3517c"></a>
+ It's a serverless solution.
+ When the export feature is used, the solution does not consume any provisioned throughput on the source table.

## Drawbacks
<a name="drawbacks.6ed2e5b9-efba-5194-82e5-c0c0838340c3"></a>
+ When reading and writing directly, the solution consumes provisioned throughput on both the source and the target tables, so it can affect performance and availability.
+ The additional AWS service, Lambda, is required, and there is additional code to manage.
+ Lambda has a runtime limit of 15 minutes.
