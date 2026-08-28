---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-connect-windows-connecting-how.html
---

# Connect to AWS Client VPN with an AWS provided client for Windows
<a name="client-vpn-connect-windows-connecting-how"></a>

Before you begin, ensure that you've read the [requirements](client-vpn-connect-windows.md#client-vpn-connect-windows-req). The AWS provided client is also referred to as *AWS VPN Client* in the following steps.

**To connect using the AWS provided client for Windows x64-based or Windows Arm64-based systems:**

1. Open the **AWS VPN Client** app.

1. Choose **File**, **Manage Profiles**.

1. Choose **Add Profile**.

1. For **Display Name**, enter a name for the profile.

1. For **VPN Configuration File**, browse to and then select the configuration file that you received from your Client VPN administrator, and choose **Add Profile**.

1. If you want to create multiple connections, repeat the **Add Profile** steps for each configuration file you want to add. You can add as many profiles as you like, but you can only have up to five open connections.

1. In the **AWS VPN Client** window, choose the profile that you want to connect to, and then choose **Connect**. If the Client VPN endpoint has been configured to use credential-based authentication, you'll be prompted to enter a user name and password. Repeat this step for each profile connection you want to initiate, connecting up to five concurrent endpoints.
**Note**
If any profile you connect to conflicts with a currently open session, you won't be able to make the connection. Either choose a new connection or disconnect from the session causing the conflict.

1. To view statistics for a connection, choose **Connection** in the **AWS VPN client** window, choose **Show Details**, and then choose the connection you want to see details about.

1. To disconnect a connection, choose a connection in the **AWS VPN client** window, and then choose **Disconnect**. If you have multiple open connections, you must close each connection individually. Alternatively, choose the client icon on the Windows taskbar, and then choose **Disconnect**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
