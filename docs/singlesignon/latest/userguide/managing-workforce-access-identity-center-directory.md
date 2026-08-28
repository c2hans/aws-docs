---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/managing-workforce-access-identity-center-directory.html
---

# Managing access for users in the Identity Center directory
<a name="managing-workforce-access-identity-center-directory"></a>

Learn how to manage passwords and multi-factor authentication (MFA) for users in the IAM Identity Center directory. These security features help protect user accounts.

**Note**
These features do not apply to Active Directory users or external identity provider users.

Administrators can manage both passwords and MFA through the IAM Identity Center console. These security features work only with the built-in Identity Center directory.

## Password management
<a name="password-management-overview"></a>

Password management includes these capabilities:
+ Reset passwords with email instructions
+ Generate one-time passwords
+ Configure automatic email verification for API-created users

AWS enforces fixed security requirements, including complexity rules and password reuse restrictions.

## MFA
<a name="mfa-overview"></a>

MFA is enabled by default and supports up to eight devices per user.

Supported device types include:
+ Authenticator apps
+ Security keys
+ Built-in biometric authenticators

Administrators can register and manage MFA devices for users.

**Topics**
+ [Password management](#password-management-overview)
+ [MFA](#mfa-overview)
+ [Setting up user passwords](set-up-user-passwords.md)
+ [MFA for Identity Center directory users](enable-mfa.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
