---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-workforce-access.html
---

# Set up workforce access to AWS resources
<a name="manage-your-workforce-access"></a>

Set up how your workforce users authenticate and access AWS resources through IAM Identity Center. This section covers the following components that govern workforce user access to your AWS environment:
+ **Authentication sessions** – Understand how IAM Identity Center manages different types of user sessions, from interactive portal sessions to background application sessions, and how they interact with each other.
+ **User access management** – Configure session durations, disable user accounts, and implement organization-wide access blocks to maintain security and compliance.
+ **Password management** – For users created in the Identity Center directory, set password requirements, handle user credential setup, and manage password resets for users.
+ **Multi-factor authentication** – For users created in the Identity Center directory, enhance security with MFA using authenticator apps, security keys, or built-in authenticators to protect user sign-ins.

**Topics**
+ [Understanding authentication sessions in IAM Identity Center](authconcept.md)
+ [Configure the session duration in IAM Identity Center](configure-user-session.md)
+ [Disable user access to AWS accounts and applications in IAM Identity Center](disableuser.md)
+ [Deny user access with Service Control Policies](authconcept-revoke-access.md)
+ [Managing access for users in the Identity Center directory](managing-workforce-access-identity-center-directory.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
