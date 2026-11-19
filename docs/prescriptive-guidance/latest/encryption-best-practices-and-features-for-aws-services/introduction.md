---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices-and-features-for-aws-services/introduction.html
---

# Introduction

## Business value of encryption
<a name="business-value-of-encryption.58f8248d-4f6f-5ea1-a7ff-e14e13c2b929"></a>

Encryption is a fundamental cybersecurity tool for protecting sensitive data. Safeguarding your data through effective encryption practices is an essential component of a comprehensive data protection strategy for all your business operations, including generative AI deployments. This guide helps you understand encryption principles and the encryption capabilities that AWS offers, so you can make informed decisions about how to meet your compliance and business goals in AWS.

Modern cybersecurity threats include the risk of unauthorized disclosure, which is loss of confidentiality of data. Data is a business asset that is unique to each organization. It can include customer information, business plans, design documents, or code. Protecting the business means protecting its data.

[Data encryption](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/about-data-encryption.html) serves as a crucial safeguard for your business data, offering defense in depth in the event of unintentional or unauthorized access to your information systems. To access encrypted data in AWS, for example, users need permissions to use the key to decrypt and need permissions to use the service where the data resides. Without both of these permissions, users are unable to decrypt and view the data.

Generally, there are three types of data that you can encrypt.
+ Data at rest is data that is stationary and dormant, such as data in storage or written to disk. Examples include block storage, object storage, file storage, database repositories, network-attached storage (NAS), and storage area networks (SANs).
+ Data in transit is data that is actively moving through your network, such as between network resources. Examples include web traffic (typically secured with Transport Layer Security (TLS)), interactive host session traffic (typically secured with Secure Shell (SSH)), and private network traffic (typically secured with IPsec and MACsec).
+ Data in use is data that applications or services are actively processing. This data is present in a system's memory during processing, awaiting use by the central processing unit (CPU). Examples include artificial intelligence and machine learning (AI/ML) model inference on sensitive inputs, database query results in a buffer, and confidential data in a virtual machine's RAM.

This guide discusses considerations and strategies for encrypting data in transit and data at rest. It also provides an overview of options for securing data in use in AWS. The recommendations in this guide can help you build a consistent, defense-in-depth encryption strategy across your AWS Cloud environment. The individual service documentation provides implementation steps tailored to your workloads.

Encryption across your AWS infrastructure can help you with the following:
+ **Risk mitigation**: Help protect against unauthorized access, even if physical security controls fail
+ **Customer trust**: Demonstrate your commitment to data protection and privacy
+ **Compliance support**: Help meet regulatory requirements and the security expectations of your customers and partners
+ **Reduced impact**: Help limit the financial and reputational impact of potential security incidents

In addition, encryption serves as a critical control for meeting various compliance frameworks:
+ **Payment Card Industry Data Security Standard (PCI DSS)**: Requires stored account data, specifically the primary account number (PAN), to be rendered unreadable wherever it is stored
+ **General Data Protection Regulation (GDPR)**: Recognized as an appropriate technical measure for data protection
+ **System and Organization Controls (SOC) 2**: Can help demonstrate security controls for confidentiality and privacy
+ **Healthcare data regulations**: Supports the protection of sensitive health information, such as under the Health Insurance Portability and Accountability Act (HIPAA) (US) or GDPR health data provisions (EU)
+ **Government cloud certifications**: Required for regulated government workloads, such as the Federal Risk and Authorization Management Program (FedRAMP) (US), Cloud Computing Compliance Criteria Catalogue (C5) (Germany), or Information Security Registered Assessors Program (IRAP) (Australia)
+ **Federal Information Processing Standards (FIPS) 140**: Required when you process US or Canadian government data. To help you meet this requirement, AWS provides FIPS 140-validated cryptographic modules and FIPS endpoints for AWS services.

### Intended audience
<a name="intended-audience"></a>

**Intended audience**

Small, medium, and large organizations in both public and private sectors can use this guide. Whether your organization is in the initial stages of assessing and implementing a data protection strategy or aiming to enhance existing security controls, the recommendations in this guide are designed for the following audiences:

Executive officers who formulate policies for their enterprise, such as chief executive officers (CEOs), chief technology officers (CTOs), chief information officers (CIOs), and chief information security officers (CISOs)

Technology officers who are responsible for setting up technical standards, such as technical vice presidents and directors

Business stakeholders and application owners who are responsible for:

Assessing risk posture, data classification, and protection requirements

Monitoring compliance with established organizational standards

Compliance, internal audit, and governance officers who are in charge of monitoring adherence to compliance policies, including statutory and voluntary compliance regimes
