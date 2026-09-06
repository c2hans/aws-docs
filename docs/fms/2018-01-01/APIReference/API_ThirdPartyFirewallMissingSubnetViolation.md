---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ThirdPartyFirewallMissingSubnetViolation.html
---

# ThirdPartyFirewallMissingSubnetViolation
<a name="API_ThirdPartyFirewallMissingSubnetViolation"></a>

The violation details for a third-party firewall for an Availability Zone that's missing the Firewall Manager managed subnet.

## Contents
<a name="API_ThirdPartyFirewallMissingSubnetViolation_Contents"></a>

 ** AvailabilityZone **   <a name="fms-Type-ThirdPartyFirewallMissingSubnetViolation-AvailabilityZone"></a>
The Availability Zone of a subnet that's causing the violation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** TargetViolationReason **   <a name="fms-Type-ThirdPartyFirewallMissingSubnetViolation-TargetViolationReason"></a>
The reason the resource is causing the violation, if a reason is available.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `\w+`
Required: No

 ** ViolationTarget **   <a name="fms-Type-ThirdPartyFirewallMissingSubnetViolation-ViolationTarget"></a>
The ID of the third-party firewall or VPC resource that's causing the violation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** VPC **   <a name="fms-Type-ThirdPartyFirewallMissingSubnetViolation-VPC"></a>
The resource ID of the VPC associated with a subnet that's causing the violation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_ThirdPartyFirewallMissingSubnetViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ThirdPartyFirewallMissingSubnetViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ThirdPartyFirewallMissingSubnetViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ThirdPartyFirewallMissingSubnetViolation)
