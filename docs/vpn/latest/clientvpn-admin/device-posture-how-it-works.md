---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-how-it-works.html
---

# How device posture works
<a name="device-posture-how-it-works"></a>

Device posture builds on your existing Client VPN authentication. It requires the AWS provided client version 6.2.0 or later. When device posture is enabled on an endpoint, Client VPN adds a device health check to each connection:

1. A user initiates a connection and authenticates as they do today, using mutual authentication, SAML, or Active Directory.

1. Before the connection is established, the AWS provided client obtains the device posture token that the device trust provider makes available on the device, and sends it to Client VPN.

1. Client VPN validates the device posture token, then evaluates your authorization policy against a combination of the device posture token, the authenticated user identity, and the connection details.

1. If the policy allows the request, the connection is established. If the policy denies the request, the connection is refused and the AWS provided client displays the message `Authorization policy evaluation failed`.

1. Every 5 minutes, Client VPN re-evaluates the policy against the most recent device posture token. The AWS provided client refreshes the token independently, on its own schedule. If a device no longer meets your requirements, Client VPN ends the session. If the device stops providing a token, Client VPN evaluates against the last token it received for up to 15 minutes. After 15 minutes without a new token, Client VPN drops the token.
