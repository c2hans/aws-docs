---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/setting-up.html
---

# Setting up AWS Elemental MediaConnect
<a name="setting-up"></a>

Before you start using AWS Elemental MediaConnect, you must sign up for AWS (if you don’t already have an AWS account) and create IAM users and roles to allow access to MediaConnect. This includes creating an IAM role for yourself. If you want to use encryption to protect your content, you also must store your encryption keys in AWS Secrets Manager, and then give MediaConnect permission to obtain the keys from your Secrets Manager account.

This section guides you through the steps required to configure users and roles to access AWS Elemental MediaConnect. For background and additional information about identity and access management for MediaConnect, see [Identity and access management for AWS Elemental MediaConnect](security-iam.md).

**Topics**
+ [Create non-admin roles](setting-up-create-nonadmin-roles.md)
+ [(Optional) Set up encryption](setting-up-encryption.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
