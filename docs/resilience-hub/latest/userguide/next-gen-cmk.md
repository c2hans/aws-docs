---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-cmk.html
---

# Customer-managed keys (optional)
<a name="next-gen-cmk"></a>

Next generation Resilience Hub supports customer-managed AWS KMS keys (CMKs) for encrypting your data. To use a CMK, ensure your IAM policy includes the following AWS KMS permissions:
+ `kms:DescribeKey`
+ `kms:GenerateDataKey`
+ `kms:Encrypt`
+ `kms:Decrypt`

For scheduled or long-running assessments, also include `kms:CreateGrant`.

No changes to the invoker role are needed for CMK encryption. Next generation Resilience Hub uses your caller identity for synchronous operations and AWS KMS grants for asynchronous operations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
