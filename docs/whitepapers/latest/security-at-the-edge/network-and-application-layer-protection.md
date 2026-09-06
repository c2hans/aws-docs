---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-at-the-edge/network-and-application-layer-protection.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Network and application layer protection
<a name="network-and-application-layer-protection"></a>

 Edge networks are architected outside of the security perimeters of traditional cloud. Extending security to edge end devices requires network and application security and continuous monitoring, as well as encryption of data in transit and at rest.

 Edge customers should define trust boundaries for networks and accounts, and verify secure system configurations and other policy-enforcement points, including web application firewalls (WAFs) and API gateways. This can be done by blocking well-known exploits, implementing protections specific to applications, responding to new threats, and performing ongoing monitoring.

 There are two important aspects to network and application layer protection at the edge:
+  Protections from well-known exploits and attacks that could affect an organization’s applications
+  Visibility and control of workloads

**Manufacturing at the edge**
 Edge computing offers manufacturers opportunities to collect, process, and analyze data to enable predictive maintenance, improve quality control, and enhance worker safety with near-real-time alerts, industrial robot fleet management, and simulation. Although these edge applications can increase efficiency and keep costs down, they should be protected against security events. AWS WAF provides security rules to help protect these edge applications against common security attacks. AWS Shield Advanced helps protect against DDoS attacks.

 A WAF deployed at AWS edge locations can help to set fundamental protections, customize them to the applications, and help organizations quickly visualize actions so they can create a dynamic security posture. With AWS WAF, you can use the AWS pre-configured rules (Managed Rules), use Marketplace Rules, or create your own custom rules to protect against common attack vectors. [AWS Managed Rules](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups.html) give you protection against common web application attacks. They are curated by multiple points of intelligence across multiple sources within AWS.

 Marketplace Rules are written, updated, and managed by third-party security experts, and can be used on their own or in conjunction with AWS Managed Rules. AWS WAF, which integrates with AWS Shield Advanced at no extra cost, provides easy setup, low operation overhead, minimal latency impact, and customizable security. It also uses advanced automation to analyze web logs, identify malicious requests, and automatically update security rules.

 In addition to preventing incidents, visibility into traffic coming into and out of a network is a second key aspect of network and application layer protection. There are multiple options available to get insights and metrics: [CloudWatch metrics](https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html), sampled web requests, and logs.

 With CloudWatch, you can monitor web requests and web access control lists (ACLs) and rules. CloudWatch collects and processes raw data from AWS WAF and Shield Advanced into readable, near-real-time metrics. AWS WAF supports full logging of all web requests inspected by the service, which can then be stored in the cloud for compliance and auditing purposes, and used for debugging and additional forensics. You can also integrate the logs with your security information and event management (SIEM) and log analysis tools. For details, see [AWS WAF Launches New Comprehensive Logging Functionality](https://aws.amazon.com/about-aws/whats-new/2018/08/aws-waf-launches-new-comprehensive-logging-functionality/).

 For more details about AWS WAF, see the [Appendix](appendix-aws-services-for-edge-computing.md).
