---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_select_network_optimize.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP07 Optimize network configuration based on metrics
<a name="perf_select_network_optimize"></a>

 Use collected and analyzed data to make informed decisions about optimizing your network configuration. Measure the impact of those changes and use the impact measurements to make future decisions.

 Enable VPC Flow Logs for all VPC networks that are used by your workload. VPC Flow Logs are a feature that allows you to capture information about the IP traffic going to and from network interfaces in your VPC. VPC Flow Logs help you with a number of tasks, such as troubleshooting why specific traffic is not reaching an instance, which in turn helps you diagnose overly restrictive security group rules. You can use flow logs as a security tool to monitor the traffic that is reaching your instance, to profile your network traffic, and to look for abnormal traffic behaviors.

 Use networking metrics to make changes to networking configuration as the workload evolves. Cloud based networks can be quickly rebuilt, so evolving your network architecture over time is necessary to maintain performance efficiency.

 **Common anti-patterns:**
+  You assume that all performance-related issues are application-related.
+  You only test your network performance from a location close to where you have deployed the workload.

 **Benefits of establishing this best practice: T**o ensure that you are meeting the metrics required for the workload, you must monitor network performance metrics. You can capture information about the IP traffic going to and from network interfaces in your VPC and use this data to add new optimizations or deploy your workload to new geographic Regions.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

 Enable VPC Flow Logs: VPC Flow Logs enable you to capture information about the IP traffic going to and from network interfaces in your VPC. VPC Flow Logs help you with a number of tasks, such as troubleshooting why specific traffic is not reaching an instance, which can help you diagnose overly restrictive security group rules. You can use flow logs as a security tool to monitor the traffic that is reaching your instance, to profile your network traffic, and to look for abnormal traffic behaviors.

 Enable appropriate metrics for network options: Ensure that you select the appropriate network metrics for your workload. You can enable metrics for VPC NAT gateway, transit gateways, and VPN tunnels.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon EBS - Optimized Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html)
+  [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
+  [EC2 Enhanced Networking on Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)
+  [EC2 Enhanced Networking on Windows](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/enhanced-networking.html)
+  [EC2 Placement Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
+  [Enabling Enhanced Networking with the Elastic Network Adapter (ENA) on Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html)
+  [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
+  [Networking Products with AWS](https://aws.amazon.com/products/networking/)
+  [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw)
+  [Transitioning to Latency-Based Routing in Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialTransitionToLBR.html)
+  [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html)
+  [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
+  [Monitoring your global and core networks with Amazon Cloudwatch metrics](https://docs.aws.amazon.com/vpc/latest/tgwnm/monitoring-cloudwatch-metrics.html)
+  [Continuously monitor network traffic and resources](https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/continuously-monitor-network-traffic-and-resources.html)

 **Related videos:**
+  [Connectivity to AWS and hybrid AWS network architectures (NET317-R1)](https://www.youtube.com/watch?v=eqW6CPb58gs)
+  [Optimizing Network Performance for Amazon EC2 Instances (CMP308-R1)](https://www.youtube.com/watch?v=DWiwuYtIgu0)
+  [Monitoring and troubleshooting network traffic](https://www.youtube.com/watch?v=Ed09ReWRQXc)
+  [Simplify Traffic Monitoring and Visibility with Amazon VPC Traffic Mirroring](https://www.youtube.com/watch?v=zPovlZxuZ-c)

 **Related examples:**
+  [AWS Transit Gateway and Scalable Security Solutions](https://github.com/aws-samples/aws-transit-gateway-and-scalable-security-solutions)
+  [AWS Networking Workshops](https://networking.workshop.aws/)
+  [AWS Network Monitoring](https://github.com/aws-samples/monitor-vpc-network-patterns)
