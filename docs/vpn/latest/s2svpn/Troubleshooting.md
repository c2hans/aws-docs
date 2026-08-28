---
source_url: https://docs.aws.amazon.com/vpn/latest/s2svpn/Troubleshooting.html
---

# Troubleshooting AWS Site-to-Site VPN customer gateway device
<a name="Troubleshooting"></a>

When troubleshooting issues with your customer gateway device, it's important to have a structured approach. The first two topics in this section provide generalized flowcharts for troubleshooting issues when using a device configured for dynamic routing (BGP enabled), and a device configured for static routing (without BGP enabled), respectively. Following those topics are device-specific troubleshooting guides for Cisco, Juniper, and Yamaha customer gateway devices.

In addition to the topics in this section, enabling [AWS Site-to-Site VPN logs](monitoring-logs.md) can be very helpful for troubleshooting and resolving VPN connectivity issues. For general testing instructions, also see [Test an AWS Site-to-Site VPN connection](HowToTestEndToEnd_Linux.md).

**Topics**
+ [Device with BGP](Generic_Troubleshooting.md)
+ [Device without BGP](Generic_Troubleshooting_noBGP.md)
+ [Cisco ASA](Cisco_ASA_Troubleshooting.md)
+ [Cisco IOS](Cisco_Troubleshooting.md)
+ [Cisco IOS without BGP](Cisco_Troubleshooting_NoBGP.md)
+ [Juniper JunOS](Juniper_Troubleshooting.md)
+ [Juniper ScreenOS](Juniper_ScreenOs_Troubleshooting.md)
+ [Yamaha](Yamaha_Troubleshooting.md)

**Additional resources**
+ [Amazon VPC forum](https://repost.aws/tags/TATGuEiYydTVCPMhSnXFN6gA/amazon-vpc)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS VPN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
