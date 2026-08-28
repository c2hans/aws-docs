---
source_url: https://docs.aws.amazon.com/detective/latest/userguide/key-management.html
---

# Key management for Amazon Detective
<a name="key-management"></a>

Because Detective does not store any personally identifiable customer data, it uses AWS managed keys.

This type of KMS key can be used across multiple accounts. See the [description of AWS owned keys in the AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk).

This type of KMS key rotates automatically every one year (approximately 365 days). See the [description of key rotation in the AWS Key Management Service Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
