---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/python_3_eventbridge_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# EventBridge examples using SDK for Python (Boto3)
<a name="python_3_eventbridge_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Python (Boto3) with EventBridge.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Scenarios](#scenarios)

## Scenarios
<a name="scenarios"></a>

### Use scheduled events to invoke a Lambda function
<a name="cross_LambdaScheduledEvents_python_3_topic"></a>

The following code example shows how to create an AWS Lambda function invoked by an Amazon EventBridge scheduled event.

**SDK for Python (Boto3)**
 This example shows how to register an AWS Lambda function as the target of a scheduled Amazon EventBridge event. The Lambda handler writes a friendly message and the full event data to Amazon CloudWatch Logs for later retrieval.
+ Deploys a Lambda function.
+ Creates an EventBridge scheduled event and makes the Lambda function the target.
+ Grants permission to let EventBridge invoke the Lambda function.
+ Prints the latest data from CloudWatch Logs to show the result of the scheduled invocations.
+ Cleans up all resources created during the demo.
 This example is best viewed on GitHub. For complete source code and instructions on how to set up and run, see the full example on [GitHub](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/lambda#readme).

**Services used in this example**
+ CloudWatch Logs
+ DynamoDB
+ EventBridge
+ Lambda
+ Amazon SNS
