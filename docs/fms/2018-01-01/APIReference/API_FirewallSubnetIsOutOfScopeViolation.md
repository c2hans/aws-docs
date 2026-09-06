---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_FirewallSubnetIsOutOfScopeViolation.html
---

# FirewallSubnetIsOutOfScopeViolation
<a name="API_FirewallSubnetIsOutOfScopeViolation"></a>

Contains details about the firewall subnet that violates the policy scope.

## Contents
<a name="API_FirewallSubnetIsOutOfScopeViolation_Contents"></a>

 ** FirewallSubnetId **   <a name="fms-Type-FirewallSubnetIsOutOfScopeViolation-FirewallSubnetId"></a>
The ID of the firewall subnet that violates the policy scope.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** SubnetAvailabilityZone **   <a name="fms-Type-FirewallSubnetIsOutOfScopeViolation-SubnetAvailabilityZone"></a>
The Availability Zone of the firewall subnet that violates the policy scope.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** SubnetAvailabilityZoneId **   <a name="fms-Type-FirewallSubnetIsOutOfScopeViolation-SubnetAvailabilityZoneId"></a>
The Availability Zone ID of the firewall subnet that violates the policy scope.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** VpcEndpointId **   <a name="fms-Type-FirewallSubnetIsOutOfScopeViolation-VpcEndpointId"></a>
The VPC endpoint ID of the firewall subnet that violates the policy scope.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** VpcId **   <a name="fms-Type-FirewallSubnetIsOutOfScopeViolation-VpcId"></a>
The VPC ID of the firewall subnet that violates the policy scope.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_FirewallSubnetIsOutOfScopeViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/FirewallSubnetIsOutOfScopeViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/FirewallSubnetIsOutOfScopeViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/FirewallSubnetIsOutOfScopeViolation)
