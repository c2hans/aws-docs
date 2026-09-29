---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-connect-linux.html
---

# AWS Client VPN for Linux
<a name="client-vpn-connect-linux"></a>

These sections describe how to establish a VPN connection using the AWS provided client for Linux. For the latest updates and downloads, see the [AWS Client VPN for Linux release notes](client-vpn-connect-linux-release-notes.md).

## Requirements for connecting to Client VPN with an AWS provided client for Linux
<a name="client-vpn-connect-linux-req"></a>

To use the AWS provided client for Linux, the following is required:
+ Ubuntu 22.04 LTS (AMD64), Ubuntu 24.04 LTS (AMD64 only), or Ubuntu 26.04 LTS (AMD64 only)
+ Endpoint security software might require exclusions to allow the AWS provided client to function. For more information, see [Endpoint security software compatibility](client-vpn-connect-endpoint-security.md).

For Client VPN endpoints that use SAML-based federated authentication (single sign-on) the client reserves TCP ports 8096-8115 on your computer.

Before you begin, ensure that your Client VPN administrator has [created a Client VPN endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html#cvpn-working-endpoint-create) and provided you with the [Client VPN endpoint configuration file](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-export.html). If you want to connect to multiple profiles simultaneously, you'll need a configuration file for each profile.

For instructions on using the client, see [Connect using the AWS provided client](client-vpn-connect-how.md).

**Topics**
+ [Requirements for connecting to Client VPN with an AWS provided client for Linux](#client-vpn-connect-linux-req)
+ [Install the client](client-vpn-connect-linux-install.md)
+ [Release notes](client-vpn-connect-linux-release-notes.md)
