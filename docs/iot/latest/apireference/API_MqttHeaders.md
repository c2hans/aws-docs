---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_MqttHeaders.html
---

# MqttHeaders
<a name="API_MqttHeaders"></a>

Specifies MQTT Version 5.0 headers information. For more information, see [ MQTT](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) from AWS IoT Core Developer Guide.

## Contents
<a name="API_MqttHeaders_Contents"></a>

 ** contentType **   <a name="iot-Type-MqttHeaders-contentType"></a>
A UTF-8 encoded string that describes the content of the publishing message.
For more information, see [ Content Type](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901118) from the MQTT Version 5.0 specification.
Supports [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** correlationData **   <a name="iot-Type-MqttHeaders-correlationData"></a>
The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when it's received.
For more information, see [ Correlation Data](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901115) from the MQTT Version 5.0 specification.
 This binary data must be based64-encoded.
Supports [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** messageExpiry **   <a name="iot-Type-MqttHeaders-messageExpiry"></a>
A user-defined integer value that will persist a message at the message broker for a specified amount of time to ensure that the message will expire if it's no longer relevant to the subscriber. The value of `messageExpiry` represents the number of seconds before it expires. For more information about the limits of `messageExpiry`, see [AWS IoT Core message broker and protocol limits and quotas ](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) from the AWS Reference Guide.
Supports [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** payloadFormatIndicator **   <a name="iot-Type-MqttHeaders-payloadFormatIndicator"></a>
An `Enum` string value that indicates whether the payload is formatted as UTF-8.
Valid values are `UNSPECIFIED_BYTES` and `UTF8_DATA`.
For more information, see [ Payload Format Indicator](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901111) from the MQTT Version 5.0 specification.
Supports [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** responseTopic **   <a name="iot-Type-MqttHeaders-responseTopic"></a>
A UTF-8 encoded string that's used as the topic name for a response message. The response topic is used to describe the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters.
For more information, see [ Response Topic](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901114) from the MQTT Version 5.0 specification.
Supports [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** userProperties **   <a name="iot-Type-MqttHeaders-userProperties"></a>
An array of key-value pairs that you define in the MQTT5 header.
Type: Array of [UserProperty](API_UserProperty.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## See Also
<a name="API_MqttHeaders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/MqttHeaders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/MqttHeaders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/MqttHeaders)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
