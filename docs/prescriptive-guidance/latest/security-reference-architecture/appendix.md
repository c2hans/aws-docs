---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/appendix.html
---

# Appendix: AWS security, identity, and compliance services
<a name="appendix"></a>

For an introduction or a refresher, see [Security, identity, and compliance on AWS](https://aws.amazon.com/products/security/) on the AWS website for a list of the AWS services that help you secure your workloads and applications in the cloud. These services are grouped into five categories: data protection, identity & access management, network & application protection, threat detection & continuous monitoring, and compliance & data privacy.

**Data protection** – AWS provides services that help you protect your data, accounts, and workloads from unauthorized access.
+ [Amazon Macie](https://aws.amazon.com/macie/) – Discover, classify, and protect sensitive data with machine learning-powered security features.
+ [AWS KMS](https://aws.amazon.com/kms/) – Create and control the keys used to encrypt your data.
+ [AWS CloudHSM](https://aws.amazon.com/cloudhsm/)– Manage your hardware security modules (HSMs) in the AWS Cloud.
+ [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) – Provision, manage, and deploy SSL/TLS certificates for use with AWS services.
+ [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) – Rotate, manage, and retrieve database credentials, API keys, and other secrets through their lifecycle.
+ AWS Private CA - Create private certificate authority (CA) hierarchies, including root and subordinate CAs.

**Identity & access management** – AWS identity services enable you to securely manage identities, resources, and permissions at scale.
+ [IAM](https://aws.amazon.com/iam/) – Securely control access to AWS services and resources.
+ IAM Access Analyzer – Use [provable security](https://aws.amazon.com/security/provable-security/) to implement least privilege by providing capabilities to set, verify, and refine permissions.
+ [IAM Identity Center](https://aws.amazon.com/single-sign-on/) – Centrally manage SSO access to multiple AWS accounts and business applications.
+ [Amazon Cognito](https://aws.amazon.com/cognito/) – Add user sign-up, sign-in, and access control to your web and mobile applications.
+ [AWS Directory Service](https://aws.amazon.com/directoryservice/) – Use managed Microsoft Active Directory in the AWS Cloud.
+ [AWS RAM](https://aws.amazon.com/ram/) – Share AWS resources simply and securely.
+ [AWS Organizations](https://aws.amazon.com/organizations/) – Implement policy-based management for multiple AWS accounts.
+ [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html) – Manage scalable, fine-grained permissions and authorization in your custom applications.

**Network & application protection** – These categories of services enable you to enforce fine-grained security policy at network control points across your organization. AWS services help you inspect and filter traffic to help prevent unauthorized resource access at the host-level, network-level, and application-level boundaries.
+ [AWS Shield](https://aws.amazon.com/shield/) – Safeguard your web applications that run on AWS with managed DDoS protection.
+ [AWS WAF](https://aws.amazon.com/waf/) – Protect your web applications from common web exploits, and ensure availability and security.
+ [AWS Firewall Manager](https://aws.amazon.com/firewall-manager/) – Configure and manage AWS WAF rules across AWS accounts and applications from a central location.
+ [AWS Systems Manager](https://aws.amazon.com/systems-manager/) – Configure and manage Amazon EC2 and on-premises systems to apply OS patches, create secure system images, and configure secure operating systems.
+ [Amazon VPC](https://aws.amazon.com/vpc/) – Provision a logically isolated section of AWS where you can launch AWS resources in a virtual network that you define.
+ [AWS Network Firewall](https://aws.amazon.com/network-firewall/) – Deploy essential network protections for your VPCs.
+ [Amazon Route 53 DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html) – Protect your outbound DNS requests from your VPCs.** **
+ [AWS Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/what-is-verified-access.html) – Provide secure access to your applications without requiring virtual private networks (VPNs).
+ [Amazon VPC Lattice](https://aws.amazon.com/vpc/lattice/) – Simplify service-to-service connectivity, security, and monitoring.
+ AWS Transit Gateway - Connect VPCs, AWS accounts, and on-premises networks to a single gateway
+ Network Access Analyzer - Identify unintended network access to your resources on AWS.

**Threat detection & continuous monitoring** – AWS monitoring and detection services provide guidance to help identify potential security incidents within your AWS environment.
+ [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/cspm/) – View and manage security alerts and automate compliance checks from a central location.
+ [AWS Security Hub](https://aws.amazon.com/security-hub/) – Correlate and enrich security findings to prioritize critical security issues across your accounts and AWS Regions.
+ [Amazon GuardDuty](https://aws.amazon.com/guardduty/) – Protect your AWS accounts and workloads with intelligent threat detection and continuous monitoring.
+ [Amazon Inspector](https://aws.amazon.com/inspector/) – Automate security assessments to help improve the security and compliance of your applications that are deployed on AWS.
+ [AWS Config](https://aws.amazon.com/config/) – Record and evaluate the configurations of your AWS resources to enable compliance auditing, resource change tracking, and security analysis.
+ [AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) – Create rules that automatically take action in response to changes in your environment, such as isolating resources, enriching events with additional data, or restoring configuration to a known good state.
+ [AWS Security Incident Response](https://aws.amazon.com/security-incident-response/) – Automate security incident response, investigation, and remediation with pre-built playbooks and workflows.
+ [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) – Track user activity and API usage to enable governance and operational and risk auditing of your AWS account.
+ [Amazon Detective](https://aws.amazon.com/detective/) – Analyze and visualize security data to rapidly get to the root cause of potential security issues.
+ [AWS Lambda](https://aws.amazon.com/lambda/) – Run code without provisioning or managing servers so you can scale your programmed, automated response to incidents.

**Compliance & data privacy** – AWS gives you a comprehensive view of your compliance status and continuously monitors your environment by using automated compliance checks based on the AWS best practices and industry standards your business follows.** **
+ [AWS Artifact](https://aws.amazon.com/artifact/) – Use a no-cost, self-service portal to get on-demand access to AWS security and compliance reports and select online agreements.
+ [AWS Audit Manager](https://aws.amazon.com/audit-manager/) – Continuously audit your AWS usage to simplify how you assess risk and compliance with regulations and industry standards.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
