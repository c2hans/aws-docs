---
source_url: https://docs.aws.amazon.com/res/latest/ug/manage-users.html
---

# Identity management
<a name="manage-users"></a>

Research and Engineering Studio can use any SAML 2.0 compliant identity provider. To use Amazon Cognito as a native user directory which allows users to log in to the web portal and Linux based VDIs with Cognito user identities, see [Setting up Amazon Cognito users](setting-up-cognito-users.md). If you deployed RES using the external resources or plan to use IAM Identity center, see [Setting up single sign-on (SSO) with IAM Identity Center](sso-idc.md). If you have your own SAML 2.0 compliant identity provider, see [Configuring your identity provider for single sign-on (SSO)](configure-id-federation.md).

**Topics**
+ [Setting up Amazon Cognito users](setting-up-cognito-users.md)
+ [Active Directory Synchronization](active-directory-sync.md)
+ [Setting up single sign-on (SSO) with IAM Identity Center](sso-idc.md)
+ [Configuring your identity provider for single sign-on (SSO)](configure-id-federation.md)
+ [Setting passwords for users](setting-user-passwords.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Research and Engineering Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query res` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
