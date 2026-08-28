---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_PositionConfigurationItem.html
---

# PositionConfigurationItem
<a name="API_PositionConfigurationItem"></a>

The wrapper for a position configuration.

## Contents
<a name="API_PositionConfigurationItem_Contents"></a>

 ** Destination **   <a name="iotwireless-Type-PositionConfigurationItem-Destination"></a>
The position data destination that describes the AWS IoT rule that processes the device's position data for use by AWS IoT Core for LoRaWAN.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: No

 ** ResourceIdentifier **   <a name="iotwireless-Type-PositionConfigurationItem-ResourceIdentifier"></a>
Resource identifier for the position configuration.
Type: String
Pattern: `[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}`
Required: No

 ** ResourceType **   <a name="iotwireless-Type-PositionConfigurationItem-ResourceType"></a>
Resource type of the resource for the position configuration.
Type: String
Valid Values: `WirelessDevice | WirelessGateway`
Required: No

 ** Solvers **   <a name="iotwireless-Type-PositionConfigurationItem-Solvers"></a>
The details of the positioning solver object used to compute the location.
Type: [PositionSolverDetails](API_PositionSolverDetails.md) object
Required: No

## See Also
<a name="API_PositionConfigurationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/PositionConfigurationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/PositionConfigurationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/PositionConfigurationItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
