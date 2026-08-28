---
source_url: https://docs.aws.amazon.com/kms/latest/cryptographic-details/enable-and-disable-key.html
---

# Enabling and disabling keys
<a name="enable-and-disable-key"></a>

Disabling a KMS key prevents the key from being used in cryptographic operations. It suspends the ability to use all HBKs that are associated with the KMS key. Enabling restores use of the HBKs and the KMS key. [Enable](https://docs.aws.amazon.com/kms/latest/APIReference/API_Enable.html) and [Disable](https://docs.aws.amazon.com/kms/latest/APIReference/API_Disable.html) are simple requests that take only the key ID or key ARN of the KMS key.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS KMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
