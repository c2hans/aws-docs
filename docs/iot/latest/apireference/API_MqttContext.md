---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_MqttContext.html
---

# MqttContext
<a name="API_MqttContext"></a>

Specifies the MQTT context to use for the test authorizer request

## Contents
<a name="API_MqttContext_Contents"></a>

 ** clientId **   <a name="iot-Type-MqttContext-clientId"></a>
The value of the `clientId` key in an MQTT authorization request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[\s\S]*`
Required: No

 ** password **   <a name="iot-Type-MqttContext-password"></a>
The value of the `password` key in an MQTT authorization request.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 65535.
Required: No

 ** username **   <a name="iot-Type-MqttContext-username"></a>
The value of the `username` key in an MQTT authorization request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_MqttContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/MqttContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/MqttContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/MqttContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
