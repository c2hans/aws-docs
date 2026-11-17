---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-no-browser.html
---

# Troubleshooting AWS Client VPN: Client does not open browser for an endpoint — federated authentication
<a name="client-no-browser"></a>

**Problem**
I use federated authentication for my Client VPN endpoint. When clients try to connect to the endpoint, the client software does not open a browser window. Instead, the client either displays a user name and password popup window, or remains in a connecting state (for example, `Waiting for identity`).

Review the following common causes and apply the corresponding solution.

**Cause 1: The configuration file is missing the auth-federate flag**
The configuration file that was provided to the clients does not contain the `auth-federate` flag. The client displays a user name and password popup window instead of opening a browser window.

**Solution**
[Export the latest configuration file](cvpn-working-endpoint-export.md), import it to the AWS provided client, and try connecting again.

**Cause 2: The client's network blocks traffic to the endpoint**
With federated authentication, the AWS provided client must reach the Client VPN endpoint before it can open a browser window for sign-in. Something between the client and the endpoint might drop this traffic on the configured transport protocol and port (for example, UDP 443). Examples include a home router security feature, the internet service provider or a guest network. If this happens, the client receives no response.

The client remains in a connecting state, does not open a browser window and does not display an error. The client logs might show `Server poll timeout` or `SAML DYNAMIC_CHALLENGE not received within timeout`.

Other users can connect to the same endpoint. The affected device can usually connect from a different network, such as a mobile hotspot.

**Solution**
To confirm and work around this cause, do the following:

1. Confirm that the Client VPN endpoint DNS name resolves from the affected device. Prepend a random string to the DNS name when you test, for example `asdfa.cvpn-endpoint-0102bc4c2eEXAMPLE.prod.clientvpn.us-west-2.amazonaws.com`.

1. Connect the same device to a different network (for example, a mobile hotspot). Then try connecting again. If the connection succeeds, the original network is blocking the traffic.

1. (Optional) Capture network traffic on the affected device while it tries to connect. If the capture shows packets sent to the endpoint IP addresses on the configured port but no responses, the network drops the traffic before it reaches the endpoint.

1. Use a transport protocol and port that the client's network allows. You can [modify the endpoint](cvpn-working-endpoint-modify.md) to use the other supported VPN port (443 or 1194). You can't change the transport protocol of an existing endpoint. To use TCP instead of UDP, [create an endpoint](cvpn-working-endpoint-create.md) that uses TCP as the transport protocol.

1. Export the updated configuration file as described earlier in this topic and distribute it to your users.
