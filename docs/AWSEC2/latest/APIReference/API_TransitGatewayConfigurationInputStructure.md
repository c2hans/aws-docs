---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TransitGatewayConfigurationInputStructure.html
---

# TransitGatewayConfigurationInputStructure
<a name="API_TransitGatewayConfigurationInputStructure"></a>

The Transit Gateway configuration for a Client VPN endpoint.

## Contents
<a name="API_TransitGatewayConfigurationInputStructure_Contents"></a>

 ** AvailabilityZone.N **
The Availability Zone names for the Transit Gateway association. You can specify up to the maximum number of Availability Zones supported by the Transit Gateway. You cannot specify both `AvailabilityZones` and `AvailabilityZoneIds`.
Type: Array of strings
Required: No

 ** AvailabilityZoneId.N **
The Availability Zone IDs for the Transit Gateway association. You can specify up to the maximum number of Availability Zones supported by the Transit Gateway. You cannot specify both `AvailabilityZones` and `AvailabilityZoneIds`.
Type: Array of strings
Required: No

 ** TransitGatewayId **
The ID of the Transit Gateway to associate with the Client VPN endpoint.
Type: String
Required: No

## See Also
<a name="API_TransitGatewayConfigurationInputStructure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/TransitGatewayConfigurationInputStructure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/TransitGatewayConfigurationInputStructure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/TransitGatewayConfigurationInputStructure)
