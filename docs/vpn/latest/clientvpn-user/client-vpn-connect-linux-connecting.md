---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-connect-linux-connecting.html
---

# Connect to the provided AWS Client VPN for Linux
<a name="client-vpn-connect-linux-connecting"></a>

The AWS provided client is also referred to as the *AWS VPN Client* in the following steps.

**To connect using the AWS provided client for Linux**

1. Open the **AWS VPN Client** app.

1. Choose **File**, **Manage Profiles**.

1. Choose **Add Profile**.

1. For **Display Name**, enter a name for the profile.

1. For **VPN Configuration File**, browse to the configuration file that you received from your Client VPN administrator. Choose **Open**.

1. Choose **Add Profile**.

1. If you want to create multiple connections, repeat the **Add Profile** steps for each configuration file you want to add. You can add as many profiles as you like, but you can only have up to five open connections.

1. In the **AWS VPN Client** window, choose the profile that you want to connect to, and then choose **Connect**. If the Client VPN endpoint has been configured to use credential-based authentication, you'll be prompted to enter a user name and password. Repeat this step for each profile connection you want to initiate, connecting up to five concurrent endpoints.
**Note**
If any profile you connect to conflicts with a currently open session, you won't be able to make the connection. Either choose a new connection or disconnect from the session causing the conflict.

1. To view statistics for a connection, choose **Connection** in the **AWS VPN client** window, choose **Show Details**, and then choose the connection you want to see details about.

1. To disconnect a connection, choose a connection in the **AWS VPN client** window, and then choose **Disconnect**. If you have multiple open connections, you must close each connection individually.
