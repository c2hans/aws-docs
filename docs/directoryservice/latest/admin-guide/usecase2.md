---
source_url: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/usecase2.html
---

# Use Case 2: Manage Amazon EC2 instances
<a name="usecase2"></a>

Using familiar Active Directory administration tools, you can apply Active Directory group policy objects (GPOs) to centrally manage your Amazon EC2 for Windows or Linux instances by [joining your instances to your AWS Managed Microsoft AD domain](https://docs.aws.amazon.com/en_us/directoryservice/latest/admin-guide/ms_ad_join_instance.html).

In addition, your users can sign in to your instances with their Active Directory credentials. This eliminates the need to use individual instance credentials or distribute private key (PEM) files. This makes it easier for you to instantly grant or revoke access to users by using Active Directory user administration tools you already use.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
