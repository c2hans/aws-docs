---
source_url: https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html
---

# Condition keys for AWS KMS
<a name="policy-conditions"></a>

You can specify conditions in the [key policies](key-policies.md) and [IAM policies](iam-policies.md) that control access to AWS KMS resources. The policy statement is effective only when the conditions are true. For example, you might want a policy statement to take effect only after a specific date. Or, you might want a policy statement to control access only when a specific value appears in an API request.

To specify conditions, you use *condition keys* in the [`Condition` element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy statement with [IAM condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html). Some condition keys apply generally to AWS; others are specific to AWS KMS.

Condition key values must adhere to the character and encoding rules for AWS KMS key policies and IAM policies. For details about key policy document rules, see [Key policy format](key-policy-overview.md#key-policy-format). For details about IAM policy document rules, see [IAM name requirements](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-quotas.html#reference_iam-quotas-names) in the *IAM User Guide*..

**Topics**
+ [AWS global condition keys](conditions-aws.md)
+ [AWS KMS condition keys](conditions-kms.md)
+ [AWS KMS condition keys for attested platforms](conditions-attestation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
