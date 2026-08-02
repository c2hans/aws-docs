---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-migrations-framework/cloud-operations.html
---

# Security and compliance cloud operations
<a name="cloud-operations"></a>

The final domain is *security and compliance cloud operations*. This is a continuous activity where you use the defined security and compliance operational runbooks to govern cloud operations. You also build a security cloud operating model to determine responsibilities for security and compliance in your organization.

## Security and compliance cloud operating model
<a name="cloud-operating-model"></a>

In this domain, you define a cloud operating model for security. Your cloud operating model should address the requirements you identified during the discovery workshops and later defined as runbooks. You can design the security and compliance cloud operating model in one of three ways:
+ **Centralized** – A more traditional model, where SecOps is responsible for identifying and remediating security events across the business. This can include reviewing general security posture findings for the business, such as patching and security configuration issues.
+ **Decentralized** – Responsibility for responding to and remediating security events across the business has been delegated to the application owners and individual business units, and there is no central operations function. Typically, there is still an overarching security governance function that defines policies and principles.
+ **Hybrid** – A mix of both approaches, where SecOps still has a level of responsibility and ownership for identifying and orchestrating the response to security events and the responsibility for remediation is owned by the application owners and individual business units.

It is important to select the right operating model based on your security and compliance requirements, organization maturity, and constraints. The security and compliance requirements and constraints were identified during the discovery workshop. Organization maturity, on the other hand, defines the level of operational security practices. The following is an example of a maturity range:
+ **Low** – Logging is local, and some or sporadic actions are taken.
+ **Intermediate **– Logs from different sources are correlated, and automated alerting is established.
+ **High** – Detailed playbooks exist and contain details about standardized process responses.  Operationally and technically, the majority of the alert responses are automated.

To further understand the security and compliance cloud operating model and assist in the selection of an appropriate design, see [Considerations for security operations in the cloud](https://aws.amazon.com/blogs/security/considerations-for-security-operations-in-the-cloud/) (AWS blog post). In scenarios where there are no predefined requirements, we recommend that you set up a Security Operations Center (SOC) as part of the cloud operating model. This is typically a centralized operating model practice. With this approach, you can direct events from multiple sources to a centralized team, which can then trigger actions and responses. This standardizes security governance through cloud operations. AWS and AWS Partners have the capability can help you build an SOC and define and implement Security Orchestration, Automation, and Response (SOAR). AWS and AWS Partners use professional services consultations, defined templates, AWS services, and third-party tools from AWS Partners.

## Ongoing security operations
<a name="ongoing-security-operations"></a>

In this domain, perform the following tasks on an ongoing basis by using your defined security and compliance operations runbooks:
+ **Security and compliance monitoring** – Perform centralized monitoring of security events and threats by using your defined AWS services, tools, metrics, criteria, and frequency. The operations team or the SOC administer this continuous monitoring, depending on your organization's structure. Security monitoring involves analysis and correlation of large amounts of logs and data. Log data comes from endpoints, networks, AWS services, infrastructure, and applications and is stored in a centralized repository, such as [Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) or a security information and event management (SIEM) system. It is important to configure alerts so that you can manually or automatically respond to events in a timely fashion.
+ **Incidents management** – Define your baseline security posture. When a deviation from a preset baseline occurs, either through misconfiguration or external factors, record an incident. Make sure that an assigned team responds to these incidents. The foundation of a successful incident response program in the cloud is to have people, process and tooling integrated into each stage of the incident response program (preparation, operations, and post-incident activity). Education, training, and experience are vital to a successful cloud incident response program. Ideally, these are implemented well in advance of having to handle a possible security incident. For more information about setting up an effective security incident response program, see the [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/introduction.html).
+ **Security validation** – Security validation involves running vulnerability assessment, penetration testing, and chaos security simulated event testing. Security validation should continue to be run periodically, especially for the following scenarios:
  + Software updates and releases
  + Newly identified threats, such as malware, viruses, or worms
  + Internal and external audit requirements
  + Security breaches

  It is important to document the security validation process and highlight the people, process, schedule, tooling, and templates for data collection and reporting. This standardizes security validations. Continue to comply to the [AWS customer support policy for penetration testing](https://aws.amazon.com/security/penetration-testing/) when running security validations in the cloud.
+ **Internal and external audits** – Conduct internal and external audits to validate that security and compliance configurations meet regulatory or internal policy requirements. Perform audits periodically based on a predefined schedule. Internal audits are normally conducted by an internal security and risk team. External audits are conducted by relevant agencies or standard officials. You can use AWS services, such as [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html) and [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html), to facilitate the audit process. These services can provide relevant evidence rfor security IT audit reports. They can also simplify risk and compliance management with regulatory and industry standards by automating evidence collection. This helps you assess whether the policies, procedures, and activities known as *controls *are operating effectively. It is also important to align audit requirements with your managed service partners to ensure compliance.

**Security architecture review** – Complete a periodic review and update of your AWS architecture from a security and compliance standpoint. Review the architecture on a quarterly basis or when there are architecture changes. AWS continues to release updates and improvements to the security and compliance features and services. Use the [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html) and AWS Well Architected Tool to facilitate these architecture reviews. It is important to document your security and compliance implementation and recommended changes after the review process.

## AWS security services for operations
<a name="aws-security-services"></a>

You share responsibility with AWS for security and compliance in the AWS Cloud. This relationship is described in detail in the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/). While AWS manages security *of* the cloud, you are responsible for security *in* the cloud. You are responsible for protecting your own content, infrastructure, applications, systems, and networks, no differently than you would for an on-premises data center. Your responsibilities for security and compliance in the AWS Cloud vary depending on the services you use, how you integrate those services into your IT environment, and applicable laws and regulations.

An advantage of the AWS Cloud is that it allows you to scale and innovate by using AWS best practices and security and compliance services. This helps you maintain a secure environment while paying only for the services you use. You also have access to the same AWS security and compliance services that highly secured enterprise organizations use to secure their cloud environments.

Building a cloud architecture on a sound and secure foundation is the first and the best step to ensure cloud security and compliance. However, your AWS resources are only as secure as you configure them to be. An effective security and compliance posture is achieved only through continuous, strict adherence at an operational level. Security and compliance operations can be broadly grouped into five categories:
+ Data protection
+ Identity access and management
+ Network and application protection
+ Threat detection and continuous monitoring
+ Compliance and data privacy

AWS security and compliance services map to these categories to help you meet a comprehensive set of requirements. Grouped into these categories, the following are the AWS security and compliance core services and their capabilities. These services can help you build and enforce cloud security governance.

### Data protection
<a name="data-protection.9e7abf4e-563c-5fa3-a551-97f9226849f3"></a>

AWS provides the following services that can help you protect your data, accounts, and workloads from unauthorized access:
+ [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) – Provision, manage, and deploy SSL/TLS certificates for use with AWS services.
+ [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html) – Manage your hardware security modules (HSMs) in the AWS Cloud.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) – Create and control the keys used to encrypt your data.
+ [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) – Discover, classify, and help protect sensitive data with machine learning-powered security features.
+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) – Rotate, manage, and retrieve database credentials, API keys, and other secrets through their lifecycle.

### Identity and access management
<a name="identity-and-access-management.19acbcec-9591-5f71-af84-8594e4f78abd"></a>

The following AWS identity services help you to securely manage identities, resources, and permissions at scale:
+ [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) – Add user sign-up, sign-in, and access control to your web and mobile applications.
+ [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) – Use managed Microsoft Active Directory in the AWS Cloud.
+ [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) – Centrally manage single sign-on (SSO) access to multiple AWS accounts and business applications.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) – Securely control access to AWS services and resources.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) – Implement policy-based management for multiple AWS accounts.
+ [AWS Resource Access Manager (AWS RAM)](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) – Share AWS resources across your accounts.

### Network and application protection
<a name="network-and-application-protection.100a2d43-01a2-534d-874c-ff6f4f0a19f5"></a>

This category of services helps you to enforce fine-grained security policy at network control points across your organization. The following AWS services help you inspect and filter traffic to help prevent unauthorized resource access at the host-level, network-level, and application-level boundaries:
+ [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) – Configure and manage AWS WAF rules across AWS accounts and applications from a central location.
+ [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) – Deploy essential network protections for your virtual private clouds (VPCs).
+ [Amazon Route 53 Resolver DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall.html) – Help protect your outbound DNS requests from your VPCs.
+ [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) – Safeguard your web applications with managed DDoS protection.
+ [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) – Configure and manage Amazon Elastic Compute Cloud (Amazon EC2) and on-premises systems to apply OS patches, create secure system images, and configure operating systems.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) – Provision a logically isolated section of AWS where you can launch AWS resources in a virtual network that you define.
+ [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) – Help protect your web applications from common web exploits.

### Threat detection and continuous monitoring
<a name="threat-detection-and-continuous-monitoring.677d3a27-8a52-5712-91a6-7dc6745dee7f"></a>

The following AWS monitoring and detection services help you identify potential security incidents within your AWS environment:
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) – Track user activity and API usage to enable governance and operational and risk auditing of your AWS account.
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) – Record and evaluate the configurations of your AWS resources to help you audit compliance, track resource changes, and analyze resource security.
+ [AWS Config rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html) – Create rules that automatically act in response to changes in your environment, such as isolating resources, enriching events with additional data, or restoring a configuration to a known-good state.
+ [Amazon Detective](https://docs.aws.amazon.com/detective/latest/adminguide/what-is-detective.html) – Analyze and visualize security data to rapidly get to the root cause of potential security issues.
+ [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) – Help protect your AWS accounts and workloads with intelligent threat detection and continuous monitoring.
+ [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) – Automate security assessments to help improve the security and compliance of your applications that are deployed on AWS.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – Run code without provisioning or managing servers so that you can scale your programmed, automated response to incidents.
+ [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) – View and manage security alerts and automate compliance checks from a central location.

### Compliance and data privacy
<a name="compliance-and-data-privacy.5dd9919e-c882-500f-879e-63060f8d0542"></a>

The following AWS services provide a comprehensive view of your compliance status. They continuously monitor your environment by using automated compliance checks that are based on AWS best practices and industry standards:
+ [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html) – Get on-demand access to AWS security and compliance reports and select online agreements.
+ [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html) – Continuously audit your AWS usage to simplify how you manage risk and maintain compliance with regulations and industry standards.
