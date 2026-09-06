---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/protect-network-traffic-further-from-your-origin-using-aws-global-accelerator-bp1.html
---

# Protect network traffic further from your origin using AWS Global Accelerator (BP1)
<a name="protect-network-traffic-further-from-your-origin-using-aws-global-accelerator-bp1"></a>

 You can implement a DDoS resilient architecture that provides many of the same benefits as the web application delivery at the edge best practices, even if your application uses protocols not supported by CloudFront or you're operating a web application that requires global static IP addresses.

 Global Accelerator is a networking service that improves availability and performance of users' TCP and UDP traffic by up to 60%. This is accomplished by ingressing traffic at the edge location closest to your users and routing it over the AWS global network infrastructure to your application, whether it runs in a single or multiple AWS Regions.

 Global Accelerator routes TCP and UDP traffic to the optimal AWS endpoint based on the user's geographic location, endpoint health, and configured endpoint weights, reducing latency and improving availability. If there is an application failure, Global Accelerator provides failover to the next best endpoint. Global Accelerator uses the vast capacity of the AWS global network and integrations with Shield—such as a stateless SYN proxy that challenges new connection attempts with SYN cookies, dropping spoofed traffic that can't complete the TCP handshake—to protect applications.

 For example, you might require IP addresses that your end users can add to the allow list in their firewalls and aren't used by any other AWS customers. In these scenarios you can use Global Accelerator to protect web applications running on Application Load Balancer and in conjunction with AWS WAF to also detect and mitigate web application layer request floods.

 For more information about protecting and optimizing the performance of network traffic using Global Accelerator, see [Getting started with Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/getting-started.html) and the diagram *DDoS-resilient reference architecture for TCP and UDP applications* in [Mitigation techniques](mitigation-techniques.md).
