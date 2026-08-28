---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UpdateWirelessGatewayTaskCreate.html
---

# UpdateWirelessGatewayTaskCreate
<a name="API_UpdateWirelessGatewayTaskCreate"></a>

UpdateWirelessGatewayTaskCreate object.

## Contents
<a name="API_UpdateWirelessGatewayTaskCreate_Contents"></a>

 ** LoRaWAN **   <a name="iotwireless-Type-UpdateWirelessGatewayTaskCreate-LoRaWAN"></a>
The properties that relate to the LoRaWAN wireless gateway.
Type: [LoRaWANUpdateGatewayTaskCreate](API_LoRaWANUpdateGatewayTaskCreate.md) object
Required: No

 ** UpdateDataRole **   <a name="iotwireless-Type-UpdateWirelessGatewayTaskCreate-UpdateDataRole"></a>
The IAM role used to read data from the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** UpdateDataSource **   <a name="iotwireless-Type-UpdateWirelessGatewayTaskCreate-UpdateDataSource"></a>
The link to the S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_UpdateWirelessGatewayTaskCreate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/UpdateWirelessGatewayTaskCreate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/UpdateWirelessGatewayTaskCreate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/UpdateWirelessGatewayTaskCreate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
