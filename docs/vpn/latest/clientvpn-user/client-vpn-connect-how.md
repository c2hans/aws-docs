---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-connect-how.html
---

# Connect using the AWS provided client
<a name="client-vpn-connect-how"></a>

Before you begin, ensure that your Client VPN administrator has [created a Client VPN endpoint](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html#cvpn-working-endpoint-create) and provided you with the [Client VPN endpoint configuration file](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-export.html). If you want to connect to multiple profiles simultaneously, you'll need a configuration file for each profile.

Before you begin, ensure that you've read the requirements for your platform ([Requirements](client-vpn-connect-windows.md#client-vpn-connect-windows-req), [Requirements](client-vpn-connect-macos.md#client-vpn-connect-macos-req), or [Requirements for connecting to Client VPN with an AWS provided client for Linux](client-vpn-connect-linux.md#client-vpn-connect-linux-req)). The AWS provided client is also referred to as the *AWS VPN Client* in the following steps.

## Version 6.0 and later
<a name="client-vpn-connect-how-6x"></a>

### Add a connection profile
<a name="client-vpn-6x-add-profile"></a>

To add one or more connection profiles, use a configuration file provided by your Client VPN administrator for each profile.

1. Open the **AWS VPN Client** app.

1. If no profiles exist, choose the **Add profile** button shown in the main window. Otherwise, choose the **Other actions** button, choose **Profiles**, and then choose **Add**.

1. For **Profile name**, enter a name for the profile.

1. For **VPN configuration file**, choose **Choose file**, browse to and then select the configuration file, and choose **Add profile**.

1. To create multiple connections, repeat the previous steps for each configuration file you want to add.

### Connect to a profile
<a name="client-vpn-6x-connect"></a>

1. Open the **AWS VPN Client** app.

1. Choose a profile from the **Select profile** dropdown, and then choose **Connect**.

1. If the Client VPN endpoint uses credential-based authentication, enter a user name and password when prompted. If it uses SAML-based federated authentication (single sign-on), complete authentication in the browser window that opens.

1. After you connect, the profile appears in the connected profiles list with a status of **Connected**.

**Note**
You can connect to multiple profiles concurrently.

**Note**
If any profile you connect to conflicts with a currently open session, you won't be able to make the connection. Either choose a new connection or disconnect from the session causing the conflict.

### Disconnect
<a name="client-vpn-6x-disconnect"></a>

To disconnect from a profile, choose the **Disconnect** button next to the connected profile. On Windows and macOS, you can also choose the AWS VPN Client icon in the system tray (or menu bar on macOS) and choose **Disconnect**. If you have multiple open connections, you must disconnect each connection individually.

### View connection statistics
<a name="client-vpn-6x-statistics"></a>

To view statistics for a connection, choose the **Other actions** button, and then choose **Statistics**.

## Earlier versions
<a name="client-vpn-connect-how-earlier"></a>

### Add a connection profile
<a name="client-vpn-earlier-add-profile"></a>

To add one or more connection profiles, use a configuration file provided by your Client VPN administrator for each profile.

1. Open the **AWS VPN Client** app.

1. Choose **File**, **Manage Profiles**.

1. Choose **Add Profile**.

1. For **Display Name**, enter a name for the profile.

1. For **VPN Configuration File**, browse to and then select the configuration file, and choose **Add Profile**.

1. To create multiple connections, repeat the previous steps for each configuration file you want to add. You can have up to five open connections.

### Connect to a profile
<a name="client-vpn-earlier-connect"></a>

1. Open the **AWS VPN Client** app.

1. In the **AWS VPN Client** window, choose the profile that you want to connect to, and then choose **Connect**.

1. If the Client VPN endpoint uses credential-based authentication, enter a user name and password when prompted. If it uses SAML-based federated authentication (single sign-on), complete authentication in the browser window that opens.

**Note**
You can connect to multiple profiles concurrently, up to five open connections. Repeat the connect step for each profile you want to initiate.

**Note**
If any profile you connect to conflicts with a currently open session, you won't be able to make the connection. Either choose a new connection or disconnect from the session causing the conflict.

### Disconnect
<a name="client-vpn-earlier-disconnect"></a>

To disconnect, choose a connection in the **AWS VPN Client** window, and then choose **Disconnect**. On Windows and macOS, you can also choose the client icon in the system tray (or menu bar on macOS) and choose **Disconnect**. If you have multiple open connections, you must close each connection individually.

### View connection statistics
<a name="client-vpn-earlier-statistics"></a>

To view statistics for a connection, choose **Connection** in the **AWS VPN Client** window, choose **Show Details**, and then choose the connection you want to see details about.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
