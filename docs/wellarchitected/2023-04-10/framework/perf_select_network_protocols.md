---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_select_network_protocols.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF05-BP05 Choose network protocols to improve performance
<a name="perf_select_network_protocols"></a>

Assess the performance requirements for your workload, and choose the network protocols that optimize your workload’s overall performance.

There is a relationship between latency and bandwidth to achieve throughput. For instance, if your file transfer is using Transmission Control Protocol (TCP), higher latencies will reduce overall throughput. There are approaches to fix this with TCP tuning and optimized transfer protocols (some approaches use User Datagram Protocol (UDP)).

 The [scalable reliable datagram (SRD)](https://ieeexplore.ieee.org/document/9167399) protocol is a network transport protocol built by AWS for Elastic Fabric Adapters that provides reliable datagram delivery. Unlike the TCP protocol, SRD can reorder packets and deliver them out of order. This out of order delivery mechanism of SRD sends packets in parallel over alternate paths, increasing throughput.

 **Common anti-patterns:**
+  Using TCP for all workloads regardless of performance requirements.

 **Benefits of establishing this best practice:**
+  Selecting the proper protocol for communication between workload components ensures that you are getting the best performance for that workload.
+  Verifying that an appropriate protocol is used for communication between users and workload components helps improve overall user experience for your applications. For instance, by using both TCP and UDP together, VDI workloads can take advantage of the reliability of TCP for critical data and the speed of UDP for real-time data.

 **Level of risk exposed if this best practice is not established:** Medium (Using an inappropriate network protocol can lead to poor performance, such as slow response times, high latency and poor scalability)

## Implementation guidance
<a name="implementation-guidance"></a>

A primary consideration for improving your workload’s performance is to understand the latency and throughput requirements, and then choose network protocols that optimize performance.

 **When to consider using TCP**

 TCP provides reliable data delivery, and can be used for communication between workload components where reliability and guaranteed delivery of data is important. Many web-based applications rely on TCP-based protocols, such as HTTP and HTTPS, to open TCP sockets for communication with servers on AWS. Email and file data transfer are common applications that also make use of TCP due to TCP’s ability to control the rate of data exchange and network congestion. Using TLS with TCP can add some overhead to the communication, which can result in increased latency and reduced throughput. The overhead comes mainly from the added overhead of the handshake process, which can take several round-trips to complete. Once the handshake is complete, the overhead of encrypting and decrypting data is relatively small.

 **When to consider using UDP**

 UDP is a connectionless-oriented protocol and is therefore suitable for applications that need fast, efficient transmission, such as log, monitoring, and VoIP data. Also, consider using UDP if you have workload components that respond to small queries from large numbers of clients to ensure optimal performance of the workload. Datagram Transport Layer Security (DTLS) is the UDP equivalent of TLS. When using DTLS with UDP, the overhead comes from encrypting and decrypting the data, as the handshake process is simplified. DTLS also adds a small amount of overhead to the UDP packets, as it includes additional fields to indicate the security parameters and to detect tampering.

 **When to consider using SRD**

 Scalable reliable datagram (SRD) is a network transport protocol optimized for high-throughput workloads due to its ability to load-balancer traffic across multiple paths and quickly recover from packet drops or link failures. SRD is therefore best used for high performance computing (HPC) workloads that require high throughput and low latency communication between compute nodes. This might include parallel processing tasks such as simulation, modelling, and data analysis that involve a large amount of data transfer between nodes.

 **Implementation steps**

1.  Use the [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) and [AWS Transfer Family](https://aws.amazon.com/aws-transfer-family/) services to improve the throughput of your online file transfer applications. The AWS Global Accelerator service helps you achieve lower latency between your client devices and your workload on AWS. With AWS Transfer Family, you can use TCP-based protocols such as Secure Shell File Transfer Protocol (SFTP) and File Transfer Protocol over SSL (FTPS) to securely scale and manage your file transfers to AWS storage services.

1.  Use network latency to determine if TCP is appropriate for communication between workload components. If the network latency between your client application and server is high, then the TCP three-way handshake can take some time, thereby impacting on the responsiveness of your application. Metrics such as Time to First Byte (TTFB) and Round-Trip Time (RTT) can be used to measure network latency. If your workload serves dynamic content to users, consider using [Amazon CloudFront](https://aws.amazon.com/cloudfront/), which establishes a persistent connection to each origin for dynamic content to eliminate the connection setup time that would otherwise slow down each client request.

1.  Using TLS with TCP or UDP can result in increased latency and reduced throughput for your workload due to the impact of encryption and decryption. For such workloads, consider SSL/TLS offloading on [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) to improve workload performance by allowing the load balancer to handle SSL/TLS encryption and decryption process instead of having backend instances do it. This can help reduce the CPU utilization on the backend instances, which can improve performance and increase capacity.

1.  Use the [Network Load Balancer (NLB)](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/) to deploy services that rely on the UDP protocol, such as authentication and authorization, logging, DNS, IoT, and streaming media, to improve the performance and reliability of your workload. The NLB distributes incoming UDP traffic across multiple targets, allowing you to scale your workload horizontally, increase capacity, and reduce the overhead of a single target.

1.  For your High Performance Computing (HPC) workloads, consider using the [Elastic Network Adapter (ENA) Express](https://aws.amazon.com/about-aws/whats-new/2022/11/elastic-network-adapter-ena-express-amazon-ec2-instances/) functionality that uses the SRD protocol to improve network performance by providing a higher single flow bandwidth (25Gbps) and lower tail latency (99.9 percentile) for network traffic between EC2 instances.

1.  Use the [Application Load Balancer (ALB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) to route and load balance your gRPC (Remote Procedure Calls) traffic between workload components or between gRPC clients and services. gRPC uses the TCP-based HTTP/2 protocol for transport and it provides performance benefits such as lighter network footprint, compression, efficient binary serialization, support for numerous languages, and bi-directional streaming.

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
+ [ Tuning Your Cloud: Improve Global Network Performance for Application ](https://www.youtube.com/watch?v=00ukhVcgWrs)
+ [ Application Scaling with EFA and SRD ](https://pages.awscloud.com/HPC-Application-Scaling-with-Elastic-Fabric-Adapter-EFA-and-Scalable-Reliable-Datagram-SRD_2020_0004-CMP_OD.html)

 **Related examples:**
+  [AWS Transit Gateway and Scalable Security Solutions](https://github.com/aws-samples/aws-transit-gateway-and-scalable-security-solutions)
+  [AWS Networking Workshops](https://networking.workshop.aws/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
