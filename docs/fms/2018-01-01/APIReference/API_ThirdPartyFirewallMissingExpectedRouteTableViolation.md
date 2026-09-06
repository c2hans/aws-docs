---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ThirdPartyFirewallMissingExpectedRouteTableViolation.html
---

# ThirdPartyFirewallMissingExpectedRouteTableViolation
<a name="API_ThirdPartyFirewallMissingExpectedRouteTableViolation"></a>

The violation details for a third-party firewall that's not associated with an AWS Firewall Manager managed route table.

## Contents
<a name="API_ThirdPartyFirewallMissingExpectedRouteTableViolation_Contents"></a>

 ** AvailabilityZone **   <a name="fms-Type-ThirdPartyFirewallMissingExpectedRouteTableViolation-AvailabilityZone"></a>
The Availability Zone of the firewall subnet that's causing the violation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** CurrentRouteTable **   <a name="fms-Type-ThirdPartyFirewallMissingExpectedRouteTableViolation-CurrentRouteTable"></a>
The resource ID of the current route table that's associated with the subnet, if one is available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ExpectedRouteTable **   <a name="fms-Type-ThirdPartyFirewallMissingExpectedRouteTableViolation-ExpectedRouteTable"></a>
The resource ID of the route table that should be associated with the subnet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ViolationTarget **   <a name="fms-Type-ThirdPartyFirewallMissingExpectedRouteTableViolation-ViolationTarget"></a>
The ID of the third-party firewall or VPC resource that's causing the violation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** VPC **   <a name="fms-Type-ThirdPartyFirewallMissingExpectedRouteTableViolation-VPC"></a>
The resource ID of the VPC associated with a fireawll subnet that's causing the violation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_ThirdPartyFirewallMissingExpectedRouteTableViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ThirdPartyFirewallMissingExpectedRouteTableViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ThirdPartyFirewallMissingExpectedRouteTableViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ThirdPartyFirewallMissingExpectedRouteTableViolation)
