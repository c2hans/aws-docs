---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/general-encryption-best-practices.html
---

# General encryption best practices
<a name="general-encryption-best-practices"></a>

This section provides recommendations that apply when encrypting data in the AWS Cloud. These general encryption best practices are not specific to AWS services. This section includes the following topics:
+ [Data classification](#data-classification)
+ [Encryption of data in transit](#encryption-of-data-in-transit)
+ [Encryption of data at rest](#encryption-of-data-at-rest)

## Data classification
<a name="data-classification"></a>

*Data classification* is a process for identifying and categorizing the data in your network based on its criticality and sensitivity. It is a critical component of any cybersecurity risk management strategy because it helps you determine the appropriate protection and retention controls for the data. [Data classification](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-classification.html) is a component of the security pillar in the AWS Well-Architected Framework. Categories might include *highly confidential*, *confidential*, *non-confidential*, and *public*, but the classification tiers and their names can vary from organization to organization. For more information about the data classification process, considerations, and models, see [Data classification](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification-overview.html) (AWS Whitepaper).

After you have classified your data, you can create an encryption strategy for your organization based on the level of protection required for each category. For example, your organization might decide that highly confidential data should use asymmetric encryption and that public data doesn't require encryption. For more information about designing an encryption strategy, see [Creating an enterprise encryption strategy for data at rest](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/welcome.html). Although the technical considerations and recommendations in that guide are specific to data at rest, you can use the phased approach to create an encryption strategy for data in transit as well.

## Encryption of data in transit
<a name="encryption-of-data-in-transit"></a>

All data transmitted between AWS Regions over the AWS global network is automatically encrypted by AWS at the physical layer before it leaves AWS secured facilities. AWS encrypts all traffic between Availability Zones.

For data flowing through your workloads, the following are general best practices when encrypting data in transit in the AWS Cloud:
+ Define an organizational encryption policy for data in transit, based on your data classification, organizational requirements, and any applicable regulatory or compliance standards. We strongly recommend that you encrypt data in transit that is classified as highly confidential or confidential. Your policy might also specify encryption for other categories, such as non-confidential or public data, on an as-needed basis.
+ When encrypting data in transit, we recommend using approved cryptography algorithms, block cipher modes, and key lengths, as defined in your encryption policy. We further recommend periodically reviewing the TLS policies associated with your Application Load Balancers, Amazon API Gateway resources, Amazon CloudFront resources, and Amazon Virtual Private Cloud Console (Amazon VPC) resources to make sure that they are aligned with your current encryption policy.
+ Encrypt traffic between information assets and systems within the corporate network and AWS Cloud infrastructure by using one of the following:
  + [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) connections
  + A combination of AWS Site-to-Site VPN and [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) connections, which provides an IPsec-encrypted private connection
  + Direct Connect connections that support MAC Security (MACsec) to encrypt data from corporate networks to the Direct Connect location
+ Identify access control policies for managed certificates and TLS policy configurations based on the principle of least privilege. *Least privilege* is the security best practice of granting users the minimum access they need to perform their job functions. For more information about applying least-privilege permissions, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) and [Best practices for IAM policies](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies-best-practices.html).

## Encryption of data at rest
<a name="encryption-of-data-at-rest"></a>

AWS has adopted transparent encryption of data at rest as the standard security posture across its service portfolio. This encryption is transparent to the customer, ensuring that data is protected at rest and without requiring explicit configuration. Unless explicitly changed by the customer to use customer managed keys via AWS KMS, the transparent encryption mechanism remains in effect across all applicable services and deployment paths.

You can encrypt data using server-side encryptionor client-side encryption basedon factors such as data classification, the need for end-to-end encryption, or technical limitations that prevent you from using end-to-end encryption:
+ Server-side encryption is the act of encrypting data at its destination, by the application or service that receives it and owns the security of its storage layer. Server-side encryption always happens transparently using keys managed by AWS on your behalf in AWS KMS, but you can also opt into each service using a customer-managed key from AWS KMS that you manage directly instead. Customer-managed keys in AWS KMS give you more control over creation, rotation, sharing (for example with software vendors), and governance.  With transparent encryption, the AWS service controls when the key is used to encrypt and decrypt your data in response to your requests of the service to write and read your data. With a customer managed key, you get to define permissions that control when the AWS service is allowed to use your key for encryption and decryption in response to your requests of the service to write and read your data.
+ Client-side encryption is the act of encrypting data locally before the target application or service receives it. The AWS service receives encrypted data; it does not play a role in encrypting or decrypting it. For client-side encryption, you can use the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html), optionally integrated with AWS KMS for key management, or use other encryption libraries and key management solutions.

  For more information and detailed examples for specific use cases, refer to the*Data Encryption *section of any AWS service's documentation.
