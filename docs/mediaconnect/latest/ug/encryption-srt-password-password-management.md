---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/encryption-srt-password-password-management.html
---

# Password management for SRT password encryption
<a name="encryption-srt-password-password-management"></a>

In AWS Elemental MediaConnect, you can use SRT password encryption to secure content in sources, outputs and router I/O. To use this method, you store an SRT password as a *secret* in AWS Secrets Manager, and you give AWS Elemental MediaConnect permission to access the secret. Secrets Manager keeps your password secure, allowing it be accessed only by entities that you specify in an AWS Identity and Access Management (IAM) policy.

With SRT password encryption, all participants (the owner of the source, the flow, the outputs and the router I/O) need the SRT password.

For more information, see [Setting up SRT password encryption](encryption-srt-password-set-up.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
