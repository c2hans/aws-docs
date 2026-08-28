---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_IotEventsAction.html
---

# IotEventsAction
<a name="API_IotEventsAction"></a>

Sends an input to an AWS IoT Events detector.

## Contents
<a name="API_IotEventsAction_Contents"></a>

 ** inputName **   <a name="iot-Type-IotEventsAction-inputName"></a>
The name of the AWS IoT Events input.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** roleArn **   <a name="iot-Type-IotEventsAction-roleArn"></a>
The ARN of the role that grants AWS IoT permission to send an input to an AWS IoT Events detector. ("Action":"iotevents:BatchPutMessage").
Type: String
Required: Yes

 ** batchMode **   <a name="iot-Type-IotEventsAction-batchMode"></a>
Whether to process the event actions as a batch. The default value is `false`.
When `batchMode` is `true`, you can't specify a `messageId`.
When `batchMode` is `true` and the rule SQL statement evaluates to an Array, each Array element is treated as a separate message when it's sent to AWS IoT Events by calling [`BatchPutMessage`](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchPutMessage.html). The resulting array can't have more than 10 messages.
Type: Boolean
Required: No

 ** messageId **   <a name="iot-Type-IotEventsAction-messageId"></a>
The ID of the message. The default `messageId` is a new UUID value.
When `batchMode` is `true`, you can't specify a `messageId`--a new UUID value will be assigned.
Assign a value to this property to ensure that only one input (message) with a given `messageId` will be processed by an AWS IoT Events detector.
Type: String
Length Constraints: Maximum length of 128.
Required: No

## See Also
<a name="API_IotEventsAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/IotEventsAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/IotEventsAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/IotEventsAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
