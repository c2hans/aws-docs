---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DnsDuplicateRuleGroupViolation.html
---

# DnsDuplicateRuleGroupViolation
<a name="API_DnsDuplicateRuleGroupViolation"></a>

A DNS Firewall rule group that Firewall Manager tried to associate with a VPC is already associated with the VPC and can't be associated again.

## Contents
<a name="API_DnsDuplicateRuleGroupViolation_Contents"></a>

 ** ViolationTarget **   <a name="fms-Type-DnsDuplicateRuleGroupViolation-ViolationTarget"></a>
Information about the VPC ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** ViolationTargetDescription **   <a name="fms-Type-DnsDuplicateRuleGroupViolation-ViolationTargetDescription"></a>
A description of the violation that specifies the rule group and VPC.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_DnsDuplicateRuleGroupViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/DnsDuplicateRuleGroupViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/DnsDuplicateRuleGroupViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/DnsDuplicateRuleGroupViolation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
