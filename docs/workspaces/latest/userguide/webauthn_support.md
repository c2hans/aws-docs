---
source_url: https://docs.aws.amazon.com/workspaces/latest/userguide/webauthn_support.html
---

# WebAuthn authentication for WorkSpaces client
<a name="webauthn_support"></a>

In-session WebAuthn authentication is supported using the DCV for Windows and Linux WorkSpaces, on Windows, Linux and macOS clients. WorkSpaces using the PCoIP protocol doesn't support WebAuthn redirection.

You can use WebAuthn authentication for in-session authentication using FIDO2-enabled authentication methods like security keys or biometrics. In-session authentication refers to WebAuthn authentication that's performed after logging in and requested by web applications running within the session. For example, you can use Yubikey for in-session authentication while using Google Chrome.

## Client version requirements
<a name="webauthn-client-versions"></a>

The following WorkSpaces client versions support WebAuthn:

| WebAuthn Type | Client versions supported |
| --- | --- |
| Standard WebAuthn |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/webauthn_support.html)  |
| Enhanced WebAuthn |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/workspaces/latest/userguide/webauthn_support.html)  |

## Get Started
<a name="webauthn_get_started"></a>
+ [Configure WebAuthn on Windows WorkSpaces](webauthn_windows.md)
+ [Configure WebAuthn on Linux WorkSpaces](webauthn_linux.md)
