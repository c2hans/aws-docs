---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/introduction.html
---

# Encryption best practices and features for AWS services
<a name="introduction"></a>

*Kurt Kumar and Niko Borodachuk, Amazon Web Services*

## Business value of encryption
<a name="business-value-of-encryption.da198e1c-fdb5-5a97-8c0d-8a0a5c414bc5"></a>

Encryption is a fundamental cybersecurity tool for protecting sensitive data. Safeguarding your data through robust encryption practices is an essential component of a comprehensive data protection strategy for all your business operations, including generative AI deployments. This guide helps you understand the encryption principles and the encryption capabilities that AWS offers, so you can make informed decisions on how to achieve your compliance and business goals in AWS.

Modern cybersecurity threats include the risk of unauthorized disclosure,which is loss of confidentiality of data. Data is a business asset that is unique to each organization. It can include customer information, business plans, design documents, or code. Protecting the business means protecting its data.

[Data encryption](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/about-data-encryption.html) serves as a crucial safeguard for your business data, offering defense in depth in the event of unintentional or unauthorized access to your information systems. To access encrypted data in AWS, for example, users need permissions to use the key to decrypt and need permissions to use the service where the data resides. Without both of these permissions, users are unable to decrypt and view the data.

Generally, there are three types of data that you can encrypt.
+ Data at rest is data that is stationary and dormant, such as data that is in storage or written to disk. Examples include block storage, object storage, electronic file storage (EFS), database repositories, network-attached storage (NAS), and storage-area networks (SANs).
+ Data in transit is data that is actively moving through your network, such as between network resources. Examples include web traffic (typically secured with TLS), interactive host session traffic (typically secured with SSH), and private network traffic (typically secured with IPSec and MACsec)
+ Data in use encompasses data that is actively being processed by applications or services and is present in a system's memory at the time of processing, awaiting use by the CPU. Examples include AI/ML model inference on sensitive inputs; database query results in a buffer, or confidential data in a virtual machine's RAM.

With encryption across your AWS infrastructure, you achieve:
+ **Risk Mitigation**: Protect against  unauthorized access, even if physical security controls fail
+ **Customer Trust**: Demonstrate commitment to data protection and privacy
+ **Simplified Compliance**: Streamline adherence to regulatory requirements and meet the security expectations of your customers and partners
+ **Reduced Liability**: Minimize financial and reputational impact of potential security incidents

In addition, encryption serves as a critical control for meeting various compliance frameworks:
+ PCI-DSS: Mandatory for cardholder data protection (Requirement 3.4)
+ GDPR: Recognized as an appropriate technical measure for data protection (Article 32)
+ SOC 2: Demonstrates security controls for confidentiality and privacy
+ Healthcare data regulations: Required for protecting sensitive health information, such as HIPAA (US) or GDPR health data provisions (EU)
+ Government cloud certifications: Required for regulated government workloads, such as FedRAMP (US), C5 (Germany), or IRAP (Australia)
+ FIPS 140: Required when processing US or Canadian government data. To support this requirement, AWS provides FIPS validated cryptographic modules and dedicated FIPS endpoints for managed services.
+ Isolated computing environments provide isolated environments that prevent operators from accessing data.

This guide discusses considerations and strategies for encrypting data in transit and data at rest. It also provides an overview of options for securing data in use in AWS. Th e recommendations in this guide can help you build a consistent, defense-in-depth encryption strategy across your AWS Cloud environment. The individual service documentation provides implementation steps tailored to your workloads.

### Intended audience
<a name="intended-audience"></a>

This guide can be used by small, medium, and large organizations in both public and private sectors. Whether your organization is in the initial stages of assessing and implementing a data protection strategy or aiming to enhance existing security controls, the recommendations outlined in this guide are best suited for the following audiences:
+ Executive officers who formulate policies for their enterprise, such as chief executive officers (CEOs), chief technology officers (CTOs), chief information officers (CIOs), and chief information security officers (CISOs)
+ Technology officers who are responsible for setting up technical standards, such as technical vice presidents and directors
+ Business stakeholders and application owners who are responsible for:
  + Assessing risk posture, data classification, and protection requirements
  + Monitoring compliance with established organizational standards
+ Compliance, internal audit, and governance officers who are in charge of monitoring adherence to compliance policies, including statutory and voluntary compliance regimes
