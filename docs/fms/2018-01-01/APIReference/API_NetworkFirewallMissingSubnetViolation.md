---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_NetworkFirewallMissingSubnetViolation.html
---

# NetworkFirewallMissingSubnetViolation
<a name="API_NetworkFirewallMissingSubnetViolation"></a>

Violation detail for AWS Network Firewall for an Availability Zone that's missing the expected Firewall Manager managed subnet.

## Contents
<a name="API_NetworkFirewallMissingSubnetViolation_Contents"></a>

 ** AvailabilityZone **   <a name="fms-Type-NetworkFirewallMissingSubnetViolation-AvailabilityZone"></a>
The Availability Zone of a violating subnet.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** TargetViolationReason **   <a name="fms-Type-NetworkFirewallMissingSubnetViolation-TargetViolationReason"></a>
The reason the resource has this violation, if one is available.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `\w+`
Required: No

 ** ViolationTarget **   <a name="fms-Type-NetworkFirewallMissingSubnetViolation-ViolationTarget"></a>
The ID of the AWS Network Firewall or VPC resource that's in violation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** VPC **   <a name="fms-Type-NetworkFirewallMissingSubnetViolation-VPC"></a>
The resource ID of the VPC associated with a violating subnet.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_NetworkFirewallMissingSubnetViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/NetworkFirewallMissingSubnetViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/NetworkFirewallMissingSubnetViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/NetworkFirewallMissingSubnetViolation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
