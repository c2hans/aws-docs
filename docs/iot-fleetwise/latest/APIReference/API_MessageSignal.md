---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_MessageSignal.html
---

# MessageSignal
<a name="API_MessageSignal"></a>

The decoding information for a specific message which support higher order data types.

## Contents
<a name="API_MessageSignal_Contents"></a>

 ** structuredMessage **   <a name="iotfleetwise-Type-MessageSignal-structuredMessage"></a>
The structured message for the message signal. It can be defined with either a `primitiveMessageDefinition`, `structuredMessageListDefinition`, or `structuredMessageDefinition` recursively.
Type: [StructuredMessage](API_StructuredMessage.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** topicName **   <a name="iotfleetwise-Type-MessageSignal-topicName"></a>
The topic name for the message signal. It corresponds to topics in ROS 2.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[a-zA-Z0-9_\-#:./]+`
Required: Yes

## See Also
<a name="API_MessageSignal_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/MessageSignal)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/MessageSignal)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/MessageSignal)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
