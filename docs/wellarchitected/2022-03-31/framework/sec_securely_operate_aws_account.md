---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_securely_operate_aws_account.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC01-BP02 Secure AWS account
<a name="sec_securely_operate_aws_account"></a>

There are a number of aspects to securing your AWS accounts, including the securing of, and not using the [root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html), and keeping your contact information up-to-date. You can use [AWS Organizations](https://aws.amazon.com/organizations/) to centrally manage and govern your accounts as you grow and scale your workloads in AWS. AWS Organizations helps you manage accounts, set controls, and configure services across your accounts.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Use AWS Organizations: Use AWS Organizations to centrally enforce policy-based management for multiple AWS accounts.
  +  [Getting started with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started.html)
  +  [How to use service control policies to set permission guardrails across accounts in your AWS Organization ](https://aws.amazon.com/blogs/security/how-to-use-service-control-policies-to-set-permission-guardrails-across-accounts-in-your-aws-organization/)
+  Limit use of the AWS account root user: Only use the root user to perform tasks that specifically require it.
  +  [Tasks that require root user credentials](https://docs.aws.amazon.com/accounts/latest/reference/root-user-tasks.html) in the *AWS Account Management Reference Guide*
+  Enable multi-factor-authentication (MFA) for the root user: Enable MFA on the AWS account root user, if AWS Organizations is not managing the root user for you.
  +  [Root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user_manage_mfa)
+  Periodically change the root user password: Changing the root user password reduces the risk that a saved password can be used. This is especially important if you are not using AWS Organizations and anyone has physical access.
  + [ Changing the AWS account root user password ](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_change-root.html)
+  Enable notification when the AWS account root user is used: Being notified automatically reduces risk.
  + [ How to receive notifications when your AWS account's root user access keys are used ](https://aws.amazon.com/blogs/security/how-to-receive-notifications-when-your-aws-accounts-root-access-keys-are-used/)
+  Restrict access to newly added Regions: For new AWS Regions, IAM resources, such as users and roles, will only be propagated to the Regions that you enable.
  + [ Setting permissions to enable accounts for upcoming AWS Regions](https://aws.amazon.com/blogs/security/setting-permissions-to-enable-accounts-for-upcoming-aws-regions/)
+  Consider AWS CloudFormation StackSets: CloudFormation StackSets can be used to deploy resources including IAM policies, roles, and groups into different AWS accounts and Regions from an approved template.
  + [ Use CloudFormation StackSets ](https://aws.amazon.com/blogs/aws/use-cloudformation-stacksets-to-provision-resources-across-multiple-aws-accounts-and-regions/)

## Resources
<a name="resources"></a>

 **Related documents:**
+ [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)
+ [AWS Security Audit Guidelines ](https://docs.aws.amazon.com/general/latest/gr/aws-security-audit-guide.html)
+ [ IAM Best Practices ](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
+  [Security Bulletins ](https://aws.amazon.com/security/security-bulletins/)

 **Related videos:**
+ [ Enable AWS adoption at scale with automation and governance ](https://youtu.be/GUMSgdB-l6s)
+ [ Security Best Practices the Well-Architected Way ](https://youtu.be/u6BCVkXkPnM)

 **Related examples:**
+ [ Lab: AWS account and root user ](https://youtu.be/u6BCVkXkPnM)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
