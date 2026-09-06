---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/macos.html
---

# Connect to an AWS Client VPN endpoint using a macOS client application
<a name="macos"></a>

These sections describe how to establish a VPN connection using the macOS-based VPN client, Tunnelblick or AWS Client VPN.

Before you begin, ensure that your Client VPN administrator has [created a Client VPN endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html#cvpn-working-endpoint-create) and provided you with the [Client VPN endpoint configuration file](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-export.html). If you want to connect to multiple profiles simultaneously, you'll need a configuration file for each profile.

For troubleshooting information, see [Troubleshooting AWS Client VPN connections with macOS clients](macos-troubleshooting.md).

**Important**
If the Client VPN endpoint has been configured to use [SAML-based federated authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-authentication.html#federated-authentication), you cannot use the OpenVPN-based VPN client to connect to a Client VPN endpoint. This includes any ARM-based architectures. If you are using a device with an ARM processor (such as Apple Silicon Macs or ARM-based Windows devices), you must use SAML-based VPN endpoints with the AWS provided client instead of OpenVPN clients.

**Topics**
+ [Establish a VPN connection on macOS](macos-tunnelblick.md)
