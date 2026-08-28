---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sns_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Code examples for Amazon SNS using AWS SDKs
<a name="sns_code_examples"></a>

The following code examples show you how to use Amazon Simple Notification Service with an AWS software development kit (SDK).

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

**More resources**
+  **[ Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)** – More information about Amazon SNS.
+ **[Amazon SNS API Reference](https://docs.aws.amazon.com/sns/latest/api/welcome.html)** – Details about all available Amazon SNS actions.
+ **[AWS Developer Center](https://aws.amazon.com/developer/code-examples/?awsf.sdk-code-examples-product=product%23sns)** – Code examples that you can filter by category or full-text search.
+ **[AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)** – GitHub repo with complete code in preferred languages. Includes instructions for setting up and running the code.

**Contents**
+ [Basics](sns_code_examples_basics.md)
  + [Hello Amazon SNS](sns_example_sns_Hello_section.md)
  + [Actions](sns_code_examples_actions.md)
    + [`CheckIfPhoneNumberIsOptedOut`](sns_example_sns_CheckIfPhoneNumberIsOptedOut_section.md)
    + [`ConfirmSubscription`](sns_example_sns_ConfirmSubscription_section.md)
    + [`CreateTopic`](sns_example_sns_CreateTopic_section.md)
    + [`DeleteTopic`](sns_example_sns_DeleteTopic_section.md)
    + [`GetSMSAttributes`](sns_example_sns_GetSMSAttributes_section.md)
    + [`GetTopicAttributes`](sns_example_sns_GetTopicAttributes_section.md)
    + [`ListPhoneNumbersOptedOut`](sns_example_sns_ListPhoneNumbersOptedOut_section.md)
    + [`ListSubscriptions`](sns_example_sns_ListSubscriptions_section.md)
    + [`ListTopics`](sns_example_sns_ListTopics_section.md)
    + [`Publish`](sns_example_sns_Publish_section.md)
    + [`SetSMSAttributes`](sns_example_sns_SetSMSAttributes_section.md)
    + [`SetSubscriptionAttributes`](sns_example_sns_SetSubscriptionAttributes_section.md)
    + [`SetSubscriptionAttributesRedrivePolicy`](sns_example_sns_SetSubscriptionAttributesRedrivePolicy_section.md)
    + [`SetTopicAttributes`](sns_example_sns_SetTopicAttributes_section.md)
    + [`Subscribe`](sns_example_sns_Subscribe_section.md)
    + [`TagResource`](sns_example_sns_TagResource_section.md)
    + [`Unsubscribe`](sns_example_sns_Unsubscribe_section.md)
+ [Scenarios](sns_code_examples_scenarios.md)
  + [Build an app to submit data to a DynamoDB table](sns_example_cross_SubmitDataApp_section.md)
  + [Building an Amazon SNS application](sns_example_cross_SnsPublishSubscription_section.md)
  + [Create a messaging topic and publish messages](sns_example_sns_GettingStarted_048_section.md)
  + [Create a platform endpoint for push notifications](sns_example_sns_CreatePlatformEndpoint_section.md)
  + [Create a serverless application to manage photos](sns_example_cross_PAM_section.md)
  + [Create an Amazon Textract explorer application](sns_example_cross_TextractExplorer_section.md)
  + [Create and publish to a FIFO topic](sns_example_sns_PublishFifoTopic_section.md)
  + [Detect people and objects in a video](sns_example_cross_RekognitionVideoDetection_section.md)
  + [Getting started with configuration management](sns_example_config_service_GettingStarted_053_section.md)
  + [Getting started with internet of things device protection](sns_example_iot_GettingStarted_079_section.md)
  + [Publish SMS messages to a topic](sns_example_sns_UsageSmsTopic_section.md)
  + [Publish a large message](sns_example_sns_PublishLargeMessage_section.md)
  + [Publish an SMS text message](sns_example_sns_PublishTextSMS_section.md)
  + [Publish messages to queues](sns_example_sqs_Scenario_TopicsAndQueues_section.md)
  + [Use API Gateway to invoke a Lambda function](sns_example_cross_LambdaAPIGateway_section.md)
  + [Use scheduled events to invoke a Lambda function](sns_example_cross_LambdaScheduledEvents_section.md)
+ [Serverless examples](sns_code_examples_serverless_examples.md)
  + [Invoke a Lambda function from an Amazon SNS trigger](sns_example_serverless_SNS_Lambda_section.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
