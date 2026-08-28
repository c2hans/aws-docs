---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-cre.html
---

# AWS Client VPN Client Route Enforcement
<a name="cvpn-working-cre"></a>

Client Route Enforcement helps enforce administrator-defined routes on devices connected through the VPN. This feature helps improve your security posture by ensuring that network traffic originating from a connected client is not inadvertently sent outside the VPN tunnel.

Client Route Enforcement monitors the main routing table of the connected device and ensures that outbound network traffic goes to a VPN tunnel, according to network routes configured in the client VPN endpoint. This includes modifying routing tables on a device if routes conflicting with VPN tunnel are detected. Client Route Enforcement supports both IPv4 and IPv6 address families.

## Requirements
<a name="requirements-cre"></a>

Client Route Enforcement only works with the following AWS provided Client VPN versions:
+ Windows version 5.2.0 or higher (IPv4 support)
+ macOS version 5.2.0 or higher (IPv4 support)
+ Ubuntu version 5.2.0 or higher (IPv4 support)
+ Windows version 5.3.0 or higher (IPv6 support)
+ macOS version 5.3.0 or higher (IPv6 support)
+ Ubuntu version 5.3.0 or higher (IPv6 support)

For dual-stack endpoints, the Client Route Enforcement setting applies to both IPv4 and IPv6 stacks simultaneously. It is not possible to enable Client Route Enforcement for only one stack.

## Routing conflicts
<a name="route-conflict-cre"></a>

While a client is connected to VPN, a comparison is made between the client's local route table, and the endpoint's network routes. A routing conflict will occur if there is network overlap between two route table entries. An example of overlapping networks is:
+ `172.31.0.0/16`
+ `172.31.1.0/24`

In this example, these CIDR blocks constitute a routing conflict. For example, `172.31.0.0/16` might be the VPN tunnel CIDR. Since `172.31.1.0/24` is more specific because it has a longer prefix, it typically takes precedence and potentially redirects VPN traffic within the `172.31.1.0/24` IP range to another destination. This could lead to unintended routing behavior. However, when Client Route Enforcement is enabled, the latter CIDR would be removed. When using this feature potential routing conflicts should be taken into consideration.

Full tunnel VPN connections direct all network traffic through the VPN connection. As a result, devices connected to the VPN will not be able to access local network (LAN) resources, if Client Route Enforcement feature is enabled. If local LAN access is required, consider using split-tunnel mode instead of full-tunnel mode. For more information about split-tunnel, see [Split-tunnel Client VPN](split-tunnel-vpn.md).

## Considerations
<a name="considerations-cre"></a>

The following information should be taken into consideration before activating Client Route Enforcement.
+ At the time of connection, if a routing conflict is detected, the feature will update the client's route table to direct the traffic into the VPN tunnel. The routes that existed before the connection was established, and were deleted by this feature, will be restored.
+ The feature is enforced only on the main routing table and does not apply to other routing mechanisms. For example, enforcement is not applied to the following:
  + policy-based routing
  + interface-scoped routing
+ Client Route Enforcement protects the VPN tunnel while it's open. There is no protection after the tunnel is disconnected or while the client is reconnecting.

### OpenVPN directives impact on Cloud Route Enforcement
<a name="considerations-openvpn"></a>

Some custom directives in the OpenVPN configuration file have specific interactions with Client Route Enforcement:
+ The `route` directive
  + When adding routes to a VPN gateway. For example, adding the route `192.168.100.0 255.255.255.0` to a VPN gateway.

    Routes added to a VPN gateway are monitored by Client Route Enforcement similarly to any other VPN route. Any conflicting routes within them will be detected and removed.
  + When adding routes to a non-VPN gateway. For example, adding the route `192.168.200.0 255.255.255.0 net_gateway`.

    Routes added to a non-VPN gateway are excluded from Client Route Enforcement as they bypass the VPN tunnel. Conflicting routes are allowed within them. In the example, above the route will be excluded from monitoring by Client Route Enforcement.
  + Similar to IPv4 routes, IPv6 routes added to a VPN gateway are monitored by Client Route Enforcement, while routes added to a non-VPN gateway are excluded from monitoring.

### Ignored routes
<a name="cre-ignored"></a>

Routes to the following IPv4 networks will be ignored by Client Route Enforcement:
+ `127.0.0.0/8` — Reserved for the local host
+ `169.254.0.0/16` — Reserved for link-local addresses
+ `224.0.0.0/4` — Reserved for multicast
+ `255.255.255.255/32` — Reserved for broadcast

Routes to the following IPv6 networks will be ignored by Client Route Enforcement:
+ `::1/128` — Reserved for loopback
+ `fe80::/10` — Reserved for link-local addresses
+ `ff00::/8` — Reserved for multicast

**Topics**
+ [Requirements](#requirements-cre)
+ [Routing conflicts](#route-conflict-cre)
+ [Considerations](#considerations-cre)
+ [Activate Client Route Enforcement](activate-cre.md)
+ [Deactivate Client Route Enforcement](deactivate-cre.md)
+ [Troubleshoot IPv6 Client Route Enforcement](cre-ipv6-troubleshooting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
