---
source_url: https://docs.aws.amazon.com/vpn/latest/s2svpn/site-site-architectures.html
---

# AWS Site-to-Site VPN architectural scenarios
<a name="site-site-architectures"></a>

The following are scenarios in which you might create multiple VPN connections with one or more customer gateway devices.

**Multiple VPN connections using the same customer gateway device**
You can create additional VPN connections from your on-premises location to other VPCs using the same customer gateway device. You can reuse the same customer gateway IP address for each of those VPN connections.

**Multiple customer gateway devices to a single virtual private gateway (Site-to-Site VPN CloudHub)**
You can establish multiple VPN connections to a single virtual private gateway from multiple customer gateway devices. This enables you to have multiple locations connected to the AWS VPN CloudHub. For more information, see [Secure communication between AWS Site-to-Site VPN connections using VPN CloudHub](VPN_CloudHub.md). When you have customer gateway devices at multiple geographic locations, each device should advertise a unique set of IP ranges specific to the location.

**Redundant VPN connection using a second customer gateway device**
To protect against a loss of connectivity if your customer gateway device becomes unavailable, you can set up a second VPN connection using a second customer gateway device. For more information, see [Redundant AWS Site-to-Site VPN connections for failover](vpn-redundant-connection.md). When you establish redundant customer gateway devices at a single location, both devices should advertise the same IP ranges.

The following are common Site-to-Site VPN architectures:
+ [Single and multiple VPN connections](Examples.md)
+ [Redundant AWS Site-to-Site VPN connections for failover](vpn-redundant-connection.md)
+ [Secure communications between VPN connections using VPN CloudHub](VPN_CloudHub.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
