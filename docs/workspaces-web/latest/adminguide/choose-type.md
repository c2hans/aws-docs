---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/choose-type.html
---

# Choosing the identity provider type for Amazon WorkSpaces Secure Browser
<a name="choose-type"></a>

WorkSpaces Secure Browser offers two authentication types: **Standard** and **AWS IAM Identity Center**. You choose the authentication type to use with your portal on the **Configure identity provider page**.
+ For **Standard** (default option), federate your 3rd party SAML 2.0 identity provider (such as Okta or Ping) directly with your portal. For more information, see [Configuring the standard authentication type for Amazon WorkSpaces Secure Browser](configure-standard.md). The standard type supports both SP-initiated and IdP-initiated authentication flows.
+ For **IAM Identity Center** (advanced option), federate the IAM Identity Center with your portal. To use this authentication type, your IAM Identity Center and WorkSpaces Secure Browser portal must both reside in the same AWS Region. For more information, see [Configuring the IAM Identity Center authentication type for Amazon WorkSpaces Secure Browser](configure-iam.md).

**Topics**
+ [Configuring the standard authentication type for Amazon WorkSpaces Secure Browser](configure-standard.md)
+ [Configuring the IAM Identity Center authentication type for Amazon WorkSpaces Secure Browser](configure-iam.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
