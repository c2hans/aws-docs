---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf16-bp01.html
---

# LSPERF16-BP01 Deploy intelligent traffic shaping with security-aware bandwidth allocation for different data types
<a name="lsperf16-bp01"></a>

 Develop traffic classification systems to identify life sciences data transfers and apply security and throughput policies based on sensitivity and size. Set up dynamic bandwidth allocation that prioritizes large research data transfers during off-peak times while maintaining security measures. Implement compression and de-duplication before encryption to reduce transmission volume and improve efficiency without compromising security.

 **Desired outcome:** You have an intelligent traffic management system that automatically classifies and optimizes life sciences data transfers while maintaining security controls. This enables efficient use of network resources without compromising data protection requirements.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Establish comprehensive classification systems that automatically identify and categorize life sciences data types based on sensitivity levels and transfer requirements. Create policies that map security controls and bandwidth allocation rules to different data classifications.

 Design intelligent bandwidth allocation systems that adapt to network conditions and usage patterns. Implement automated scheduling for large data transfers during off-peak periods while maintaining required security controls.

 Configure compression and de-duplication mechanisms that operate before encryption to maximize transfer efficiency. Implement monitoring systems to verify that optimization doesn't impact data integrity or security requirements.

### Implementation steps
<a name="implementation-steps"></a>

1.  Implement comprehensive data classification with AWS Network Firewall for traffic categorization, Application Load Balancer for content-based routing, and AWS WAF rules for precise traffic identification.

1.  Deploy bandwidth management tools including AWS Transit Gateway for centralized traffic control, VPC traffic mirroring for detailed analysis, and AWS Global Accelerator for optimized routing across networks.

1.  Establish multi-layered security with AWS Shield for DDoS protection, AWS WAF rate-based rules to block abuse, and security groups for granular traffic control between resources.

1.  Configure detailed monitoring and analytics using Amazon CloudWatch for bandwidth metrics, VPC Flow Logs for traffic pattern analysis, and Amazon GuardDuty for automated threat detection and response.

1.  Document traffic management policies with classification criteria, bandwidth allocation priorities, and security enforcement points.

1.  Implement automated alerting for unusual traffic patterns, bandwidth threshold violations, and potential security issues.

1.  Conduct regular traffic analysis to optimize bandwidth allocation and security rules based on evolving usage patterns.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
