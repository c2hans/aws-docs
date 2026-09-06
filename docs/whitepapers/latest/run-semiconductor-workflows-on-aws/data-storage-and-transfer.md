---
source_url: https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/data-storage-and-transfer.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data storage and transfer
<a name="data-storage-and-transfer"></a>

 AWS offers many ways to protect data, both in transit and at rest. Many third-party storage vendors also offer additional encryption and security technologies in their own implementations of storage in the AWS Cloud.

## AWS Key Management Service (KMS)
<a name="aws-key-management-service-kms"></a>

 [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms) makes it easy for you to create and manage cryptographic keys and control their use across a wide range of AWS services and in your applications. AWS KMS is a secure and resilient service that uses hardware security modules that have been validated under FIPS 140-2, or are in the process of being validated, to protect your keys. AWS KMS is integrated with AWS CloudTrail to provide you with logs of all key usage to help meet your regulatory and compliance needs.

## Amazon EBS Encryption
<a name="amazon-ebs-encryption"></a>

 Use [Amazon EBS encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) as a straight-forward encryption solution for your EBS resources associated with your EC2 instances. With Amazon EBS encryption, you aren't required to build, maintain, and secure your own key management infrastructure. Amazon EBS encryption uses AWS Key Management Service (AWS KMS) keys (formerly CMKs) when creating encrypted volumes and snapshots.

 Encryption operations occur on the servers that host EC2 instances, ensuring the security of both data-at-rest and data-in-transit between an instance and its attached EBS storage.

 You can attach both encrypted and unencrypted volumes to an instance simultaneously.

## EC2 Instance Store Encryption
<a name="ec2-instance-store-encryption"></a>

 The data on NVMe instance store volumes is encrypted using an XTS-AES-256 cipher implemented on a hardware module on the instance. The encryption keys are generated using the hardware module and are unique to each NVMe instance storage device. All encryption keys are destroyed when the instance is stopped or terminated and cannot be recovered. You cannot disable this encryption and you cannot provide your own encryption key. For more information, see [Data protection in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances*.

## Amazon S3 Encryption
<a name="amazon-s3-encryption"></a>

 Data protection refers to protecting data while in-transit (as it travels to and from Amazon S3) and at rest (while it is stored on disks in Amazon S3 data centers). You can protect data in transit using Secure Socket Layer/Transport Layer Security (SSL/TLS) or client-side encryption. You have the following options for protecting data at rest in Amazon S3:
+  **Server-Side Encryption** – Request Amazon S3 to encrypt your object before saving it on disks in its data centers and then decrypt it when you download the objects.
+  **Client-Side Encryption** – Encrypt data client-side and upload the encrypted data to Amazon S3. In this case, you manage the encryption process, the encryption keys, and related tools.

 For more information about encryption on Amazon S3, see [Protecting data using encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html) in the *Amazon Simple Storage Service User Guide.*
