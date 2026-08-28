---
source_url: https://docs.aws.amazon.com/signer/latest/developerguide/authen-overview.html
---

# Identity and Access Management for AWS Signer
<a name="authen-overview"></a>

An AWS account owner or an authorized administrator can attach permissions policies to IAM identities (users, groups, and roles) that were created in the account. When managing permissions, an account owner or administrator decides who gets the permissions and what specific actions are allowed.

A *permissions policy* describes who has access to what. Administrators can use IAM to create policies that apply permissions to IAM users, groups, and roles. The following types of *identity-based policies* can grant permission for AWS Signer resources:
+  **Customer managed policies** – Policies that an administrator creates and manages in an AWS account and which can be attached to multiple users, groups, and roles.
+  **Inline policies** – Policies that an administrator creates and manages for a single IAM entity and which can be embedded directly into a single user, group, or role.

For more information, see:
+ [Customer managed policies for Signer](authen-custmanagedpolicies.md)
+ [Inline policies for Signer](authen-inlinepolicies.md)
+ [Use Signer actions in IAM](authen-apipermissions.md)
+ [Managed policies and inline policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html) in the IAM documentation.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Signer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query signer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
