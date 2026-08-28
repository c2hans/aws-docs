---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GatewaySummary.html
---

# GatewaySummary
<a name="API_GatewaySummary"></a>

Contains a summary of a gateway.

## Contents
<a name="API_GatewaySummary_Contents"></a>

 ** creationDate **   <a name="iotsitewise-Type-GatewaySummary-creationDate"></a>
The date the gateway was created, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** gatewayId **   <a name="iotsitewise-Type-GatewaySummary-gatewayId"></a>
The ID of the gateway device.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** gatewayName **   <a name="iotsitewise-Type-GatewaySummary-gatewayName"></a>
The name of the gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** lastUpdateDate **   <a name="iotsitewise-Type-GatewaySummary-lastUpdateDate"></a>
The date the gateway was last updated, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** gatewayCapabilitySummaries **   <a name="iotsitewise-Type-GatewaySummary-gatewayCapabilitySummaries"></a>
A list of gateway capability summaries that each contain a namespace and status. Each gateway capability defines data sources for the gateway. To retrieve a capability configuration's definition, use [DescribeGatewayCapabilityConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGatewayCapabilityConfiguration.html).
Type: Array of [GatewayCapabilitySummary](API_GatewayCapabilitySummary.md) objects
Required: No

 ** gatewayPlatform **   <a name="iotsitewise-Type-GatewaySummary-gatewayPlatform"></a>
The gateway's platform configuration. You can only specify one platform type in a gateway.
(Legacy only) For Greengrass V1 gateways, specify the `greengrass` parameter with a valid Greengrass group ARN.
For Greengrass V2 gateways, specify the `greengrassV2` parameter with a valid core device thing name. If creating a V3 gateway (`gatewayVersion=3`), you must also specify the `coreDeviceOperatingSystem`.
For Siemens Industrial Edge gateways, specify the `siemensIE` parameter with a valid IoT Core thing name.
Type: [GatewayPlatform](API_GatewayPlatform.md) object
Required: No

 ** gatewayVersion **   <a name="iotsitewise-Type-GatewaySummary-gatewayVersion"></a>
The version of the gateway. A value of `3` indicates an MQTT-enabled, V3 gateway, while `2` indicates a Classic streams, V2 gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`
Required: No

## See Also
<a name="API_GatewaySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/GatewaySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/GatewaySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/GatewaySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
