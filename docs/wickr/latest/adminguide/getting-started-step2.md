---
source_url: https://docs.aws.amazon.com/wickr/latest/adminguide/getting-started-step2.html
---

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Step 2: Configure your network
<a name="getting-started-step2"></a>

Complete the following procedure to access the AWS Management Console for Wickr, where you can add users, add security groups, configure SSO, configure data retention, and additional network settings.

1. On the **Networks** page, select the network name to navigate to that network.

   You're redirected to the Wickr Admin Console for the selected network.

1. The following user management options are available. For more information about configuring these settings, see [Manage your AWS Wickr network](managing-network.md).
   + **Security Group** — Manage security groups and their settings, such as password complexity policies, messaging preferences, calling features, security features and external federation. For more information, see [Security groups for AWS Wickr](security-groups.md).
   + **Single Sign-on (SSO) Configuration** — Configure SSO and view the endpoint address for your Wickr network. Wickr supports SSO providers who use OpenID Connect (OIDC) only. Providers who use Security Assertion Markup Language (SAML) are not supported. For more information, see [Single sign-on configuration for AWS Wickr](sso-configuration.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
