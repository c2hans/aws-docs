---
source_url: https://docs.aws.amazon.com/wickr/latest/adminguide/sso-configuration.html
---

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Single sign-on configuration for AWS Wickr
<a name="sso-configuration"></a>

In the AWS Management Console for Wickr, you can configure Wickr to use a single sign-on system to authenticate. SSO provides an added layer of security when paired with an appropriate multi-factor authentication (MFA) system. Wickr supports SSO providers who use OpenID Connect (OIDC) only. Providers who use Security Assertion Markup Language (SAML) are not supported.

**Topics**
+ [View SSO details in AWS Wickr](view-sso-details.md)
+ [Configure SSO in AWS Wickr](configure-sso.md)
+ [Grace period for token refresh](token-refresh.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
