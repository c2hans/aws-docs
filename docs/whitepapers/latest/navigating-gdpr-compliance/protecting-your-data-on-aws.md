---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/protecting-your-data-on-aws.html
---

# Protecting your Data on AWS
<a name="protecting-your-data-on-aws"></a>

Article 32 of the GDPR requires that organizations must “[…] implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk, including […] the pseudonymization and encryption of personal data [...]”. In addition, organizations must safeguard against the unauthorized disclosure of, or access to personal data.

Encryption reduces the risks associated with the storage of personal data because data is unreadable without the correct key. A thorough encryption strategy can help mitigate the impact of various security events, including some security breaches.

AWS and AWS Marketplace partners offer a variety of solutions for protecting sensitive data within the AWS platform, but for applications and data subject to rigorous contractual or regulatory requirements for managing cryptographic keys, additional protection is sometimes necessary. Previously, the only option to store sensitive data (or the encryption keys protecting the sensitive data) may have been in on-premises datacenters. This might have prevented you from migrating these applications to the cloud, or significantly slowed their performance.

AWS supports encryption at rest and in transit, provides key management options through [AWS KMS](https://aws.amazon.com/kms/) and [AWS CloudHSM](https://aws.amazon.com/cloudhsm/), and enables client-side encryption through libraries like the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html). These services help customers comply with data protection regulations and align with industry security standards.
