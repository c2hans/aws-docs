---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/sec_network_protection_inspection.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC05-BP04 Implement inspection and protection
<a name="sec_network_protection_inspection"></a>

 Inspect and filter your traffic at each layer. You can inspect your VPC configurations for potential unintended access using [VPC Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-vaa.html). You can specify your network access requirements and identify potential network paths that do not meet them. For components transacting over HTTP-based protocols, a web application firewall can help protect from common attacks. [AWS WAF](https://aws.amazon.com/waf) is a web application firewall that lets you monitor and block HTTP(s) requests that match your configurable rules that are forwarded to an Amazon API Gateway API, Amazon CloudFront, or an Application Load Balancer. To get started with AWS WAF, you can use [AWS Managed Rules](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html#getting-started-wizard-add-rule-group) in combination with your own, or use existing [partner integrations](https://aws.amazon.com/waf/partners/).

 For managing AWS WAF, AWS Shield Advanced protections, and Amazon VPC security groups across AWS Organizations, you can use AWS Firewall Manager. It allows you to centrally configure and manage firewall rules across your accounts and applications, making it easier to scale enforcement of common rules. It also allows you to rapidly respond to attacks, using [AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-responding.html), or [solutions](https://aws.amazon.com/solutions/aws-waf-security-automations/) that can automatically block unwanted requests to your web applications. Firewall Manager also works with [AWS Network Firewall](https://aws.amazon.com/network-firewall/). AWS Network Firewall is a managed service that uses a rules engine to give you fine-grained control over both stateful and stateless network traffic. It supports the [Suricata compatible](https://docs.aws.amazon.com/network-firewall/latest/developerguide/stateful-rule-groups-ips.html) open source intrusion prevention system (IPS) specifications for rules to help protect your workload.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Configure Amazon GuardDuty: GuardDuty is a threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts and workloads. Use GuardDuty and configure automated alerts.
  +  [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
  +  [Lab: Automated Deployment of Detective Controls](https://wellarchitectedlabs.com/Security/200_Automated_Deployment_of_Detective_Controls/README.html)
+  Configure virtual private cloud (VPC) Flow Logs: VPC Flow Logs is a feature that allows you to capture information about the IP traffic going to and from network interfaces in your VPC. Flow log data can be published to Amazon CloudWatch Logs and Amazon Simple Storage Service (Amazon S3). After you've created a flow log, you can retrieve and view its data in the chosen destination.
+  Consider VPC traffic mirroring: Traffic mirroring is an Amazon VPC feature that you can use to copy network traffic from an elastic network interface of Amazon Elastic Compute Cloud (Amazon EC2) instances and then send it to out-of-band security and monitoring appliances for content inspection, threat monitoring, and troubleshooting.
  +  [VPC traffic mirroring](https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-section.html)
+  [Amazon Inspector](https://aws.amazon.com/inspector)
+  [Amazon VPC Security](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Security.html)
+  [Getting started with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html)

 **Related videos:**
+  [AWS Transit Gateway reference architectures for many VPCs](https://youtu.be/9Nikqn_02Oc)
+  [Application Acceleration and Protection with Amazon CloudFront, AWS WAF, and AWS Shield](https://youtu.be/0xlwLEccRe0)
