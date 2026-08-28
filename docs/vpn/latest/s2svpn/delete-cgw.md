---
source_url: https://docs.aws.amazon.com/vpn/latest/s2svpn/delete-cgw.html
---

# Delete an AWS Site-to-Site VPN customer gateway
<a name="delete-cgw"></a>

If you no longer need a customer gateway, you can delete it. You can't delete a customer gateway that's being used in a Site-to-Site VPN connection.

**To delete a customer gateway using the console**

1. In the navigation pane, choose **Customer gateways**.

1. Select the customer gateway and choose **Actions**, **Delete customer gateway**.

1. When prompted for confirmation, enter **delete** and then choose **Delete**.

**To delete a customer gateway using the command line or API**
+ [DeleteCustomerGateway](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteCustomerGateway.html) (Amazon EC2 Query API)
+ [delete-customer-gateway](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-customer-gateway.html) (AWS CLI)
+ [Remove-EC2CustomerGateway](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2CustomerGateway.html) (AWS Tools for Windows PowerShell)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
