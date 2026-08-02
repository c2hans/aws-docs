---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-best-practices/encrypt.html
---

# Step 5. Encrypt backup data and vault
<a name="encrypt"></a>

Organizations increasingly need to improve their data security strategy, and they might be required to meet data protection regulations as they scale in the cloud. The correct implementation of encryption methods can provide an additional layer of protection above foundational access control mechanisms. This added layer provides a mitigation if your primary access control policies fail.

For example, if you configure overly permissive access control policies on your AWS Backup data, your key management system or process can mitigate the maximum impact of a security event. This is because there are separate authorization mechanisms to access your data and encryption key, which means that the backup data is viewable only as cipher text.

To get the most from AWS Cloud encryption, encrypt data both in transit and at rest. To protect data in transit, AWS uses published API calls to access AWS Backup through the network using the[ TLS protocol](https://aws.amazon.com/blogs/security/tls-1-2-to-become-the-minimum-for-all-aws-fips-endpoints/) to provide encryption between you, your application, and the AWS Backup service. To protect data at rest, you can use AWS cloud-native [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) or [AWS CloudHSM](https://aws.amazon.com/cloudhsm/). A cloud-based hardware security model (HSM), AWS CloudHSM uses Advanced Encryption Standard (AES) with 256-bit keys (AES-256), a strong industry-adopted algorithm for encrypting data. Evaluate your data governance and regulatory requirements, and select the appropriate encryption service to encrypt your cloud data and backup vaults.

Encryption configuration differs depending on the resource type and backup operations across accounts or Regions. Certain resource types support the ability to encrypt your backups using a separate encryption key from the key used to encrypt the source resource. Because you are responsible for managing access controls to determine who can access your AWS Backup data or vault encryption keys and under which conditions, use the policy language offered by AWS KMS to define access controls on keys. You can also use [AWS Backup Audit Manager](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-audit-manager.html) to confirm that your backup is properly encrypted. For more information, see [Encryption for backups in AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html).

You can use [AWS KMS multi-Region keys](https://aws.amazon.com/blogs/security/encrypt-global-data-client-side-with-aws-kms-multi-region-keys/) to replicate keys from one Region into another. Multi-Region keys are designed to simplify encryption management when your encrypted data has to be copied into other Regions for disaster recovery. Evaluate the need to implement multi-Region AWS KMS keys as part of your overall backup strategy.
