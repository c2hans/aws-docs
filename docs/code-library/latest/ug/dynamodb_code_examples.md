---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/dynamodb_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Code examples for DynamoDB using AWS SDKs
<a name="dynamodb_code_examples"></a>

The following code examples show you how to use Amazon DynamoDB with an AWS software development kit (SDK).

*Basics* are code examples that show you how to perform the essential operations within a service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

*AWS community contributions* are examples that were created and are maintained by multiple teams across AWS. To provide feedback, use the mechanism provided in the linked repositories.

**More resources**
+  **[ DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)** – More information about DynamoDB.
+ **[DynamoDB API Reference](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/Welcome.html)** – Details about all available DynamoDB actions.
+ **[AWS Developer Center](https://aws.amazon.com/developer/code-examples/?awsf.sdk-code-examples-product=product%23dynamodb)** – Code examples that you can filter by category or full-text search.
+ **[AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)** – GitHub repo with complete code in preferred languages. Includes instructions for setting up and running the code.

**Contents**
+ [Basics](dynamodb_code_examples_basics.md)
  + [Hello DynamoDB](dynamodb_example_dynamodb_Hello_section.md)
  + [Learn the basics](dynamodb_example_dynamodb_Scenario_GettingStartedMovies_section.md)
  + [Actions](dynamodb_code_examples_actions.md)
    + [`BatchExecuteStatement`](dynamodb_example_dynamodb_BatchExecuteStatement_section.md)
    + [`BatchGetItem`](dynamodb_example_dynamodb_BatchGetItem_section.md)
    + [`BatchWriteItem`](dynamodb_example_dynamodb_BatchWriteItem_section.md)
    + [`CreateTable`](dynamodb_example_dynamodb_CreateTable_section.md)
    + [`DeleteItem`](dynamodb_example_dynamodb_DeleteItem_section.md)
    + [`DeleteTable`](dynamodb_example_dynamodb_DeleteTable_section.md)
    + [`DescribeTable`](dynamodb_example_dynamodb_DescribeTable_section.md)
    + [`DescribeTimeToLive`](dynamodb_example_dynamodb_DescribeTimeToLive_section.md)
    + [`ExecuteStatement`](dynamodb_example_dynamodb_ExecuteStatement_section.md)
    + [`GetItem`](dynamodb_example_dynamodb_GetItem_section.md)
    + [`ListTables`](dynamodb_example_dynamodb_ListTables_section.md)
    + [`PutItem`](dynamodb_example_dynamodb_PutItem_section.md)
    + [`Query`](dynamodb_example_dynamodb_Query_section.md)
    + [`Scan`](dynamodb_example_dynamodb_Scan_section.md)
    + [`UpdateItem`](dynamodb_example_dynamodb_UpdateItem_section.md)
    + [`UpdateTable`](dynamodb_example_dynamodb_UpdateTable_section.md)
    + [`UpdateTimeToLive`](dynamodb_example_dynamodb_UpdateTimeToLive_section.md)
+ [Scenarios](dynamodb_code_examples_scenarios.md)
  + [Accelerate reads with DAX](dynamodb_example_dynamodb_Usage_DaxDemo_section.md)
  + [Advanced Global Secondary Index scenarios](dynamodb_example_dynamodb_Scenario_GSIAdvanced_section.md)
  + [Build an app to submit data to a DynamoDB table](dynamodb_example_cross_SubmitDataApp_section.md)
  + [Compare multiple values with a single attribute](dynamodb_example_dynamodb_Scenario_CompareMultipleValues_section.md)
  + [Conditionally update an item's TTL](dynamodb_example_dynamodb_UpdateItemConditionalTTL_section.md)
  + [Connect to a local instance](dynamodb_example_dynamodb_local_section.md)
  + [Count expression operators](dynamodb_example_dynamodb_Scenario_ExpressionOperatorCounting_section.md)
  + [Create a REST API to track COVID-19 data](dynamodb_example_cross_ApiGatewayDataTracker_section.md)
  + [Create a messenger application](dynamodb_example_cross_StepFunctionsMessenger_section.md)
  + [Create a serverless application to manage photos](dynamodb_example_cross_PAM_section.md)
  + [Create a table with global secondary index](dynamodb_example_dynamodb_CreateTableWithGlobalSecondaryIndex_section.md)
  + [Create a table with warm throughput enabled](dynamodb_example_dynamodb_CreateTableWarmThroughput_section.md)
  + [Create a web application to track DynamoDB data](dynamodb_example_cross_DynamoDBDataTracker_section.md)
  + [Create a websocket chat application](dynamodb_example_cross_ApiGatewayWebsocketChat_section.md)
  + [Create an item with a TTL](dynamodb_example_dynamodb_PutItemTTL_section.md)
  + [Create and manage MRSC global tables](dynamodb_example_dynamodb_Scenario_MRSCGlobalTables_section.md)
  + [Create and manage global tables demonstrating MREC](dynamodb_example_dynamodb_Scenario_GlobalTableOperations_section.md)
  + [Delete data using PartiQL DELETE](dynamodb_example_dynamodb_PartiQLDelete_section.md)
  + [Detect PPE in images](dynamodb_example_cross_RekognitionPhotoAnalyzerPPE_section.md)
  + [Getting started with NoSQL databases](dynamodb_example_dynamodb_GettingStarted_070_section.md)
  + [Insert data using PartiQL INSERT](dynamodb_example_dynamodb_PartiQLInsert_section.md)
  + [Invoke a Lambda function from a browser](dynamodb_example_cross_LambdaForBrowser_section.md)
  + [Manage Global Secondary Indexes](dynamodb_example_dynamodb_Scenario_GSILifecycle_section.md)
  + [Manage resource-based policies](dynamodb_example_dynamodb_Scenario_ResourcePolicyLifecycle_section.md)
  + [Monitor DynamoDB performance](dynamodb_example_cross_MonitorDynamoDB_section.md)
  + [Perform advanced query operations](dynamodb_example_dynamodb_Scenario_AdvancedQueryTechniques_section.md)
  + [Perform list operations](dynamodb_example_dynamodb_Scenario_ListOperations_section.md)
  + [Perform map operations](dynamodb_example_dynamodb_Scenario_MapOperations_section.md)
  + [Perform set operations](dynamodb_example_dynamodb_Scenario_SetOperations_section.md)
  + [Query a table by using batches of PartiQL statements](dynamodb_example_dynamodb_Scenario_PartiQLBatch_section.md)
  + [Query a table using PartiQL](dynamodb_example_dynamodb_Scenario_PartiQLSingle_section.md)
  + [Query a table using a Global Secondary Index](dynamodb_example_dynamodb_Scenarios_QueryWithGlobalSecondaryIndex_section.md)
  + [Query a table using a begins\_with condition](dynamodb_example_dynamodb_Scenarios_QueryWithBeginsWithCondition_section.md)
  + [Query a table using a date range](dynamodb_example_dynamodb_Scenarios_QueryWithDateRange_section.md)
  + [Query a table with a complex filter expression](dynamodb_example_dynamodb_Scenarios_QueryWithComplexFilter_section.md)
  + [Query a table with a dynamic filter expression](dynamodb_example_dynamodb_Scenarios_QueryWithDynamicFilter_section.md)
  + [Query a table with a filter expression and limit](dynamodb_example_dynamodb_Scenarios_QueryWithFilterAndLimit_section.md)
  + [Query a table with nested attributes](dynamodb_example_dynamodb_Scenarios_QueryWithNestedAttributes_section.md)
  + [Query a table with pagination](dynamodb_example_dynamodb_Scenarios_QueryWithPagination_section.md)
  + [Query a table with strongly consistent reads](dynamodb_example_dynamodb_Scenarios_QueryWithStronglyConsistentReads_section.md)
  + [Query data using PartiQL SELECT](dynamodb_example_dynamodb_PartiQLSelect_section.md)
  + [Query for TTL items](dynamodb_example_dynamodb_QueryFilteredTTL_section.md)
  + [Query tables using date and time patterns](dynamodb_example_dynamodb_Scenario_DateTimeQueries_section.md)
  + [Save EXIF and other image information](dynamodb_example_cross_DetectLabels_section.md)
  + [Set up Attribute-Based Access Control](dynamodb_example_dynamodb_Scenario_ABACSetup_section.md)
  + [Understand update expression order](dynamodb_example_dynamodb_Scenario_UpdateExpressionOrder_section.md)
  + [Update a table's warm throughput setting](dynamodb_example_dynamodb_UpdateTableWarmThroughput_section.md)
  + [Update an item's TTL](dynamodb_example_dynamodb_UpdateItemTTL_section.md)
  + [Update data using PartiQL UPDATE](dynamodb_example_dynamodb_PartiQLUpdate_section.md)
  + [Use API Gateway to invoke a Lambda function](dynamodb_example_cross_LambdaAPIGateway_section.md)
  + [Use Step Functions to invoke Lambda functions](dynamodb_example_cross_ServerlessWorkflows_section.md)
  + [Use a document model](dynamodb_example_dynamodb_MidLevelInterface_section.md)
  + [Use a high-level object persistence model](dynamodb_example_dynamodb_HighLevelInterface_section.md)
  + [Use atomic counter operations](dynamodb_example_dynamodb_Scenario_AtomicCounterOperations_section.md)
  + [Use conditional operations](dynamodb_example_dynamodb_Scenario_ConditionalOperations_section.md)
  + [Use expression attribute names](dynamodb_example_dynamodb_Scenario_ExpressionAttributeNames_section.md)
  + [Use scheduled events to invoke a Lambda function](dynamodb_example_cross_LambdaScheduledEvents_section.md)
  + [Work with Local Secondary Indexes](dynamodb_example_dynamodb_Scenario_LSIExamples_section.md)
  + [Work with Streams and Time-to-Live](dynamodb_example_dynamodb_Scenario_StreamsAndTTL_section.md)
  + [Work with global tables and multi-Region replication eventual consistency (MREC)](dynamodb_example_dynamodb_Scenario_MultiRegionReplication_section.md)
  + [Work with resource tagging](dynamodb_example_dynamodb_Scenario_TaggingExamples_section.md)
  + [Work with table encryption](dynamodb_example_dynamodb_Scenario_EncryptionExamples_section.md)
+ [Serverless examples](dynamodb_code_examples_serverless_examples.md)
  + [Invoke a Lambda function from a DynamoDB trigger](dynamodb_example_serverless_DynamoDB_Lambda_section.md)
  + [Reporting batch item failures for Lambda functions with a DynamoDB trigger](dynamodb_example_serverless_DynamoDB_Lambda_batch_item_failures_section.md)
+ [AWS community contributions](dynamodb_code_examples_aws_community_contributions.md)
  + [Build and test a serverless application](dynamodb_example_tributary-lite_serverless-application_section.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
