---
source_url: https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_LoRaWANGateway.html
---

# LoRaWANGateway
<a name="API_LoRaWANGateway"></a>

LoRaWANGateway object.

## Contents
<a name="API_LoRaWANGateway_Contents"></a>

 ** Beaconing **   <a name="iotwireless-Type-LoRaWANGateway-Beaconing"></a>
Beaconing object information, which consists of the data rate and frequency parameters.
Type: [Beaconing](API_Beaconing.md) object
Required: No

 ** GatewayEui **   <a name="iotwireless-Type-LoRaWANGateway-GatewayEui"></a>
The gateway's EUI value.
Type: String
Pattern: `^(([0-9A-Fa-f]{2}-){7}|([0-9A-Fa-f]{2}:){7}|([0-9A-Fa-f]{2}\s){7}|([0-9A-Fa-f]{2}){7})([0-9A-Fa-f]{2})$`
Required: No

 ** JoinEuiFilters **   <a name="iotwireless-Type-LoRaWANGateway-JoinEuiFilters"></a>
A list of JoinEuiRange used by LoRa gateways to filter LoRa frames.
Type: Array of arrays of strings
Array Members: Minimum number of 0 items. Maximum number of 3 items.
Array Members: Fixed number of 2 items.
Pattern: `[a-fA-F0-9]{16}`
Required: No

 ** MaxEirp **   <a name="iotwireless-Type-LoRaWANGateway-MaxEirp"></a>
The MaxEIRP value.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 30.
Required: No

 ** NetIdFilters **   <a name="iotwireless-Type-LoRaWANGateway-NetIdFilters"></a>
A list of NetId values that are used by LoRa gateways to filter the uplink frames.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Pattern: `[a-fA-F0-9]{6}`
Required: No

 ** RfRegion **   <a name="iotwireless-Type-LoRaWANGateway-RfRegion"></a>
The frequency band (RFRegion) value.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** SubBands **   <a name="iotwireless-Type-LoRaWANGateway-SubBands"></a>
A list of integer indicating which sub bands are supported by LoRa gateway.
Type: Array of integers
Array Members: Minimum number of 0 items. Maximum number of 8 items.
Valid Range: Minimum value of 1. Maximum value of 8.
Required: No

## See Also
<a name="API_LoRaWANGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotwireless-2025-11-06/LoRaWANGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotwireless-2025-11-06/LoRaWANGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotwireless-2025-11-06/LoRaWANGateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Wireless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-wireless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
