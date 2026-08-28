---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/webauthn-usage.html
---

# Using WebAuthn redirection in remote browser sessions
<a name="webauthn-usage"></a>

Once WebAuthn redirection is enabled in the portal settings and the local browser policy is configured, users can use WebAuthn authentication on websites within their WorkSpaces Secure Browser remote browser sessions.

Users can authenticate to websites using:
+ FIDO2 security keys connected to their local device
+ Passkeys
+ Platform authenticators like Windows Hello or Touch ID

The WebAuthn authentication process is seamlessly forwarded from the remote browser session to the user's local device, providing secure passwordless authentication while maintaining the security benefits of the remote browsing environment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
