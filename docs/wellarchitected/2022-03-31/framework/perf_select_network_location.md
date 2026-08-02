---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_select_network_location.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP06 Choose your workload’s location based on network requirements
<a name="perf_select_network_location"></a>

 Use the cloud location options available to reduce network latency or improve throughput. Use AWS Regions, Availability Zones, placement groups, and edge locations such as AWS Outposts, AWS Local Zones, and AWS Wavelength, to reduce network latency or improve throughput.

 The AWS Cloud infrastructure is built around Regions and Availability Zones. A Region is a physical location in the world having multiple Availability Zones.

 Availability Zones consist of one or more discrete data centers, each with redundant power, networking, and connectivity, housed in separate facilities. These Availability Zones offer you the ability to operate production applications and databases that are more highly available, fault tolerant, and scalable than would be possible from a single data center

 Choose the appropriate Region or Regions for your deployment based on the following key elements:
+  **Where your users are located**: Choosing a Region close to your workload’s users ensures lower latency when they use the workload.
+  **Where your data is located**: For data-heavy applications, the major bottleneck in latency is data transfer. Application code should execute as close to the data as possible.
+  **Other constraints**: Consider constraints such as security and compliance.

 Amazon EC2 provides placement groups for networking. A placement group is a logical grouping of instances to decrease latency or increase reliability. Using placement groups with supported instance types and an Elastic Network Adapter (ENA) enables workloads to participate in a low-latency, 25 Gbps network. Placement groups are recommended for workloads that benefit from low network latency, high network throughput, or both. Using placement groups has the benefit of lowering jitter in network communications.

 Latency-sensitive services are delivered at the edge using a global network of edge locations. These edge locations commonly provide services such as content delivery network (CDN) and domain name system (DNS). By having these services at the edge, workloads can respond with low latency to requests for content or DNS resolution. These services also provide geographic services such as geo targeting of content (providing different content based on the end users’ location), or latency-based routing to direct end users to the nearest Region (minimum latency).

 [https://aws.amazon.com/cloudfront/](https://aws.amazon.com/cloudfront/) is a global CDN that can be used to accelerate both static content such as images, scripts, and videos, as well as dynamic content such as APIs or web applications. It relies on a global network of edge locations that will cache the content and provide high-performance network connectivity to your users. CloudFront also accelerates many other features such as content uploading and dynamic applications, making it a performance addition to all applications serving traffic over the internet. [https://aws.amazon.com/lambda/edge/](https://aws.amazon.com/lambda/edge/) is a feature of Amazon CloudFront that will let you run code closer to users of your workload, which improves performance and reduces latency.

 Amazon Route 53 is a highly available and scalable cloud DNS web service. It’s designed to give developers and businesses an extremely reliable and cost-effective way to route end users to internet applications by translating names, like www.example.com, into numeric IP addresses, like 192.168.2.1, that computers use to connect to each other. Route 53 is fully compliant with IPv6.

 [https://aws.amazon.com/outposts/](https://aws.amazon.com/outposts/) is designed for workloads that need to remain on-premises due to latency requirements, where you want that workload to run seamlessly with the rest of your other workloads in AWS. AWS Outposts are fully managed and configurable compute and storage racks built with AWS-designed hardware that allow you to run compute and storage on-premises, while seamlessly connecting to the broad array of AWS services in in the cloud.

 [https://aws.amazon.com/about-aws/global-infrastructure/localzones/](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) is designed to run workloads that require single-digit millisecond latency, like video rendering and graphics intensive, virtual desktop applications. Local Zones allow you to gain all the benefits of having compute and storage resources closer to end-users.

 [https://aws.amazon.com/wavelength/](https://aws.amazon.com/wavelength/) is designed to deliver ultra-low latency applications to 5G devices by extending AWS infrastructure, services, APIs, and tools to 5G networks. Wavelength embeds storage and compute inside telco providers 5G networks to help your 5G workload if it requires single-digit millisecond latency, such as IoT devices, game streaming, autonomous vehicles, and live media production.

 Use edge services to reduce latency and to enable content caching. Ensure that you have configured cache control correctly for both DNS and HTTP/HTTPS to gain the most benefit from these approaches.

 **Common anti-patterns:**
+  You consolidate all workload resources into one geographic location.
+  You chose the closest region to your location but not to the workload end user.

 **Benefits of establishing this best practice:** You must ensure that your network is available wherever you want to reach customers. Using the AWS private global network ensures that your customers get the lowest latency experience by deploying workloads into the locations nearest them.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Reduce latency by selecting the correct locations: Identify where your users and data are located. Take advantage of AWS Regions, Availability Zones, placement groups, and edge locations to reduce latency.

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

 **Related videos:**
+  [Connectivity to AWS and hybrid AWS network architectures (NET317-R1)](https://www.youtube.com/watch?v=eqW6CPb58gs)
+  [Optimizing Network Performance for Amazon EC2 Instances (CMP308-R1)](https://www.youtube.com/watch?v=DWiwuYtIgu0)

 **Related examples:**
+  [AWS Transit Gateway and Scalable Security Solutions](https://github.com/aws-samples/aws-transit-gateway-and-scalable-security-solutions)
+  [AWS Networking Workshops](https://networking.workshop.aws/)
