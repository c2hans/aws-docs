---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_select_network_evaluate_features.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP02 Evaluate available networking features
<a name="perf_select_network_evaluate_features"></a>

Evaluate networking features in the cloud that may increase performance. Measure the impact of these features through testing, metrics, and analysis. For example, take advantage of network-level features that are available to reduce latency, packet loss, or jitter.

Many services are created to improve performance and others commonly offer features to optimize network performance. Services such as AWS Global Accelerator and Amazon CloudFront exist to improve performance while most other services have product features to optimize network traffic. Review service features, such as EC2 instance network capability, enhanced networking instance types, Amazon EBS-optimized instances, Amazon S3 transfer acceleration, and CloudFront, to improve your workload performance.

**Desired outcome:** You have documented the inventory of components within your workload and have identified which networking configurations per component will help you meet your performance requirements. After evaluating the networking features, you have experimented and measured the performance metrics to identify how to use the features available to you.

**Common anti-patterns:**
+ You put all your workloads into an AWS Region closest to your headquarters instead of an AWS Region close to your end users.
+ Failing to benchmark your workload performance and continually evaluating your workload performance against that benchmark.
+ You do not review service configurations for performance improving options.

**Benefits of establishing this best practice:** Evaluating all service features and options can increase your workload performance, reduce the cost of infrastructure, decrease the effort required to maintain your workload, and increase your overall security posture. You can use the global AWS backbone to ensure that you provide the optimal networking experience for your customers.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Review which network-related configuration options are available to you, and how they could impact your workload. Understanding how these options interact with your architecture and the impact that they will have on both measured performance and the performance perceived by users is critical for performance optimization.

**Implementation steps:**

1. Create a list of workload components.

   1. Build, manage and monitor your organizations network using [AWS Cloud WAN](https://aws.amazon.com/cloud-wan/).

   1. Get visibility into your network using [Network Manager](https://docs.aws.amazon.com/vpc/latest/tgwnm/what-is-network-manager.html). Use an existing configuration management database (CMDB) tool or a tool such as [AWS Config](https://aws.amazon.com/config/) to create an inventory of your workload and how it’s configured.

1. If this is an existing workload, identify and document the benchmark for your performance metrics, focusing on the bottlenecks and areas to improve. Performance-related networking metrics will differ per workload based on business requirements and workload characteristics. As a start, these metrics might be important to review for your workload: bandwidth, latency, packet loss, jitter, and retransmits.

1. If this is a new workload, perform [load tests](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) to identify performance bottlenecks.

1. For the performance bottlenecks you identify, review the configuration options for your solutions to identify performance improvement opportunities.

1. If you don’t know your network path or routes, use [Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-vaa.html) to identify them.

1. Review your network protocols to further reduce your latency.
   + [PERF05-BP05 Choose network protocols to improve performance](perf_select_network_protocols.md)

1. If you are using an AWS Site-to-Site VPN across multiple locations to connect to an AWS Region, then review [accelerated Site-to-Site VPN connections](https://docs.aws.amazon.com/vpn/latest/s2svpn/accelerated-vpn.html) for opportunities to improve networking performance.

1. When your workload traffic is spread across multiple accounts, evaluate your network topology and services to reduce latency.
   + Evaluate your operational and performance tradeoffs between [VPC Peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) and [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) when connecting multiple accounts. AWS Transit Gateway supports an AWS Site-to-Site VPN throughput to scale beyond a single [IPsec maximum limit](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-vpn-throughput-using-aws-transit-gateway/) by using multi-path. Traffic between an Amazon VPC and AWS Transit Gateway remains on the private AWS network and is not exposed to the internet. AWS Transit Gateway simplifies how you interconnect all of your VPCs, which can span across thousands of AWS accounts and into on-premises networks. Share your AWS Transit Gateway between multiple accounts using [Resource Access Manager](https://aws.amazon.com/ram/). To get visibility into your global network traffic, use [Network Manager](https://aws.amazon.com/transit-gateway/network-manager/) to get a central view of your network metrics.

1. Review your user locations and minimize the distance between your users and the workload.

   1. [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) is a networking service that improves the performance of your users’ traffic by up to 60% using the Amazon Web Services global network infrastructure. When the internet is congested, AWS Global Accelerator optimizes the path to your application to keep packet loss, jitter, and latency consistently low. It also provides static IP addresses that simplify moving endpoints between Availability Zones or AWS Regions without needing to update your DNS configuration or change client-facing applications.

   1. [Amazon CloudFront](https://aws.amazon.com/cloudfront/) can improve the performance of your workload content delivery and latency globally. CloudFront has over 410 globally dispersed points of presence that can cache your content and lower the latency to the end user.

   1. Amazon Route 53 offers [latency-based routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html), [geolocation routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geo.html), [geoproximity routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geoproximity.html), and [IP-based routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-ipbased.html) options to help you improve your workload’s performance for a global audience. Identify which routing option would optimize your workload performance by reviewing your workload traffic and user location.

1. Evaluate additional Amazon S3 features to improve storage IOPs.

   1.  [Amazon S3 Transfer acceleration](https://aws.amazon.com/s3/transfer-acceleration/) is a feature that lets external users benefit from the networking optimizations of CloudFront to upload data to Amazon S3. This improves the ability to transfer large amounts of data from remote locations that don’t have dedicated connectivity to the AWS Cloud.

   1.  [Amazon S3 Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html) replicates content to multiple Regions and simplifies the workload by providing one access point. When a Multi-Region Access Point is used, you can request or write data to Amazon S3 with the service identifying the lowest latency bucket.

1. Review your compute resource network bandwidth.

   1. Elastic Network Interfaces (ENA) used by EC2 instances, containers, and Lambda functions are limited on a per-flow basis. Review your placement groups to optimize your [EC2 networking throughput](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html). To avoid the bottleneck at the per flow-basis, design your application to use multiple flows. To monitor and get visibility into your compute related networking metrics, use [CloudWatch Metrics](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ec2-instance-network-bandwidth.html) and [`ethtool`](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-network-performance-ena.html). `ethtool` is included in the ENA driver and exposes additional network-related metrics that can be published as a [custom metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) to CloudWatch.

   1. Newer EC2 instances can leverage enhanced networking. [N-series EC2 instances](https://aws.amazon.com/ec2/nitro/), such as `M5n` and `M5dn`, take advantage of the fourth generation of custom Nitro cards to deliver up to 100 Gbps of network throughput to a single instance. These instances offer four times the network bandwidth and packet process compared to the base `M5` instances and are ideal for network intensive applications.

   1. [Amazon Elastic Network Adapters](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html) (ENA) provide further optimization by delivering better throughput for your instances within a [cluster placement group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#placement-groups-cluster%23placement-groups-limitations-cluster).

   1. [Elastic Fabric Adapter](https://aws.amazon.com/hpc/efa/) (EFA) is a network interface for Amazon EC2 instances that enables you to run workloads requiring high levels of internode communications at scale on AWS. With EFA, High Performance Computing (HPC) applications using the Message Passing Interface (MPI) and Machine Learning (ML) applications using NVIDIA Collective Communications Library (NCCL) can scale to thousands of CPUs or GPUs.

   1. [Amazon EBS-optimized](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) instances use an optimized configuration stack and provide additional, dedicated capacity to increase the Amazon EBS I/O. This optimization provides the best performance for your EBS volumes by minimizing contention between Amazon EBS I/O and other traffic from your instance.

**Level of effort for the implementation plan: **

To establish this best practice, you must be aware of your current workload component options that impact network performance. Gathering the components, evaluating network improvement options, experimenting, implementing, and documenting those improvements is a *low* to *moderate* level of effort.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon EBS - Optimized Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html)
+  [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
+  [Amazon EC2 instance network bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)
+  [EC2 Enhanced Networking on Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)
+  [EC2 Enhanced Networking on Windows](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/enhanced-networking.html)
+  [EC2 Placement Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
+  [Enabling Enhanced Networking with the Elastic Network Adapter (ENA) on Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html)
+  [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
+  [Networking Products with AWS](https://aws.amazon.com/products/networking/)
+  [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw)
+  [Transitioning to Latency-Based Routing in Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialTransitionToLBR.html)
+  [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html)
+  [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
+  [Building a cloud CMDB](https://aws.amazon.com/blogs/mt/building-a-cloud-cmdb-on-aws-for-consistent-resource-configuration-in-hybrid-environments/)
+  [Scaling VPN throughput using AWS Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-vpn-throughput-using-aws-transit-gateway/)

 **Related videos:**
+  [Connectivity to AWS and hybrid AWS network architectures (NET317-R1)](https://www.youtube.com/watch?v=eqW6CPb58gs)
+  [Optimizing Network Performance for Amazon EC2 Instances (CMP308-R1)](https://www.youtube.com/watch?v=DWiwuYtIgu0)
+  [AWS Global Accelerator](https://www.youtube.com/watch?v=lAOhr-5Urfk)

 **Related examples:**
+  [AWS Transit Gateway and Scalable Security Solutions](https://github.com/aws-samples/aws-transit-gateway-and-scalable-security-solutions)
+  [AWS Networking Workshops](https://networking.workshop.aws/)
