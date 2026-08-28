---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/mitigation-techniques.html
---

# Mitigation techniques
<a name="mitigation-techniques"></a>

 Some forms of DDoS mitigation are included automatically with AWS services. DDoS resilience can be improved further by using an AWS architecture with specific services—covered in the following sections—and by implementing additional best practices for each part of the network flow between users and your application.

 You can use AWS services that operate from edge locations, such as [Amazon CloudFront](https://aws.amazon.com/cloudfront/), [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/), and [Amazon Route 53](https://aws.amazon.com/route53/) to build comprehensive availability protection against all known infrastructure layer attacks. These services are part of the [AWS Global Edge Network](https://aws.amazon.com/products/networking/edge-networking/), and can improve the DDoS resilience of your application when serving any type of application traffic from edge locations distributed around the world. You can run your application in any AWS Region and use these services to protect your application availability and optimize the performance of your application for legitimate end users.

 Benefits of using Amazon CloudFront, Global Accelerator, and Amazon Route 53 include:
+  Access to internet and DDoS mitigation capacity across the AWS Global Edge Network. This is useful in mitigating larger volumetric attacks, which can reach terabits per second (Tbps).
+  [AWS Shield](https://aws.amazon.com/shield/) DDoS mitigation systems are integrated with AWS edge services, reducing time-to-mitigate from minutes to sub second.
+  Stateless SYN Flood mitigation verifies incoming connections using SYN cookies before passing them to the protected service. This is designed to help ensure that only valid connections reach your application while protecting your legitimate end users against false positives drops.
+  Automatic traffic engineering systems that disperse or isolate the impact of large volumetric DDoS attacks. All these services isolate attacks at the source before they reach your origin, which means less impact on systems protected by these services.
+  The AWS Threat research team curates and maintains a list of IP addresses by tracking malicious activities against customer's AWS resources. IP addresses exhibiting repeated malicious behavior are added to this list, which is automatically enforced through CloudFront edge protection systems to help safeguard customer resources.
+  Application layer defense using CloudFront with [AWS WAF](https://aws.amazon.com/waf/), without requiring changes to your existing origin architecture—whether hosted in an AWS Region or on-premises.
+  [CloudFront](https://aws.amazon.com/cloudfront/) origin fetches are free from any AWS origin such as [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3), [Amazon EC2](https://aws.amazon.com/ec2/), or [Elastic Load Balancers](https://aws.amazon.com/elasticloadbalancing/), including origins in private subnets through [VPC origins](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-vpc-origins.html). Additionally, you aren't charged for HTTP requests or data transfer out for requests rejected by CloudFront or AWS WAF.

 The following architecture diagrams include AWS Global Edge Network services. The BP labels in these diagrams see best practices that are detailed in later sections of this document.

 The following figure illustrates a typical reference architecture web applications and maps its components to best practices that will be elaborated in the following sections of the chapter. These applications include the application layer of the Open Systems Interconnection (OSI) model and for that reason use CloudFront and AWS WAF at the edge for the protection.

![DDoS-resilient reference architecture for web applications](http://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/images/ddos-resilient-ref-arch-web.png)

 The following figure illustrates a typical architecture for applications that operate at the transport layer of the OSI model and because of that the best practices include a different component for protection at the Edge.

![DDoS-resilient reference architecture for TCP and UDP applications](http://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/images/ddos-resilient-ref-arch-tcp-udp.png)

 With AWS service you can also protect applications that run inside corporate data centers, the following figure illustrates a collection of best practices applicable to that scenario.

![DDoS-resilient reference architecture for web applications on-premises](http://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/images/ddos-resilient-ref-arch-on-premises.png)

 These architectures include several AWS services that can help you improve your application's resiliency against DDoS attacks. The following table provides a summary of these services and the capabilities that they can provide. AWS has tagged each service with a best practice indicator (BP1, BP2) for easier reference within this document. For example, an upcoming section discusses the capabilities provided by Amazon CloudFront and Global Accelerator that includes the best practice indicator BP1.

 *Table 2 – Summary of best practices*

<table>
<thead>
  <tr><th> </th><th colspan="3"> AWS Edge</th><th colspan="3">AWS Region</th></tr>
</thead>
<tbody>
  <tr><td> </td><td> Using Amazon CloudFront (BP1) with AWS WAF (BP2) </td><td> Using Global Accelerator (BP1) </td><td> Using Amazon Route 53 (BP3) </td><td> Using <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html">Application Load Balancer</a> (BP6) with AWS WAF (BP2) </td><td> Using security groups and network ACLs in Amazon VPC (BP5) </td><td> Using <a href="https://aws.amazon.com/ec2/">Amazon Elastic Compute Cloud</a>, <a href="https://aws.amazon.com/eks/">Amazon EKS</a>, and <a href="https://aws.amazon.com/ecs/">Amazon ECS</a> with auto scaling, and <a href="https://aws.amazon.com/lambda/">Lambda</a> (BP7) </td></tr>
  <tr><td> Layer 3 (for example, UDP reflection) attack mitigation </td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td></tr>
  <tr><td> Layer 4 (for example, SYN flood) attack mitigation </td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td> Layer 6 (for example, TLS) attack mitigation </td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td> Reduce attack surface </td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td></td></tr>
  <tr><td> Scale to absorb application layer traffic </td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td><td>✔</td></tr>
  <tr><td> Layer 7 (application layer) attack mitigation </td><td>✔</td><td></td><td>✔</td><td>✔</td><td></td><td></td></tr>
  <tr><td>Geographic isolation and dispersion of excess traffic and larger DDoS attacks</td><td>✔</td><td>✔</td><td>✔</td><td></td><td></td><td></td></tr>
</tbody>
</table>

 Another way to improve your readiness to respond to and mitigate DDoS attacks is by subscribing to [AWS Shield Advanced](https://aws.amazon.com/shield/). Benefits of using AWS Shield Advanced include:
+ Access to 24x7 specialized support from the [AWS Shield Response Team](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-srt-support.html) (AWS SRT) for assistance with mitigating DDoS attacks that impact application availability, including an optional proactive engagement feature. It requires a Business Support\+ or Enterprise Support subscription.
+ Sensitive detection thresholds that route traffic into the DDoS mitigation system earlier and can improve time-to-mitigate attacks against Amazon EC2 (including elastic Load Balancer) or [Network Load Balancer](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/), when used with an Elastic IP address
+ [Automatic application layer DDoS mitigation](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-automatic-app-layer-response.html) where Shield Advanced responds to detected DDoS attacks by creating, evaluating, and deploying custom AWS WAF rules
+ Shield Advanced includes WAF request coverage at no additional cost (subject to usage thresholds). For current pricing details, see the [AWS Shield Pricing](https://aws.amazon.com/shield/pricing/) page.
+ Centralized management of security policies through [AWS Firewall Manager](https://aws.amazon.com/firewall-manager/) at no additional cost.
+ Cost protection that enables you to request a limited refund of scaling-related costs that result from a DDoS attack.
+ [Protection groups](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html#ddos-advanced-protection-groups) that enable you to bundle resources, providing a self-service way to customize the scope of detection and mitigation for your application by treating multiple resources as a single unit.
+ DDoS attack visibility by using the [AWS Management Console](https://aws.amazon.com/console/), API, and [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) [metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) and [alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html).

 This optional DDoS mitigation service helps protect applications hosted on any AWS Region. The service is available globally for CloudFront, Route 53, and Global Accelerator. Regionally, you can protect Application Load Balancer and Elastic IP addresses which allows you to protect [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) (NLBs) or [Amazon EC2](https://aws.amazon.com/ec2/) instances.

 For a complete list of AWS Shield Advanced features and for more information about [AWS Shield](https://aws.amazon.com/shield/), see [How AWS Shield Advanced works](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
