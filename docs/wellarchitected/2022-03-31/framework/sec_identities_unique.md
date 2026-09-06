---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_identities_unique.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC02-BP02 Use temporary credentials
<a name="sec_identities_unique"></a>

 Require identities to dynamically acquire [temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html). For workforce identities, use AWS IAM Identity Center, or federation with AWS Identity and Access Management (IAM) roles to access AWS accounts. For machine identities, such as Amazon Elastic Compute Cloud(Amazon EC2) instances or AWS Lambda functions, require the use of IAM roles instead of users with long-term access keys.

For human identities using the AWS Management Console, require users to acquire temporary credentials and federate into AWS. You can do this using the AWS IAM Identity Center user portal. For users requiring CLI access, ensure that they use [AWS CLI v2](http://aws.amazon.com/blogs/developer/aws-cli-v2-is-now-generally-available/), which supports direct integration with IAM Identity Center. Users can create CLI profiles that are linked to IAM Identity Center accounts and roles. The CLI automatically retrieves AWS credentials from IAM Identity Center and refreshes them on your behalf. This eliminates the need to copy and paste temporary AWS credentials from the IAM Identity Center console. For SDK, users should rely on AWS Security Token Service (AWS STS) to assume roles to receive temporary credentials. In certain cases, temporary credentials might not be practical. You should be aware of the risks of storing access keys, rotate these often, and require multi-factor authentication (MFA) as a condition when possible. Use last accessed information to determine when to rotate or remove access keys.

For cases where you need to grant consumers access to your AWS resources, use [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/role-based-access-control.html) identity pools and assign them a set of temporary, limited privilege credentials to access your AWS resources. The permissions for each user are controlled through [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) that you create. You can define rules to choose the role for each user based on claims in the user's ID token. You can define a default role for authenticated users. You can also define a separate IAM role with limited permissions for guest users who are not authenticated.

For machine identities, you should rely on IAM roles to grant access to AWS. For Amazon Elastic Compute Cloud(Amazon EC2) instances, you can use [roles for Amazon EC2](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html). You can attach an IAM role to your Amazon EC2 instance to enable your applications running on Amazon EC2 to use temporary security credentials that AWS creates, distributes, and rotates automatically through the Instance Metadata Service (IMDS). The [latest version](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/) of IMDS helps protect against vulnerabilities that expose the temporary credentials and should be implemented. For accessing Amazon EC2 instances using keys or passwords, [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) is a more secure way to access and manage your instances using a pre- installed agent without the stored secret. Additionally, other AWS services, such as AWS Lambda, enable you to configure an IAM service role to grant the service permissions to perform AWS actions using temporary credentials. In situations where you cannot use temporary credentials, use programmatic tools, such as [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), to automate credential rotation and management.

**Audit and rotate credentials periodically: **Periodic validation, preferably through an automated tool, is necessary to verify that the correct controls are enforced. For human identities, you should require users to change their passwords periodically and retire access keys in favor of temporary credentials. As you are moving from users to centralized identities, you can [generate a credential report ](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html)to audit your users. We also recommend that you enforce MFA settings in your identity provider. You can set up [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) to monitor these settings. For machine identities, you should rely on temporary credentials using IAM roles. For situations where this is not possible, frequent auditing and rotating access keys is necessary.

**Store and use secrets securely:** For credentials that are not IAM-related and cannot take advantage of temporary credentials, such as database logins, use a service that is designed to handle management of secrets, such as [Secrets Manager](https://aws.amazon.com/secrets-manager/). Secrets Manager makes it easy to manage, rotate, and securely store encrypted secrets using [supported services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating.html). Calls to access the secrets are logged in AWS CloudTrail for auditing purposes, and IAM permissions can grant least-privilege access to them.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Implement least privilege policies: Assign access policies with least privilege to IAM groups and roles to reflect the user's role or function that you have defined.
  +  [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)
+  Remove unnecessary permissions: Implement least privilege by removing permissions that are unnecessary.
  +  [Reducing policy scope by viewing user activity](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html)
  +  [View role access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_manage_delete.html#roles-delete_prerequisites)
+  Consider permissions boundaries: A permissions boundary is an advanced feature for using a managed policy that sets the maximum permissions that an identity-based policy can grant to an IAM entity. An entity's permissions boundary allows it to perform only the actions that are allowed by both its identity-based policies and its permissions boundaries.
  +  [Lab: IAM permissions boundaries delegating role creation](https://wellarchitectedlabs.com/Security/300_IAM_Permission_Boundaries_Delegating_Role_Creation/README.html)
+  Consider resource tags for permissions: You can use tags to control access to your AWS resources that support tagging. You can also tag users and roles to control what they can access.
  +  [Lab: IAM tag based access control for EC2](https://wellarchitectedlabs.com/Security/300_IAM_Tag_Based_Access_Control_for_EC2/README.html)
  +  [Attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Getting Started with AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html)
+  [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
+  [Identity Providers and Federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html)
+  [Security Partner Solutions: Access and Access Control](https://aws.amazon.com/security/partner-solutions/#access-control)
+  [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)
+  [The AWS Account Root User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html)

 **Related videos:**
+  [Best Practices for Managing, Retrieving, and Rotating Secrets at Scale](https://youtu.be/qoxxRlwJKZ4)
+  [Managing user permissions at scale with AWS IAM Identity Center](https://youtu.be/aEIqeFCcK7E)
+  [Mastering identity at every layer of the cake](https://www.youtube.com/watch?v=vbjFjMNVEpc)
