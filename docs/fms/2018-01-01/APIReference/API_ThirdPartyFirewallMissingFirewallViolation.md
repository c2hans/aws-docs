---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ThirdPartyFirewallMissingFirewallViolation.html
---

# ThirdPartyFirewallMissingFirewallViolation
<a name="API_ThirdPartyFirewallMissingFirewallViolation"></a>

The violation details about a third-party firewall's subnet that doesn't have a Firewall Manager managed firewall in its VPC.

## Contents
<a name="API_ThirdPartyFirewallMissingFirewallViolation_Contents"></a>

 ** AvailabilityZone **   <a name="fms-Type-ThirdPartyFirewallMissingFirewallViolation-AvailabilityZone"></a>
The Availability Zone of the third-party firewall that's causing the violation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** TargetViolationReason **   <a name="fms-Type-ThirdPartyFirewallMissingFirewallViolation-TargetViolationReason"></a>
The reason the resource is causing this violation, if a reason is available.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `\w+`
Required: No

 ** ViolationTarget **   <a name="fms-Type-ThirdPartyFirewallMissingFirewallViolation-ViolationTarget"></a>
The ID of the third-party firewall that's causing the violation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** VPC **   <a name="fms-Type-ThirdPartyFirewallMissingFirewallViolation-VPC"></a>
The resource ID of the VPC associated with a third-party firewall.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_ThirdPartyFirewallMissingFirewallViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ThirdPartyFirewallMissingFirewallViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ThirdPartyFirewallMissingFirewallViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ThirdPartyFirewallMissingFirewallViolation)
