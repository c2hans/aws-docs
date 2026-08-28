---
source_url: https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-inbound-inspection.html
---

# Centralized inbound inspection
<a name="centralized-inbound-inspection"></a>

Internet-facing applications, by their nature, have a larger attack surface and are exposed to categories of threats most other types of applications don’t have to face. Having the necessary protection from attacks on these types of applications, and minimizing the impact surface area, are a core part of any security strategy.

As you deploy applications in your Landing Zone, many apps will be accessed by the users over the public internet (for example, through a Content Delivery Network (CDN), or through a public facing web-application) via a public facing load balancer, API gateway or directly through an internet gateway. You can secure your workloads and applications in this case by using AWS Web Application Firewall (AWS WAF) for Inbound Application Inspection, or alternatively IDS/IPS Inbound Inspection using Gateway Load Balancer or AWS Network Firewall.

As you continue to deploy applications in your Landing Zone, you might have a requirement to inspect inbound internet traffic. You can achieve this in multiple ways, using either distributed, centralized, or combined inspection architectures using Gateway Load Balancer running your third-party firewall appliances or AWS Network Firewall with advance DPI and IDS/IPS capabilities through the use of open source Suricata rules. This section covers both Gateway Load Balancer and AWS Network Firewall in a centralized deployment, using AWS Transit Gateway acting as a central hub for routing traffic.

## AWS WAF and AWS Firewall Manager for inspecting inbound traffic from the internet
<a name="waf-and-firewall-manager"></a>

AWS WAF is a web application firewall that helps protect your web applications or APIs against common web exploits and bots that may affect availability, compromise security, or consume excessive resources. AWS WAF gives you control over how traffic reaches your applications by enabling you to create security rules that control bot traffic and block common attack patterns, such as SQL injection or cross-site scripting (XSS). You can also customize rules that filter out specific traffic patterns.

You can deploy AWS WAF on Amazon CloudFront as part of your CDN solution, the Application Load Balancer that fronts your web servers, Amazon API Gateway for your REST APIs, or AWS AppSync for your GraphQL APIs.

Once you deploy AWS WAF, you can then create your own traffic filter rules using the visual rule builder, code in JSON, managed rules maintained by AWS, or you can subscribe to third-party rules from the AWS Marketplace. These rules can filter out unwanted traffic by evaluating the traffic against the specified patterns. You can further use Amazon CloudWatch for monitoring incoming traffic metrics and logging.

For centralized management across all your accounts and applications in AWS Organizations, you can use AWS Firewall Manager. AWS Firewall Manager is a security management service which allows you to centrally configure and manage firewall rules. As your new applications are created, AWS Firewall Manager makes it easy to bring new applications and resources into compliance by enforcing a common set of security rules.

Using AWS Firewall Manager, you can easily roll out AWS WAF rules for your Application Load Balancers, API Gateway instances, and Amazon CloudFront distributions. AWS Firewall Manager integrates with AWS Managed Rules for AWS WAF, which gives you an easy way to deploy pre-configured, curated AWS WAF rules on your applications. For more information on centrally managing AWS WAF with AWS Firewall Manager, refer to [Centrally manage AWS WAF (API v2) and AWS Managed Rules at scale with AWS Firewall Manager](https://aws.amazon.com/blogs/security/centrally-manage-aws-waf-api-v2-and-aws-managed-rules-at-scale-with-firewall-manager/).

![A diagram depicting centralized inbound traffic inspection using AWS WAF](http://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/images/inbound-traffic-inspection-with-waf.png)

In the preceding architecture, applications are running on Amazon EC2 instances in multiple availability zones in the private subnets. There is a public-facing Application Load Balancer (ALB) deployed in front of the Amazon EC2 instances, load balancing the requests between different targets. The AWS WAF is associated with the ALB.

### Advantages
<a name="advantages-21"></a>
+ With [AWS WAF Bot Control](https://aws.amazon.com/waf/features/bot-control/), you get visibility and control over common and pervasive bot traffic to your applications.
+ With [Managed Rules for AWS WAF](https://aws.amazon.com/marketplace/solutions/security/waf-managed-rules), you can quickly get started and protect your web application or APIs against common threats. You can select from many rule types, such as those that address issues such as the Open Web Application Security Project (OWASP) Top 10 security risks, threats specific to Content Management Systems (CMS) like WordPress or Joomla, or even emerging Common Vulnerabilities and Exposures (CVE). Managed rules are automatically updated as new issues emerge, so that you can spend more time building applications.
+ AWS WAF is a managed service and no appliance is needed for inspection in this architecture. In addition, it provides near real-time logs through [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/). AWS WAF gives near real-time visibility into your web traﬃc, which you can use to create new rules or alerts in Amazon CloudWatch.

### Key considerations
<a name="key-considerations-42"></a>
+ This architecture is best suited for HTTP header inspection and distributed inspections, because AWS WAF is integrated on a per-ALB, CloudFront distribution and API Gateway. AWS WAF does not log the request body.
+ Traffic going to a second set of ALB (if present) may not get inspected by the same AWS WAF instance; because a new request would be made to the second set of ALB.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
