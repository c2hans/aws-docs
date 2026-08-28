---
source_url: https://docs.aws.amazon.com/vpn/latest/s2svpn/modify-vpn-tunnel-options.html
---

# Modify AWS Site-to-Site VPN tunnel options
<a name="modify-vpn-tunnel-options"></a>

You can modify the tunnel options for the VPN tunnels in your Site-to-Site VPN connection. You can modify one VPN tunnel at a time.

**Important**
When you modify a VPN tunnel, connectivity over the tunnel is interrupted for up to several minutes. Ensure that you plan for the expected downtime.

**To modify the VPN tunnel options using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Site-to-Site VPN connections**.

1. Select the Site-to-Site VPN connection, and choose **Actions**, **Modify VPN tunnel options**.

1. For **VPN tunnel outside IP address**, choose the tunnel endpoint IP of the VPN tunnel.

1. Choose or enter new values for the tunnel options as needed. For more information about the tunnel options, see [VPN tunnel options](VPNTunnels.md).
**Note**
Some tunnel options have multiple default values. Click to remove any default value. That default value is then removed from the tunnel option.

1. Choose **Save changes**.

**To modify the VPN tunnel options using the command line or API**
+  (AWS CLI) Use [describe-vpn-connections](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpn-connections.html) to view the current tunnel options, and [modify-vpn-tunnel-options](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpn-tunnel-options.html) to modify the tunnel options.
+ (Amazon EC2 Query API) Use [DescribeVpnConnections](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpnConnections.html) to view the current tunnel options, and [ModifyVpnTunnelOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpnTunnelOptions.html) to modify the tunnel options.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
