---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/delete-direct-connect-gateway.html
---

# Delete a Direct Connect gateway
<a name="delete-direct-connect-gateway"></a>

If you no longer require a Direct Connect gateway, you can delete it. You must first disassociate all associated virtual private gateways and delete the attached private virtual interface. Once you've disassociated any associated virtual private gateways and deleted any attached private virtual interfaces, you can delete the Direct Connect gateway using either the Direct Connect console or using the command line or API.
+ For the steps to disassociate a virutal private gateway, see [Associate or disassociate virtual private gateways](associate-vgw-with-direct-connect-gateway.md).
+ For the steps to delete a virtual interface, see [Delete a virtual interface](deletevif.md).

**To delete a Direct Connect gateway**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Direct Connect Gateways**.

1. Select the gateways and choose **Delete**.

**To delete a Direct Connect gateway using the command line or API**
+ [delete-direct-connect-gateway](https://docs.aws.amazon.com/cli/latest/reference/directconnect/delete-direct-connect-gateway.html) (AWS CLI)
+ [DeleteDirectConnectGateway](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DeleteDirectConnectGateway.html) (Direct Connect API)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
