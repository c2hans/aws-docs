---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-routes-create.html
---

# Create an AWS Client VPN endpoint route
<a name="cvpn-working-routes-create"></a>

When you create a Client VPN endpoint route, you specify how traffic for the destination network should be directed.

To allow clients to access the internet, add a destination `0.0.0.0/0` route.

You can add routes to a Client VPN endpoint by using the console and the AWS CLI.

**To create a Client VPN endpoint route (console)**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN Endpoints**.

1. Select the Client VPN endpoint to which to add the route, choose **Route table**, and then choose **Create route**.

1. For **Route destination**, specify the IPv4 CIDR range for the destination network. For example:
   + To add a route for the VPC of the Client VPN endpoint, enter the VPC's IPv4 CIDR range.
   + To add a route for internet access, enter `0.0.0.0/0`.
   + To add a route for a peered VPC, enter the peered VPC's IPv4 CIDR range.
   + To add a route for an on-premises network, enter the AWS Site-to-Site VPN connection's IPv4 CIDR range.

1. For **Subnet ID for target network association**, select the subnet that is associated with the Client VPN endpoint.

   Alternatively, if you're adding a route for the local Client VPN endpoint network, select `local`.

1. (Optional) For **Description**, enter a brief description for the route.

1. Choose **Create route**.

**To create a Client VPN endpoint route (AWS CLI)**
Use the [create-client-vpn-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-client-vpn-route.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
