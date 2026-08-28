---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/enable-webauthn-portal.html
---

# Enabling WebAuthn redirection in portal settings
<a name="enable-webauthn-portal"></a>

To enable WebAuthn redirection for websites accessed within the remote browser session, follow these steps.

1. Open the WorkSpaces Secure Browser console at [https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/](https://console.aws.amazon.com/workspaces-web/home?region=us-east-1#/).

1. Choose **WorkSpaces Secure Browser**, **Web portals**, choose your web portal, and then choose **Edit**.

1. Navigate to the **User settings** section.

1. Under **User permissions**, set **Allow users to use local authentication in their portal session** to **Allowed**.

1. Choose **Save** to apply the configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
