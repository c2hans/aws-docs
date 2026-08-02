---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/security-and-compliance.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security and compliance
<a name="security-and-compliance"></a>

 Despite the common misconception that a cloud environment is less secure than on-premises infrastructure, strategic goals in relation to security and compliance are often key drivers for organizations to migrate to the cloud. Leading hyperscale cloud service providers such as AWS invest heavily in security and compliance and deliver a better security profile than what the biggest and most conservative organizations can deliver internally.

 Security is a top priority at AWS. As an AWS customer, regardless of your size or investment, you inherit all the benefits of AWS experience, tested against the strictest of third-party assurance frameworks.

## AWS Shared Responsibility Model
<a name="aws-shared-responsibility-model"></a>

 Under the AWS [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/), AWS provides a global secure infrastructure and foundation for compute, storage, networking and database services, as well as higher level services. AWS provides a range of security services and features that AWS customers can use to secure their assets. AWS customers are responsible for protecting the confidentiality, integrity, and availability of their data in the cloud, and for meeting specific business requirements for information protection. In a simple way, AWS is responsible for security *of* the cloud and the customer is responsible for security *in* the cloud.

 When leveraging the AWS Cloud, customers can choose a security solution that is designed to protect their organization’s content, platform, applications, systems and networks, while also meeting their business needs. AWS offers a wide range of tools and features that help organizations increase privacy and control network access so they can more easily meet their needs within the AWS Shared Responsibility Model. Amazon Virtual Private Cloud (Amazon VPC) enables you to create a logically isolated portion of the AWS Cloud, from which you can launch Amazon EC2 instances in a virtual network that you define. Security groups allow you to define a virtual firewall around your EC2 instances, which contains rules that control the inbound and outbound traffic to your instances. Network access control lists (ACLs) provide an optional layer that allows you to control traffic in and out of one or more subnets in your VPC.

## Best practices
<a name="best-practices"></a>

 AWS and Magento open-source or Adobe Commerce on cloud infrastructure self-service offer a range of tools to help secure your cloud resources and to help you meet your compliance needs under organizational and open standards. Best practices include the following:

### Network security
<a name="network-security"></a>

 Amazon VPC allows you to create private networks within AWS and control network access to your instances and subnets. Use private or dedicated connectivity options such as AWS Direct Connect to connect your on-premises office or datacenter to AWS. If you are already using AWS in your organization then use AWS Private Link to connect Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service hosted cloud to your existing VPC. Lastly, always include a web application firewall (AWS WAF) and distributed denial of service (DDoS) mitigation technologies (AWS Shield) as part of your automatic scaling or content delivery strategy.

### Data encryption
<a name="data-encryption"></a>

 Always encrypt your data both at rest and in transit. You can use TLS to encrypt the data in transit. Encryption at rest is achieved via data encryption capabilities available in AWS storage services such as Amazon Elastic Block Store (Amazon EBS), Amazon Simple Storage Service (Amazon S3), and Amazon Relational Database Service (Amazon RDS). Also, there are dedicated hardware-based cryptographic key storage options available for customers to help satisfy their compliance requirements.

### Access control
<a name="access-control"></a>

 Protect your AWS and Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service user credentials. AWS credentials are used to access AWS services where Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service credentials are used to manage your storefront within Magento. Use appropriate permissions across user accounts that access AWS resources and user accounts that access Magento store front customizing capabilities. AWS Identity and Access Management (IAM) enables you to create multiple users and manage the permissions. AWS supplies two types of security credentials: AWS access keys and X.509 certificates. Access keys and certificates for authentication to AWS services. As a good practice, it is recommended that you incorporate a key rotation mechanism into your application architecture. Lastly for extra security, AWS recommends that you use multifactor authentication (MFA) for all user accounts, including options for hardware-based authenticators, and integrate with federated identity providers such as on-premised corporate directories to reduce administrative overhead and improve end- user experience.

 If users already have identities (user credentials) outside of AWS, such as in a corporate directory, then you can use identity federation along with AWS IAM Identity Center to simplify the user management process. You can use the identity information from the external corporate directory system and use appropriate roles inside IAM for managing permissions.

 AWS Secrets Manager can be used to rotate, manage, and retrieve database credentials, API keys, as well as Magento open-source or Adobe Commerce on cloud infrastructure self-service secrets (user names and passwords). You can configure Secrets Manager to rotate secrets automatically, which can help you meet your security and compliance needs. Secrets Manager offers built-in integrations for Amazon Aurora Amazon RDS and can rotate credentials for these databases natively. To retrieve secrets for Magento open-source or Adobe Commerce on cloud infrastructure self-service application, you can replace plaintext secrets with a call to Secrets Manager APIs, eliminating the need to hardcode secrets in source code or update configuration files and redeploy code when secrets are rotated.

### Monitoring and logging
<a name="monitoring-and-logging"></a>

 Always have the right monitoring and logging tools enabled to give you the visibility you need to spot issues before they impact your business. [AWS features a variety of services](https://aws.amazon.com/products/security/) that give you deep visibility (who, what, when, and from where) such as 1) AWS CloudTrail for API calls (access requests), 2) AWS Config (configuration history), 3) Amazon CloudWatch to gain system-wide visibility into resource utilization, application performance, and operational health and 4) VPC flow logs that log all network traffic flowing through the VPC. In addition, you can configure CloudWatch Events to automatically alert as well as respond to adverse events. Lastly, Amazon GuardDuty is a threat detection service that automates continuous monitoring for malicious activity and unauthorized behavior using machine learning.

### Security guidance
<a name="security-guidance"></a>

 AWS provides customers with guidance and expertise through online tools, resources, support, and professional services provided by AWS and its partners. AWS Trusted Advisor is an online tool that inspects your AWS environment to help close security gaps, and finds opportunities to save money, improve system performance, and increase reliability. AWS Advisories and [Security Bulletins](https://aws.amazon.com/security/security-bulletins/?nc=sn&loc=6&card-body.sort-by=item.additionalFields.bulletinDateSort&card-body.sort-order=desc) provide advisories around current vulnerabilities and threats, and enable customers to work with AWS security experts to address concerns like reporting abuse, vulnerabilities, and penetration testing. Magento security center provides advisories around latest Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service patches and security updates. Magento security scan tool, a free tool from Adobe, can be used to monitor your websites for security risks, update malware patches, and detect unauthorized access.

### PCI DSS
<a name="pci-dss"></a>

 AWS supports a variety of security standards and compliance certifications including the Payment Card Industry Data Security Standard (PCI DSS), which is a crucial requirement for organizations who process credit cards and store cardholder information. Organizations that fail to comply with PCI requirements can expect large fines, which can also result in canceling their ability to process payments. PCI compliance requires organizations to safeguard their customers’ payment card information following security requirements that include policies and procedures, software design, and network architecture.

 AWS is certified as a PCI DSS 3.2 Level 1 Service Provider, the highest level of assessment available. Magento Commerce is PCI certified as a Level 1 Solution Provider. Organizations can use AWS and Magento’s PCI Attestation of Compliance to aid their own PCI certification process.

 The PCI DSS certification for an organization involves attestation of the following 12 requirements, broken into 6 groups: 1) Build and Maintain a Secure Network, 2) Protect Cardholder Data 3) Maintain a Vulnerability Management Program, 4) Implement Strong Access Control Measures, 5) Implement Strong Access Control Measures and 6) Regularly Monitor and Test Networks. For more information on PCI Compliance, refer to [PCI DSS resources on AWS website](https://aws.amazon.com/compliance/pci-dss-level-1-faqs/) and [PCI Security Standards Council website](https://www.pcisecuritystandards.org/).
