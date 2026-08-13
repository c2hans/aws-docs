---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/perf_select_network_encryption_offload.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP04 Leverage load-balancing and encryption offloading
<a name="perf_select_network_encryption_offload"></a>

 Distribute traffic across multiple resources or services to allow your workload to take advantage of the elasticity that the cloud provides. You can also use load balancing for offloading encryption termination to improve performance and to manage and route traffic effectively.

 When implementing a scale-out architecture where you want to use multiple instances for service content, you can use load balancers inside your Amazon VPC. AWS provides multiple models for your applications in the ELB service. Application Load Balancer is best suited for load balancing of HTTP and HTTPS traffic and provides advanced request routing targeted at the delivery of modern application architectures, including microservices and containers.

 Network Load Balancer is best suited for load balancing of TCP traffic where extreme performance is required. It is capable of handling millions of requests per second while maintaining ultra-low latencies, and it is optimized to handle sudden and volatile traffic patterns.

 [*Elastic Load Balancing*](https://aws.amazon.com/elasticloadbalancing/) provides integrated certificate management and SSL/TLS decryption, allowing you the flexibility to centrally manage the SSL settings of the load balancer and offload CPU intensive work from your workload.

 **Common anti-patterns:**
+  You route all internet traffic through existing load balancers.
+  You use generic TCP load balancing and making each compute node handle SSL encryption.

 **Benefits of establishing this best practice:** A load balancer handles the varying load of your application traffic in a single Availability Zone, or across multiple Availability Zones. Load balancers feature the high availability, automatic scaling, and robust security necessary to make your applications fault tolerant.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Use the appropriate load balancer for your workload: Select the appropriate load balancer for your workload. If you must load balance HTTP requests, we recommend Application Load Balancer. For network and transport protocols (layer 4 – TCP, UDP) load balancing, and for extreme performance and low latency applications, we recommend Network Load Balancer. Application Load Balancers support HTTPS and Network Load Balancers support TLS encryption offloading.

 Enable offload of HTTPS or TLS encryption: Elastic Load Balancing includes integrated certificate management, user-authentication, and SSL/TLS decryption. It provides the flexibility to centrally manage TLS settings and offload CPU intensive workloads from your applications. Encrypt all HTTPS traffic as part of your load balancer deployment.

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
