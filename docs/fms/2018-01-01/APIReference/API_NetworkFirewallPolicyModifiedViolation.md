---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_NetworkFirewallPolicyModifiedViolation.html
---

# NetworkFirewallPolicyModifiedViolation
<a name="API_NetworkFirewallPolicyModifiedViolation"></a>

Violation detail for AWS Network Firewall for a firewall policy that has a different [NetworkFirewallPolicyDescription](API_NetworkFirewallPolicyDescription.md) than is required by the Firewall Manager policy.

## Contents
<a name="API_NetworkFirewallPolicyModifiedViolation_Contents"></a>

 ** CurrentPolicyDescription **   <a name="fms-Type-NetworkFirewallPolicyModifiedViolation-CurrentPolicyDescription"></a>
The policy that's currently in use in the individual account.
Type: [NetworkFirewallPolicyDescription](API_NetworkFirewallPolicyDescription.md) object
Required: No

 ** ExpectedPolicyDescription **   <a name="fms-Type-NetworkFirewallPolicyModifiedViolation-ExpectedPolicyDescription"></a>
The policy that should be in use in the individual account in order to be compliant.
Type: [NetworkFirewallPolicyDescription](API_NetworkFirewallPolicyDescription.md) object
Required: No

 ** ViolationTarget **   <a name="fms-Type-NetworkFirewallPolicyModifiedViolation-ViolationTarget"></a>
The ID of the AWS Network Firewall or VPC resource that's in violation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

## See Also
<a name="API_NetworkFirewallPolicyModifiedViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/NetworkFirewallPolicyModifiedViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/NetworkFirewallPolicyModifiedViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/NetworkFirewallPolicyModifiedViolation)
