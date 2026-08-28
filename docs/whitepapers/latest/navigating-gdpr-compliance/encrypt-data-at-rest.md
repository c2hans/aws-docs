---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/encrypt-data-at-rest.html
---

# Encrypt Data at Rest
<a name="encrypt-data-at-rest"></a>

Encrypting data at rest is vital for regulatory compliance and data protection. It helps to ensure that sensitive data saved on disks is not readable by any user or application without a valid key. AWS provides multiple options for encryption at rest and encryption key management. For example, you can use the [AWS Encryption SDK](https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/introduction.html) with an [AWS KMS Key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) created and managed in AWS KMS to encrypt arbitrary data. All AWS services that store customer data offer the ability to encrypt that data.

Encrypted data can be securely stored at rest and can be decrypted only by a party with authorized access to the AWS KMS Key. As a result, you get confidential envelope-encrypted data, policy mechanisms for authorization and authenticated encryption, and audit logging through AWS CloudTrail. Some of the AWS foundation services have built-in encryption at rest features, providing the option to encrypt data before it is written to non-volatile storage. For example, you can encrypt Amazon EBS volumes and configure Amazon S3 buckets for Server-Side Encryption (SSE) using AES-256 encryption. Amazon S3 also supports client-side encryption, which allows you to encrypt data before sending it to Amazon S3. AWS SDKs support client-side encryption to facilitate encryption and decryption operations of objects. [Amazon RDS](https://aws.amazon.com/rds/) also supports Transparent Data Encryption (TDE).

It is possible to encrypt data on Linux Amazon EC2 instance stores by using built-in Linux or Microsoft libraries. This method encrypts files transparently, which protects confidential data. As a result, applications that process the data are unaware of the disk-level encryption.

You can use two methods to encrypt files on instance stores:
+ Disk-level encryption — With this method, the entire disk, or a block within the disk, is encrypted using one or more encryption keys. Disk encryption operates below the file system level, is operating-system agnostic, and hides directory and file information, such as name and size. Encrypting File System, for example, is a Microsoft extension to the Windows NT operating system’s New Technology File System (NTFS) that provides disk encryption.
+ File system-level encryption — With this method, files and directories are encrypted, but not the entire disk or partition. File-system-level encryption operates on top of the file system and is portable across operating systems.

For Non-Volatile Memory express (NVMe) SSD instance store volumes, disk-level encryption is the default option. Data in an NVMe instance storage is encrypted using an XTS-AES-256 block cipher implemented in a hardware module on the instance. The encryption keys are generated using the hardware module and are unique to each NVMe instance storage device. All encryption keys are destroyed when the instance is stopped or terminated and cannot be recovered. You cannot use your own encryption keys.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
