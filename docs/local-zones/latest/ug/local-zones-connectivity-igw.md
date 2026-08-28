---
source_url: https://docs.aws.amazon.com/local-zones/latest/ug/local-zones-connectivity-igw.html
---

# Internet gateway connection in Local Zones
<a name="local-zones-connectivity-igw"></a>

Internet gateways provide two-way public connectivity to applications running in AWS Regions and/or in Local Zones. For more information, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) in the *Amazon VPC User Guide*.

In the following diagram, end users access a public-facing application in Local Zone 1. Traffic goes directly to the internet gateway in Local Zone 1 without going through the parent AWS Region. Use this type of connectivity for low-latency use-cases where you want your public-facing applications to be closer to end users than an AWS Region can provide.

![An AWS Region with a VPC. The VPC contains two Availability Zones and a Local Zone. Each zone has a public subnet and a private subnet. The VPC also has an internet gateway through which traffic passes between an application in the public subnet of the Local Zone and the end user.](http://docs.aws.amazon.com/local-zones/latest/ug/images/local-zones-internet-gateway.png)

For your private applications that require outbound-only connectivity to the internet, use a NAT gateway.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Local Zones. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query local-zones` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
