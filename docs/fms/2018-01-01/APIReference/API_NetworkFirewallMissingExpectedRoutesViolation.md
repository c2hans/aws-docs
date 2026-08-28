---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_NetworkFirewallMissingExpectedRoutesViolation.html
---

# NetworkFirewallMissingExpectedRoutesViolation
<a name="API_NetworkFirewallMissingExpectedRoutesViolation"></a>

Violation detail for an expected route missing in AWS Network Firewall.

## Contents
<a name="API_NetworkFirewallMissingExpectedRoutesViolation_Contents"></a>

 ** ExpectedRoutes **   <a name="fms-Type-NetworkFirewallMissingExpectedRoutesViolation-ExpectedRoutes"></a>
The expected routes.
Type: Array of [ExpectedRoute](API_ExpectedRoute.md) objects
Required: No

 ** ViolationTarget **   <a name="fms-Type-NetworkFirewallMissingExpectedRoutesViolation-ViolationTarget"></a>
The target of the violation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** VpcId **   <a name="fms-Type-NetworkFirewallMissingExpectedRoutesViolation-VpcId"></a>
Information about the VPC ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_NetworkFirewallMissingExpectedRoutesViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/NetworkFirewallMissingExpectedRoutesViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/NetworkFirewallMissingExpectedRoutesViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/NetworkFirewallMissingExpectedRoutesViolation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
