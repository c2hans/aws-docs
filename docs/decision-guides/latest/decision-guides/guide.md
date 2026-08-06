---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/guide.html
---

# Choosing an AWS cryptography service
<a name="guide"></a>

**Taking the first step**

|  |  |
| --- |--- |
| **Purpose** | Help determine which AWS cryptography services are the best fit for your organization. |
| **Last updated** | January 31, 2025 |
| **Covered services** |  + [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) <br />+ [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html) <br />+ [AWS Database Encryption SDK](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/what-is-database-encryption-sdk.html) <br />+ [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) <br />+ [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) <br />+ [AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) <br />+ [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)   |
| **Related guides** | [ Choosing AWS security, identity, and governance services](https://docs.aws.amazon.com/decision-guides/latest/security-on-aws-how-to-choose/choosing-aws-security-services.html) |

## Introduction
<a name="introduction"></a>

 Cryptography is a cornerstone of security in cloud computing, helping to ensure data confidentiality, integrity, and authenticity. In a cloud environment, sensitive data may traverse public networks and reside on shared infrastructure, making robust cryptographic measures essential for protecting against unauthorized access or tampering.

 AWS offers a comprehensive range of cryptographic services to secure data, manage encryption keys, and protect sensitive information. These include AWS Key Management Service (KMS) for centralized key management, AWS CloudHSM for PKCS11 applications and dedicated hardware security modules, and the AWS Encryption SDK for client-side encryption. AWS Secrets Manager is a service that enables you to securely store, manage, and retrieve sensitive information such as database credentials, API keys, and other secrets throughout their lifecycle. AWS Certificate Manager (ACM) simplifies the process of provisioning, managing, and deploying publicly trusted transport layer security (TLS) certificates for use with AWS services. The AWS Private Certificate Authority (PCA) enables you to generate and distribute x509 certificates for your internal resources.

 The guide is designed to help you choose the AWS cryptography services and tools that are the best fit for your needs and your organization.

[![AWS Videos](http://img.youtube.com/vi/1vqaZBgPOiE?si=SoAZe1zQCWUlqF0K&start=475&end=535/0.jpg)](http://www.youtube.com/watch?v=1vqaZBgPOiE?si=SoAZe1zQCWUlqF0K&start=475&end=535)

## Understand
<a name="understand"></a>

![A diagram showing the suite of AWS services that enable data protection on AWS.](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/data-protection-on-aws-jan-2024.png)

 Choosing the right AWS cryptography services depends on your specific use case, data security requirements, compliance obligations, and operational preferences as outlined in the following tables.

------
#### [ Key management  ]

 If you need to securely manage encryption keys, consider AWS Key Management Service (KMS). It allows you to create, rotate, and manage cryptographic keys integrated with other AWS services. KMS uses FIPS-validated HSMs to help you meet compliance rewuirements and to provide assurance on the correctness of the implementation of the cryptographic primitives exposed by KMS. Some applications require certain cryptographic functions or application interfaces that are only available with a traditional HSM and AWS CloudHSM provides dedicated hardware security modules (HSMs) in the cloud which gives you full control over your cryptographic keys and operations.

------
#### [ Data encryption  ]

 For encrypting sensitive data such as customer details or intellectual property, AWS KMS is tightly integrated with AWS storage, database, and messaging services (e.g. S3, RDS, or EBS). If you require client-side encryption, the AWS Encryption SDK is an open-source library that makes it easy to encrypt data within your application before sending it to the cloud.

------
#### [ Secure communications  ]

 To protect data in transit, AWS Certificate Manager (ACM) simplifies the management of publicly trusted TLS certificates. Use it for asserting the identity of your internet-facing applications and facilitating encrypting communications between your application, users, and cloud services without worrying about certificate renewals. For internal applications, you can use AWS Private Certificate Authority (PCA) for generating and distributing x509 certificates for your internal resources, including both clients and servers.

------
#### [ Secrets and credentials management  ]

 For securely storing and retrieving application secrets such as database credentials, API keys, or certificates, consider AWS Secrets Manager. It provides automated secret rotation and fine-grained access controls. Alternatively, AWS Systems Manager Parameter Store is a lower-cost option for managing non-sensitive configurations and can integrate with AWS Secrets Manager.

------
#### [ Compliance and auditing  ]

 For regulatory compliance work, consider AWS KMS and AWS CloudHSM to help ensure encryption standards are met. AWS Artifact is a self-service portal that provides on-demand access to AWS's security and compliance reports, such as ISO certifications and SOC reports, as well as the ability to review and accept agreements such as the Business Associate Addendum (BAA). You can also use services like AWS Config, AWS Security Hub CSPM, and AWS Audit Manager to monitor compliance and produce the appropriate artifacts for your own use or for consumption by your stakeholders.

------

 When choosing between AWS cryptography services, consider the following requirements.

|  Requirement  |  Service  |
| --- | --- |
|  Low effort, fully managed  |  AWS KMS or AWS Secrets Manager  |
|  Require specific application interfaces or cryptographic algorithms not supported by KMS  |  AWS CloudHSM  |
|  Encrypting/decrypting data in your applications  |  AWS Encryption SDK  |
|  Simplified public TLS Certificate Management  |  AWS Certificate Manager  |
|  Secrets management  |  AWS Secrets Manager  |

 By aligning your requirements with these options, you can implement cryptographic solutions tailored to your security and operational needs.

## Consider
<a name="consider"></a>

 Choosing the right AWS cryptography service involves understanding your specific security, operational, and compliance needs. AWS offers a variety of cryptographic services, each designed to address different use cases, from key management to data encryption and secure communication. To make an informed decision, you should evaluate your requirements based on several critical criteria, including your use case, control and flexibility needs, compliance obligations, cost considerations, and integration with AWS services. These criteria will help you align your choice with your organization’s security goals and operational workflows.

------
#### [ Use case  ]

 Consider what you need the cryptographic service for: data encryption, key management, secure communication, or secrets management. For example, AWS KMS is ideal for encryption integrated into AWS services, while AWS CloudHSM suits organizations who need certain cryptographic capabilities, application interfaces, or a single-tenant HSM, often due to stringent compliance or specific application needs. Clarifying the purpose ensures you select a service suitable for for your requirements, optimizing both functionality and cost.

------
#### [ Control and flexibility  ]

 Evaluate the level of control you need over your cryptographic operations. Managed services like AWS KMS provide ease of use with minimal management overhead with a multi-tenant HSM while maintaining full control over your key material. In contrast, AWS CloudHSM offers a single-tenant model for specific application, cryptographic, or compliance needs.

------
#### [ Compliance requirements  ]

 If you operate in a regulated industry, ensure the service aligns with standards like GDPR, PCI DSS, or HIPAA. AWS KMS and AWS CloudHSM are both FIPS 140-2 Level 3 certified. Selecting a service that meets your non-functional requirements helps maintain trust and may avoid potential legal or financial penalties.

------
#### [ Cost considerations  ]

 Assess your budget against the service’s pricing model. AWS KMS is cost-effective for general encryption needs, while AWS CloudHSM incurs higher costs due to dedicated hardware. Understanding cost implications helps you optimize your security expenditure.

------
#### [ Integration with AWS ecosystem  ]

 If you heavily use AWS services, prioritize a cryptography solution like AWS KMS or ACM that integrates seamlessly with S3, RDS, or Lambda. This ensures smoother workflows and reduces development effort. Integration capabilities can significantly enhance operational efficiency.

------

## Choose
<a name="choose"></a>

 Choosing the right AWS cryptography service involves understanding your specific security, operational, and compliance needs. AWS offers a variety of cryptographic services, each designed to address different use cases, from key management to data encryption and secure communication. To make an informed decision, you should evaluate your requirements based on several critical criteria, including your use case, control and flexibility needs, compliance obligations, cost considerations, and integration with AWS services. These criteria will help you align your choice with your organization’s security goals and operational workflows.

|  Target use case  |  When would you use it?  |  Recommended service  |
| --- | --- | --- |
|  Key management  |  To securely create, rotate, and manage cryptographic keys integrated with other AWS services  |  [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)  |
|  Key management  |  For specific application integrations or cryptographic primitives  |  [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html)  |
|  Data encryption  |  To implement client-side encryption to protect sensitive data such as customer details or intellectual property.  |  [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) <br /> [AWS Database Encryption SDK](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/what-is-database-encryption-sdk.html)  |
|  Secure communications  |  To protect data in transit and simplify the management of SSL/TLS certificates.  |  [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) <br /> [AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html)  |
|  Secrets and credential management  |  To securely store and retrieve application secrets like database credentials, API keys, or certificates.  |  [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) <br /> [AWS Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)  |

## Use
<a name="use"></a>

 You should now have a clear understanding of what each AWS cryptography service does, and which ones might be right for you.

 To explore how to use and learn more about each of the available AWS cryptography services, we have provided a pathway to explore how each of them works. The following sections provide links to in-depth documentation, hands-on tutorials, and other resources to get you started.

------
#### [ AWS Certificate Manager  ]
+  **Get started with AWS Certificate Manager **

   Start using AWS Certificate Manager, including working with both public and private certificates.

   [Explore the guide](https://docs.aws.amazon.com/acm/latest/userguide/setup.html)
+  **Best practices for AWS Certificate Manager **

   Review recommendations that can help you use AWS Certificate Manager more effectively.

   [Explore the guide](https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html)
+  **AWS Certificate Manager FAQ **

   Review the AWS Certificate Manager (ACM) FAQ page for detailed answers to common questions about ACM's features, capabilities, and usage. It covers topics such as the types of certificates ACM manages, integration with other AWS services, and guidance on provisioning and managing SSL/TLS certificates.

   [Explore the FAQs](https://aws.amazon.com/certificate-manager/faqs/)

------
#### [ AWS CloudHSM  ]
+  **Get started with AWS CloudHSM **

   Learn how to create, initialize, and activate a cluster in AWS CloudHSM. After you complete these procedures, you'll be ready to manage users, manage clusters, and use the included software libraries to perform cryptographic operations.

   [Explore the guide](https://docs.aws.amazon.com/cloudhsm/latest/userguide/getting-started.html)
+  **Best practices for AWS CloudHSM **

   Explore best practices for managing and monitoring your AWS CloudHSM cluster.

   [Explore the guide](https://docs.aws.amazon.com/cloudhsm/latest/userguide/best-practices.html)
+  **AWS CloudHSM pricing **

   Review the pricing page to learn about AWS CloudHSM pricing. There are no upfront costs to use AWS CloudHSM. With AWS CloudHSM, you pay an hourly fee for each HSM you launch until you terminate the HSM. This guide provides the hourly rate for each AWS region.

   [Explore the pricing page](https://aws.amazon.com/cloudhsm/pricing/)
+ ** AWS CloudHSM FAQ **

   Review the AWS CloudHSM FAQ page for detailed answers to common questions about AWS CloudHSM, including its features, pricing, provisioning, security, compliance, performance, and integration with third-party applications.

   [Explore the FAQs](https://aws.amazon.com/cloudhsm/faqs/)

------
#### [ AWS Encryption SDK  ]
+  **Get started with the AWS Encryption SDK **

   Learn how to use the AWS Encryption SDK with AWS KMS.

   [Explore the guide](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/getting-started.html)
+  **Best practices for the AWS Encryption SDK **

   Review the AWS Encryption SDK Best Practices page for guidance on effectively utilizing the AWS Encryption SDK to secure your data. Adhering to these best practices helps ensure the confidentiality and integrity of your encrypted data.

   [Explore the guide](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/best-practices.html)
+  **AWS Encryption SDK FAQ **

   Review the AWS Encryption SDK FAQ page for answers to common questions about the AWS Encryption SDK, including its features, supported programming languages, and best practices for implementation.

   [Explore the FAQ](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/faq.html)

------
#### [ AWS Database Encryption SDK  ]
+ ** Get started with the AWS Database Encryption SDK **

   Learn how to use the AWS Database Encryption SDK with AWS KMS.

   [Explore the guide](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/using-kms.html)
+  **Configure the AWS Database Encryption SDK **

   Learn how to configure the AWS Database Encryption SDK, including selecting a programming language and selecting wrapping keys.

   [Explore the guide](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/configure.html)

------
#### [ AWS KMS  ]
+  **Get started with AWS KMS **

   Learn how to create KMS keys, including symmetric and asymmetric encryption keys.

   [Explore the guide](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html)
+  **Best practices for AWS KMS **

   Learn encryption best practices for AWS KMS.

   [Explore the guide](https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/kms.html)
+  **AWS KMS pricing **

   Review the AWS Key Management Service (KMS) Pricing page to learn about the costs associated with using AWS KMS, including charges for key storage, API requests, and optional features like custom key stores.

   [Explore the pricing page](https://aws.amazon.com/kms/pricing/)
+  **AWS KMS FAQ **

   The AWS Key Management Service (KMS) FAQ page provides detailed answers to common questions about AWS KMS, including its features, security measures, billing practices, key management options, and integration with other AWS services.

   [Explore the FAQs](https://aws.amazon.com/kms/faqs/)

------
#### [ AWS Private CA  ]
+  **Best practices for AWS Private CA **

   Review recommendations that can help you use AWS Private CA effectively.

   [Explore the guide](https://docs.aws.amazon.com/privateca/latest/userguide/ca-best-practices.html)
+  **Get started with AWS Private CA **

   Learn how to create and activate a root CA programmatically.

   [Explore the guide](https://docs.aws.amazon.com/privateca/latest/userguide/JavaApi-ActivateRootCA.html)
+  **AWS Private CA pricing **

   Review costs associated with operating private CAs and issuing private certificates.

   [Explore the pricing page](https://aws.amazon.com/private-ca/pricing/)
+  **AWS Private CA FAQ **

   Get detailed answers to common questions about AWS Private CA, including its features, pricing, provisioning, security, compliance, performance, and integration with other AWS services.

   [Explore the FAQs](https://aws.amazon.com/private-ca/faqs/)

------
#### [ AWS Secrets Manager  ]
+  **Get started with AWS Secrets Manager **

   Learn how to create an AWS Secrets Manager secret.

   [Explore the guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html)
+  **Best practices for AWS Secrets Manager **

   Learn about best practices you should consider when using AWS Secrets Manager.

   [Explore the guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/best-practices.html)
+  **AWS Secrets Manager pricing **

   Review the AWS Secrets Manager pricing page to learn about costs associated with securely storing, managing, and retrieving secrets such as database credentials and API keys.

   [Explore the pricing page](https://aws.amazon.com/secrets-manager/pricing)
+  **AWS Secrets Manager FAQ **

   Review the AWS Secrets Manager FAQ page for detailed answers to common questions about AWS Secrets Manager, including its features, security measures, pricing, and integration capabilities.

   [Explore the FAQs](https://aws.amazon.com/secrets-manager/faqs)

------

## Explore
<a name="explore"></a>
+  **Research and resources**

  Explore AWS blogs, videos and tools on cryptography.

   [ Review resources](https://aws.amazon.com/security/cryptographic-computing/)
+  **Videos**

  Watch these videos from the AWS Developers channel on YouTube to further develop and refine your cryptography strategy.

  [Explore cryptography videos](http://www.youtube.com/@awsdevelopers/search?query=cryptography)
