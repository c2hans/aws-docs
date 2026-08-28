---
source_url: https://docs.aws.amazon.com/vpc/latest/userguide/advanced-routing.html
---

# Advanced routing in your VPC
<a name="advanced-routing"></a>

Configure advanced routing scenarios for your VPC. This section covers both static and dynamic routing approaches for managing traffic flow:
+ **Static ingress routing**: Configure static routes to direct inbound internet traffic destined for your BYOIP (Bring Your Own IP) address pools to specific network interfaces within your VPC.
+ **Dynamic routing with VPC Route Server:** Use BGP-based dynamic routing to automatically update VPC and internet gateway route tables, providing fault tolerance and automatic failover for your workloads.

**Topics**
+ [Route internet traffic to a single network interface](igw-ingress-routing.md)
+ [Dynamic routing in your VPC using VPC Route Server](dynamic-routing-route-server.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon VPC. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
