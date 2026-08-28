---
source_url: https://docs.aws.amazon.com/reference-architecture-diagrams/latest/govcloud-hybrid-connectivity/govcloud-public-ip.html
---

# Using Public IP Addressing
<a name="govcloud-public-ip"></a>

Publication date: **November 22, 2024 ([Diagram history](#gpub-diagram-history))**

This architecture connects AWS GovCloud (US) and commercial Regions using public IP addresses on both sides. Although the traffic uses public addresses, it does not leave the AWS network. Packets that originate from and are destined for the AWS network stay on the AWS global network.

## GovCloud hybrid connectivity with public IP addressing architecture
<a name="gpub-diagram1"></a>

![Architecture diagram showing hybrid connectivity between AWS GovCloud and commercial Regions using public IP addresses with traffic staying on the AWS global network.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/govcloud-hybrid-connectivity/images/govcloud-hybrid-connectivity-1.png)

The following steps describe the data flow in this architecture:

1. Traffic from an Amazon EC2 instance in **VPC A** in the commercial Region follows the route table through NAT Gateway.

1. Traffic flows from NAT Gateway to the internet gateway of **VPC A** and into the Application Load Balancer of **VPC B** in the GovCloud Region. This traffic does not leave the AWS global network.

1. Traffic flows from the **VPC B** Application Load Balancer to the target Amazon EC2 instance. Return traffic traverses the same path.

For more information about VPC network behavior, see [Amazon VPC FAQs](https://aws.amazon.com/vpc/faqs/).

## Further reading
<a name="gpub-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="gpub-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date |
| --- |--- |--- |
| [Initial publication](#gpub-diagram-history) | Reference architecture diagram first published. | November 22, 2024 |
| [Initial publication](govcloud-site-to-site-vpn.md#gvpn-diagram-history) | Reference architecture diagram first published. | November 22, 2024 |
| [Initial publication](govcloud-direct-connect.md#gdx-diagram-history) | Reference architecture diagram first published. | November 22, 2024 |
| [Initial publication](govcloud-tgw-connect.md#gtgw-diagram-history) | Reference architecture diagram first published. | November 22, 2024 |

**Note**
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Reference Architecture Diagrams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query reference-architecture-diagrams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
