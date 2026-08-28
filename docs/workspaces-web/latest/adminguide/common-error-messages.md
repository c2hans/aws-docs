---
source_url: https://docs.aws.amazon.com/workspaces-web/latest/adminguide/common-error-messages.html
---

# Common error messages
<a name="common-error-messages"></a>

The following are common error messages and their resolutions:

**WebAuthn error messages and resolutions**

| Error message | Resolution |
| --- | --- |
| Amazon DCV WebAuthn redirection failed to complete the registration request: Webauthn redirection is not supported by the client | Check that you are using a supported browser and version (Chrome 136\+ or Edge 137\+). |
| Prompt appears but unable to interact with local authenticators | Check that the Amazon DCV WebAuthn redirection extension is installed and enabled in your remote browser. |
| Amazon DCV WebAuthn redirection failed to complete the registration request: The relying party ID is not a registrable domain suffix of, nor equal to the current domain. Subsequently, an attempt to fetch the .well-known/webauthn resource of the claimed RP ID failed. | This means that the WebAuthenticationRemoteDesktopAllowedOrigins local browser policy is not applied. Check the policy and update to allow the content domain. Ensure that the browser is restarted. You may have to start a new session for changes to apply. |
| The operation either timed out or was not allowed. See: https://www.w3.org/TR/webauthn-2/\#sctn-privacy-considerations-client. | This error could occur if: (1) The DCV WebAuthn redirection extension is not installed or enabled, (2) The user cancels the authentication prompt, (3) The user enters an incorrect PIN for their security key, or (4) The user does not interact with the prompt and the request times out. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Secure Browser. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-web` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
