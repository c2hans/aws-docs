---
source_url: https://docs.aws.amazon.com/security-ir/latest/userguide/cloudshell-permissions.html
---

# Obtaining IAM permissions for AWS CloudShell
<a name="cloudshell-permissions"></a>

Using the access management resources provided by AWS Identity and Access Management, administrators can grant permissions to IAM users so they can access AWS CloudShell and use the environment's features.

The quickest way for an administrator to grant access to users is through an AWS managed policy. An [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) is a standalone policy that's created and administered by AWS. The following AWS managed policy for CloudShell can be attached to IAM identities:
+ `AWSCloudShellFullAccess`: Grants permission to use AWS CloudShell with full access to all features.

 If you want to limit the scope of actions that an IAM user can perform with AWS CloudShell, you can create a custom policy that uses the `AWSCloudShellFullAccess` managed policy as a template. For more information about limiting the actions that are available to users in CloudShell, see [Managing AWS CloudShell access and usage with IAM policies](https://docs.aws.amazon.com/cloudshell/latest/userguide/sec-auth-with-identities.html) in the *AWS CloudShell User Guide*.

**Note**
Your IAM identity also requires a policy that grants permission to make calls to Security Incident Response.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Incident Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-ir` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
