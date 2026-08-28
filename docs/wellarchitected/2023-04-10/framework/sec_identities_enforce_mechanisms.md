---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sec_identities_enforce_mechanisms.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC02-BP01 Use strong sign-in mechanisms
<a name="sec_identities_enforce_mechanisms"></a>

Sign-ins (authentication using sign-in credentials) can present risks when not using mechanisms like multi-factor authentication (MFA), especially in situations where sign-in credentials have been inadvertently disclosed or are easily guessed. Use strong sign-in mechanisms to reduce these risks by requiring MFA and strong password policies.

 **Desired outcome:** Reduce the risks of unintended access to credentials in AWS by using strong sign-in mechanisms for [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) users, the [AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html), [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) (successor to AWS Single Sign-On), and third-party identity providers. This means requiring MFA, enforcing strong password policies, and detecting anomalous login behavior.

 **Common anti-patterns:**
+  Not enforcing a strong password policy for your identities including complex passwords and MFA.
+  Sharing the same credentials among different users.
+  Not using detective controls for suspicious sign-ins.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 There are many ways for human identities to sign-in to AWS. It is an AWS best practice to rely on a centralized identity provider using federation (direct federation or using AWS IAM Identity Center) when authenticating to AWS. In that case, you should establish a secure sign-in process with your identity provider or Microsoft Active Directory.

 When you first open an AWS account, you begin with an AWS account root user. You should only use the account root user to set up access for your users (and for [tasks that require the root user](https://docs.aws.amazon.com/accounts/latest/reference/root-user-tasks.html)). It’s important to turn on MFA for the account root user immediately after opening your AWS account and to secure the root user using the AWS [best practice guide](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_securely_operate_aws_account.html).

 If you create users in AWS IAM Identity Center, then secure the sign-in process in that service. For consumer identities, you can use [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/index.html) and secure the sign-in process in that service, or by using one of the identity providers that Amazon Cognito user pools supports.

 If you are using [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) users, you would secure the sign-in process using IAM.

 Regardless of the sign-in method, it’s critical to enforce a strong sign-in policy.

 **Implementation steps**

 The following are general strong sign-in recommendations. The actual settings you configure should be set by your company policy or use a standard like [NIST 800-63](https://pages.nist.gov/800-63-3/sp800-63b.html).
+  Require MFA. It’s an [IAM best practice to require MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#enable-mfa-for-privileged-users) for human identities and workloads. Turning on MFA provides an additional layer of security requiring that users provide sign-in credentials and a one-time password (OTP) or a cryptographically verified and generated string from a hardware device.
+  Enforce a minimum password length, which is a primary factor in password strength.
+  Enforce password complexity to make passwords more difficult to guess.
+  Allow users to change their own passwords.
+  Create individual identities instead of shared credentials. By creating individual identities, you can give each user a unique set of security credentials. Individual users provide the ability to audit each user’s activity.

 IAM Identity Center recommendations:
+  IAM Identity Center provides a predefined [password policy](https://docs.aws.amazon.com/singlesignon/latest/userguide/password-requirements.html) when using the default directory that establishes password length, complexity, and reuse requirements.
+  [Turn on MFA](https://docs.aws.amazon.com/singlesignon/latest/userguide/mfa-enable-how-to.html) and configure the context-aware or always-on setting for MFA when the identity source is the default directory, AWS Managed Microsoft AD, or AD Connector.
+  Allow users to [register their own MFA devices](https://docs.aws.amazon.com/singlesignon/latest/userguide/how-to-allow-user-registration.html).

 Amazon Cognito user pools directory recommendations:
+  Configure the [Password strength](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html) settings.
+  [Require MFA](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html) for users.
+  Use the Amazon Cognito user pools [advanced security settings](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html) for features like [adaptive authentication](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html) which can block suspicious sign-ins.

 IAM user recommendations:
+  Ideally you are using IAM Identity Center or direct federation. However, you might have the need for IAM users. In that case, [set a password policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html) for IAM users. You can use the password policy to define requirements such as minimum length or whether the password requires non-alphabetic characters.
+  Create an IAM policy to [enforce MFA sign-in](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_users-self-manage-mfa-and-creds.html#tutorial_mfa_step1) so that users are allowed to manage their own passwords and MFA devices.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [SEC02-BP03 Store and use secrets securely](sec_identities_secrets.md)
+  [SEC02-BP04 Rely on a centralized identity provider](sec_identities_identity_provider.md)
+  [SEC03-BP08 Share resources securely within your organization](sec_permissions_share_securely.md)

 **Related documents:**
+ [AWS IAM Identity Center Password Policy ](https://docs.aws.amazon.com/singlesignon/latest/userguide/password-requirements.html)
+ [ IAM user password policy ](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html)
+ [ Setting the AWS account root user password ](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html)
+ [ Amazon Cognito password policy ](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-policies.html)
+ [AWS credentials ](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html)
+ [ IAM security best practices ](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

 **Related videos:**
+  [Managing user permissions at scale with AWS IAM Identity Center](https://youtu.be/aEIqeFCcK7E)
+  [Mastering identity at every layer of the cake](https://www.youtube.com/watch?v=vbjFjMNVEpc)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
