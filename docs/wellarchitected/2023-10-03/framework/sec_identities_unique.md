---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec_identities_unique.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC02-BP02 Use temporary credentials
<a name="sec_identities_unique"></a>

 When doing any type of authentication, it’s best to use temporary credentials instead of long-term credentials to reduce or eliminate risks, such as credentials being inadvertently disclosed, shared, or stolen.

**Desired outcome:** To reduce the risk of long-term credentials, use temporary credentials wherever possible for both human and machine identities. Long-term credentials create many risks, for example, they can be uploaded in code to public GitHub repositories. By using temporary credentials, you significantly reduce the chances of credentials becoming compromised.

**Common anti-patterns:**
+  Developers using long-term access keys from IAM users rather than obtaining temporary credentials from the CLI using federation.
+  Developers embedding long-term access keys in their code and uploading that code to public Git repositories.
+  Developers embedding long-term access keys in mobile apps that are then made available in app stores.
+  Users sharing long-term access keys with other users, or employees leaving the company with long-term access keys still in their possession.
+  Using long-term access keys for machine identities when temporary credentials could be used.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Use temporary security credentials instead of long-term credentials for all AWS API and CLI requests. API and CLI requests to AWS services must, in nearly every case, be signed using [AWS access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html). These requests can be signed with either temporary or long-term credentials. The only time you should use long-term credentials, also known as long-term access keys, is if you are using an [IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) or the [AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html). When you federate to AWS or assume an [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) through other methods, temporary credentials are generated. Even when you access the AWS Management Console using sign-in credentials, temporary credentials are generated for you to make calls to AWS services. There are few situations where you need long-term credentials and you can accomplish nearly all tasks using temporary credentials.

 Avoiding the use of long-term credentials in favor of temporary credentials should go hand in hand with a strategy of reducing the usage of IAM users in favor of federation and IAM roles. While IAM users have been used for both human and machine identities in the past, we now recommend not using them to avoid the risks in using long-term access keys.

### Implementation steps
<a name="implementation-steps"></a>

 For human identities like employees, administrators, developers, operators, and customers:
+  You should [rely on a centralized identity provider](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_identity_provider.html) and [require human users to use federation with an identity provider to access AWS using temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp). Federation for your users can be done either with [direct federation to each AWS account](https://aws.amazon.com/identity/federation/) or using [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) and the identity provider of your choice. Federation provides a number of advantages over using IAM users in addition to eliminating long-term credentials. Your users can also request temporary credentials from the command line for [direct federation](https://aws.amazon.com/blogs/security/how-to-implement-federated-api-and-cli-access-using-saml-2-0-and-ad-fs/) or by using [IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html). This means that there are few uses cases that require IAM users or long-term credentials for your users.
+  When granting third parties, such as software as a service (SaaS) providers, access to resources in your AWS account, you can use [cross-account roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) and [resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html).
+  If you need to grant applications for consumers or customers access to your AWS resources, you can use [Amazon Cognito identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html) or [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) to provide temporary credentials. The permissions for the credentials are configured through IAM roles. You can also define a separate IAM role with limited permissions for guest users who are not authenticated.

 For machine identities, you might need to use long-term credentials. In these cases, you should [require workloads to use temporary credentials with IAM roles to access AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-workloads-use-roles).
+  For [Amazon Elastic Compute Cloud](https://aws.amazon.com/pm/ec2/) (Amazon EC2), you can use [roles for Amazon EC2](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html).
+  [AWS Lambda](https://aws.amazon.com/lambda/) allows you to configure a [Lambda execution role to grant the service permissions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) to perform AWS actions using temporary credentials. There are many other similar models for AWS services to grant temporary credentials using IAM roles.
+  For IoT devices, you can use the [AWS IoT Core credential provider](https://docs.aws.amazon.com/iot/latest/developerguide/authorizing-direct-aws.html) to request temporary credentials.
+  For on-premises systems or systems that run outside of AWS that need access to AWS resources, you can use [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html).

 There are scenarios where temporary credentials are not an option and you might need to use long-term credentials. In these situations, [audit and rotate credentials periodically](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_audit.html) and [rotate access keys regularly for use cases that require long-term credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials). Some examples that might require long-term credentials include WordPress plugins and third-party AWS clients. In situations where you must use long-term credentials, or for credentials other than AWS access keys, such as database logins, you can use a service that is designed to handle the management of secrets, such as [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/). Secrets Manager makes it simple to manage, rotate, and securely store encrypted secrets using [supported services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating.html). For more information about rotating long-term credentials, see [rotating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey).

## Resources
<a name="resources"></a>

 **Related best practices:**
+ [SEC02-BP03 Store and use secrets securely](sec_identities_secrets.md)
+ [SEC02-BP04 Rely on a centralized identity provider](sec_identities_identity_provider.md)
+ [SEC03-BP08 Share resources securely within your organization](sec_permissions_share_securely.md)

 **Related documents:**
+  [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)
+  [AWS Credentials](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html)
+  [IAM Security Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
+  [IAM Roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
+  [IAM Identity Center](https://aws.amazon.com/iam/identity-center/)
+  [Identity Providers and Federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html)
+  [Rotating Access Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey)
+  [Security Partner Solutions: Access and Access Control](https://aws.amazon.com/security/partner-solutions/#access-control)
+  [The AWS Account Root User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html)

 **Related videos:**
+  [Managing user permissions at scale with AWS IAM Identity Center](https://youtu.be/aEIqeFCcK7E)
+  [Mastering identity at every layer of the cake](https://www.youtube.com/watch?v=vbjFjMNVEpc)
