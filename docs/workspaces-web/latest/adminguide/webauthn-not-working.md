---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/webauthn-not-working.html
---

# WebAuthn redirection not working
<a name="webauthn-not-working"></a>

If WebAuthn authentication prompts do not appear or fail to work:

1. Verify WebAuthn is enabled in the portal settings under **User permissions**.

1. Check that the local browser policy is configured correctly by navigating to `chrome://policy` or `edge://policy` and confirming `WebAuthenticationRemoteDesktopAllowedOrigins` includes your region's content URL.

1. Ensure the browser version meets requirements: Chrome 136\+ or Edge 137\+.

1. Test with a different authenticator (security key vs. platform authenticator).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
