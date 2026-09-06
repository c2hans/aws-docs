---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/lambda_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Code examples for Lambda using AWS SDKs
<a name="lambda_code_examples"></a>

The following code examples show you how to use AWS Lambda with an AWS software development kit (SDK).

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

*AWS community contributions* are examples that were created and are maintained by multiple teams across AWS. To provide feedback, use the mechanism provided in the linked repositories.

**More resources**
+  **[ Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)** – More information about Lambda.
+ **[Lambda API Reference](https://docs.aws.amazon.com/lambda/latest/dg/API_Reference.html)** – Details about all available Lambda actions.
+ **[AWS Developer Center](https://aws.amazon.com/developer/code-examples/?awsf.sdk-code-examples-product=product%23lambda)** – Code examples that you can filter by category or full-text search.
+ **[AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)** – GitHub repo with complete code in preferred languages. Includes instructions for setting up and running the code.

**Contents**
+ [Basics](lambda_code_examples_basics.md)
  + [Hello Lambda](lambda_example_lambda_Hello_section.md)
  + [Learn the basics](lambda_example_lambda_Scenario_GettingStartedFunctions_section.md)
  + [Actions](lambda_code_examples_actions.md)
    + [`CreateAlias`](lambda_example_lambda_CreateAlias_section.md)
    + [`CreateFunction`](lambda_example_lambda_CreateFunction_section.md)
    + [`DeleteAlias`](lambda_example_lambda_DeleteAlias_section.md)
    + [`DeleteFunction`](lambda_example_lambda_DeleteFunction_section.md)
    + [`DeleteFunctionConcurrency`](lambda_example_lambda_DeleteFunctionConcurrency_section.md)
    + [`DeleteProvisionedConcurrencyConfig`](lambda_example_lambda_DeleteProvisionedConcurrencyConfig_section.md)
    + [`GetAccountSettings`](lambda_example_lambda_GetAccountSettings_section.md)
    + [`GetAlias`](lambda_example_lambda_GetAlias_section.md)
    + [`GetFunction`](lambda_example_lambda_GetFunction_section.md)
    + [`GetFunctionConcurrency`](lambda_example_lambda_GetFunctionConcurrency_section.md)
    + [`GetFunctionConfiguration`](lambda_example_lambda_GetFunctionConfiguration_section.md)
    + [`GetPolicy`](lambda_example_lambda_GetPolicy_section.md)
    + [`GetProvisionedConcurrencyConfig`](lambda_example_lambda_GetProvisionedConcurrencyConfig_section.md)
    + [`Invoke`](lambda_example_lambda_Invoke_section.md)
    + [`ListFunctions`](lambda_example_lambda_ListFunctions_section.md)
    + [`ListProvisionedConcurrencyConfigs`](lambda_example_lambda_ListProvisionedConcurrencyConfigs_section.md)
    + [`ListTags`](lambda_example_lambda_ListTags_section.md)
    + [`ListVersionsByFunction`](lambda_example_lambda_ListVersionsByFunction_section.md)
    + [`PublishVersion`](lambda_example_lambda_PublishVersion_section.md)
    + [`PutFunctionConcurrency`](lambda_example_lambda_PutFunctionConcurrency_section.md)
    + [`PutProvisionedConcurrencyConfig`](lambda_example_lambda_PutProvisionedConcurrencyConfig_section.md)
    + [`RemovePermission`](lambda_example_lambda_RemovePermission_section.md)
    + [`TagResource`](lambda_example_lambda_TagResource_section.md)
    + [`UntagResource`](lambda_example_lambda_UntagResource_section.md)
    + [`UpdateAlias`](lambda_example_lambda_UpdateAlias_section.md)
    + [`UpdateFunctionCode`](lambda_example_lambda_UpdateFunctionCode_section.md)
    + [`UpdateFunctionConfiguration`](lambda_example_lambda_UpdateFunctionConfiguration_section.md)
+ [Scenarios](lambda_code_examples_scenarios.md)
  + [Automatically confirm known users with a Lambda function](lambda_example_cross_CognitoAutoConfirmUser_section.md)
  + [Automatically migrate known users with a Lambda function](lambda_example_cross_CognitoAutoMigrateUser_section.md)
  + [Create a REST API to track COVID-19 data](lambda_example_cross_ApiGatewayDataTracker_section.md)
  + [Create a lending library REST API](lambda_example_cross_AuroraRestLendingLibrary_section.md)
  + [Create a messenger application](lambda_example_cross_StepFunctionsMessenger_section.md)
  + [Create a rest API with function proxy integration](lambda_example_api_gateway_GettingStarted_087_section.md)
  + [Create a serverless application to manage photos](lambda_example_cross_PAM_section.md)
  + [Create a websocket chat application](lambda_example_cross_ApiGatewayWebsocketChat_section.md)
  + [Create an application to analyze customer feedback](lambda_example_cross_FSA_section.md)
  + [Creating a monitoring dashboard with function name as a variable](lambda_example_cloudwatch_GettingStarted_031_section.md)
  + [Creating your first serverless function](lambda_example_lambda_GettingStarted_019_section.md)
  + [Invoke a Lambda function from a browser](lambda_example_cross_LambdaForBrowser_section.md)
  + [Transform data with S3 Object Lambda](lambda_example_cross_ServerlessS3DataTransformation_section.md)
  + [Use API Gateway to invoke a Lambda function](lambda_example_cross_LambdaAPIGateway_section.md)
  + [Use Step Functions to invoke Lambda functions](lambda_example_cross_ServerlessWorkflows_section.md)
  + [Use scheduled events to invoke a Lambda function](lambda_example_cross_LambdaScheduledEvents_section.md)
  + [Use the Neptune API to query graph data](lambda_example_cross_Neptune_Query_section.md)
  + [Using property variables in monitoring dashboards to monitor multiple serverless functions](lambda_example_iam_GettingStarted_032_section.md)
  + [Write custom activity data with a Lambda function after Amazon Cognito user authentication](lambda_example_cross_CognitoCustomActivityLog_section.md)
+ [Serverless examples](lambda_code_examples_serverless_examples.md)
  + [Connecting to an Amazon RDS database in a Lambda function](lambda_example_serverless_connect_RDS_Lambda_section.md)
  + [Invoke a Lambda function from a Kinesis trigger](lambda_example_serverless_Kinesis_Lambda_section.md)
  + [Invoke a Lambda function from a DynamoDB trigger](lambda_example_serverless_DynamoDB_Lambda_section.md)
  + [Invoke a Lambda function from a Amazon DocumentDB trigger](lambda_example_serverless_DocumentDB_Lambda_section.md)
  + [Invoke a Lambda function from an Amazon MSK trigger](lambda_example_serverless_MSK_Lambda_section.md)
  + [Invoke a Lambda function from an Amazon S3 trigger](lambda_example_serverless_S3_Lambda_section.md)
  + [Invoke a Lambda function from an Amazon SNS trigger](lambda_example_serverless_SNS_Lambda_section.md)
  + [Invoke a Lambda function from an Amazon SQS trigger](lambda_example_serverless_SQS_Lambda_section.md)
  + [Reporting batch item failures for Lambda functions with a Kinesis trigger](lambda_example_serverless_Kinesis_Lambda_batch_item_failures_section.md)
  + [Reporting batch item failures for Lambda functions with a DynamoDB trigger](lambda_example_serverless_DynamoDB_Lambda_batch_item_failures_section.md)
  + [Reporting batch item failures for Lambda functions with an Amazon SQS trigger](lambda_example_serverless_SQS_Lambda_batch_item_failures_section.md)
+ [AWS community contributions](lambda_code_examples_aws_community_contributions.md)
  + [Build and test a serverless application](lambda_example_tributary-lite_serverless-application_section.md)
