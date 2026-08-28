---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_select_network_optimize.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP07 Optimize network configuration based on metrics
<a name="perf_select_network_optimize"></a>

Improper network configuration often affects network performance, efficiency, and cost. In common network environments, in order to quickly complete the deployment in the early stage, the proper network configuration is not fully considered in terms of network performance. To optimize your network configuration, you must first have visibility and data about your network environment.

To understand how your network resources are performing, collect and analyze data to make informed decisions about optimizing your network configuration. Measure the impact of those changes and use the impact measurements to make future decisions.

 **Desired outcome:** Use metrics and network monitoring tools to optimize network configuration as workloads evolve. Cloud-based networks can be optimized quickly, so evolving your network architecture over time is necessary to maintain performance efficiency.

 **Common anti-patterns:**
+  You assume that all performance-related issues are application-related.
+  You only test your network performance from a location close to where you have deployed the workload.
+  You use default configurations for all network services.
+  You overprovision the network resource to provide sufficient capacity.

 **Benefits of establishing this best practice:** Collecting necessary metrics of your AWS network and implementing network monitoring tools allows you to understand network performance and optimize network configurations.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Monitoring traffic to and from VPCs, subnets, or network interfaces is crucial to understanding how to utilize AWS network resources and how you can optimize network configurations. By using the following tools, you can further inspect information about the traffic usage, network access and logs.

 **Implementation steps**

1.  Use [Amazon VPC IP Address Manager](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html). You can use IPAM to plan, track, and monitor IP addresses for your AWS and on-premises workloads. This is the best practice for you for to optimize IP address usage and allocation.

1.  Turn on [VPC Flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html). Use VPC Flow Logs to capture detailed information about traffic to and from network interfaces in your VPCs. With VPC Flow Logs, you can diagnose overly restrictive or permissive security group rules and determine the direction of the traffic to and from the network interfaces. Data ingestion and archival charges for vended logs apply when you publish flow logs.

1.  Turn on [DNS query logging](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html). You can configure Amazon Route 53 to log information about public or private DNS queries Route 53 receives. With DNS logs, you can optimize DNS configurations by understanding the domain or subdomain that was requested or Route 53 EDGE locations that responded to DNS queries.

1.  Use [Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) to analyze and debug network reachability. Reachability Analyzer is a configuration analysis tool that allows you to perform connectivity testing between a source resource and a destination resource in your VPCs. This tool helps you verify that your network configuration matches your intended connectivity.

1.  Use [Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html) to understand network access to your resources. You can use Network Access Analyzer to specify your network access requirements and identify potential network paths that do not meet your specified requirements. By optimizing your corresponding network configuration, you can understand and verify the state of your network and demonstrate if your network on AWS meets your compliance requirements.

1.  Use [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) and turn on the appropriate metrics for network options. Make sure to choose the right network metric for your workload. For example, you can turn on metrics for VPC Network Address Usage, VPC NAT Gateway, AWS Transit Gateway, VPN tunnel, AWS Network Firewall, Elastic Load Balancing, and AWS Direct Connect. Continually monitoring metrics is a good practice to observe and understand your network status and usage, and helps you optimize network configuration based on your observations.

 **Level of effort for the implementation plan:** Medium

## Resources
<a name="resources"></a>

 **Related documents:**
+  [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
+ [ Public DNS query logging ](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html)
+ [ What is IPAM? ](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html)
+  [What is Reachability Analyzer?](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html)
+ [ What is Network Access Analyzer? ](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html)
+ [ CloudWatch metrics for your VPCs ](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cloudwatch.html)
+ [ Optimize performance and reduce costs for network analytics with VPC Flow Logs in Apache Parquet format ](https://aws.amazon.com/blogs/big-data/optimize-performance-and-reduce-costs-for-network-analytics-with-vpc-flow-logs-in-apache-parquet-format/)
+  [Monitoring your global and core networks with Amazon Cloudwatch metrics](https://docs.aws.amazon.com/vpc/latest/tgwnm/monitoring-cloudwatch-metrics.html)
+  [Continuously monitor network traffic and resources](https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/continuously-monitor-network-traffic-and-resources.html)

 **Related videos:**
+ [ Networking best practices and tips with the Well-Architected Framework ](https://www.youtube.com/watch?v=wOMNpG49BeM)
+ [ Monitoring and troubleshooting network traffic ](https://www.youtube.com/watch?v=Ed09ReWRQXc)

 **Related examples:**
+  [AWS Networking Workshops](https://networking.workshop.aws/)
+  [AWS Network Monitoring](https://github.com/aws-samples/monitor-vpc-network-patterns)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
