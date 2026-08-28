---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/android.html
---

# AWS Client VPN connections on Android and iOS applications
<a name="android"></a>

**Important**
If the Client VPN endpoint has been configured to use [SAML-based federated authentication](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/client-authentication.html#federated-authentication), you cannot use the OpenVPN-based VPN client to connect to a Client VPN endpoint. This includes any ARM-based architectures. If you are using a device with an ARM processor (such as Apple Silicon Macs or ARM-based Windows devices), you must use SAML-based VPN endpoints with the AWS provided client instead of OpenVPN clients.

The following information shows how to establish a VPN connection using the OpenVPN client application on an Android or iOS mobile device. The steps for Android and iOS are the same.

**Note**
For more information about downloading and using the OpenVPN client application for iOS or Android, see the [OpenVPN Connect User Guide](https://openvpn.net/connect-docs/user-guide.html) on the OpenVPN website.

Before you begin, ensure that your Client VPN administrator has [created a Client VPN endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html#cvpn-working-endpoint-create) and provided you with the [Client VPN endpoint configuration file](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-export.html). If you want to connect to multiple profiles simultaneously, you'll need a configuration file for each profile.

To establish the connection, start the OpenVPN client application, and then import the file that you received from your Client VPN administrator.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
