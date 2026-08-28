---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/set-up-user-passwords.html
---

# Setting up user passwords
<a name="set-up-user-passwords"></a>

For users created in the Identity Center directory, administrators can manage password policies, handle users without initial passwords, and reset passwords when needed. These password management features apply only to users in the built-in Identity Center directory. If you're using Active Directory or an external identity provider, you must manage passwords in those systems.

**Password management options**
+  **Password requirements** – Security requirements that users must meet when setting or changing passwords. This includes complexity rules and reuse restrictions.
+  **One-time password setup** – Configure email verification for users created through API or CLI who don't have initial passwords. You can also generate temporary passwords for immediate access.
+  **Password resets** – Reset passwords for users who are locked out or need new credentials. You can send reset instructions using email or generate one-time passwords.

**Topics**
+ [Password requirements when managing identities in IAM Identity Center](password-requirements.md)
+ [Email one-time password to users created with API or CLI](userswithoutpwd.md)
+ [Reset the IAM Identity Center user password for an end user](reset-password-for-user.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
