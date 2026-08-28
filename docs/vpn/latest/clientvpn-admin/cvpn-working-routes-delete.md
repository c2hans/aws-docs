---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-routes-delete.html
---

# Delete an AWS Client VPN endpoint route
<a name="cvpn-working-routes-delete"></a>

You can only delete Client VPN routes that you added manually. You can't delete routes that were automatically added when you associated a subnet with the Client VPN endpoint. To delete routes that were automatically added, you must disassociate the subnet that initiated its creation from the Client VPN endpoint.

You can delete a route from a Client VPN endpoint by using the console or the AWS CLI.

**To delete a Client VPN endpoint route (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint from which to delete the route and choose **Route table**.

1. Select the route to delete, choose **Delete route**, and choose **Delete route**.

**To delete a Client VPN endpoint route (AWS CLI)**
Use the [delete-client-vpn-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-client-vpn-route.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
