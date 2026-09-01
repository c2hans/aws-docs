---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

Network Flow Monitor is a feature of Amazon CloudWatch Network Monitoring that provides visibility into the performance of network flows for your AWS workloads, between instances in subnets, as well as to and from AWS. Lightweight agents that you install on the instances capture performance metrics for your network flows, such as packet loss and latency, and send them to the Network Flow Monitor backend. Then, you can view and analyze metrics from the top contributors for each metric type, to help troubleshoot issues.

In addition, when you create a monitor, Network Flow Monitor provides a network health indicator (NHI) that informs you whether there were AWS network issues for one or more of the network flows tracked by a monitor, during a time period that you choose. By using this value, you can independently determine if the AWS network is impacting your workload during a specific time frame, to help you focus troubleshooting efforts.

To learn more about Network Flow Monitor, see the [Network Flow Monitor User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor.html) in the Amazon CloudWatch User Guide.

This document was last published on September 1, 2026.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Network Flow Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkflowmonitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
