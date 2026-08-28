---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_RepublishAction.html
---

# RepublishAction
<a name="API_RepublishAction"></a>

Describes an action to republish to another topic.

## Contents
<a name="API_RepublishAction_Contents"></a>

 ** roleArn **   <a name="iot-Type-RepublishAction-roleArn"></a>
The ARN of the IAM role that grants access.
Type: String
Required: Yes

 ** topic **   <a name="iot-Type-RepublishAction-topic"></a>
The name of the MQTT topic.
Type: String
Required: Yes

 ** headers **   <a name="iot-Type-RepublishAction-headers"></a>
MQTT Version 5.0 headers information. For more information, see [ MQTT](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) from the AWS IoT Core Developer Guide.
Type: [MqttHeaders](API_MqttHeaders.md) object
Required: No

 ** qos **   <a name="iot-Type-RepublishAction-qos"></a>
The Quality of Service (QoS) level to use when republishing messages. The default value is 0.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

## See Also
<a name="API_RepublishAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/RepublishAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/RepublishAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/RepublishAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
