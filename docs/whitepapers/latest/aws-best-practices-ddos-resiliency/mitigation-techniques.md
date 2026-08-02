---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/mitigation-techniques.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Mitigation techniques
<a name="mitigation-techniques"></a>

 Some forms of DDoS mitigation are included automatically with AWS services. DDoS resilience can be improved further by using an AWS architecture with specific services, covered in the following sections, and by implementing additional best practices for each part of the network flow between users and your application.

 You can use AWS services that operate from edge locations, such as Amazon CloudFront, AWS Global Accelerator, and Amazon Route 53 to build comprehensive availability protection against all known infrastructure layer attacks. These services are part of the [AWS Global Edge Network](https://aws.amazon.com/products/networking/edge-networking/), and can improve the DDoS resilience of your application when serving any type of application traffic from edge locations distributed around the world. You can run your application in any AWS Region, and use these services to protect your application availability and optimize the performance of your application for legitimate end users.

 Benefits of using Amazon CloudFront, Global Accelerator, and Amazon Route 53 include:
+  Access to internet and DDoS mitigation capacity across the AWS Global Edge Network. This is useful in mitigating larger volumetric attacks, which can reach terabit scale.
+  AWS Shield DDoS mitigation systems are integrated with AWS edge services, reducing time-to-mitigate from minutes to sub second.
+  Stateless SYN Flood mitigation verifies incoming connections using SYN cookies before passing them to the protected service. This ensures that only valid connections reach your application while protecting your legitimate end users against false positives drops.
+  Automatic traffic engineering systems that disperse or isolate the impact of large volumetric DDoS attacks. All of these services isolate attacks at the source before they reach your origin, which means less impact on systems protected by these services.
+  Application layer defense for CloudFront when combined with [AWS WAF](https://aws.amazon.com/waf/) that does not require changing current application architecture (for example, in an AWS Region or on-premises data center).

 There is no charge for inbound data transfer on AWS and you do not pay for DDoS attack traffic that is mitigated by AWS Shield. The following architecture diagram includes AWS Global Edge Network services.

![Diagram showing DDoS-resilient reference architecture](http://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/images/ddos-resilient-ref-arch.png)

 This architecture includes several AWS services that can help you improve your web application’s resiliency against DDoS attacks. The following table provides a summary of these services and the capabilities that they can provide. AWS has tagged each service with a best practice indicator (BP1, BP2) for easier reference within this document. For example, an upcoming section discusses the capabilities provided by Amazon CloudFront and Global Accelerator that includes the best practice indicator BP1.

 *Table 2 - Summary of best practices*

<table>
<thead>
  <tr><th> </th><th colspan="3"> AWS Edge</th><th colspan="3">AWS Region </th></tr>
</thead>
<tbody>
  <tr><td> </td><td> Using Amazon CloudFront (BP1) with AWS WAF (BP2) </td><td> Using Global Accelerator (BP1) </td><td> Using Amazon Route 53 (BP3) </td><td> Using Elastic Load Balancing (BP6) with AWS WAF (BP2) </td><td> Using security groups and network ACLs in Amazon VPC (BP5) </td><td> Using [Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling](https://aws.amazon.com/pm/ec2/) (BP7)</td></tr>
  <tr><td> Layer 3 (for example, UDP reflection) attack mitigation </td><td> ✔ </td><td> ✔ </td><td> ✔ </td><td> ✔ </td><td> ✔ </td><td> ✔ </td></tr>
  <tr><td> Layer 4 (for example, SYN flood) attack mitigation </td><td> ✔ </td><td> ✔ </td><td> ✔ </td><td> ✔ </td><td> </td><td> </td></tr>
  <tr><td> Layer 6 (for example, TLS) attack mitigation </td><td> ✔ </td><td> ✔ </td><td> ✔ </td><td> ✔ </td><td> </td><td> </td></tr>
  <tr><td> Reduce attack surface </td><td> ✔ </td><td> ✔ </td><td> ✔ </td><td> ✔ </td><td> ✔ </td><td> </td></tr>
  <tr><td> Scale to absorb application layer traffic </td><td> ✔ </td><td> ✔ </td><td> ✔ </td><td> ✔ </td><td> ✔ </td><td> ✔ </td></tr>
  <tr><td> Layer 7 (application layer) attack mitigation </td><td> ✔ </td><td> ✔(\*) </td><td> ✔ </td><td> ✔ </td><td> ✔(\*) </td><td> ✔(\*) </td></tr>
  <tr><td> Geographic isolation and dispersion of excess traffic and larger DDoS attacks </td><td> ✔ </td><td> ✔ </td><td> ✔ </td><td> </td><td> </td><td> </td></tr>
</tbody>
</table>

 ✔(\*): If used with AWS WAF with [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)

 Another way to improve your readiness to respond to and mitigate DDoS attacks is by subscribing to AWS Shield Advanced. Benefits of using AWS Shield Advanced include:
+ Access to 24x7 specialized support from the [AWS Shield Response Team](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-support.html) (AWS SRT) for assistance with mitigating DDoS attacks that impact application availability, including an optional Proactive engagement feature
+ Sensitive detection thresholds that route traffic into the DDoS mitigation system earlier and can improve time-to-mitigate attacks against Amazon EC2 (including elastic Load Balancer) or Network Load Balancer, when used with an Elastic IP address
+ Tailored Layer 7 detection based on baselined traffic patterns of your application when used with AWS WAF
+ Automatic application layer DDoS mitigation where Shield Advanced responds to detected DDoS attacks by creating, evaluating, and deploying custom AWS WAF rules
+ Access to AWS WAF at no additional cost for the mitigation of application layer DDoS attacks (when used with Amazon CloudFront or Application Load Balancer)
+ Centralized management of security policies through [AWS Firewall Manager](https://aws.amazon.com/firewall-manager/) at no additional cost.
+ Cost protection that enables you to request a limited refund of scaling-related costs that result from a DDoS attack.
+ Enhanced service level agreement that is specific to AWS Shield Advanced customers.
+ Protection groups that enable you to bundle resources, providing a self-service way to customize the scope of detection and mitigation for your application by treating multiple resources as a single unit. For information about protection groups, refer to [Shield](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html#ddos-advanced-protection-groups) [Advanced protection groups.](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html#ddos-advanced-protection-groups)
+ DDoS attack visibility by using the [AWS Management Console](https://aws.amazon.com/console/), API, and Amazon CloudWatch [metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) and [alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html).

 This optional DDoS mitigation service helps protect applications hosted on any AWS Region. The service is available globally for CloudFront, Route 53, and Global Accelerator. Regionally, you can protect Application Load Balancer, Classic Load Balancer and Elastic IP addresses which allows you to protect [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) (NLBs) or [Amazon EC2](https://aws.amazon.com/ec2/) instances.

 For a complete list of AWS Shield Advanced features and for more information about AWS Shield, refer to [How AWS Shield works](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html).
