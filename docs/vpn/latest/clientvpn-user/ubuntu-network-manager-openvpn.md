---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-user/ubuntu-network-manager-openvpn.html
---

# Establish an AWS Client VPN connection on Linux
<a name="ubuntu-network-manager-openvpn"></a>

Establish a VPN connection using the using either the Network Manager GUI on an Ubuntu computer or the OpenVPN application.

**To establish a VPN connection using OpenVPN - Network Manager**

1. Install the network manager module using the following command.

   ```
   sudo apt-get install --reinstall network-manager network-manager-gnome network-manager-openvpn network-manager-openvpn-gnome
   ```

1. Go to **Settings**, **Network**.

1. Choose the plus symbol (**\+**) next to **VPN**, and then choose **Import from file...**.

1. Navigate to the configuration file that you received from your VPN administrator and choose **Open**.

1. In the **Add VPN** window, choose **Add**.

1. Start the connection by enabling the toggle next to the VPN profile that you added.

**To establish a VPN connection using OpenVPN**

1. Install OpenVPN using the following command.

   ```
   sudo apt-get install openvpn
   ```

1. Start the connection by loading the configuration file that you received from your VPN administrator.

   ```
   sudo openvpn --config {{/path/to/config/file}}
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
