---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ApplicationConfig.html
---

# ApplicationConfig
<a name="API_ApplicationConfig"></a>

LoRaWAN application configuration, which can be used to perform geolocation.

## Contents
<a name="API_ApplicationConfig_Contents"></a>

 ** DestinationName **   <a name="iotwireless-Type-ApplicationConfig-DestinationName"></a>
The name of the position data destination that describes the AWS IoT rule that processes the device's position data for use by AWS IoT Core for LoRaWAN.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** FPort **   <a name="iotwireless-Type-ApplicationConfig-FPort"></a>
The Fport value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 223.
Required: No

 ** Type **   <a name="iotwireless-Type-ApplicationConfig-Type"></a>
Application type, which can be specified to obtain real-time position information of your LoRaWAN device.
Type: String
Valid Values: `SemtechGeolocation`
Required: No

## See Also
<a name="API_ApplicationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/ApplicationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/ApplicationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/ApplicationConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
