---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_network_protection_auto_protect.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC05-BP03 Automate network protection
<a name="sec_network_protection_auto_protect"></a>

 Automate protection mechanisms to provide a self-defending network based on threat intelligence and anomaly detection. For example, intrusion detection and prevention tools that can adapt to current threats and reduce their impact. A web application firewall is an example of where you can automate network protection, for example, by using the AWS WAF Security Automations solution ([https://github.com/awslabs/aws-waf-security-automations](https://github.com/awslabs/aws-waf-security-automations)) to automatically block requests originating from IP addresses associated with known threat actors.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Automate protection for web-based traffic: AWS offers a solution that uses AWS CloudFormation to automatically deploy a set of AWS WAF rules designed to filter common web-based attacks. Users can select from preconfigured protective features that define the rules included in an AWS WAF web access control list (web ACL).
  +  [AWS WAF security automations](https://aws.amazon.com/solutions/aws-waf-security-automations/)
+  Consider AWS Partner solutions: AWS Partners offer hundreds of industry-leading products that are equivalent, identical to, or integrate with existing controls in your on-premises environments. These products complement the existing AWS services to enable you to deploy a comprehensive security architecture and a more seamless experience across your cloud and on-premises environments.
  +  [Infrastructure security](https://aws.amazon.com/security/partner-solutions/#infrastructure_security)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-section.html)
+  [Amazon Inspector](https://aws.amazon.com/inspector)
+ [Amazon VPC Security](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Security.html)
+  [Getting started with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html)

 **Related videos:**
+  [AWS Transit Gateway reference architectures for many VPCs](https://youtu.be/9Nikqn_02Oc)
+  [Application Acceleration and Protection with Amazon CloudFront, AWS WAF, and AWS Shield](https://youtu.be/0xlwLEccRe0)

 **Related examples:**
+  [Lab: Automated Deployment of VPC](https://www.wellarchitectedlabs.com/Security/200_Automated_Deployment_of_VPC/README.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
