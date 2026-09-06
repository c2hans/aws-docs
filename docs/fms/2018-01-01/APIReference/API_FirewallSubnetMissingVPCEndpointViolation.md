---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_FirewallSubnetMissingVPCEndpointViolation.html
---

# FirewallSubnetMissingVPCEndpointViolation
<a name="API_FirewallSubnetMissingVPCEndpointViolation"></a>

The violation details for a firewall subnet's VPC endpoint that's deleted or missing.

## Contents
<a name="API_FirewallSubnetMissingVPCEndpointViolation_Contents"></a>

 ** FirewallSubnetId **   <a name="fms-Type-FirewallSubnetMissingVPCEndpointViolation-FirewallSubnetId"></a>
The ID of the firewall that this VPC endpoint is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** SubnetAvailabilityZone **   <a name="fms-Type-FirewallSubnetMissingVPCEndpointViolation-SubnetAvailabilityZone"></a>
The name of the Availability Zone of the deleted VPC subnet.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** SubnetAvailabilityZoneId **   <a name="fms-Type-FirewallSubnetMissingVPCEndpointViolation-SubnetAvailabilityZoneId"></a>
The ID of the Availability Zone of the deleted VPC subnet.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** VpcId **   <a name="fms-Type-FirewallSubnetMissingVPCEndpointViolation-VpcId"></a>
The resource ID of the VPC associated with the deleted VPC subnet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_FirewallSubnetMissingVPCEndpointViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/FirewallSubnetMissingVPCEndpointViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/FirewallSubnetMissingVPCEndpointViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/FirewallSubnetMissingVPCEndpointViolation)
