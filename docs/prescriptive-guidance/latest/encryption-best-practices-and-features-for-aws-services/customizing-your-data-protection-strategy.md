---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices-and-features-for-aws-services/customizing-your-data-protection-strategy.html
---

# Customizing your data protection strategy

## Customizing your data protection strategy
<a name="customizing-your-data-protection-strategy.15df6e7f-5829-557b-bfda-6b9574419f99"></a>

Before you build your encryption strategy, understand how the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) shapes your decisions. AWS is responsible for security of the cloud, which includes protecting the infrastructure, hardware, software, networking, and facilities that run AWS services. You, as the customer, are responsible for security in the cloud, which includes managing your data encryption choices, access controls, and application-level security configurations.

For encryption specifically, this means AWS provides the cryptographic building blocks: services like [AWS KMS](https://aws.amazon.com/kms/) for key management and access to hardware security modules (HSMs), Transport Layer Security (TLS) endpoints for data in transit, and transparent encryption behaviors across services. AWS also manages the security of the underlying cryptographic implementations, which includes vetting algorithms, using formally verified libraries, and physically securing the infrastructure. You decide how to use these building blocks based on your business and compliance requirements.

Understanding where AWS's responsibility ends and yours begins is what makes data classification so important.

### Data classification
<a name="data-classification.571a7630-5966-593a-9efe-bfb31ad0c48e"></a>

Data classification is a process for identifying and categorizing the data in your network based on its criticality and sensitivity. It is a key component of a cybersecurity risk management strategy because it helps you determine the protection and retention controls that your data requires. Data classification is a component of the security pillar in the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html). Categories might include highly confidential, confidential, non-confidential, and public, but classification tiers and their names vary by organization.

Your data classification directly informs how you exercise your side of the shared responsibility model. Highly confidential data may require customer managed AWS KMS keys with strict access policies, TLS endpoints that use Federal Information Processing Standard (FIPS) 140-validated cryptography, and explicit audit trails for every cryptographic operation. For non-confidential data, AWS managed encryption defaults might meet your requirements, and AWS handles the key lifecycle on your behalf. The higher the classification, the more of the encryption responsibility you manage actively rather than delegate to AWS defaults.

### Customized encryption strategy
<a name="customized-encryption-strategy.6337ad35-b7da-5535-9f2f-eda1b31bfe2e"></a>

For more information, see [Creating an enterprise encryption strategy for data at rest](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/introduction.html) in AWS Prescriptive Guidance.
