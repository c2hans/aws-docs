---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_AwsVPCSecurityGroupViolation.html
---

# AwsVPCSecurityGroupViolation
<a name="API_AwsVPCSecurityGroupViolation"></a>

Violation detail for the rule violation in a security group when compared to the primary security group of the AWS Firewall Manager policy.

## Contents
<a name="API_AwsVPCSecurityGroupViolation_Contents"></a>

 ** PartialMatches **   <a name="fms-Type-AwsVPCSecurityGroupViolation-PartialMatches"></a>
List of rules specified in the security group of the AWS Firewall Manager policy that partially match the `ViolationTarget` rule.
Type: Array of [PartialMatch](API_PartialMatch.md) objects
Required: No

 ** PossibleSecurityGroupRemediationActions **   <a name="fms-Type-AwsVPCSecurityGroupViolation-PossibleSecurityGroupRemediationActions"></a>
Remediation options for the rule specified in the `ViolationTarget`.
Type: Array of [SecurityGroupRemediationAction](API_SecurityGroupRemediationAction.md) objects
Required: No

 ** ViolationTarget **   <a name="fms-Type-AwsVPCSecurityGroupViolation-ViolationTarget"></a>
The security group rule that is being evaluated.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** ViolationTargetDescription **   <a name="fms-Type-AwsVPCSecurityGroupViolation-ViolationTargetDescription"></a>
A description of the security group that violates the policy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_AwsVPCSecurityGroupViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/AwsVPCSecurityGroupViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/AwsVPCSecurityGroupViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/AwsVPCSecurityGroupViolation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
