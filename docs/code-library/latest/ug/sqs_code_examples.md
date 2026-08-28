---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sqs_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Code examples for Amazon SQS using AWS SDKs
<a name="sqs_code_examples"></a>

The following code examples show you how to use Amazon Simple Queue Service with an AWS software development kit (SDK).

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

**More resources**
+  **[ Amazon SQS Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)** – More information about Amazon SQS.
+ **[Amazon SQS API Reference](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/Welcome.html)** – Details about all available Amazon SQS actions.
+ **[AWS Developer Center](https://aws.amazon.com/developer/code-examples/?awsf.sdk-code-examples-product=product%23sqs)** – Code examples that you can filter by category or full-text search.
+ **[AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)** – GitHub repo with complete code in preferred languages. Includes instructions for setting up and running the code.

**Contents**
+ [Basics](sqs_code_examples_basics.md)
  + [Hello Amazon SQS](sqs_example_sqs_Hello_section.md)
  + [Actions](sqs_code_examples_actions.md)
    + [`AddPermission`](sqs_example_sqs_AddPermission_section.md)
    + [`ChangeMessageVisibility`](sqs_example_sqs_ChangeMessageVisibility_section.md)
    + [`ChangeMessageVisibilityBatch`](sqs_example_sqs_ChangeMessageVisibilityBatch_section.md)
    + [`CreateQueue`](sqs_example_sqs_CreateQueue_section.md)
    + [`DeleteMessage`](sqs_example_sqs_DeleteMessage_section.md)
    + [`DeleteMessageBatch`](sqs_example_sqs_DeleteMessageBatch_section.md)
    + [`DeleteQueue`](sqs_example_sqs_DeleteQueue_section.md)
    + [`GetQueueAttributes`](sqs_example_sqs_GetQueueAttributes_section.md)
    + [`GetQueueUrl`](sqs_example_sqs_GetQueueUrl_section.md)
    + [`ListDeadLetterSourceQueues`](sqs_example_sqs_ListDeadLetterSourceQueues_section.md)
    + [`ListQueues`](sqs_example_sqs_ListQueues_section.md)
    + [`PurgeQueue`](sqs_example_sqs_PurgeQueue_section.md)
    + [`ReceiveMessage`](sqs_example_sqs_ReceiveMessage_section.md)
    + [`RemovePermission`](sqs_example_sqs_RemovePermission_section.md)
    + [`SendMessage`](sqs_example_sqs_SendMessage_section.md)
    + [`SendMessageBatch`](sqs_example_sqs_SendMessageBatch_section.md)
    + [`SetQueueAttributes`](sqs_example_sqs_SetQueueAttributes_section.md)
+ [Scenarios](sqs_code_examples_scenarios.md)
  + [Create a messaging application](sqs_example_cross_SQSMessageApp_section.md)
  + [Create a messenger application](sqs_example_cross_StepFunctionsMessenger_section.md)
  + [Create an Amazon Textract explorer application](sqs_example_cross_TextractExplorer_section.md)
  + [Create and publish to a FIFO topic](sqs_example_sns_PublishFifoTopic_section.md)
  + [Detect people and objects in a video](sqs_example_cross_RekognitionVideoDetection_section.md)
  + [Manage large messages using S3](sqs_example_sqs_Scenario_SqsExtendedClient_section.md)
  + [Process S3 event notifications](sqs_example_s3_Scenario_ProcessS3EventNotification_section.md)
  + [Publish messages to queues](sqs_example_sqs_Scenario_TopicsAndQueues_section.md)
  + [Send and receive batches of messages](sqs_example_sqs_Scenario_SendReceiveBatch_section.md)
  + [Use the AWS Message Processing Framework for .NET with Amazon SQS](sqs_example_cross_MessageProcessingFrameworkTutorial_section.md)
  + [Use the Amazon SQS Java Messaging Library to work with the JMS interface](sqs_example_sqs_Scenario_UseJMS_section.md)
  + [Work with queue tags](sqs_example_sqs_Scenario_WorkWithTags_section.md)
+ [Serverless examples](sqs_code_examples_serverless_examples.md)
  + [Invoke a Lambda function from an Amazon SQS trigger](sqs_example_serverless_SQS_Lambda_section.md)
  + [Reporting batch item failures for Lambda functions with an Amazon SQS trigger](sqs_example_serverless_SQS_Lambda_batch_item_failures_section.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
