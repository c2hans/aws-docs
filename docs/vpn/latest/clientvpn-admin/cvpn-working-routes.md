---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-routes.html
---

# AWS Client VPN routes
<a name="cvpn-working-routes"></a>

Each AWS Client VPN endpoint has a route table that describes the available destination network routes. Each route in the route table determines where the network traffic is directed. You must configure authorization rules for each Client VPN endpoint route to specify which clients have access to the destination network.

When you associate a subnet from a VPC with a Client VPN endpoint, a route for the VPC is automatically added to the Client VPN endpoint's route table. To enable access for additional networks, such as peered VPCs, on-premises networks, the local network (to enable clients to communicate with each other), or the internet, you must manually add a route to the Client VPN endpoint's route table.

**Note**
If you are associating multiple subnets to the Client VPN endpoint, you should make sure to create a route for each subnet as described here [Troubleshooting AWS Client VPN: Access to a peered VPC, Amazon S3, or the internet is intermittent](intermittent-access.md). Each associated subnet should have an identical set of routes.

## Considerations for using split-tunnel on Client VPN endpoints
<a name="split-tunnel-routes"></a>

When you use split-tunnel on a Client VPN endpoint, all of the routes that are in the Client VPN route tables are added to the client route table when the VPN is established. If you add a route after the VPN is established, you must reset the connection so that the new route is sent to the client.

We recommend that you account for the number of routes that the client device can handle before you modify the Client VPN endpoint route table.

**Topics**
+ [Considerations for using split-tunnel on Client VPN endpoints](#split-tunnel-routes)
+ [Create an endpoint route](cvpn-working-routes-create.md)
+ [View endpoint routes](cvpn-working-routes-view.md)
+ [Delete an endpoint route](cvpn-working-routes-delete.md)
