---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DnsRuleGroupPriorityConflictViolation.html
---

# DnsRuleGroupPriorityConflictViolation
<a name="API_DnsRuleGroupPriorityConflictViolation"></a>

A rule group that Firewall Manager tried to associate with a VPC has the same priority as a rule group that's already associated.

## Contents
<a name="API_DnsRuleGroupPriorityConflictViolation_Contents"></a>

 ** ConflictingPolicyId **   <a name="fms-Type-DnsRuleGroupPriorityConflictViolation-ConflictingPolicyId"></a>
The ID of the Firewall Manager DNS Firewall policy that was already applied to the VPC. This policy contains the rule group that's already associated with the VPC.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: No

 ** ConflictingPriority **   <a name="fms-Type-DnsRuleGroupPriorityConflictViolation-ConflictingPriority"></a>
The priority setting of the two conflicting rule groups.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

 ** UnavailablePriorities **   <a name="fms-Type-DnsRuleGroupPriorityConflictViolation-UnavailablePriorities"></a>
The priorities of rule groups that are already associated with the VPC. To retry your operation, choose priority settings that aren't in this list for the rule groups in your new DNS Firewall policy.
Type: Array of integers
Valid Range: Minimum value of 0. Maximum value of 10000.
Required: No

 ** ViolationTarget **   <a name="fms-Type-DnsRuleGroupPriorityConflictViolation-ViolationTarget"></a>
Information about the VPC ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** ViolationTargetDescription **   <a name="fms-Type-DnsRuleGroupPriorityConflictViolation-ViolationTargetDescription"></a>
A description of the violation that specifies the VPC and the rule group that's already associated with it.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_DnsRuleGroupPriorityConflictViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/DnsRuleGroupPriorityConflictViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/DnsRuleGroupPriorityConflictViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/DnsRuleGroupPriorityConflictViolation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
