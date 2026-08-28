---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_LambdaEventSource.html
---

# LambdaEventSource
<a name="API_LambdaEventSource"></a>

Contains information about an event source for an AWS Lambda function. The event source defines the topics on which this Lambda function subscribes to receive messages that run the function.

## Contents
<a name="API_LambdaEventSource_Contents"></a>

 ** topic **   <a name="greengrassv2-Type-LambdaEventSource-topic"></a>
The topic to which to subscribe to receive event messages.
Type: String
Required: Yes

 ** type **   <a name="greengrassv2-Type-LambdaEventSource-type"></a>
The type of event source. Choose from the following options:
+  `PUB_SUB` – Subscribe to local publish/subscribe messages. This event source type doesn't support MQTT wildcards (`+` and `#`) in the event source topic.
+  `IOT_CORE` – Subscribe to AWS IoT Core MQTT messages. This event source type supports MQTT wildcards (`+` and `#`) in the event source topic.
Type: String
Valid Values: `PUB_SUB | IOT_CORE`
Required: Yes

## See Also
<a name="API_LambdaEventSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/LambdaEventSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/LambdaEventSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/LambdaEventSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
