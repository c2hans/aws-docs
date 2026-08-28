---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_identities_audit.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC02-BP05 Audit and rotate credentials periodically
<a name="sec_identities_audit"></a>

 When you cannot rely on temporary credentials and require long-term credentials, audit credentials to ensure that the defined controls for example, multi-factor authentication (MFA), are enforced, rotated regularly, and have the appropriate access level. Periodic validation, preferably through an automated tool, is necessary to verify that the correct controls are enforced. For human identities, you should require users to change their passwords periodically and retire access keys in favor of temporary credentials. As you are moving from users to centralized identities, you can [generate a credential report ](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)to audit your users. We also recommend that you enforce MFA settings in your identity provider. You can set up [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) to monitor these settings. For machine identities, you should rely on temporary credentials using IAM roles. For situations where this is not possible, frequent auditing and rotating access keys is necessary.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Regularly audit credentials: Use credential reports, and Identify and Access Management (IAM) Access Analyzer to audit IAM credentials and permissions.
  +  [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
  +  [Getting credential report](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)
  +  [Lab: Automated IAM user cleanup](https://wellarchitectedlabs.com/Security/200_Automated_IAM_User_Cleanup/README.html?ref=wellarchitected-tool)
+  Use Access Levels to Review IAM Permissions: To improve the security of your AWS account, regularly review and monitor each of your IAM policies. Make sure that your policies grant the least privilege that is needed to perform only the necessary actions.
  +  [Use access levels to review IAM permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#use-access-levels-to-review-permissions)
+  Consider automating IAM resource creation and updates: AWS CloudFormation can be used to automate the deployment of IAM resources, including roles and policies, to reduce human error because the templates can be verified and version controlled.
  +  [Lab: Automated deployment of IAM groups and roles](https://wellarchitectedlabs.com/Security/200_Automated_Deployment_of_IAM_Groups_and_Roles/README.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Getting Started with AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html)
+  [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
+  [Identity Providers and Federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html)
+  [Security Partner Solutions: Access and Access Control](https://aws.amazon.com/security/partner-solutions/#access-control)
+  [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)

 **Related videos:**
+  [Best Practices for Managing, Retrieving, and Rotating Secrets at Scale](https://youtu.be/qoxxRlwJKZ4)
+  [Managing user permissions at scale with AWS IAM Identity Center](https://youtu.be/aEIqeFCcK7E)
+  [Mastering identity at every layer of the cake](https://www.youtube.com/watch?v=vbjFjMNVEpc)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
