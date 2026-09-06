---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-max-duration.html
---

# AWS Client VPN maximum VPN session duration timeout
<a name="cvpn-working-max-duration"></a>

AWS Client VPN provides several options for the maximum VPN session duration, which is the maximum time allowed for a client connection to the Client VPN endpoint. You can configure a shorter maximum VPN session duration to help meet security and compliance requirements. By default, the maximum VPN session duration is 24 hours. Once you set the maximum session duration, you can control what happens with that session when that timeout is reached. The disconnect on session timeout option allows you to terminate the session or to automatically attempt a reconnection to the endpoint. Terminating a session allows you more control over endpoint security by enforcing maximum VPN session duration. If a session is set to terminate when the maximum time is reached, users will need to reconnect and provide their authentication credentials in order to re-establish the VPN connection.

When disconnect on session timeout is set to automatically reconnect, and the maximum session time is reached,
+ a new session is automatically established in the case of cached user credentials (Active Directory) or certificate-based authentication (Mutual Authentication). To fully disconnect and not automatically reconnect, these users should manually disconnect.
+ a new session is not automatically established in the case of federated authentication (SAML). These users must authenticate again after session timeout expiration to re-establish the VPN connection.

**Note**
When the maximum VPN session duration value is decreased from its current value, any active VPN sessions that are connected to the endpoint for a time frame longer than the newly set duration are disconnected.
Changing the disconnect on session timeout option applies the new setting to any currently open sessions.
Client VPN enforces the maximum session duration for each connection. If a connection drops and a new connection is started, the maximum session duration timer resets for the new connection.

## Configure the maximum VPN session during creation of an AWS Client VPN endpoint
<a name="configure-max-duration-endpoint-creation"></a>

The duration of a VPN session is configured during the creation of a Client VPN endpoint. See [Create an AWS Client VPN endpoint](cvpn-working-endpoint-create.md) for the steps to create a Client VPN endpoint and set the maximum session duration.

**Topics**
+ [Configure the maximum VPN session during creation of an endpoint](#configure-max-duration-endpoint-creation)
+ [View current maximum VPN session duration](display-max-duration.md)
+ [Modify the maximum VPN session duration](modify-max-timeout.md)
