---
source_url: https://docs.aws.amazon.com/vpn/latest/s2svpn/FirewallRules.html
---

# Firewall rules for an AWS Site-to-Site VPN customer gateway device
<a name="FirewallRules"></a>

You must have a static IP address to use as the endpoint for the IPsec tunnels that connect your customer gateway device to AWS Site-to-Site VPN endpoints. If a firewall is in place between AWS and your customer gateway device, the rules in the following tables must be in place to establish the IPsec tunnels. The IP addresses for the AWS-side will be in the configuration file.

**Inbound (from the internet)**

|
|
|  Input rule I1  |
| --- |
| Source IP | Tunnel1 Outside IP |
| Dest IP | Customer Gateway |
| Protocol | UDP |
| Source port | 500 |
| Destination | 500 |
|  Input rule I2  |
| --- |
| Source IP | Tunnel2 Outside IP |
| Dest IP | Customer Gateway |
| Protocol | UDP |
| Source port | 500 |
| Destination port | 500 |
|  Input rule I3  |
| --- |
| Source IP | Tunnel1 Outside IP |
| Dest IP | Customer Gateway |
| Protocol | IP 50 (ESP) |
|  Input rule I4  |
| --- |
| Source IP | Tunnel2 Outside IP |
| Dest IP | Customer Gateway |
| Protocol | IP 50 (ESP) |

**Outbound (to the internet)**

|
|
|  Output rule O1  |
| --- |
| Source IP | Customer Gateway |
| Dest IP | Tunnel1 Outside IP |
| Protocol | UDP |
| Source port | 500 |
| Destination port | 500 |
|  Output rule O2  |
| --- |
| Source IP | Customer Gateway |
| Dest IP | Tunnel2 Outside IP |
| Protocol | UDP |
| Source port | 500 |
| Destination port | 500 |
|  Output rule O3  |
| --- |
| Source IP | Customer Gateway |
| Dest IP | Tunnel1 Outside IP |
| Protocol | IP 50 (ESP)  |
|  Output rule O4  |
| --- |
| Source IP | Customer Gateway |
| Dest IP | Tunnel2 Outside IP |
| Protocol | IP 50 (ESP) |

Rules I1, I2, O1, and O2 enable the transmission of IKE packets. Rules I3, I4, O3, and O4 enable the transmission of IPsec packets that contain the encrypted network traffic.

**Note**
If you are using NAT traversal (NAT-T) on your device, ensure that UDP traffic on port 4500 is also allowed to pass between your network and the AWS Site-to-Site VPN endpoints. Check if your device is advertising NAT-T.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
