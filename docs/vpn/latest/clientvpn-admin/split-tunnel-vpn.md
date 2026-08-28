---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/split-tunnel-vpn.html
---

# Split-tunnel on AWS Client VPN endpoints
<a name="split-tunnel-vpn"></a>

By default, when you have a Client VPN endpoint, all traffic from clients is routed over the Client VPN tunnel. When you enable split-tunnel on the Client VPN endpoint, we push the routes on the [Client VPN endpoint route table](cvpn-working-routes.md) to the device that is connected to the Client VPN endpoint. This ensures that only traffic with a destination to the network matching a route from the Client VPN endpoint route table is routed over the Client VPN tunnel.

You can use a split-tunnel Client VPN endpoint when you do not want all user traffic to route through the Client VPN endpoint.

In the following example, split-tunnel is enabled on the Client VPN endpoint. Only traffic that's destined for the VPC (`172.31.0.0/16`) is routed over the Client VPN tunnel. Traffic that's destined for on-premises resources is not routed over the Client VPN tunnel.

![Split-tunnel Client VPN endpoint](http://docs.aws.amazon.com/vpn/latest/clientvpn-admin/images/client-vpn-split-tunnel.png)

## Split-tunnel benefits
<a name="split-tunnel-benefits"></a>

Split-tunnel on Client VPN endpoints offers the following benefits:
+ You can optimize the routing of traffic from clients by having only the AWS destined traffic traverse the VPN tunnel.
+ You can reduce the volume of outgoing traffic from AWS, therefore reducing the data transfer cost.

## Routing considerations
<a name="split-tunnel-routing"></a>
+ When you enable split-tunnel mode, all of the routes in the Client VPN endpoint's route table are added to the client's route table when the VPN connection is established. This operation is different from the default behavior, which overwrites the client's route table with the entry `0.0.0.0/0` to route all traffic over the VPN.
**Note**
Adding a 0.0.0.0/0 route to the Client VPN endpoint's route table when using split-tunnel mode may cause connectivity disruption and is not recommended
+ When split-tunnel mode is enabled, any modification to the Client VPN endpoint route table will result in all client connections being reset.

## Enabling split-tunnel
<a name="split-tunnel-enable"></a>

You can enable split-tunnel on a new or existing Client VPN endpoint. For more information, see the following topics:
+ [Create an AWS Client VPN endpoint](cvpn-working-endpoint-create.md)
+ [Modify an AWS Client VPN endpoint](cvpn-working-endpoint-modify.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
