---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool.html
---

# Amazon WorkSpaces Applications User Pools
<a name="user-pool"></a>

The WorkSpaces Applications user pool provides a simplified way to manage access to applications for your users through a persistent portal for each AWS Region. This feature is a built-in alternative to user management through [Active Directory](active-directory.md) and [SAML 2.0 federation](external-identity-providers.md). Stacks can't be assigned to users in the user pool if the stacks are associated with a fleet that is joined to an Active Directory domain.

The WorkSpaces Applications user pool provides the following key features:
+ Users can access application stacks through a persistent URL and login credentials by using their email address and a password that they choose.
+ Users' email addresses are case-sensitive. During login, if they specify an email address that doesn't use the same capitalization as the email address specified when their user pool account was created, a "user does not exist" error message displays.
+ You can assign multiple stacks to users. Doing so enables WorkSpaces Applications to display multiple application catalogs to users when they log in.
+ When you create new users, a welcome email is automatically sent to them. The email includes instructions, a login portal link, and a temporary password for connecting to the login portal.
+ After you create users, they are enabled unless you specifically disable them.
+ You can control which users have access to which application stacks, or disable access completely.

**Topics**
+ [User Pool End User Experience for Amazon WorkSpaces Applications](user-pool-end-user.md)
+ [Resetting a Forgotten Password in Amazon WorkSpaces Applications](user-pool-end-user-reset-password.md)
+ [User Pool Administration in Amazon WorkSpaces Applications](user-pool-admin.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
