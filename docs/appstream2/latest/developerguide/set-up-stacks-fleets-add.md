---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets-add.html
---

# Provide Access to Users in Amazon WorkSpaces Applications
<a name="set-up-stacks-fleets-add"></a>

After you create a stack with an associated fleet, you can provide access to users through the WorkSpaces Applications user pool, SAML 2.0 [single sign-on (SSO)], or the WorkSpaces Applications API. For more information, see [User Pool Administration in Amazon WorkSpaces Applications](user-pool-admin.md) and [Amazon WorkSpaces Applications Integration with SAML 2.0](external-identity-providers.md).

**Note**
Users in the WorkSpaces Applications user pool can't be assigned to stacks with fleets that are joined to an Active Directory domain.

After you provide your users with access to WorkSpaces Applications, they can start WorkSpaces Applications streaming sessions by using a web browser or by using the WorkSpaces Applications client application for a supported device. If you provide access to users through the WorkSpaces Applications user pool, they must use a web browser for streaming sessions. If you use SAML 2.0 or the WorkSpaces Applications API, you can make the WorkSpaces Applications client available to them. The WorkSpaces Applications client is a native application that is designed for users who require additional functionality during their WorkSpaces Applications streaming sessions. For more information, see [Provide Access Through the WorkSpaces Applications Client](client-application.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
