---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/identify-domains.html
---

# Identifying domains for the single sign-on extension in Amazon WorkSpaces Secure Browser
<a name="identify-domains"></a>

First, determine which domains you need for your SAML IdP and websites. You can add up to 10 domains.

You are responsible for testing and identifying the appropriate domain for the cookies to be synchronized. Changes might be required at the IdP or website authentication level to ensure single sign-on works as expected.

To see which domains to use with most common IdP, refer to the following table:

**IdP and domains**

| IdP | Domain |
| --- | --- |
| Okta | okta.com |
| Entra ID | microsoftonline.com |
| AWS Identity Center | awsapps.com |
| One Login | onelogin.com |
| Duo | duosecurity.com |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
