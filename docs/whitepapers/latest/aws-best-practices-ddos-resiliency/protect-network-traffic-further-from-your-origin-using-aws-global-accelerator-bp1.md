---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/protect-network-traffic-further-from-your-origin-using-aws-global-accelerator-bp1.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Protect network traffic further from your origin using AWS Global Accelerator (BP1)
<a name="protect-network-traffic-further-from-your-origin-using-aws-global-accelerator-bp1"></a>

 Global Accelerator is a networking service that improves availability and performance of users’ traffic by up to 60%. This is accomplished by ingressing traffic at the edge location closest to your users and routing it over the AWS global network infrastructure to your application, whether it runs in a single or multiple AWS Regions.

 Global Accelerator routes TCP and UDP traffic to the optimal endpoint based on performance in the closest AWS Region to the user. If there is an application failure, Global Accelerator provides failover to the next best endpoint within 30 seconds. Global Accelerator uses the vast capacity of the AWS global network and integrations with Shield, such as a stateless SYN proxy capability that challenges new connection attempts and only serves legitimate end users, to protect applications.

 You can implement a DDoS resilient architecture that provides many of the same benefits as the Web Application Delivery at the Edge best practices, even if your application uses protocols not supported by CloudFront or you are operating a web application that requires global static IP addresses.

 For example, you may require IP addresses that your end users can add to the allow list in their firewalls and are not used by any other AWS customers. In these scenarios you can use Global Accelerator to protect web applications running on Application Load Balancer and in conjunction with AWS WAF to also detect and mitigate web application layer request floods.

 For more information about protecting and optimizing the performance of network traffic using Global Accelerator, refer to [Getting started with Global Accelerator.](https://docs.aws.amazon.com/global-accelerator/latest/dg/getting-started.html)
