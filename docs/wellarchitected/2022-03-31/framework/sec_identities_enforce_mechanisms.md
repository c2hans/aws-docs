---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_identities_enforce_mechanisms.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC02-BP01 Use strong sign-in mechanisms
<a name="sec_identities_enforce_mechanisms"></a>

 Enforce minimum password length, and educate your users to avoid common or reused passwords. Enforce multi-factor authentication (MFA) with software or hardware mechanisms to provide an additional layer of verification. For example, when using IAM Identity Center as the identity source, configure the “context-aware” or “always-on” setting for MFA, and allow users to enroll their own MFA devices to accelerate adoption. When using an external identity provider (IdP), configure your IdP for MFA.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Create an AWS Identity and Access Management (IAM) policy to enforce MFA sign-in: Create a customer-managed IAM policy that prohibits all IAM actions except for the ones that allow a user to assume roles, change their own credentials, and manage their MFA devices on the [My Security Credentials page](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_users-self-manage-mfa-and-creds.html#tutorial_mfa_step1).
+  Enable MFA in your identity provider: Enable [MFA](https://aws.amazon.com/iam/details/mfa) in the identity provider or single sign-on service, such as [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/step1.html), that you use.
+  Configure a strong password policy: Configure a strong [password policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html?ref=wellarchitected) in IAM and federated identity systems to help protect against brute-force attacks.
+  [Rotate credentials regularly](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials): Ensure administrators of your workload change their passwords and access keys (if used) regularly.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Getting Started with AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html)
+  [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
+  [Identity Providers and Federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html)
+  [The AWS Account Root User](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html?ref=wellarchitected)
+  [Temporary Security Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html?ref=wellarchitected)
+  [Security Partner Solutions: Access and Access Control](https://aws.amazon.com/security/partner-solutions/#access-control)

 **Related videos:**
+  [Best Practices for Managing, Retrieving, and Rotating Secrets at Scale](https://youtu.be/qoxxRlwJKZ4)
+  [Managing user permissions at scale with IAM Identity Center](https://youtu.be/aEIqeFCcK7E)
+  [Mastering identity at every layer of the cake](https://www.youtube.com/watch?v=vbjFjMNVEpc)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
