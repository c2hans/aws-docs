---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_select_network_location.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP06 Choose your workload’s location based on network requirements
<a name="perf_select_network_location"></a>

Evaluate options for resource placement to reduce network latency and improve throughput, providing an optimal user experience by reducing page load and data transfer times.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

Resources, such as Amazon EC2 instances, are placed into availability zones within [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/), [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/), [AWS Outposts](https://aws.amazon.com/outposts/), or [AWS Wavelength](https://aws.amazon.com/wavelength/) zones. Selection of this location influences network latency and throughput from a given user location. Edge services such as [Amazon CloudFront](https://aws.amazon.com/cloudfront/) and [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) can also be used to improve network performance by either caching content at edge locations or providing users with an optimal path to the workload through the AWS global network.

 **Implementation steps**

1.  Choose the appropriate AWS Region or Regions for your deployment based on the following key elements:

   1.  **Where your users are located:** choosing a Region close to your workload’s users to ensure low latency when they use the workload.

   1.  **Where your data is located:** for data-heavy applications, the major bottleneck in data transfer is latency. Application code should run as close to the data as possible.

   1.  **Other constraints:** consider constraints such as security and compliance (for example, data residency requirements).

1.  For a given workload, if a component consists of a group of interdependent Amazon EC2 instances requiring low-latency, consider using [cluster placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) to influence placement of those instances to meet the requirements of the workload. Instances in the same cluster placement group enjoy a higher per-flow throughput limit for TCP/IP traffic and are placed in the same high-bisection bandwidth segment of the network. Cluster placement groups are recommended for applications that benefit from low network latency, high network throughput, or both.

1.  For a workload that is location-sensitive, for example with low-latency or data residency requirements, review [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) or [AWS Outposts](https://aws.amazon.com/outposts/).

   1.  AWS Local Zones are a type of infrastructure deployment that places compute, storage, database, and other select AWS services close to large population and industry centers.

   1.  AWS Outposts is a family of fully managed solutions delivering AWS infrastructure and services to virtually any on-premises or edge location for a truly consistent hybrid experience.

1.  Applications such as high-resolution live video streaming, high-fidelity audio, and augmented reality/virtual reality (AR/VR) require ultra-low-latency for 5G devices. For such applications, consider [AWS Wavelength](https://aws.amazon.com/wavelength/). AWS Wavelength embeds AWS compute and storage services within 5G networks, providing mobile edge computing infrastructure for developing, deploying, and scaling ultra-low-latency applications.

1.  If you have geographically distributed users, a content distribution network (CDN) may be used to accelerate distribution of static and dynamic web content by delivering data through globally dispersed points of presence (PoPs). CDNs typically also provide edge computing capabilities, performing latency sensitive operations such as HTTP header manipulations and URL rewrites and redirects at large scale at the edge. [Amazon CloudFront](https://aws.amazon.com/cloudfront/) is a web service that speeds up distribution of your static and dynamic web content. Use cases for CloudFront include accelerating static website content delivery and serving video on demand or live streaming video. CloudFront can also be used to customize the content and experience for viewers, at reduced latency.

1.  Some applications require fixed entry points or higher performance by reducing first byte latency and jitter, and increasing throughput. These applications can benefit from networking services that provide static anycast IP addresses and TCP termination at edge locations. [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) can improve performance for your applications by up to 60% and provide quick failover for multi-region architectures. AWS Global Accelerator provides you with static anycast IP addresses that serve as a fixed entry point for your applications hosted in one or more AWS Regions. These IP addresses permit traffic to ingress onto the AWS global network as close to your users as possible. AWS Global Accelerator reduces the initial connection setup time by establishing a TCP connection between the client and the AWS edge location closest to the client. Review the use of AWS Global Accelerator to improve the performance of your TCP/UDP workloads and provide quick failover for multi-region architectures.

1.  If you have applications or users on-premises, you may benefit from having a dedication network connection between your network and the cloud. A dedicated network connection can reduce the chance of encountering congestion or unexpected increases in latency. [AWS Direct Connect](https://aws.amazon.com/directconnect/) can improve application performance by connecting your network directly to AWS and bypassing the public internet. When creating a new connection, you can choose a hosted connection provided by an AWS Direct Connect Delivery Partner, or choose a dedicated connection from AWS and deploy at over 100 AWS Direct Connect locations around the globe. You can also reduce your networking costs with low data transfer rates out of AWS, and optionally configure a Site-to-Site VPN for failover.

1.  If you configure a [Site-to-Site VPN](https://aws.amazon.com/vpn/site-to-site-vpn/) to connect to your resources within AWS, you can optionally turn on acceleration. An accelerated Site-to-Site VPN connection uses AWS Global Accelerator to route traffic from your on-premises network to an AWS edge location that is closest to your customer gateway device.

1.  Identify which DNS routing option would optimize your workload performance by reviewing your workload traffic and user location. [Amazon Route 53](https://aws.amazon.com/route53) offers [latency-based routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html), [geolocation routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geo.html), [geoproximity routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geoproximity.html), and [IP-based routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-ipbased.html) options to help you improve your workload’s performance for a global audience.

   1.  Route 53 also offers low query latency for your end users. Using a global anycast network of DNS servers around the world, Route 53 is designed to automatically answer queries from the optimal location depending on network conditions.

## Resources
<a name="resources"></a>

 **Related best practices:**
+ [ COST07-BP02 Implement Regions based on cost ](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost_pricing_model_region_cost.html)
+ [ COST08-BP03 Implement services to reduce data transfer costs ](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost_data_transfer_implement_services.html)
+ [ REL10-BP01 Deploy the workload to multiple locations ](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_fault_isolation_multiaz_region_system.html)
+ [ REL10-BP02 Select the appropriate locations for your multi-location deployment ](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_fault_isolation_select_location.html)
+ [ SUS01-BP01 Choose Regions near Amazon renewable energy projects and Regions where the grid has a published carbon intensity that is lower than other locations (or Regions) ](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus_sus_region_a2.html)
+ [ SUS02-BP04 Optimize geographic placement of workloads for user locations ](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus_sus_user_a5.html)
+ [ SUS04-BP07 Minimize data movement across networks ](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus_sus_data_a8.html)

 **Related documents:**
+ [AWS Global Infrastructure ](https://aws.amazon.com/about-aws/global-infrastructure/)
+ [AWS Local Zones and AWS Outposts, choosing the right technology for your edge workload ](https://aws.amazon.com/blogs/compute/aws-local-zones-and-aws-outposts-choosing-the-right-technology-for-your-edge-workload/)
+  [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
+  [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/)
+  [AWS Outposts](https://aws.amazon.com/outposts/)
+  [AWS Wavelength](https://aws.amazon.com/wavelength/)
+  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+  [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/)
+  [AWS Direct Connect](https://aws.amazon.com/directconnect/)
+  [Site-to-Site VPN](https://aws.amazon.com/vpn/site-to-site-vpn/)
+  [Amazon Route 53](https://aws.amazon.com/route53)

 **Related videos:**
+ [AWS Local Zones Explainer Video ](https://www.youtube.com/watch?v=JHt-D4_zh7w)
+ [AWS Outposts: Overview and How It Works ](https://www.youtube.com/watch?v=ppG2FFB0mMQ)
+ [AWS re:Invent 2021 - AWS Outposts: Bringing the AWS experience on premises ](https://www.youtube.com/watch?v=FxVF6A22498)
+ [AWS re:Invent 2020: AWS Wavelength: Run apps with ultra-low latency at 5G edge ](https://www.youtube.com/watch?v=AQ-GbAFDvpM)
+ [AWS re:Invent 2022 - AWS Local Zones: Building applications for a distributed edge ](https://www.youtube.com/watch?v=bDnh_d-slhw)
+ [AWS re:Invent 2021 - Building low-latency websites with Amazon CloudFront ](https://www.youtube.com/watch?v=9npcOZ1PP_c)
+ [AWS re:Invent 2022 - Improve performance and availability with AWS Global Accelerator](https://www.youtube.com/watch?v=s5sjsdDC0Lg)
+ [AWS re:Invent 2022 - Build your global wide area network using AWS](https://www.youtube.com/watch?v=flBieylTwvI)
+ [AWS re:Invent 2020: Global traffic management with Amazon Route 53 ](https://www.youtube.com/watch?v=E33dA6n9O7I)

 **Related examples:**
+ [AWS Global Accelerator Workshop ](https://catalog.us-east-1.prod.workshops.aws/workshops/effb1517-b193-4c59-8da5-ce2abdb0b656/en-US)
+ [ Handling Rewrites and Redirects using Edge Functions ](https://catalog.us-east-1.prod.workshops.aws/workshops/814dcdac-c2ad-4386-98d5-27d37bb77766/en-US)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
