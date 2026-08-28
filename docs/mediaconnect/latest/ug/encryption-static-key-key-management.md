---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/encryption-static-key-key-management.html
---

# Key management for static key encryption
<a name="encryption-static-key-key-management"></a>

In AWS Elemental MediaConnect, you can use static key encryption to secure content in sources, outputs, entitlements and router I/O. To use this method, you store an encryption key as a *secret* in AWS Secrets Manager, and you give AWS Elemental MediaConnect permission to access the secret. Secrets Manager keeps your encryption key secure, allowing it be accessed only by entities that you specify in an AWS Identity and Access Management (IAM) policy.

With static key encryption, all participants (the owner of the flow source, the flow, and any flow outputs, entitlements and router I/O) need the encryption key. If the content is shared using an entitlement, both AWS account owners must store the encryption key in AWS Secrets Manager.

For more information, see [Setting up static key encryption](encryption-static-key-set-up.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
