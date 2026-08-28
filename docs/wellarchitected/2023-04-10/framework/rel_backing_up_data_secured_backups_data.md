---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/rel_backing_up_data_secured_backups_data.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL09-BP02 Secure and encrypt backups
<a name="rel_backing_up_data_secured_backups_data"></a>

Control and detect access to backups using authentication and authorization. Prevent and detect if data integrity of backups is compromised using encryption.

 **Common anti-patterns:**
+  Having the same access to the backups and restoration automation as you do to the data.
+  Not encrypting your backups.

 **Benefits of establishing this best practice:** Securing your backups prevents tampering with the data, and encryption of the data prevents access to that data if it is accidentally exposed.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Control and detect access to backups using authentication and authorization, such as AWS Identity and Access Management (IAM). Prevent and detect if data integrity of backups is compromised using encryption.

 Amazon S3 supports several methods of encryption of your data at rest. Using server-side encryption, Amazon S3 accepts your objects as unencrypted data, and then encrypts them as they are stored. Using client-side encryption, your workload application is responsible for encrypting the data before it is sent to Amazon S3. Both methods allow you to use AWS Key Management Service (AWS KMS) to create and store the data key, or you can provide your own key, which you are then responsible for. Using AWS KMS, you can set policies using IAM on who can and cannot access your data keys and decrypted data.

 For Amazon RDS, if you have chosen to encrypt your databases, then your backups are encrypted also. DynamoDB backups are always encrypted. When using AWS Elastic Disaster Recovery, all data in transit and at rest is encrypted. With Elastic Disaster Recovery, data at rest can be encrypted using either the default Amazon EBS encryption Volume Encryption Key or a custom customer-managed key.

 **Implementation steps**

1.  Use encryption on each of your data stores. If your source data is encrypted, then the backup will also be encrypted.
   + [Use encryption in Amazon RDS.](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html). You can configure encryption at rest using AWS Key Management Service when you create an RDS instance.
   + [Use encryption on Amazon EBS volumes.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html). You can configure default encryption or specify a unique key upon volume creation.
   +  Use the required [Amazon DynamoDB encryption](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EncryptionAtRest.html). DynamoDB encrypts all data at rest. You can either use an AWS owned AWS KMS key or an AWS managed KMS key, specifying a key that is stored in your account.
   + [Encrypt your data stored in Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/encryption.html). Configure the encryption when you create your file system.
   +  Configure the encryption in the source and destination Regions. You can configure encryption at rest in Amazon S3 using keys stored in KMS, but the keys are Region-specific. You can specify the destination keys when you configure the replication.
   +  Choose whether to use the default or custom [Amazon EBS encryption for Elastic Disaster Recovery](https://docs.aws.amazon.com/drs/latest/userguide/volumes-drs.html#ebs-encryption). This option will encrypt your replicated data at rest on the Staging Area Subnet disks and the replicated disks.

1.  Implement least privilege permissions to access your backups. Follow best practices to limit the access to the backups, snapshots, and replicas in accordance with [security best practices](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html).

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Marketplace: products that can be used for backup](https://aws.amazon.com/marketplace/search/results?searchTerms=Backup)
+  [Amazon EBS Encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)
+  [Amazon S3: Protecting Data Using Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html)
+  [CRR Additional Configuration: Replicating Objects Created with Server-Side Encryption (SSE) Using Encryption Keys stored in AWS KMS](https://docs.aws.amazon.com/AmazonS3/latest/dev/crr-replication-config-for-kms-objects.html)
+  [DynamoDB Encryption at Rest](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EncryptionAtRest.html)
+  [Encrypting Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)
+  [Encrypting Data and Metadata in Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/encryption.html)
+  [Encryption for Backups in AWS](https://docs.aws.amazon.com/aws-backup/latest/devguide/encryption.html)
+  [Managing Encrypted Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/encryption.tutorial.html)
+  [Security Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)
+ [ What is AWS Elastic Disaster Recovery? ](https://docs.aws.amazon.com/drs/latest/userguide/what-is-drs.html)

 **Related examples:**
+  [Well-Architected Lab - Implementing Bi-Directional Cross-Region Replication (CRR) for Amazon S3](https://wellarchitectedlabs.com/reliability/200_labs/200_bidirectional_replication_for_s3/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
