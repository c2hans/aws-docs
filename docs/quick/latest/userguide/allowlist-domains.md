---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/allowlist-domains.html
---

# Allowlisting Amazon Quick domains
<a name="allowlist-domains"></a>

If your end users are signing in to Amazon Quick using AWS root (not recommended), AWS Identity and Access Management (IAM), corporate Active Directory, or native Quick credentials, make sure to allow-list the following domains within your organization's network.

| User type | Domain or domains to allow-list |
| --- | --- |
| Users who sign in directly through Amazon Quick and Active Directory users | `signin.aws` and `awsapps.com` |
| AWS root user  | `signin.aws.amazon.com` and `amazon.com` |
| IAM users | `signin.aws.amazon.com` |

**Important**
We strongly recommend that you don't use the AWS root user for your everyday tasks, even the administrative ones. Instead, adhere to the best practice of using the root user only to create your first IAM user. Then securely lock away the root user credentials and use them to perform only a few account and service management tasks. For more information, see [AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html) in the *IAM User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
