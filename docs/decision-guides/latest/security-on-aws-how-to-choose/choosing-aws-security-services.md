---
source_url: https://docs.aws.amazon.com/decision-guides/latest/security-on-aws-how-to-choose/choosing-aws-security-services.html
---

# Choosing AWS security, identity, and governance services
<a name="choosing-aws-security-services"></a>

**Taking the first step**

<table>
<tbody>
  <tr><td>**Time to read**</td><td colspan="2">27 minutes</td></tr>
  <tr><td>**Purpose**</td><td colspan="2">Help you determine which AWS security, identity, and governance services are the best fit for your organization.</td></tr>
  <tr><td>**Last updated**</td><td colspan="2">December 30, 2024</td></tr>
  <tr><td>**Services covered**</td><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/decision-guides/latest/security-on-aws-how-to-choose/choosing-aws-security-services.html) </td><td> [See the AWS documentation website for more details](http://docs.aws.amazon.com/decision-guides/latest/security-on-aws-how-to-choose/choosing-aws-security-services.html) </td></tr>
</tbody>
</table>

## Introduction
<a name="intro"></a>

Security, identity, and governance in the cloud are important components for you in achieving and maintaining integrity and safety for your data and services. This is especially relevant as more businesses migrate to cloud providers such as Amazon Web Services (AWS).

 This guide helps you select the AWS security, identity, and governance services and tools that are the best fit for your needs and your organization.

 First, let's explore what we mean by security, identity, and governance:
+  [Cloud security](https://aws.amazon.com/security/) refers to using measures and practices to protect digital assets from threats. This includes both the physical security of data centers and cybersecurity measures to guard against online threats. AWS prioritizes security through encrypted data storage, network security, and continuous monitoring of potential threats.
+  [Identity](https://aws.amazon.com/identity/) services help you securely manage identities, resources, and permissions in a scalable way. AWS provides identity services designed for workforce and customer-facing applications, and for managing access to your workloads and applications.
+  [Cloud governance](https://aws.amazon.com/cloudops/cloud-governance/) is a set of rules, processes, and reports that guide your organization to follow best practices. You can establish cloud governance across your AWS resources, use built-in best practices and standards, and automate compliance and auditing processes. [Compliance](https://aws.amazon.com/compliance/) in the cloud refers to adhering to laws and regulations governing data protection and privacy. [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) provides information about the certifications, regulations, and frameworks that AWS aligns with.

[![AWS Videos](http://img.youtube.com/vi/T4svAhNLNfc/0.jpg)](http://www.youtube.com/watch?v=T4svAhNLNfc)

## Understand AWS security, identity, and governance services
<a name="understand"></a>

### Security and compliance are shared responsibilities
<a name="security-and-compliance-are-shared-responsibilities"></a>

Before choosing your AWS security, identity, and governance services, it's important for you to understand that security and compliance are [shared responsibilities](https://aws.amazon.com/compliance/shared-responsibility-model/) between you and AWS.

The nature of this shared responsibility helps relieve your operational burden, and it provides you with flexibility and control over your deployment. This differentiation of responsibility is commonly referred to as *security "of" the cloud* and *security "in" the cloud*.

With an understanding of this model, you can understand the range of options available to you, and how the applicable AWS services fit together.

### You can combine AWS tools and services to help safeguard your workloads
<a name="you-can-combine-aws-tools-and-services-to-help-safeguard-your-workloads"></a>

![The five domains across security, identity, and governance include identity and access management, network and app protection, data protection, detection and response, and governance and compliance.](http://docs.aws.amazon.com/decision-guides/latest/security-on-aws-how-to-choose/images/security-identity-governance-services.png)

As shown in the previous diagram, AWS offers tools and services across five domains to help you achieve and maintain robust security, identity management, and governance in the cloud. You can use AWS services across these five domains to help you do the following:
+ Form a multilayered approach to safeguarding your data and environments
+ Fortify your cloud infrastructure against evolving threats
+ Adhere to strict regulatory standards

 To learn more about AWS security, including security documentation for AWS services, see [AWS Security Documentation](https://docs.aws.amazon.com/security/).

 In the following sections, we examine each domain further.

#### Understand AWS identity and access management services
<a name="identity-and-access-management-2"></a>

At the center of AWS security is the principle of least privilege: individuals and services have only the access that they need. [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) is the recommended AWS service for managing user access to AWS resources. You can use this service to manage access to your accounts and permissions within those accounts, including identities from external identity providers.

The following table summarizes the identity and access management offerings discussed in this guide:

------
#### [ AWS IAM Identity Center ]

 [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) helps you connect your source of identities, or create users. You can centrally manage workforce access to multiple AWS accounts and applications.

------
#### [ Amazon Cognito ]

 [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) provides an identity tool for web and mobile apps to authenticate and authorize users from the built-in user directory, your enterprise directory, and consumer identity providers.

------
#### [ AWS RAM ]

 [AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) helps you securely share your resources across AWS accounts, within your organization, and with IAM roles and users.

------
#### [ IAM ]

 [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) enables secure, fine-grained control over access to AWS workload resources.

------

#### Understand AWS data protection services
<a name="data-protection-2"></a>

Data protection is vital in the cloud, and AWS provides services that help you protect your data, accounts, and workloads. For example, encrypting your data both in transit and at rest helps protect it from exposure. With [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) (AWS KMS) and [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html) you can create and control the cryptographic keys that you use to protect your data.

The following table summarizes the data protection offerings discussed in this guide:

------
#### [ Amazon Macie ]

 [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) discovers sensitive data by using machine learning and pattern matching, and enables automated protection against associated risks.

------
#### [ AWS KMS ]

 [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) creates and controls the cryptographic keys that you use to protect your data.

------
#### [ AWS CloudHSM ]

 [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html) provides highly available, cloud-based hardware security modules (HSMs).

------
#### [ AWS Certificate Manager ]

 [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) handles the complexity of creating, storing, and renewing public and private SSL/TLS X.509 certificates and keys.

------
#### [ AWS Private CA ]

 [AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) helps you create private certificate authority hierarchies, including root and subordinate certificate authorities (CAs).

------
#### [ AWS Secrets Manager ]

 [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) helps you manage, retrieve, and rotate database credentials, application credentials, OAuth tokens, API keys, and other secrets.

------
#### [ AWS Payment Cryptography ]

 [AWS Payment Cryptography](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/what-is.html) provides access to cryptographic functions and key management used in payment processing in accordance with payment card industry (PCI) standards.

------

#### Understand AWS network and application protection services
<a name="network-and-app-protection-2"></a>

AWS offers several services to protect your networks and applications. [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) provides you with protection against Distributed Denial of Service (DDoS) attacks, and [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) helps you protect web applications from common web exploitation attacks.

The following table summarizes the network and application protection offerings discussed in this guide:

------
#### [ AWS Firewall Manager ]

 [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) simplifies your administration and maintenance tasks across multiple accounts and resources for protection.

------
#### [ AWS Network Firewall ]

 [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html) provides a stateful, managed network firewall and intrusion detection and prevention service with your VPC.

------
#### [ AWS Shield ]

 [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) provides protections against DDoS attacks for AWS resources at the network, transport, and application layers.

------
#### [ AWS WAF ]

 [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) provides a web application firewall so you can monitor the HTTP(S) requests that are forwarded to your protected web application resources.

------

#### Understand AWS detection and response services
<a name="detection-and-response-2"></a>

AWS provides tools to help you streamline security operations across your AWS environment, including [multi-account environments](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html). For example, you can use [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) for intelligent threat detection, and you can use [Amazon Detective](https://docs.aws.amazon.com/detective/latest/adminguide/what-is-detective.html) to identify and analyze security findings by collecting log data. [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) supports multiple security standards and provides an overview of security alerts and compliance status across AWS accounts. [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) tracks user activity and application programming interface (API) usage, which is crucial for understanding and responding to security events.

The following table summarizes the detection and response offerings discussed in this guide:

------
#### [ AWS Config ]

 [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) provides a detailed view of the configuration of AWS resources in your AWS account.

------
#### [ AWS CloudTrail ]

 [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) records actions taken by a user, role, or AWS service.

------
#### [ AWS Security Hub CSPM ]

 [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) provides a comprehensive view of your security state in AWS.

------
#### [ Amazon GuardDuty ]

 [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) continuously monitors your AWS accounts, workloads, runtime activity, and data for malicious activity.

------
#### [ Amazon Inspector ]

 [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) scans your AWS workloads for software vulnerabilities and unintended network exposure.

------
#### [ Amazon Security Lake ]

 [Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) automatically centralizes security data from AWS environments, SaaS providers, on-premises environments, cloud sources, and third-party sources into a data lake.

------
#### [ Amazon Detective ]

 [Amazon Detective](https://docs.aws.amazon.com/detective/latest/adminguide/what-is-detective.html) helps you analyze, investigate, and quickly identify the root cause of security findings or suspicious activities.

------
#### [ AWS Security Incident Response ]

 [AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/what-is.html)

Helps you quickly prepare for, respond to, and receive guidance to help recover from security incidents.

------

#### Understand AWS governance and compliance services
<a name="governance-and-compliance-2"></a>

AWS provides tools that help you adhere to your security, operational, compliance, and cost standards. For example, you can use [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) to set up and govern a multi-account environment with prescriptive controls. With [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html), you can set up policy-based management for multiple accounts within your organization.

AWS also gives you a comprehensive view of your compliance status and continuously monitors your environment by using automated compliance checks based on the AWS best practices and industry standards that your organization follows. For example, [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html) provides on-demand access to compliance reports, and [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html) automates evidence collection so that you can more easily assess whether your controls are operating effectively.

The following table summarizes the governance and compliance offerings discussed in this guide:

------
#### [ AWS Organizations ]

 [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.

------
#### [ AWS Control Tower ]

 [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) helps you set up and govern an AWS multi-account environment that's based on best practices.

------
#### [ AWS Artifact ]

 [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html) provides on-demand downloads of AWS security and compliance documents.

------
#### [ AWS Audit Manager ]

 [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html)

Helps you continuously audit your AWS usage to simplify how you assess risk and compliance.

------

## Consider AWS security, identity, and governance criteria
<a name="consider"></a>

Choosing the right security, identity, and governance services on AWS depends on your specific requirements and use cases. [Deciding to adopt an AWS security service](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-evaluating-security-service/introduction.html) provides a decision tree to help you decide if adopting AWS services for security, identity, and governance is suitable for your organization. In addition, here are some criteria to consider when making your decision about which services to use.

------
#### [ Security requirements and threat landscape ]

Conduct a comprehensive assessment of your organization's **specific vulnerabilities and threats**. This involves identifying the types of data that you handle, such as personal customer information, financial records, or proprietary business data. Understand the potential risks associated with each.

Assess your application and infrastructure **architecture**. Determine whether your applications are public-facing and what kind of web traffic they handle. This factors into your need for services such as AWS WAF to protect against web exploitation. For internal applications, consider the importance of internal threat detection and continuous monitoring with Amazon GuardDuty, which can identify unusual access patterns or unauthorized deployments.

Finally, consider the sophistication of your **existing security posture** and the expertise of your security team. If your team has limited resources, choosing services that offer more automation and integration can provide you with effective security enhancements, without overwhelming your team. Example services include AWS Shield for DDoS protection and AWS Security Hub CSPM for centralized security monitoring.

------
#### [ Compliance and regulatory requirements ]

Identify the **relevant laws and standards** for your industry or geographic region, such as [General Data Protection Regulation](https://aws.amazon.com/compliance/gdpr-center/) (GDPR), the [U.S. Health Insurance Portability and Accountability Act of 1996](https://aws.amazon.com/compliance/hipaa-compliance/) (HIPAA), or [Payment Card Industry Data Security Standard](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/) (PCI DSS).

AWS offers services such as AWS Config and AWS Artifact to help you manage compliance with various standards. With AWS Config, you can assess, audit, and evaluate the configurations of your AWS resources, making it easier for you to ensure compliance with internal policies and regulatory requirements. AWS Artifact provides on-demand access to AWS compliance documentation, aiding you with audits and compliance reporting.

Choosing services that align with your specific compliance needs can help your organization meet legal requirements and build a secure and trustworthy environment for your data. Explore [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) to learn more.

------
#### [ Scalability and flexibility ]

Consider how your organization will grow, and how fast. Choose AWS services that will help your security measures grow seamlessly with your infrastructure and adapt to evolving threats.

To help you **scale quickly**, AWS Control Tower orchestrates the capabilities of several other [AWS services](https://docs.aws.amazon.com/controltower/latest/userguide/integrated-services.html), including AWS Organizations and AWS IAM Identity Center, to build a landing zone in less than an hour. Control Tower sets up and manages resources on your behalf.

AWS also designs many services to **automatically scale** with an application's traffic and usage patterns, such as Amazon GuardDuty for threat detection and AWS WAF for protecting web applications. As your business scales up, these services scale with it, without requiring manual adjustments or causing bottlenecks.

In addition, it's critical that you can **customize your security controls** to match your business requirements and threat landscapes. Consider managing your accounts with AWS Organizations, so you can manage [40\+ services](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html)' resources across multiple accounts. This gives individual application teams the flexibility and visibility to manage security needs that are specific to their workload, while also giving them governance and visibility to centralized security teams.

Considering scalability and flexibility helps you ensure that your security posture is robust, responsive, and capable of supporting dynamic business environments.

------
#### [ Integration with existing systems ]

Consider security measures that enhance, rather than disrupt, your current operations. For example, consider the following:
+ Streamline your workflows by **aggregating** security data and alerts from AWS services and analyzing them alongside existing security information and event management (SIEM) systems.
+ Create a **unified view** of security threats and vulnerabilities across both AWS and on-premises environments.
+ Integrate AWS CloudTrail with existing log management solutions for **comprehensive monitoring** of user activities and API usage across your AWS infrastructure and existing applications.
+ Examine ways that you can optimize **resource utilization** and consistently apply security policies across environments. This helps you reduce the risk of gaps in security coverage.

------
#### [ Cost and budget considerations ]

Review the [pricing models](https://aws.amazon.com/pricing) for each service that you're considering. AWS often charges based on usage, such as the number of API calls, the volume of data processed, or the amount of data stored. For example, Amazon GuardDuty charges based on the amount of log data analyzed for threat detection, while AWS WAF bills are based on the number of rules deployed and the number of web requests received.

Estimate your expected usage to **forecast costs** accurately. Consider both current needs and potential growth or spikes in demand. For example, scalability is a key feature of AWS services, but it can also lead to increased costs if not managed carefully. Use the [AWS Pricing Calculator](https://calculator.aws/) to model different scenarios and assess their financial impact.

Evaluate the **total cost of ownership** (TCO), which includes both direct costs and indirect costs, such as the time and resources needed for management and maintenance. Opting for managed services can reduce operational overhead, but it might come at a higher price point.

Lastly, **prioritize** your security investments based on risk assessment. Not all security services will be equally critical to your infrastructure, so focus your budget on the areas that will have the most significant impact on reducing risk and ensuring compliance. Balancing cost-effectiveness with the level of security that you need is key to a successful AWS security strategy.

------
#### [ Organizational structure and access needs ]

Evaluate how your organization is structured and operates, and how your access needs might vary by team, project, or location. This factors in to how you manage and authenticate user identities, assign roles, and enforce access controls across your AWS environment. Implement [best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), such as the applying least-privilege permissions and requiring multi-factor authentication (MFA).

Most organizations need a **multi-account** environment. Review [best practices](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices.html) for this type of environment, and consider using AWS Organizations and AWS Control Tower to help you implement it.

Another aspect that you should consider is the management of **credentials and access keys**. Consider using IAM Identity Center for centralizing access management across multiple AWS accounts and business applications, which enhances both security and user convenience. To help you smoothly manage access across your organization's accounts, IAM Identity Center [integrates](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-sso.html) with AWS Organizations.

Additionally, evaluate how these identity and access management services **integrate** with your existing directory services. If you have an existing identity provider, you can integrate it with IAM Identity Center by using [SAML 2.0](https://docs.aws.amazon.com/singlesignon/latest/userguide/scim-profile-saml.html) or [OpenID Connect](https://docs.aws.amazon.com/singlesignon/latest/OIDCAPIReference/Welcome.html) (OIDC). IAM Identity Center also has support for [System for Cross-domain Identity Management](https://docs.aws.amazon.com/singlesignon/latest/userguide/scim-profile-saml.html) (SCIM) provisioning to help keep your directories synchronized. This helps you ensure a seamless and secure user experience while accessing AWS resources.

------

## Choose an AWS security, identity, and governance service
<a name="choose"></a>

Now that you know the criteria for evaluating your security options, you're ready to choose which AWS security services might be a good fit for your organizational requirements.

The following table highlights which services are optimized for which circumstances. Use the table to help determine the service that is the best fit for your organization and use case.

**Note**
1 Integrates with AWS Security Hub CSPM ([full list](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-internal-providers.html))
2 Integrates with Amazon GuardDuty ([full list](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_integrations.html))
3 Integrates with Amazon Security Lake ([full list](https://docs.aws.amazon.com/security-lake/latest/userguide/aws-integrations.html))

### Choose AWS identity and access management services
<a name="identity-and-access-management"></a>

Grant appropriate individuals the appropriate level of access to systems, applications, and data.

- **Use these services to help you securely manage and govern access for your customers, workforce, and workloads. **
  - ****What is it optimized for?**:** Helps you connect your source of identities, or create users. You can centrally manage workforce access to multiple AWS accounts and applications. / ****Security, identity, and governance services**:** [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
  - ****What is it optimized for?**:** Optimized for authenticating and authorizing users for web and mobile applications.  / ****Security, identity, and governance services**:** [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)
  - ****What is it optimized for?**:** Optimized for securely sharing resources within AWS.  / ****Security, identity, and governance services**:** [AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html)
  - ****What is it optimized for?**:** Enables secure, fine-grained control over access to AWS workload resources.  / ****Security, identity, and governance services**:** [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) 1

### Choose AWS data protection services
<a name="data-protection"></a>

Automate and simplify data protection and security tasks that range from key management and sensitive data discovery to credential management.

- **Use these services to help you achieve and maintain the confidentiality, integrity, and availability of sensitive data stored and processed within AWS environments. **
  - ****What is it optimized for?**:** Optimized for discovering sensitive data.  / ****Data protection services**:** [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) 1
  - ****What is it optimized for?**:** Optimized for cryptographic keys.  / ****Data protection services**:** [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
  - ****What is it optimized for?**:** Optimized for HSMs.  / ****Data protection services**:** [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html)
  - ****What is it optimized for?**:** Optimized for private SSL/TLS X.509 certificates and keys.   / ****Data protection services**:** [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html)
  - ****What is it optimized for?**:** Optimized for creating private certificate authority hierarchies.  / ****Data protection services**:** [AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html)
  - ****What is it optimized for?**:** Optimized for database credentials, application credentials, OAuth tokens, API keys, and other secrets.  / ****Data protection services**:** [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
  - ****What is it optimized for?**:** Optimized for providing access to cryptographic functions and key management used in payment processing in accordance with PCI standards.   / ****Data protection services**:** [AWS Payment Cryptography](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/what-is.html)

### Choose AWS network and application protection services
<a name="network-and-application-protection"></a>

Centrally protect your internet resources against common DDoS and application attacks.

- **Use these services to help you enforce detailed security policies at every network control point. **
  - ****What is it optimized for?**:** Optimized for centrally configuring and managing firewall rules.  / ****Network and application protection services**:** [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html) 1
  - ****What is it optimized for?**:** Optimized for providing a stateful, managed network firewall and intrusion detection and prevention service.  / ****Network and application protection services**:** [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)
  - ****What is it optimized for?**:** Optimized for protecting against DDoS attacks for AWS resources at the network, transport, and application layers.  / ****Network and application protection services**:** [AWS Shield](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html)
  - ****What is it optimized for?**:** Optimized for providing a web application firewall.  / ****Network and application protection services**:** [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)

### Choose AWS detection and response services
<a name="detection-and-response"></a>

Continuously identify and prioritize security risks, while integrating security best practices early.

- **Use these services to help you detect and respond to security risks [across your accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html), so you can protect your workloads at scale. **
  - ****What is it optimized for?**:** Optimized for automating security checks and centralizing security alerts with AWS and third-party integrations.  / ****Detection and response services**:** [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) 2, 3
  - ****What is it optimized for?**:** Optimized for assessing, auditing, and evaluating the configuration of your resources.  / ****Detection and response services**:** [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) 1
  - ****What is it optimized for?**:** Optimized for logging events from other AWS services as an audit trail.  / ****Detection and response services**:** [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
  - ****What is it optimized for?**:** Optimized for intelligent threat detection and detailed reporting.  / ****Detection and response services**:** [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) 1
  - ****What is it optimized for?**:** Optimized for vulnerability management.  / ****Detection and response services**:** [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) 1
  - ****What is it optimized for?**:** Optimized for centralizing security data.  / ****Detection and response services**:** [ Amazon Security Lake](https://docs.aws.amazon.com/security-lake/latest/userguide/what-is-security-lake.html) 1
  - ****What is it optimized for?**:** Optimized for aggregating and summarizing potential security issues.  / ****Detection and response services**:** [Amazon Detective](https://docs.aws.amazon.com/detective/latest/adminguide/what-is-detective.html)  1, 2, 3
  - ****What is it optimized for?**:** Optimized for helping you triage findings, escalate security events, and manage cases that require your immediate attention.  / ****Detection and response services**:** [AWS Security Incident Response](https://docs.aws.amazon.com/security-ir/latest/userguide/what-is.html)

### Choose AWS governance and compliance services
<a name="governance-and-compliance"></a>

Establish cloud governance across your resources, and automate your compliance and auditing processes.

- **Use these services to help you implement best practices and meet industry standards when using AWS. **
  - ****What is it optimized for?**:** Optimized for centrally managing multiple accounts and consolidated billing.  / ****Governance and compliance services**:** [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)
  - ****What is it optimized for?**:** Optimized for providing on-demand downloads of AWS security and compliance documents.  / ****Governance and compliance services**:** [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html)
  - ****What is it optimized for?**:** Optimized for auditing AWS usage.  / ****Governance and compliance services**:** [AWS Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/what-is.html) 1
  - ****What is it optimized for?**:** Optimized for setting up and governing an AWS multi-account environment.  / ****Governance and compliance services**:** [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)

## Use AWS security, identity, and governance services
<a name="use"></a>

You should now have a clear understanding of what each AWS security, identity, and governance service (and the supporting AWS tools and services) does, and which ones might be right for you.

To explore how to use and learn more about each of the available AWS security, identity, and governance services, we have provided a pathway to explore how each of the services works. The following sections provide links to in-depth documentation, hands-on tutorials, and resources to get you started.

### Use AWS identity and access management services
<a name="identity-and-access-management-1"></a>

The following tables show some useful identity and access management resources, organized by service, to help you get started.

------
#### [ AWS IAM Identity Center ]
+  **Enabling AWS IAM Identity Center**

  Enable IAM Identity Center and begin using it with your AWS Organizations.

   [Explore the guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/get-set-up-for-idc.html)
+  **Configure user access with the default IAM Identity Center directory**

  Use the default directory as your identity source and set up and test user access.

   [Get started with the tutorial](https://docs.aws.amazon.com/singlesignon/latest/userguide/quick-start-default-idc.html)
+  **Using Active Directory as an identity source**

  Complete the basic setup for using Active Directory as an IAM Identity Center identity source.

   [Get started with the tutorial](https://docs.aws.amazon.com/singlesignon/latest/userguide/gs-ad.html)
+  **Configure SAML and SCIM with Okta and IAM Identity Center**

  Set up a SAML connection with Okta and IAM Identity Center.

   [Get started with the tutorial](https://docs.aws.amazon.com/singlesignon/latest/userguide/gs-okta.html)

------
#### [ Amazon Cognito ]
+  **Getting started with Amazon Cognito**

  Learn about the most common Amazon Cognito tasks.

   [Explore the guide](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-getting-started.html)
+  **Tutorial: Creating a user pool**

  Create a user pool, which allows your users to sign in to your web or mobile app.

   [Get started with the tutorial](https://docs.aws.amazon.com/cognito/latest/developerguide/tutorial-create-user-pool.html)
+  **Tutorial: Creating an identity pool**

  Create an identity pool, which allows your users to obtain temporary AWS credentials to access AWS services.

   [Get started with the tutorial](https://docs.aws.amazon.com/cognito/latest/developerguide/identity-pools.html)
+  **Amazon Cognito workshop**

  Practice using Amazon Cognito to build an authentication solution for a hypothetical pet store.

   [Get started with the tutorial](https://www.cognitobuilders.training/)

------
#### [ AWS RAM ]
+  **Getting started with AWS RAM**

  Learn about AWS RAM terms and concepts.

   [Explore the guide](https://docs.aws.amazon.com/ram/latest/userguide/getting-started.html)
+  **Working with shared AWS resources**

  Share AWS resources that you own, and access AWS resources that are shared with you.

   [Explore the guide](https://docs.aws.amazon.com/ram/latest/userguide/working-with.html)
+  **Managing permissions in AWS RAM**

  Learn about the two types of managed permissions: AWS managed permissions and customer managed permissions.

   [Explore the guide](https://docs.aws.amazon.com/ram/latest/userguide/security-ram-permissions.html)
+  **Configure detailed access to your resources that are shared using AWS RAM**

  Use customer managed permissions to customize your resource access and achieve the best practice of least privilege.

   [Read the blog](https://aws.amazon.com/blogs/security/configure-fine-grained-access-to-your-resources-shared-using-aws-resource-access-manager/)

------
#### [ IAM ]
+  **Getting started with IAM**

  Create IAM roles, users, and policies using the AWS Management Console.

   [Get started with the tutorial](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started.html)
+  **Delegate access across AWS accounts using roles**

  Use a role to delegate access to resources in different AWS accounts that you own called **Production** and **Development**.

   [Get started with the tutorial](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html)
+  **Create a customer managed policy**

  Use the AWS Management Console to create a [customer managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) and then attach that policy to an IAM user in your AWS account.

   [Get started with the tutorial](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_managed-policies.html)
+  **Define permissions to access AWS resources based on tags**

  Create and test a policy that allows IAM roles with principal tags to access resources with matching tags.

   [Get started with the tutorial](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html)
+  **Security best practices in IAM**

  Help secure your AWS resources by using IAM best practices.

   [Explore the guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

------

### Use AWS data protection services
<a name="data-protection-1"></a>

The following section provides you with links to detailed resources that describe AWS data protection.

------
#### [ Macie ]
+  **Getting started with Amazon Macie**

  Enable Macie for your AWS account, assess your Amazon S3 security posture, and configure key settings and resources for discovering and reporting sensitive data in your S3 buckets.

   [Explore the guide](https://docs.aws.amazon.com/macie/latest/user/getting-started.html)
+  **Monitoring data security and privacy with Amazon Macie**

  Use Amazon Macie to monitor Amazon S3 data security and assess your security posture.

   [Explore the guide](https://docs.aws.amazon.com/macie/latest/user/monitoring-s3.html)
+  **Analyzing Amazon Macie findings**

  Review, analyze, and manage Amazon Macie findings.

   [Explore the guide](https://docs.aws.amazon.com/macie/latest/user/findings.html)
+  **Retrieving sensitive data samples with Amazon Macie findings**

  Use Amazon Macie to retrieve and reveal samples of sensitive data that are reported by individual findings.

   [Explore the guide](https://docs.aws.amazon.com/macie/latest/user/findings-retrieve-sd.html)
+  **Discovering sensitive data with Amazon Macie**

  Automate the discovery, logging, and reporting of sensitive data in your Amazon S3 data estate.

   [Explore the guide](https://docs.aws.amazon.com/macie/latest/user/data-classification.html)

------
#### [ AWS KMS ]
+  **Getting started with AWS KMS**

  Manage symmetric encryption KMS keys, from creation to deletion.

   [Explore the guide](https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html)
+  **Special-purpose keys**

  Learn about the different types of keys that AWS KMS supports, in addition to symmetric encryption KMS keys.

   [Explore the guide](https://docs.aws.amazon.com/kms/latest/developerguide/key-types.html)
+  **Scaling your encryption at rest capabilities with AWS KMS**

  Learn about the encryption at rest options available within AWS.

   [Explore the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/05f16f1a-0bbf-45a7-a304-4fcd7fca3d1f/en-US)

------
#### [ AWS CloudHSM ]
+  **Getting started with AWS CloudHSM**

  Create, initialize, and activate an AWS CloudHSM cluster.

   [Explore the guide](https://docs.aws.amazon.com/cloudhsm/latest/userguide/getting-started.html)
+  **Managing AWS CloudHSM clusters**

  Connect to your AWS CloudHSM cluster and the various administrative tasks in managing your cluster.

   [Explore the guide](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-clusters.html)
+  **Managing HSM users and keys in AWS CloudHSM**

  Create users and keys on the HSMs in your cluster.

   [Explore the guide](https://docs.aws.amazon.com/cloudhsm/latest/userguide/manage-hsm-users-and-keys.html)
+  **Automate the deployment of an NGINX web service using Amazon ECS with TLS offload in CloudHSM**

  Use AWS CloudHSM to store your private keys for your websites that are hosted in the cloud.

   [Read the blog](https://aws.amazon.com/blogs/security/automate-the-deployment-of-an-nginx-web-service-using-amazon-ecs-with-tls-offload-in-cloudhsm/)

------
#### [ AWS Certificate Manager ]
+  **Requesting a public certificate**

  Use the AWS Certificate Manager (ACM) console or AWS CLI to request a public ACM certificate.

   [Explore the guide](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html)
+  **Best practices for AWS Certificate Manager**

  Learn best practices based on real-world experience from current ACM customers.

   [Explore the guide](https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html)
+  **How to use AWS Certificate Manager to enforce certificate issuance controls**

  Use IAM condition keys to ensure that your users are issuing or requesting TLS certificates in accordance with your organization's guidelines.

   [Read the blog](https://aws.amazon.com/blogs/security/how-to-use-aws-certificate-manager-to-enforce-certificate-issuance-controls/)

------
#### [ AWS Private CA ]
+  **Planning your AWS Private CA deployment**

  Prepare AWS Private CA for use before you create a private certificate authority.

   [Explore the guide](https://docs.aws.amazon.com/privateca/latest/userguide/PcaPlanning.html)
+  **AWS Private CA administration**

  Create an entirely AWS hosted hierarchy of root and subordinate certificate authorities for internal use by your organization.

   [Explore the guide](https://docs.aws.amazon.com/privateca/latest/userguide/creating-managing.html)
+  **Certificate administration**

  Perform basic certificate administration tasks with AWS Private CA, such as issuing, retrieving, and listing private certificates.

   [Explore the guide](https://docs.aws.amazon.com/privateca/latest/userguide/PcaUsing.html)
+  **AWS Private CA workshop**

  Develop hands-on experience with various use cases of private certificate authorities.

   [Explore the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/1d889b6d-52c9-49be-95a0-5e5e97c37f81/en-US)
+  **How to simplify certificate provisioning in Active Directory with AWS Private CA**

  Use AWS Private CA to more easily provision certificates for users and machines within your Microsoft Active Directory environment.

   [Read the blog](https://aws.amazon.com/blogs/modernizing-with-aws/simplify-certificate-provisioning-in-ad-with-aws-private-ca/)
+  **How to enforce DNS name constraints in AWS Private CA**

   Apply DNS name constraints to a subordinate CA by using the AWS Private CA service.

   [Read the blog](https://aws.amazon.com/blogs/security/how-to-enforce-dns-name-constraints-in-aws-private-ca/)

------
#### [ AWS Secrets Manager ]
+  **AWS Secrets Manager concepts**

  Perform basic certificate administration tasks with AWS Private CA, such as issuing, retrieving, and listing private certificates.

   [Explore the guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html)
+  **Set up alternating users rotation for AWS Secrets Manager**

  Set up an alternating users rotation for a secret that contains database credentials.

   [Explore the guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_rotation-alternating.html)
+  **Using AWS Secrets Manager secrets with Kubernetes**

  Show secrets from Secrets Manager as files mounted in Amazon EKS pods by using the AWS Secrets and Configuration Provider (ASCP).

   [Explore the guide](https://docs.aws.amazon.com/eks/latest/userguide/manage-secrets.html)

------
#### [ AWS Payment Cryptography ]
+  **Getting started with AWS Payment Cryptography**

   Create keys and use them in various cryptographic operations.

   [Explore the guide](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/getting-started.html)
+  **AWS Payment Cryptography FAQs**

  Understand the basics of AWS Payment Cryptography.

   [Explore the FAQs](https://aws.amazon.com/payment-cryptography/faqs/)

------

### Use AWS network and application protection services
<a name="network-and-application-protection-1"></a>

The following tables provide links to detailed resources that describe AWS network and application protection.

------
#### [ AWS Firewall Manager ]
+  **Getting started with AWS Firewall Manager policies**

  Use AWS Firewall Manager to activate different types of security policies.

   [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms-intro.html)
+  **How to continuously audit and limit security groups with AWS Firewall Manager**

  Use AWS Firewall Manager to limit security groups, ensuring that only required ports are open.

   [Read the blog](https://aws.amazon.com/blogs/security/how-to-continuously-audit-and-limit-security-groups-with-aws-firewall-manager/)
+ **Use AWS Firewall Manager to deploy protection at scale in AWS Organizations**

  Use AWS Firewall Manager to deploy and manage security policies across your AWS Organizations.

   [Read the blog](https://aws.amazon.com/blogs/security/use-aws-firewall-manager-to-deploy-protection-at-scale-in-aws-organizations/)

------
#### [ AWS Network Firewall ]
+  **Getting started with AWS Network Firewall**

  Configure and implement an AWS Network Firewall firewall for a VPC with a basic internet gateway architecture.

   [Explore the guide](https://docs.aws.amazon.com/network-firewall/latest/developerguide/getting-started.html)
+  **AWS Network Firewall Workshop**

  Deploy an AWS Network Firewall by using infrastructure as code.

   [Explore the workshop](https://catalog.workshops.aws/networkfirewall/en-US)
+ **Hands-on walkthrough of the AWS Network Firewall flexible rules engine – Part 1**

  Deploy a demonstration of AWS Network Firewall within your AWS account to interact with its rules engine.

   [Read the blog](https://aws.amazon.com/blogs/security/hands-on-walkthrough-of-the-aws-network-firewall-flexible-rules-engine/)
+ **Hands-on walkthrough of the AWS Network Firewall flexible rules engine – Part 2**

  Create a firewall policy with a strict rule order and set one or more default actions.

   [Read the blog](https://aws.amazon.com/blogs/security/hands-on-walkthrough-of-the-aws-network-firewall-flexible-rules-engine-part-2/)
+  **Deployment models for AWS Network Firewall**

  Learn deployment models for common use cases where you can add AWS Network Firewall to the traffic path.

   [Read the blog](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall/)
+ **Deployment models for AWS Network Firewall with VPC routing enhancements**

  Use enhanced VPC routing primitives to insert AWS Network Firewall between workloads in different subnets of the same VPC.

   [Read the blog](https://aws.amazon.com/blogs/networking-and-content-delivery/deployment-models-for-aws-network-firewall-with-vpc-routing-enhancements/)

------
#### [ AWS Shield ]
+  **How AWS Shield works**

  Learn how AWS Shield Standard and AWS Shield Advanced provide protections against DDoS attacks for AWS resources at the network and transport layers (layer 3 and 4) and the application layer (layer 7).

   [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html)
+  **Getting started with AWS Shield Advanced**

  Get started with AWS Shield Advanced by using the Shield Advanced console.

   [Explore the guide](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html)
+  **AWS Shield Advanced workshop**

  Protect internet-exposed resources against DDoS attacks, monitor DDoS attacks against your infrastructure, and notify the appropriate teams.

   [Explore the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/6396761b-6d1f-4a4d-abf1-ffb69dee6995/en-US)

------
#### [ AWS WAF ]
+  **Getting started with AWS WAF**

  Set up AWS WAF, create a web ACL, and protect Amazon CloudFront by adding rules and rules groups to filter web requests.

   [Get started with the tutorial](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html)
+  **Analyzing AWS WAF Logs in Amazon CloudWatch Logs**

  Set up native AWS WAF logging to Amazon CloudWatch logs and visualize and analyze the data in the logs.

   [Read the blog](https://aws.amazon.com/blogs/mt/analyzing-aws-waf-logs-in-amazon-cloudwatch-logs/)
+  **Visualize AWS WAF logs with an Amazon CloudWatch dashboard**

  Use Amazon CloudWatch to monitor and analyze AWS WAF activity by using CloudWatch metrics, Contributor Insights, and Logs Insights.

   [Read the blog](https://aws.amazon.com/blogs/security/visualize-aws-waf-logs-with-an-amazon-cloudwatch-dashboard/)

------

### Use AWS detection and response services
<a name="detection-and-response-1"></a>

The following tables provide links to detailed resources that describe AWS detection and response services.

------
#### [ AWS Config ]
+  **Getting started with AWS Config**

  Set up AWS Config and work with AWS SDKs.

   [Explore the guide](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html)
+  **Risk and Compliance workshop**

  Automate controls by using AWS Config and AWS Managed Config Rules.

   [Explore the workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/dd2bea89-dc7a-4bda-966a-70b4ff6e90e0/en-US/3-detective-controls-config/1-config-setup)
+ **AWS Config Rule Development Kit library: Build and operate rules at scale**

  Use the Rule Development Kit (RDK) to build a custom AWS Config rule and deploy it with the RDKLib.

   [Read the blog](https://aws.amazon.com/blogs/mt/aws-config-rule-development-kit-library-build-and-operate-rules-at-scale/)

------
#### [ AWS CloudTrail ]
+  **View event history**

  Review the AWS API activity in your AWS account for services that support CloudTrail.

   [Get started with the tutorial](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-event-history.html)
+  **Create a trail to log management events**

  Create a trail to log management events in all Regions.

   [Get started with the tutorial](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-trail.html)

------
#### [ AWS Security Hub CSPM ]
+  **Enabling AWS Security Hub CSPM**

  Enable AWS Security Hub CSPM with AWS Organizations or in a standalone account.

   [Explore the guide](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html)
+  **Cross-Region aggregation**

  Aggregate AWS Security Hub CSPM findings from multiple AWS Regions to a single aggregation Region.

   [Explore the guide](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html)
+  **AWS Security Hub CSPM workshop**

  Learn how to use AWS Security Hub CSPM and to manage and improve the security posture of your AWS environments.

   [Explore the workshop](https://catalog.workshops.aws/security-hub/en-US)
+ **Three recurring Security Hub CSPM usage patterns and how to deploy them**

  Learn about the three most common AWS Security Hub CSPM usage patterns and how to improve your strategy for identifying and managing findings.

   [Read the blog](https://aws.amazon.com/blogs/security/three-recurring-security-hub-usage-patterns-and-how-to-deploy-them/)

------
#### [ Amazon GuardDuty ]
+  **Getting started with Amazon GuardDuty**

  Enable Amazon GuardDuty, generate sample findings, and set up alerts.

   [Explore the tutorial](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html)
+  **EKS protection in Amazon GuardDuty**

  Use Amazon GuardDuty to monitor your Amazon Elastic Kubernetes Service (Amazon EKS) audit logs.

   [Explore the guide](https://docs.aws.amazon.com/guardduty/latest/ug/kubernetes-protection.html)
+  **Lambda protection in Amazon GuardDuty**

  Identify potential security threats when you invoke an AWS Lambda function.

   [Explore the guide](https://docs.aws.amazon.com/guardduty/latest/ug/lambda-protection.html)
+  **GuardDuty Amazon RDS protection**

  Use Amazon GuardDuty to analyze and profile Amazon Relational Database Service (Amazon RDS) login activity for potential access threats to your Amazon Aurora databases.

   [Explore the guide](https://docs.aws.amazon.com/guardduty/latest/ug/rds-protection.html)
+  **Amazon S3 protection in Amazon GuardDuty**

  Use GuardDuty to monitor CloudTrail data events and to identify potential security risks within your S3 buckets.

   [Explore the guide](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html)
+ **Threat detection and response with Amazon GuardDuty and Amazon Detective**

   Learn the basics of Amazon GuardDuty and Amazon Detective.

   [Explore the workshop](https://catalog.workshops.aws/guardduty/en-US)

------
#### [ Amazon Inspector ]
+  **Getting started with Amazon Inspector**

  Activate Amazon Inspector scans to understand findings in the console.

   [Get started with the tutorial](https://docs.aws.amazon.com/inspector/latest/user/getting_started_tutorial.html)
+  **Vulnerability management with Amazon Inspector**

  Use Amazon Inspector to scan Amazon EC2 instances and container images in Amazon Elastic Container Registry (Amazon ECR) for software vulnerabilities.

   [Explore the workshop](https://catalog.workshops.aws/inspector/en-US)
+  **How to scan EC2 AMIs by using Amazon Inspector**

  Build a solution by using multiple AWS services to scan your AMIs for known vulnerabilities.

   [Read the blog](https://aws.amazon.com/blogs/security/how-to-scan-ec2-amis-using-amazon-inspector/)

------
#### [ Amazon Security Lake ]
+  **Getting started with Amazon Security Lake**

   Enable and start using Amazon Security Lake.

   [Explore the guide](https://docs.aws.amazon.com/security-lake/latest/userguide/getting-started.html)
+  **Managing multiple accounts with AWS Organizations**

   Collect security logs and events from multiple AWS accounts.

   [Explore the guide](https://docs.aws.amazon.com/security-lake/latest/userguide/multi-account-management.html)
+ **Ingest, transform, and deliver events that are published by Amazon Security Lake to Amazon OpenSearch Service**

  Ingest, transform, and deliver Amazon Security Lake data to Amazon OpenSearch Service for use by your SecOps teams.

   [Read the blog](https://aws.amazon.com/blogs/big-data/ingest-transform-and-deliver-events-published-by-amazon-security-lake-to-amazon-opensearch-service/)
+ **How to visualize Amazon Security Lake findings with Quick**

   Query and visualize data from Amazon Security Lake by using Amazon Athena and Quick.

   [Read the blog](https://aws.amazon.com/blogs/security/how-to-visualize-amazon-security-lake-findings-with-amazon-quicksight/)

------
#### [ Amazon Detective ]
+  **Amazon Detective terms and concepts**

   Learn the key terms and concepts that are important for understanding Amazon Detective and how it works.

   [Explore the guide](https://docs.aws.amazon.com/detective/latest/userguide/detective-terms-concepts.html)
+  **Setting up Amazon Detective**

   Enable Amazon Detective from the Amazon Detective console, Amazon Detective API, or AWS CLI.

   [Explore the guide](https://docs.aws.amazon.com/detective/latest/userguide/detective-setup.html)
+ **Threat detection and response with Amazon GuardDuty and Amazon Detective**

   Learn the basics of Amazon GuardDuty and Amazon Detective.

   [Explore the workshop](https://catalog.workshops.aws/guardduty/en-US)

------

### Use AWS governance and compliance services
<a name="governance-and-compliance-1"></a>

The following tables provide links to detailed resources that describe governance and compliance.

------
#### [ AWS Organizations ]
+  **Creating and configuring an organization**

  Create your organization and configure it with two AWS member accounts.

   [Get started with the tutorial](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html)
+  **Services that work with AWS Organizations**

   Understand which AWS services you can use with AWS Organizations and the benefits of using each service on an organization-wide level.

   [Explore the guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html)
+  **Organizing your AWS environment by using multiple accounts**

  Implement best practices and current recommendations for organizing your overall AWS environment.

   [Read the whitepaper](https://docs.aws.amazon.com/pdfs/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.pdf)

------
#### [ AWS Artifact ]
+  **Getting started with AWS Artifact **

  Download security and compliance reports, manage legal agreements, and manage notifications.

   [Explore the guide](https://docs.aws.amazon.com/artifact/latest/ug/getting-started.html)
+  **Managing agreements in AWS Artifact**

  Use the AWS Management Console to review, accept, and manage agreements for your account or organization.

   [Explore the guide](https://docs.aws.amazon.com/artifact/latest/ug/managing-agreements.html)
+ **Prepare for an Audit in AWS Part 1 – AWS Audit Manager, AWS Config, and AWS Artifact**

  Use AWS services to help you automate the collection of evidence that's used in audits.

   [Read the blog](https://aws.amazon.com/blogs/mt/prepare-for-an-audit-in-aws-part-1-aws-audit-manager-aws-config-and-aws-artifact/)

------
#### [ AWS Audit Manager ]
+  **Enabling AWS Audit Manager**

   Enable Audit Manager by using the AWS Management Console, the Audit Manager API, or the AWS CLI.

   [Explore the guide](https://docs.aws.amazon.com/audit-manager/latest/userguide/setup-audit-manager.html)
+  **Tutorial for Audit Owners: Creating an assessment**

   Create an assessment by using the Audit Manager Sample Framework.

   [Explore the guide](https://docs.aws.amazon.com/audit-manager/latest/userguide/tutorial-for-audit-owners.html)
+  **Tutorial for Delegates: Reviewing a control set**

   Review a control set that was shared with you by an audit owner in Audit Manager.

   [Explore the guide](https://docs.aws.amazon.com/audit-manager/latest/userguide/tutorial-for-delegates.html)

------
#### [ AWS Control Tower ]
+  **Getting started with AWS Control Tower**

  Set up and launch a multi-account environment, called a landing zone, that follows prescriptive best practices.

   [Explore the guide](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html)
+ **Modernizing Account Management with Amazon Bedrock and AWS Control Tower**

  Provision a security tooling account and leverage generative AI to expedite the AWS account setup and management process.

   [Read the blog](https://aws.amazon.com/blogs/mt/modernizing-account-management-with-amazon-bedrock-and-aws-control-tower/)
+ **Building a well-architected AWS GovCloud (US) environment with AWS Control Tower**

  Set up your governance in the AWS GovCloud (US) Regions, including governing your AWS workloads by using Organizational Units (OUs) and AWS accounts.

   [Read the blog](https://aws.amazon.com/blogs/mt/building-a-well-architected-aws-govcloud-us-environment-with-aws-control-tower/)

------

## Explore AWS security, identity, and governance services
<a name="explore"></a>

------
#### [ Editable architecture diagrams ]

**Reference architecture diagrams**

Explore reference architecture diagrams to help you develop your security, identity, and governance strategy.

[Explore security, identity, and governance reference architectures](https://aws.amazon.com/architecture/?nc2=h_ql_le_arc&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23reference-arch-diagram&awsf.methodology=*all&awsf.tech-category=tech-category%23security-identity-compliance&awsf.industries=*all&awsf.business-category=*all)

------
#### [ Ready-to-use code ]

****

|  |  |
| --- |--- |
| *Featured solution*<br />**Security Insights on AWS**<br />Deploy AWS-built code to help you visualize data in Amazon Security Lake to more rapidly investigate and respond to security events.<br />[Explore this solution](https://aws.amazon.com/solutions/implementations/security-insights-on-aws/) | **AWS Solutions**<br />Explore pre-configured, deployable solutions and their implementation guides, built by AWS.<br />[Explore all AWS security, identity, and governance solutions](https://aws.amazon.com/architecture/?nc2=h_ql_le_arc&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23solution&awsf.methodology=*all&awsf.tech-category=tech-category%23security-identity-compliance&awsf.industries=*all&awsf.business-category=*all) |

------
#### [ Documentation ]

****

|  |  |
| --- |--- |
| **Security, identity, and governance whitepapers** <br />Explore whitepapers for further insights and best practices on choosing, implementing, and using the security, identity, and governance services that best fit your organization. <br /> [Explore security, identity, and governance whitepapers](https://aws.amazon.com/architecture/?nc2=h_ql_le_arc&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=content-type%23whitepaper&awsf.methodology=*all&awsf.tech-category=tech-category%23security-identity-compliance&awsf.industries=*all&awsf.business-category=*all)  | **AWS Security Blog** <br />Explore blog posts that address specific security use cases. <br /> [Explore the AWS Security blog](https://aws.amazon.com/blogs/security/)  |

------
