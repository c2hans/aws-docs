---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-09.html
---

# WKLD.09 Encrypt Amazon RDS databases
<a name="wkld-09"></a>

Enable encryption for [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/) databases to protect data at rest. Amazon RDS encrypts data at the underlying volume level and delivers the same IOPS performance as unencrypted volumes with a minimal effect on latency. For more information, see [Overview of encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html) in the Amazon RDS documentation.

To encrypt a new Amazon RDS database instance, see [Encrypt a database instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html#Overview.Encryption.Enabling) in the Amazon RDS documentation.

**Note**
Encryption must be enabled when creating the database. You cannot enable encryption on an existing unencrypted Amazon RDS database instance. If you need to encrypt an existing unencrypted database, you must create a new encrypted database and migrate your data. For more information, see [Copying a DB snapshot for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CopySnapshot.html) in the Amazon RDS documentation.

**Note**
Encrypting Amazon RDS databases with an AWS managed AWS KMS key is available at no additional charge. Customer-managed keys incur a monthly charge per key and a charge per API call. For more information, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/).
