---
source_url: https://docs.aws.amazon.com/grafana/latest/userguide/authentication-in-AMG.html
---

# Authenticate users in Amazon Managed Grafana workspaces
<a name="authentication-in-AMG"></a>

Individual users sign into your workspaces, to edit and view your dashboards. You can assign users to your workspaces and [give them user, editor, or administrator permissions](AMG-manage-users-and-groups-AMG.md). To get started, you create (or use an existing) identity provider to authenticate users.

Users are authenticated to use the Grafana console in an Amazon Managed Grafana workspace by single sign-on using your organization’s identity provider, instead of by using IAM. Each workspace can use one or both of the following authentication methods:
+ User credentials stored in identity providers (IdPs) that support Security Assertion Markup Language 2.0 (SAML 2.0)
+ AWS IAM Identity Center. AWS Single-sign-on (**AWS SSO**) was rebranded to **IAM Identity Center**.

For each of your workspaces, you can use SAML, IAM Identity Center, or both. If you begin by using one method, you can switch to using the other.

You must give your users (or groups that they belong to) permissions to the workspace before they can access functionality within the workspace. For more information about giving permissions to your users, see [Manage user and group access to Amazon Managed Grafana workspaces](AMG-manage-users-and-groups-AMG.md).

**Topics**
+ [Use SAML with your Amazon Managed Grafana workspace](authentication-in-AMG-SAML.md)
+ [Use AWS IAM Identity Center with your Amazon Managed Grafana workspace](authentication-in-AMG-SSO.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Grafana. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query grafana` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
