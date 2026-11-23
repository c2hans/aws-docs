---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/encryption-best-practices.html
---

# Encryption best practices and features for AWS services

*Kurt Kumar and Niko Borodachuk, Amazon Web Services*

## Customizing your data protection strategy
<a name="customizing-your-data-protection-strategy.52b0706d-7fb0-5d80-85cd-88526c509268"></a>

Before you build your encryption strategy, understand how the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) shapes the decisions you make. AWS is responsible for security of the cloud, which includes protecting the infrastructure, hardware, software, networking, and facilities that run AWS services. You are responsible for security in the cloud, which includes managing your data encryption choices, access controls, and application-level security configurations.

For encryption, this means AWS provides the cryptographic building blocks: services like [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/) for key management and access to hardware security modules (HSMs), Transport Layer Security (TLS) endpoints for data in transit, and transparent encryption behaviors across services. AWS also manages the security of the underlying cryptographic implementations, including vetted algorithms, formally verified libraries, and physically secured infrastructure. You decide how to use these building blocks based on your business and compliance requirements.

Understanding where AWS's responsibility ends and yours begins is what makes data classification so important.

### Data classification
<a name="data-classification.d315e4e8-70a8-57ec-895c-9c19ca5fd8e7"></a>

Data classification is a process for identifying and categorizing the data in your network based on its criticality and sensitivity. It is an important component of a cybersecurity risk management strategy because it helps you determine the protection and retention controls that your data requires. Data classification is a component of the security pillar in the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html). Categories might include highly confidential, confidential, non-confidential, and public, but the classification tiers and their names can vary from organization to organization.

Your data classification directly informs how you meet your side of the shared responsibility model. Highly confidential data may require customer managed AWS KMS keys with strict access policies, TLS endpoints that use FIPS 140-validated cryptography, and explicit audit trails for cryptographic operations. For non-confidential data, AWS managed encryption defaults may meet your requirements, because AWS handles the key lifecycle on your behalf. As the classification level increases, you typically manage more of the encryption responsibility yourself instead of relying on AWS defaults.

### Customized encryption strategy
<a name="customized-encryption-strategy.d63fda6d-8c01-54a6-b7a7-d2bba2556217"></a>

For more information, see [Creating an enterprise encryption strategy for data at rest](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/introduction.html) in AWS Prescriptive Guidance.

#### Intended audience
<a name="intended-audience"></a>

Small, medium, and large organizations in both public and private sectors can use this guide. Whether your organization is in the initial stages of assessing and implementing a data protection strategy or aiming to enhance existing security controls, the recommendations in this guide are designed for the following audiences:
+ Executive officers who formulate policies for their enterprise, such as chief executive officers (CEOs), chief technology officers (CTOs), chief information officers (CIOs), and chief information security officers (CISOs)
+ Technology officers who are responsible for setting up technical standards, such as technical vice presidents and directors
+ Business stakeholders and application owners who are responsible for:
  + Assessing risk posture, data classification, and protection requirements
  + Monitoring compliance with established organizational standards
+ Compliance, internal audit, and governance officers who are responsible for monitoring adherence to compliance policies, including statutory and voluntary compliance regimes
