---
source_url: https://docs.aws.amazon.com/networkmonitor/latest/APIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

Network Synthetic Monitor is feature of Network Monitoring in Amazon CloudWatch that provides visibility into the performance of network flows for your workloads, between instances in VPC subnets, as well as to and from AWS. Network Synthetic Monitor can also identify if a network issue for your workload is caused by the AWS network or is within your own company network. To configure Network Synthetic Monitor, you choose source VPCs and subnets from the AWS network that you operate within, and then, destination IP addresses from your on-premises network. Using these sources and destinations, Network Synthetic Monitor creates a monitor with all the source and destination combinations, each of which is called a probe. These probes monitor your network traffic, to help you identify where network issues might be affecting your traffic, and if the cause is an AWS network impairment.

You can create a monitor in any subnet that belongs to a VPC owned by your account. Network Synthetic Monitor doesn’t support creating resources across accounts.

For more information, see [ Using Network Synthetic Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/what-is-network-monitor.html) in the *Amazon CloudWatch User Guide*.

This document was last published on September 1, 2026.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Network Synthetic Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmonitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
