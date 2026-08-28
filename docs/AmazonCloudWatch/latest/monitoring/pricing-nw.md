---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/pricing-nw.html
---

# Pricing for Network Synthetic Monitor
<a name="pricing-nw"></a>

With Network Synthetic Monitor, there are no upfront costs or long-term commitments. Pricing for Network Synthetic Monitor has the following two components:
+ An hourly fee per monitored AWS resource
+ CloudWatch metrics fees

When you create a monitor in Network Synthetic Monitor, you associate AWS resources (sources) with it to be monitored. For Network Synthetic Monitor, these resources are subnets in Amazon Virtual Private Cloud (VPC). For each resource, you can create up to four probes, each of which is for traffic from a subnet in the VPC to four of your destination IP addresses. To help control your bill, you can adjust your subnet coverage and on-premises IP address destination coverage by reducing the number of resources that you monitor.

For more information about pricing, see the [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/) page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
