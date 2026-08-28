---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_GatewayListItem.html
---

# GatewayListItem
<a name="API_GatewayListItem"></a>

Gateway list item object that specifies the frequency and list of gateways for which the downlink message should be sent.

## Contents
<a name="API_GatewayListItem_Contents"></a>

 ** DownlinkFrequency **   <a name="iotwireless-Type-GatewayListItem-DownlinkFrequency"></a>
The frequency to use for the gateways when sending a downlink message to the wireless device.
Type: Integer
Valid Range: Minimum value of 100000000. Maximum value of 1000000000.
Required: Yes

 ** GatewayId **   <a name="iotwireless-Type-GatewayListItem-GatewayId"></a>
The ID of the wireless gateways that you want to add to the list of gateways when sending downlink messages.
Type: String
Length Constraints: Maximum length of 256.
Required: Yes

## See Also
<a name="API_GatewayListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/GatewayListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/GatewayListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/GatewayListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
