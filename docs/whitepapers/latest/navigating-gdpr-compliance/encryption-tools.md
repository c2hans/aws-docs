---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/encryption-tools.html
---

# Encryption Tools
<a name="encryption-tools"></a>

AWS offers various highly scalable data encryption services, tools, and mechanisms to help protect your data stored and processed on AWS. For information about AWS Service functionality and privacy, refer to [Privacy Features of AWS services](https://aws.amazon.com/compliance/privacy-features/).

Cryptographic services from AWS use a wide range of encryption and storage technologies that are designed to maintain integrity of your data at rest or in transit. AWS offers four primary tools for cryptographic operations.
+ [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) is an AWS managed service that generates and manages both root keys and data keys. AWS KMS is integrated with many AWS services to provide server-side encryption of data using AWS KMS keys from customer accounts. AWS KMS Hardware Security Modules (HSMs) are FIPS 140-2 Level 3 validated. In November 2022, AWS announced the availability of AWS Key Management Service (AWS KMS) External Key Store. Customers who have a regulatory need to store and use their encryption keys on premises or outside of the AWS Cloud can now do so. This capability allows you to store AWS KMS customer managed keys on a hardware security module (HSM) that you operate on-premises or at any location of your choice. KMS External Key Stores (XKS) allow you to protect your AWS resources using cryptographic keys stored in an external key management system that you control. External key stores support the AWS digital sovereignty pledge to give you sovereign control over your data in AWS, including the ability to encrypt with key material that you own and control outside of AWS.
+ AWS CloudHSM provides HSMs that are FIPS 140-2 Level 3 validated. They securely store a variety of your self-managed cryptographic keys, including KMS keys and data keys.
+ AWS Cryptographic Services and Tools
+ [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) is a client-side encryption library designed to make it easy for everyone to encrypt and decrypt data using industry standards and best practices. It enables you to focus on the core functionality of your application, rather than on how to best encrypt and decrypt your data.
+ [AWS Database Encryption SDK](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/what-is-database-encryption-sdk.html) is a set of software libraries that enable you to include client-side encryption in your database design. The AWS Database Encryption SDK provides record-level encryption solutions. You specify which fields are encrypted and which fields are included in the signatures that ensure the authenticity of your data. Encrypting your sensitive data in transit and at rest helps ensure that your plaintext data isn’t available to any third party, including AWS.

## AWS Key Management Service
<a name="aws-key-management-service"></a>

[AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) is a managed service that makes it easy for you to create and control the encryption keys used to encrypt your data, and uses Hardware Security Modules (HSMs) to protect the security of your keys. AWS KMS is integrated with several other AWS services to help you protect the data you store with these services. AWS KMS is also integrated with AWS CloudTrail to provide you with logs of all your key usage for your regulatory and compliance needs.

AWS KMS supports several different types of keys for different uses and the several special purpose KMS key types including key with imported key material (BYOK) and key in a custom key store, that is backed by an AWS CloudHSM cluster or an external key manager outside of AWS.

You can easily create, import, and rotate keys, as well as define usage policies and audit usage from the AWS Management Console or by using the AWS SDK or AWS CLI.

The AWS KMS Keys in AWS KMS, whether imported by you or created on your behalf by KMS, are stored in highly durable storage in an encrypted format to help ensure that they can be used when needed. You can choose to have KMS automatically rotate AWS KMS Keys created in KMS once per year without having to re-encrypt data that has already been encrypted with your KMS key. You don’t need to keep track of older versions of your AWS KMS Keys because KMS keeps them available to automatically decrypt previously encrypted data.

For any AWS KMS Key in AWS KMS, you can control who has access to those keys and which services they can be used with through a number of access controls, including grants, and key policy conditions within key policies or IAM policies. You can also import keys from your own key management infrastructure and use them in KMS.

For example, the following policy uses the kms:ViaService condition to allow a customer managed AWS KMS Key to be used for the specified actions only when the request comes from Amazon EC2 or Amazon RDS in a specific Region (us-west-2) on behalf of a specific user (ExampleUser).

```
{
“Version”: “2012-10-17”,
“Statement”: [
{
“Effect”: “Allow”,
“Principal”: {
“AWS”: “arn:aws:iam::111122223333:user/ExampleUser”
}
“Action”: [
“kms:Encrypt*”,
“kms:Decrypt”,
“kms:ReEncrypt*”,
“kms:GenerateDataKey*”,
“kms:CreateGrant”,
“kms:ListGrants”,
“kms:DescribeKey”
],
“Resource”: “*”,
“Condition”: {
“ForAnyValue:StringEquals”: {
“kms:ViaService”: [
“ec2.us-west-2.amazonaws.com”,
“rds.us-west-2.amazonaws.com”
]
}
}
}
```

### AWS Service Integration
<a name="aws-service-integration"></a>

AWS KMS has integrated with a number of AWS services – refer to the [KMS website](https://aws.amazon.com/kms/) for a full list of integrated services. These integrations enable you to easily use AWS KMS Keys to encrypt the data you store with these services. In addition to using a customer managed AWS KMS Key, a number of the integrated services enable you to use an AWS-managed AWS KMS Key that is created and managed for you automatically, but is only usable within the specific service that created it.

### Audit Capabilities
<a name="audit-capabilities"></a>

[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) records each use of a key that you store in AWS KMS in a log file that is delivered to the Amazon S3 bucket that you specified in your configuration of CloudTrail. The information recorded includes details of the user, time, date, operation performed, and the key used.

### Security
<a name="security"></a>

AWS KMS is designed to make sure that no one has access to your KMS keys. The service is built on systems that are designed to protect your KMS keys with extensive hardening techniques, such as never storing plaintext KMS keys on disk, not persisting them in memory, and limiting which systems can access hosts that use keys. All access to update software on the service is controlled by a multi-party access control that is audited and reviewed by an independent group within AWS.

For more information about AWS KMS, see the AWS Key Management Service whitepaper.

## AWS CloudHSM
<a name="aws-cloudhsm"></a>

The [AWS CloudHSM](https://aws.amazon.com/cloudhsm/) is a cloud-based hardware security module (HSM) that helps you meet corporate, contractual, and regulatory compliance requirements for data security by enabling you to generate and use your encryption keys on a FIPS 140-2 Level 3 validated hardware.

With AWS CloudHSM, you control the encryption keys and cryptographic operations performed by HSM.

This is designed and validated to government standards for secure key management. You can securely generate, store, and manage the cryptographic keys used for data encryption to make sure that only you can get access to them. AWS CloudHSM helps you comply with strict key management requirements without sacrificing application performance.

The AWS CloudHSM service works with Amazon VPC. AWS CloudHSM instances are provisioned inside your Amazon VPC with an IP address that you specify, which provides simple and private network connectivity to your Amazon EC2 instances. When you locate your HSM instances near your Amazon EC2 instances, you decrease network latency, which can improve application performance. AWS provides dedicated and exclusive (single tenant) access to HSM instances, which are isolated from other customers. Available in multiple Regions and Availability Zones, AWS CloudHSM enables you to add secure and durable key storage to your applications.

### Integration with AWS Services and Third-Party Applications
<a name="integration-with-aws-services-and-third-party-applications"></a>

You can use CloudHSM with [Amazon Redshift](https://aws.amazon.com/redshift/), [Amazon RDS](https://aws.amazon.com/rds/) for Oracle, or third-party applications (such as SafeNet Virtual KeySecure) as your Root of Trust, Apache (SSL termination), or Microsoft SQL Server (transparent data encryption). You can also use AWS CloudHSM when you write your own applications and continue to use the standard cryptographic libraries, including PKCS\#11, Java JCA/JCE, and Microsoft CAPI and CNG.

### Audit Activities
<a name="audit-activities"></a>

If you need to track resource changes, or audit activities for security and compliance purposes, you can review the management API calls over the AWS CloudHSM made from your account using [AWS CloudTrail](https://aws.amazon.com/cloudtrail/). Additionally, you can audit operations on the HSM appliance using syslog or send syslog log messages to your own log collector.

## AWS Cryptographic Services and Tools
<a name="aws-cryptographic-services-and-tools"></a>

AWS offers mechanisms that comply with a wide range of cryptographic security standards that you can use to implement best-practice encryption. The [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) is a client-side encryption library, available in Java, Python, C, JavaScript, and a command line interface that supports Linux, macOS, and Windows. It offers advanced data protection features including secure, authenticated, symmetric key algorithm suites, such as 256-bit AES-GCM with key derivation and signing. Because it was specifically designed for applications that use [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), the DynamoDB Encryption Client enables users to protect their table data before it is sent to the database. It also verifies and decrypts data when it is retrieved. The client is available in Java and Python.

### Linux DM-Crypt Infrastructure
<a name="linux-dm-crypt-infrastructure"></a>

Dm-crypt is a Linux kernel-level encryption mechanism that allows users to mount an encrypted file system. Mounting a file system is the process in which a file system is attached to a directory (mount point), which makes it available to the operating system. After mounting, all files in the file system are available to applications without any additional interaction. These files are, however, encrypted when stored on disk.

Device mapper is an infrastructure in the Linux 2.6 and 3.x kernel that provides a generic method to create virtual layers of block devices. The device mapper crypt target provides transparent encryption of block devices using the kernel crypto API. The solution in this post uses dm-crypt in conjunction with a disk-backed file system mapped to a logical volume by the Logical Volume Manager (LVM). LVM provides logical volume management for the Linux kernel.

### Client-side Encryption
<a name="client-side-encryption"></a>

Client-side encryption provides an additional layer of data protection by encrypting data before it is sent to AWS. This approach ensures that the data is encrypted at its source and remains encrypted throughout its lifecycle in the cloud, reducing the risk of unauthorized access during transmission and storage. AWS provides several tools and libraries to facilitate client-side encryption. The AWS Encryption SDK, available in multiple programming languages including Java, Python, C, and JavaScript, offers a framework for implementing envelope encryption with support for AWS KMS for key management. For Amazon S3 specifically, the [Amazon S3 Encryption Client](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/what-is-s3-encryption-client.html) enables easy implementation of client-side encryption for S3 objects. When using [Amazon DynamoDB,](https://aws.amazon.com/dynamodb/) the [AWS Database Encryption SDK](https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/what-is-database-encryption-sdk.html) allows for client-side encryption of table data before it's sent to the database. These tools support both symmetric and asymmetric encryption algorithms and can be integrated with AWS KMS for enhanced key management. By implementing client-side encryption, customers maintain full control over their encryption keys and can ensure that their most sensitive data is never exposed in plaintext outside their own environments. This approach can be particularly valuable for customers with stringent data protection requirements or those looking to implement an additional safeguard for highly sensitive personal data under the GDPR.

### Post-Quantum Cryptography
<a name="post-quantum-cryptography"></a>

AWS's encryption tools and services are evolving to address the emerging challenges of quantum computing and its potential impact on current cryptographic methods. AWS KMS supports hybrid post-quantum TLS, which combines traditional and quantum-resistant algorithms to help protect data in transit from both current and future threats. This capability is particularly relevant for data that must remain confidential over extended periods, as required by the GDPR's security principles. For implementation, AWS provides the s2n-tls library, which includes hybrid post-quantum key exchange algorithms that are being evaluated as part of NIST's Post-Quantum Cryptography standardization process. The [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) is designed with crypto-agility in mind, allowing for the integration of post-quantum algorithms as they become standardized. [AWS Certificate Manager's](https://aws.amazon.com/certificate-manager/) integration with hybrid post-quantum TLS enables customers to prepare their applications for the post-quantum era while maintaining backward compatibility. These tools support AWS's quantum-safe strategy, which includes the principle of crypto-agility – designing systems that can smoothly transition to new cryptographic algorithms as they become necessary. Customers can use AWS CloudTrail to audit their use of cryptographic operations and AWS Config to track their cryptographic configurations, helping them prepare for and manage the eventual transition to post-quantum cryptography while maintaining continuous compliance with data protection requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
