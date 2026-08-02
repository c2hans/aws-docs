---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_Destinations.html
---

# Destinations
<a name="API_Destinations"></a>

Describes a destination.

## Contents
<a name="API_Destinations_Contents"></a>

 ** Arn **   <a name="iotwireless-Type-Destinations-Arn"></a>
The Amazon Resource Name of the resource.
Type: String
Required: No

 ** Description **   <a name="iotwireless-Type-Destinations-Description"></a>
The description of the resource.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** Expression **   <a name="iotwireless-Type-Destinations-Expression"></a>
The rule name or topic rule to send messages to.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** ExpressionType **   <a name="iotwireless-Type-Destinations-ExpressionType"></a>
The type of value in `Expression`.
Type: String
Valid Values: `RuleName | MqttTopic`
Required: No

 ** Name **   <a name="iotwireless-Type-Destinations-Name"></a>
The name of the resource.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** RoleArn **   <a name="iotwireless-Type-Destinations-RoleArn"></a>
The ARN of the IAM Role that authorizes the destination.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## See Also
<a name="API_Destinations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/Destinations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/Destinations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/Destinations)
