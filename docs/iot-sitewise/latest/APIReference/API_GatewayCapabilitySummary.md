---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GatewayCapabilitySummary.html
---

# GatewayCapabilitySummary
<a name="API_GatewayCapabilitySummary"></a>

Contains a summary of a gateway capability configuration.

## Contents
<a name="API_GatewayCapabilitySummary_Contents"></a>

 ** capabilityNamespace **   <a name="iotsitewise-Type-GatewayCapabilitySummary-capabilityNamespace"></a>
The namespace of the capability configuration. For example, if you configure OPC UA sources for an MQTT-enabled gateway, your OPC-UA capability configuration has the namespace `iotsitewise:opcuacollector:3`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^[a-zA-Z]+:[a-zA-Z]+:[0-9]+$`
Required: Yes

 ** capabilitySyncStatus **   <a name="iotsitewise-Type-GatewayCapabilitySummary-capabilitySyncStatus"></a>
The synchronization status of the gateway capability configuration. The sync status can be one of the following:
+  `IN_SYNC` - The gateway is running with the latest configuration.
+  `OUT_OF_SYNC` - The gateway hasn't received the latest configuration.
+  `SYNC_FAILED` - The gateway rejected the latest configuration.
+  `UNKNOWN` - The gateway hasn't reported its sync status.
+  `NOT_APPLICABLE` - The gateway doesn't support this capability. This is most common when integrating partner data sources, because the data integration is handled externally by the partner.
Type: String
Valid Values: `IN_SYNC | OUT_OF_SYNC | SYNC_FAILED | UNKNOWN | NOT_APPLICABLE`
Required: Yes

## See Also
<a name="API_GatewayCapabilitySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/GatewayCapabilitySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/GatewayCapabilitySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/GatewayCapabilitySummary)
