---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_select_network_understand_impact.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP01 Understand how networking impacts performance
<a name="perf_select_network_understand_impact"></a>

 Analyze and understand how network-related decisions impact workload performance. The network is responsible for the connectivity between application components, cloud services, edge networks and on-premises data and therefor it can highly impact workload performance. In addition to workload performance, user experience is also impacted by network latency, bandwidth, protocols, location, network congestion, jitter, throughput, and routing rules.

 **Desired outcome:** Have a documented list of networking requirements from the workload including latency, packet size, routing rules, protocols, and supporting traffic patterns. Review the available networking solutions and identify which service meets your workload networking characteristics. Cloud-based networks can be quickly rebuilt, so evolving your network architecture over time is necessary to improve performance efficiency.

 **Common anti-patterns:**
+  All traffic flows through your existing data centers.
+  You overbuild Direct Connect sessions without understanding the actual usage requirements.
+  You don’t consider workload characteristics and encryption overhead when defining your networking solutions.
+  You use on-premises concepts and strategies for networking solutions in the cloud.

 **Benefits of establishing this best practice:** Understanding how networking impacts workload performance will help you identify potential bottlenecks, improve user experience, increase reliability, and lower operational maintenance as the workload changes.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Identify important network performance metrics of your workload and capture its networking characteristics. Define and document requirements as part of a data-driven approach, using benchmarking or load testing. Use this data to identify where your network solution is constrained, and examine configuration options that could improve the workload. Understand the cloud-native networking features and options available and how they can impact your workload performance based on the requirements. Each networking feature has advantages and disadvantages and can be configured to meet your workload characteristics and scale based on your needs.

 **Implementation steps:**

1.  Define and document networking performance requirements:

   1.  Include metrics such as network latency, bandwidth, protocols, locations, traffic patterns (spikes and frequency), throughput, encryption, inspection, and routing rules

1.  Capture your foundational networking characteristics:

   1.  [VPC Flow Logs ](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

   1.  [AWS Transit Gateway metrics](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-cloudwatch-metrics.html)

   1.  [AWS PrivateLink metrics](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-cloudwatch-metrics.html)

1.  Capture your application networking characteristics:

   1.  [Elastic Network Adaptor](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-network-performance-ena.html)

   1.  [AWS App Mesh metrics](https://docs.aws.amazon.com/app-mesh/latest/userguide/envoy-metrics.html)

   1.  [Amazon API Gateway metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html)

1.  Capture your edge networking characteristics:

   1.  [Amazon CloudFront metrics](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.html)

   1.  [Amazon Route 53 metrics](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-cloudwatch.html)

   1.  [AWS Global Accelerator metrics](https://docs.aws.amazon.com/global-accelerator/latest/dg/cloudwatch-monitoring.html)

1.  Capture your hybrid networking characteristics:

   1.  [Direct Connect metrics](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-cloudwatch.html)

   1.  [AWS Site-to-Site VPN metrics](https://docs.aws.amazon.com/vpn/latest/s2svpn/monitoring-cloudwatch-vpn.html)

   1.  [AWS Client VPN metrics](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/monitoring-cloudwatch.html)

   1.  [AWS Cloud WAN metrics](https://docs.aws.amazon.com/vpc/latest/cloudwan/cloudwan-cloudwatch-metrics.html)

1.  Capture your security networking characteristics:

   1.  [AWS Shield, WAF, and Network Firewall metrics](https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html)

1.  Capture end-to-end performance metrics with tracing tools:

   1.  [AWS X-Ray](https://aws.amazon.com/xray/)

   1.  [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)

1.  Benchmark and test network performance:

   1.  [Benchmark](https://aws.amazon.com/premiumsupport/knowledge-center/network-throughput-benchmark-linux-ec2/) network throughput: Some factors that can affect EC2 network performance when the instances are in the same VPC. Measure the network bandwidth between EC2 Linux instances in the same VPC.

   1.  Perform [load tests](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) to experiment with networking solutions and options

 **Level of effort for the implementation plan: **There is a *medium* level of effort to document workload networking requirements, options, and available solutions.

## Resources
<a name="resources"></a>

 **Related documents:**
+ [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
+ [EC2 Enhanced Networking on Linux ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)
+ [EC2 Enhanced Networking on Windows ](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/enhanced-networking.html)
+ [EC2 Placement Groups ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
+ [Enabling Enhanced Networking with the Elastic Network Adapter (ENA) on Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html)
+ [Network Load Balancer ](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
+ [Networking Products with AWS](https://aws.amazon.com/products/networking/)
+  [Transit Gateway ](https://docs.aws.amazon.com/vpc/latest/tgw)
+ [Transitioning to latency-based routing in Amazon Route 53 ](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialTransitionToLBR.html)
+ [VPC Endpoints ](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html)
+ [VPC Flow Logs ](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

 **Related videos:**
+ [Connectivity to AWS and hybrid AWS network architectures (NET317-R1) ](https://www.youtube.com/watch?v=eqW6CPb58gs)
+ [Optimizing Network Performance for Amazon EC2 Instances (CMP308-R1) ](https://www.youtube.com/watch?v=DWiwuYtIgu0)
+  [Improve Global Network Performance for Applications](https://youtu.be/vNIALfLTW9M)
+  [EC2 Instances and Performance Optimization Best Practices](https://youtu.be/W0PKclqP3U0)
+  [Optimizing Network Performance for Amazon EC2 Instances](https://youtu.be/DWiwuYtIgu0)
+  [Networking best practices and tips with the Well-Architected Framework](https://youtu.be/wOMNpG49BeM)
+  [AWS networking best practices in large-scale migrations](https://youtu.be/qCQvwLBjcbs)

 **Related examples:**
+  [AWS Transit Gateway and Scalable Security Solutions](https://github.com/aws-samples/aws-transit-gateway-and-scalable-security-solutions)
+  [AWS Networking Workshops](https://networking.workshop.aws/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
