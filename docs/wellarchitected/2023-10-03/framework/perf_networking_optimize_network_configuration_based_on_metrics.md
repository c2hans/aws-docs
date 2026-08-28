---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_networking_optimize_network_configuration_based_on_metrics.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF04-BP07 Optimize network configuration based on metrics
<a name="perf_networking_optimize_network_configuration_based_on_metrics"></a>

 Use collected and analyzed data to make informed decisions about optimizing your network configuration.

 **Common anti-patterns:**
+  You assume that all performance-related issues are application-related.
+  You only test your network performance from a location close to where you have deployed the workload.
+  You use default configurations for all network services.
+  You overprovision the network resource to provide sufficient capacity.

 **Benefits of establishing this best practice:** Collecting necessary metrics of your AWS network and implementing network monitoring tools allows you to understand network performance and optimize network configurations.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

 Monitoring traffic to and from VPCs, subnets, or network interfaces is crucial to understand how to utilize AWS network resources and optimize network configurations. By using the following AWS networking tools, you can further inspect information about the traffic usage, network access and logs.

### Implementation steps
<a name="implementation-steps"></a>
+  Identify the key performance metrics such as latency or packet loss to collect. AWS provides several tools that can help you to collect these metrics. By using the following tools, you can further inspect information about the traffic usage, network access, and logs:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/perf_networking_optimize_network_configuration_based_on_metrics.html)
+  Identify top talkers and application traffic patterns using VPC and AWS Transit Gateway Flow Logs.
+  Assess and optimize your current network architecture including VPCs, subnets, and routing. As an example, you can evaluate how different VPC peering or AWS Transit Gateway can help you improve the networking in your architecture.
+  Assess the routing paths in your network to verify that the shortest path between destinations is always used. Network Access Analyzer can help you do this.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
+  [Public DNS query logging](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html)
+  [What is IPAM?](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html)
+  [What is Reachability Analyzer?](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html)
+  [What is Network Access Analyzer?](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html)
+  [CloudWatch metrics for your VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cloudwatch.html)
+  [Optimize performance and reduce costs for network analytics with VPC Flow Logs in Apache Parquet format ](https://aws.amazon.com/blogs/big-data/optimize-performance-and-reduce-costs-for-network-analytics-with-vpc-flow-logs-in-apache-parquet-format/)
+  [Monitoring your global and core networks with Amazon CloudWatch metrics](https://docs.aws.amazon.com/vpc/latest/tgwnm/monitoring-cloudwatch-metrics.html)
+  [Continuously monitor network traffic and resources](https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/continuously-monitor-network-traffic-and-resources.html)

 **Related videos:**
+  [Networking best practices and tips with the AWS Well-Architected Framework ](https://www.youtube.com/watch?v=wOMNpG49BeM)
+  [Monitoring and troubleshooting network traffic ](https://www.youtube.com/watch?v=Ed09ReWRQXc)

 **Related examples:**
+  [AWS Networking Workshops](https://networking.workshop.aws/)
+  [AWS Network Monitoring](https://github.com/aws-samples/monitor-vpc-network-patterns)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
