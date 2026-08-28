---
source_url: https://docs.aws.amazon.com/vpn/latest/s2svpn/change-vpn-cgw.html
---

# Change the customer gateway for an AWS Site-to-Site VPN connection
<a name="change-vpn-cgw"></a>

You can change the customer gateway of your Site-to-Site VPN connection by using the Amazon VPC console or a command line tool.

After you change the customer gateway, your VPN connection will be temporarily unavailable for a brief period while we provision the new endpoints.

**To change the customer gateway using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Site-to-Site VPN connections**.

1. Select the VPN connection.

1. Choose **Actions**, **Modify VPN connection**.

1. For **Target type**, choose **Customer gateway**.

1. For **Target customer gateway**, choose the new customer gateway.

1. Choose **Save changes**.

**To change the customer gateway using the command line or API**
+ [ModifyVpnConnection](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpnConnection.html) (Amazon EC2 Query API)
+ [modify-vpn-connection](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-vpn-connection.html) (AWS CLI)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
