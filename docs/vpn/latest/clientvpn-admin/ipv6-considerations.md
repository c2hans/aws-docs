---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/ipv6-considerations.html
---

# IPv6 considerations for AWS Client VPN
<a name="ipv6-considerations"></a>

Client VPN now supports native IPv6 connectivity alongside existing IPv4 capabilities. You can create IPv6-only, IPv4-only, or dual-stack (both IPv4 and IPv6) endpoints to meet your networking requirements.

## Key components of IPv6 support
<a name="ipv6-key-components"></a>

When working with IPv6 in Client VPN, there are two key configuration parameters:

Endpoint IP address type
This parameter defines the endpoint management IP type, which determines the type of EC2 instance provisioned for the endpoint. This IP type is used for managing outer VPN tunnel traffic (the encrypted traffic that flows between the OpenVPN client and server over the public internet).

Traffic IP address type
This parameter defines the type of traffic that flows through the VPN tunnel. This IP type is used for managing inner encrypted traffic (the actual payload), client CIDR ranges, subnet association, routes, and rules per endpoint.

## IPv6 client CIDR assignment
<a name="ipv6-client-cidr"></a>

For IPv6 client CIDR, you do not need to specify a CIDR block. Amazon automatically assigns CIDR ranges for IPv6 clients. This auto-assignment enables no-SNATing for IPv6 tunnel traffic, providing enhanced visibility into the connected user's IPv6 address.

## Compatibility requirements
<a name="ipv6-compatibility"></a>

IPv6 and dual-stack endpoints have dependencies on user devices and internet service providers (ISPs):
+ User devices running the CVPN client must support the required IP configuration as shown in the compatibility table below.
+ ISPs must support the required IP configuration for the connection to work properly.
+ For IPv6 or dual-stack traffic, the associated VPC subnets must have IPv6 or dual-stack CIDR ranges.

## DNS support
<a name="ipv6-dns"></a>

DNS is supported in all types of endpoints - IPv4, IPv6, and dual-stack. For IPv6 endpoints, you can configure IPv6 DNS servers using the `--dns-server-ipv6` parameter. AAAA DNS records are supported on both the service and client end.

## Limitations
<a name="ipv6-feature-limitations"></a>

The following are the limitations with IPv6:
+ Client-to-client (C2C) communication is not supported for IPv6 clients. If an IPv6 client tries to communicate with another IPv6 client, the traffic will be dropped.

## Client Routes Enforcement for IPv6
<a name="ipv6-cre"></a>

Client VPN now supports Client Routes Enforcement for IPv6 traffic. This feature helps ensure that IPv6 network traffic from connected clients follows the routes defined by the administrator and is not inadvertently sent outside the VPN tunnel.

Key aspects of IPv6 Client Route Enforcement support:
+ The existing `ClientRouteEnforcementOptions.enforced` flag enables CRE for both IPv4 and IPv6 stacks.
+ IPv6 Client Route Enforcement excludes certain IPv6 ranges to maintain critical IPv6 functionalities:
  + `::1/128` — Reserved for loopback
  + `fe80::/10` — Reserved for link-local addresses
  + `ff00::/8` — Reserved for multicast
+ IPv6 Client Route Enforcement is available in AWS VPN Client version 5.3.0 and higher on Windows, macOS, and Ubuntu.

For more detailed information about CRE, including how to enable and configure it, see [AWS Client VPN Client Route Enforcement](cvpn-working-cre.md).

## IPv6 leak prevention (legacy information)
<a name="ipv6-leak-prevention"></a>

For older configurations that don't use the native IPv6 support, you may still need to prevent IPv6 leak. IPv6 leak can happen when both IPv4 and IPv6 are enabled and connected to the VPN, but the VPN doesn't route IPv6 traffic into its tunnel. In this case, when connecting to an IPv6 enabled destination, you are actually still connecting with your IPv6 address provided by your ISP. This will leak your real IPv6 address. The instructions below explain how to route IPv6 traffic into the VPN tunnel.

The following IPv6-related directives should be added to your Client VPN configuration file to prevent IPv6 leak:

```
ifconfig-ipv6 arg0 arg1
route-ipv6 arg0
```

An example might be:

```
ifconfig-ipv6 fd15:53b6:dead::2 fd15:53b6:dead::1
route-ipv6 2000::/4
```

In this example, `ifconfig-ipv6 fd15:53b6:dead::2 fd15:53b6:dead::1` will set the local tunnel device IPv6 address to be `fd15:53b6:dead::2` and the remote VPN endpoint IPv6 address to be `fd15:53b6:dead::1`.

The next command, `route-ipv6 2000::/4` will route IPv6 addresses from `2000:0000:0000:0000:0000:0000:0000:0000` to `2fff:ffff:ffff:ffff:ffff:ffff:ffff:ffff` into the VPN connection.

**Note**
For "TAP" device routing in Windows for example, the second parameter of `ifconfig-ipv6` will be used as route target for `--route-ipv6`.

Organizations should configure the two parameters of `ifconfig-ipv6` themselves, and can use addresses in `100::/64` (from `0100:0000:0000:0000:0000:0000:0000:0000` to `0100:0000:0000:0000:ffff:ffff:ffff:ffff`) or `fc00::/7` (from `fc00:0000:0000:0000:0000:0000:0000:0000` to `fdff:ffff:ffff:ffff:ffff:ffff:ffff:ffff`). `100::/64` is Discard-Only Address Block, and `fc00::/7` is Unique-Local.

Another example:

```
ifconfig-ipv6 fd15:53b6:dead::2 fd15:53b6:dead::1
route-ipv6 2000::/3
route-ipv6 fc00::/7
```

In this example, the configuration will route all currently allocated IPv6 traffic into the VPN connection.

**Verification**
Your organization will likely have its own tests. A basic verification is to set up a full tunnel VPN connection, then run ping6 to an IPv6 server using the IPv6 address. The IPv6 address of the server should be in the range specified by the `route-ipv6` command. This ping test should fail. However, this may change if IPv6 support is added to the Client VPN service in the future. If the ping is successful and you are able to access public sites when connected in full tunnel mode, you may need to do further troubleshooting. There are also some publicly available tools.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
