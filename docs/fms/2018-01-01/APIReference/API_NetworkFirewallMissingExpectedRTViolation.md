---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_NetworkFirewallMissingExpectedRTViolation.html
---

# NetworkFirewallMissingExpectedRTViolation
<a name="API_NetworkFirewallMissingExpectedRTViolation"></a>

Violation detail for AWS Network Firewall for a subnet that's not associated to the expected Firewall Manager managed route table.

## Contents
<a name="API_NetworkFirewallMissingExpectedRTViolation_Contents"></a>

 ** AvailabilityZone **   <a name="fms-Type-NetworkFirewallMissingExpectedRTViolation-AvailabilityZone"></a>
The Availability Zone of a violating subnet.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** CurrentRouteTable **   <a name="fms-Type-NetworkFirewallMissingExpectedRTViolation-CurrentRouteTable"></a>
The resource ID of the current route table that's associated with the subnet, if one is available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ExpectedRouteTable **   <a name="fms-Type-NetworkFirewallMissingExpectedRTViolation-ExpectedRouteTable"></a>
The resource ID of the route table that should be associated with the subnet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ViolationTarget **   <a name="fms-Type-NetworkFirewallMissingExpectedRTViolation-ViolationTarget"></a>
The ID of the AWS Network Firewall or VPC resource that's in violation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** VPC **   <a name="fms-Type-NetworkFirewallMissingExpectedRTViolation-VPC"></a>
The resource ID of the VPC associated with a violating subnet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_NetworkFirewallMissingExpectedRTViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/NetworkFirewallMissingExpectedRTViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/NetworkFirewallMissingExpectedRTViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/NetworkFirewallMissingExpectedRTViolation)
