---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_dax_NotificationConfiguration.html
---

# NotificationConfiguration
<a name="API_dax_NotificationConfiguration"></a>

Describes a notification topic and its status. Notification topics are used for publishing DAX events to subscribers using Amazon Simple Notification Service (SNS).

## Contents
<a name="API_dax_NotificationConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** TopicArn **   <a name="DDB-Type-dax_NotificationConfiguration-TopicArn"></a>
The Amazon Resource Name (ARN) that identifies the topic.
Type: String
Required: No

 ** TopicStatus **   <a name="DDB-Type-dax_NotificationConfiguration-TopicStatus"></a>
The current state of the topic. A value of “active” means that notifications will be sent to the topic. A value of “inactive” means that notifications will not be sent to the topic.
Type: String
Required: No

## See Also
<a name="API_dax_NotificationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dax-2017-04-19/NotificationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dax-2017-04-19/NotificationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dax-2017-04-19/NotificationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
