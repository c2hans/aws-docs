---
source_url: https://docs.aws.amazon.com/wickr/latest/adminguide/consideration-secure.html
---

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Security considerations
<a name="consideration-secure"></a>

Carefully evaluate where and how to deploy a data retention bot. These bots centrally collect and decrypt all end-to-end encrypted messages sent or received by users, consolidating content that was previously accessible only on individual devices. As a result, this component and its data storage have exceptionally high security value.

If you deploy a data retention bot, ensure it meets the highest security standards and aligns with your organizations security policy. For deployments using AWS services, follow the additional guidance in our [Security best practices for AWS Wickr](security-best-practices.md) and AWS Cloud Security [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
