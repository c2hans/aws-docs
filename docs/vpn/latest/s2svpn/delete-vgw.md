---
source_url: https://docs.aws.amazon.com/vpn/latest/s2svpn/delete-vgw.html
---

# Detach and delete a virtual private gateway in AWS Site-to-Site VPN
<a name="delete-vgw"></a>

If you no longer require a virtual private gateway for your VPC, you can detach it from the VPC.

**To detach a virtual private gateway using the console**

1. In the navigation pane, choose **Virtual private gateways**.

1. Select the virtual private gateway and choose **Actions**, **Detach from VPC**.

1. Choose **Detach virtual private gateway**.

If you no longer require a detached virtual private gateway, you can delete it. You can't delete a virtual private gateway that's still attached to a VPC. After you delete your virtual private gateway, it remains visible for a short while with a state of `deleted`, and then the entry is automatically removed.

**To delete a virtual private gateway using the console**

1. In the navigation pane, choose **Virtual private gateways**.

1. Select the virtual private gateway and choose **Actions**, **Delete virtual private gateway**.

1. When prompted for confirmation, enter **delete** and then choose **Delete**.

**To detach a virtual private gateway using the command line or API**
+ [DetachVpnGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DetachVpnGateway.html) (Amazon EC2 Query API)
+ [detach-vpn-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/detach-vpn-gateway.html) (AWS CLI)
+ [Dismount-EC2VpnGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/Dismount-EC2VpnGateway.html) (AWS Tools for Windows PowerShell)

**To delete a virtual private gateway using the command line or API**
+ [DeleteVpnGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteVpnGateway.html) (Amazon EC2 Query API)
+ [delete-vpn-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpn-gateway.html) (AWS CLI)
+ [Remove-EC2VpnGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2VpnGateway.html) (AWS Tools for Windows PowerShell)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
