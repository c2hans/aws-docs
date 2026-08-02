---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_NetworkTelemetry.html
---

# NetworkTelemetry
<a name="API_NetworkTelemetry"></a>

Describes the telemetry information for a resource.

## Contents
<a name="API_NetworkTelemetry_Contents"></a>

 ** AccountId **   <a name="networkmanager-Type-NetworkTelemetry-AccountId"></a>
The AWS account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[\s\S]*`
Required: No

 ** Address **   <a name="networkmanager-Type-NetworkTelemetry-Address"></a>
The address.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** AwsRegion **   <a name="networkmanager-Type-NetworkTelemetry-AwsRegion"></a>
The AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[\s\S]*`
Required: No

 ** CoreNetworkId **   <a name="networkmanager-Type-NetworkTelemetry-CoreNetworkId"></a>
The ID of a core network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `^core-network-([0-9a-f]{8,17})$`
Required: No

 ** Health **   <a name="networkmanager-Type-NetworkTelemetry-Health"></a>
The connection health.
Type: [ConnectionHealth](API_ConnectionHealth.md) object
Required: No

 ** RegisteredGatewayArn **   <a name="networkmanager-Type-NetworkTelemetry-RegisteredGatewayArn"></a>
The ARN of the gateway.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1500.
Pattern: `[\s\S]*`
Required: No

 ** ResourceArn **   <a name="networkmanager-Type-NetworkTelemetry-ResourceArn"></a>
The ARN of the resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1500.
Pattern: `[\s\S]*`
Required: No

 ** ResourceId **   <a name="networkmanager-Type-NetworkTelemetry-ResourceId"></a>
The ID of the resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** ResourceType **   <a name="networkmanager-Type-NetworkTelemetry-ResourceType"></a>
The resource type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_NetworkTelemetry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/NetworkTelemetry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/NetworkTelemetry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/NetworkTelemetry)
