---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_RetainedMessageSummary.html
---

# RetainedMessageSummary
<a name="API_iotdata_RetainedMessageSummary"></a>

Information about a single retained message.

## Contents
<a name="API_iotdata_RetainedMessageSummary_Contents"></a>

 ** lastModifiedTime **   <a name="iot-Type-iotdata_RetainedMessageSummary-lastModifiedTime"></a>
The Epoch date and time, in milliseconds, when the retained message was stored by AWS IoT.
Type: Long
Required: No

 ** payloadSize **   <a name="iot-Type-iotdata_RetainedMessageSummary-payloadSize"></a>
The size of the retained message's payload in bytes.
Type: Long
Required: No

 ** qos **   <a name="iot-Type-iotdata_RetainedMessageSummary-qos"></a>
The quality of service (QoS) level used to publish the retained message.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

 ** topic **   <a name="iot-Type-iotdata_RetainedMessageSummary-topic"></a>
The topic name to which the retained message was published.
Type: String
Required: No

## See Also
<a name="API_iotdata_RetainedMessageSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-data-2015-05-28/RetainedMessageSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-data-2015-05-28/RetainedMessageSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-data-2015-05-28/RetainedMessageSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
