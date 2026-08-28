---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-controls-by-caf-capability/data-controls.html
---

# Security control recommendations for protecting data
<a name="data-controls"></a>

The AWS Well-Architected Framework groups the best practices for protecting data into three categories: data classification, protecting data at rest, and protecting data in transit. The security controls in this section can help you implement best practices for data protection. These foundational best practices should be in place before you architect any workloads in the cloud. They prevent data mishandling, and they help you meet organizational, regulatory, and compliance obligations. Use the security controls in this section to implement best practices for data protection.

Controls in this section:
+ [Identify and classify data at the workload level](#data-classification)
+ [Establish controls for each data classification level](#data-controls-classification-level)
+ [Encrypt data at rest](#encrypt-data-at-rest)
+ [Encrypt data in transit](#encrypt-data-in-transit)
+ [Block public access to Amazon EBS snapshots](#block-public-ebs)
+ [Block public access to Amazon RDS snapshots](#block-public-rds)
+ [Block public access to Amazon RDS, Amazon Redshift, and AWS DMS resources](#block-public-access-instances)
+ [Block public access to Amazon S3 buckets](#block-public-access-s3)
+ [Require MFA to delete data in critical Amazon S3 buckets](#mfa-delete-s3-data)
+ [Configure Amazon OpenSearch Service domains in a VPC](#opensearch-domains-vpc)
+ [Configure alerts for AWS KMS key deletion](#kms-key-deletion)
+ [Block public access to AWS KMS keys](#block-public-access-keys)
+ [Configure load balancer listeners to use secure protocols](#load-balancer-listeners)

## Identify and classify data at the workload level
<a name="data-classification"></a>

*Data classification* is a process for identifying and categorizing the data in your network based on its criticality and sensitivity. It is a critical component of any cybersecurity risk management strategy because it helps you determine the appropriate protection and retention controls for the data. Data classification often reduces the frequency of data duplication. This can reduce storage and backup costs and accelerate searches.

We recommend that you understand the type and classification of data that your workload is processing, the associated business processes, where the data is stored, and who owns the data. Data classification helps workload owners to identify locations that store sensitive data and determine how that data should be accessed and shared. *Tags* are key-value pairs that act as metadata for organizing the AWS resources. Tags can help to manage, identify, organize, search for, and filter resources.

For more information, see the following resources:
+ [Data classification](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification-overview.html) in AWS Whitepapers
+ [Identify the data within your workload](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_identify_data.html) in the AWS Well-Architected Framework

## Establish controls for each data classification level
<a name="data-controls-classification-level"></a>

Define data protection controls for each classification level. For example, use recommended controls to secure data that is classified as public, and protect sensitive data with additional controls. Use mechanisms and tools that reduce or eliminate the need to directly access or manually process data. Automation of data identification and classification reduces the risk of misclassification, mishandling, modification, or human error.

For example, consider using Amazon Macie to scan Amazon Simple Storage Service (Amazon S3) buckets for sensitive data, such as personally identifiable information (PII). Also, you can automate the detection of unintended data access by using VPC Flow Logs in Amazon Virtual Private Cloud (Amazon VPC).

For more information, see the following resources:
+ [Define data protection controls](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_define_protection.html) in the AWS Well-Architected Framework
+ [Automate identification and classification](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_data_classification_auto_classification.html) in the AWS Well-Architected Framework
+ [AWS Privacy Reference Architecture (AWS PRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/introduction.html) in AWS Prescriptive Guidance
+ [Discovering sensitive data with Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/data-classification.html) in the Macie documentation
+ [Logging IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html?ref=wellarchitected) in the Amazon VPC documentation
+ [Common techniques to detect PHI and PII data using AWS services](https://aws.amazon.com/blogs/industries/common-techniques-to-detect-phi-and-pii-data-using-aws-services/) in the AWS for Industries blog

## Encrypt data at rest
<a name="encrypt-data-at-rest"></a>

*Data at rest* is data that is stationary in your network, such as data that is in storage. Implementing encryption and appropriate access controls for data at rest helps reduce the risk of unauthorized access. *Encryption* is a computing process that transforms plaintext data, which Is human-readable, into ciphertext. You need an encryption key in order to decrypt the content back into plaintext so that it can be used. In the AWS Cloud, you can use AWS Key Management Service (AWS KMS) to create and control cryptographic keys that help protect your data.

As discussed in [Establish controls for each data classification level](#data-controls-classification-level), we recommend creating a policy that specifies what type of data requires encryption. Include criteria for how to determine which data should be encrypted and which data should be protected with another technique, such as tokenization or hashing.

For more information, see the following resources:
+ [Configuring default encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html) in the Amazon S3 documentation
+ [Encryption by default for new EBS volumes and snapshot copies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html) in the Amazon EC2 documentation
+ [Encrypting Amazon Aurora resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html) in the Amazon Aurora documentation
+ [Introduction to the cryptographic details of AWS KMS](https://docs.aws.amazon.com/kms/latest/cryptographic-details/intro.html) in the AWS KMS documentation
+ [Creating an enterprise encryption strategy for data at rest](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-data-at-rest-encryption/welcome.html) in AWS Prescriptive Guidance
+ [Enforce encryption at rest](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_encrypt.html) in the AWS Well-Architected Framework
+ For more information about encryption in specific AWS services, see the [AWS documentation](https://docs.aws.amazon.com/index.html#products) for that service

## Encrypt data in transit
<a name="encrypt-data-in-transit"></a>

*Data in transit* is data that is actively moving through your network, such as between network resources. Encrypt all data in transit by using secure TLS protocols and cipher suites. Network traffic between the resources and the internet must be encrypted in order to help prevent unauthorized access to the data. When possible, use TLS to encrypt network traffic within your internal AWS environment.

For more information, see the following resources:
+ [Requiring HTTPS for communication between viewers and CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https-viewers-to-cloudfront.html) in the Amazon CloudFront documentation
+ [AWS PrivateLink documentation](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html)
+ [Enforce encryption in transit](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_encrypt.html) in the AWS Well-Architected Framework
+ For more information about encryption in specific AWS services, see the [AWS documentation](https://docs.aws.amazon.com/index.html#products) for that service

## Block public access to Amazon EBS snapshots
<a name="block-public-ebs"></a>

[Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) provides block-level storage volumes for use with Amazon Elastic Compute Cloud (Amazon EC2) instances. You can back up the data on your Amazon EBS volumes to Amazon S3 by taking point-in-time snapshots. You can share snapshots publicly with all other AWS accounts, or you can share them privately with individual AWS accounts that you specify.

We recommend that you don't publicly share Amazon EBS snapshots. This might inadvertently expose sensitive data. When you share a snapshot, you are giving others access to the data in the snapshot. Share snapshots only with people that you trust with all of this data.

For more information, see the following resources:
+ [Share a snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html#share-unencrypted-snapshot) in the Amazon EC2 documentation
+ [Amazon EBS snapshots should not be publicly restorable](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-1) in the AWS Security Hub CSPM documentation
+ [ebs-snapshot-public-restorable-check](https://docs.aws.amazon.com/config/latest/developerguide/ebs-snapshot-public-restorable-check.html) in the AWS Config documentation

## Block public access to Amazon RDS snapshots
<a name="block-public-rds"></a>

[Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud. Amazon RDS creates and saves automated backups of your database (DB) instance or Multi-AZ DB cluster during the backup window of your DB instance. Amazon RDS creates a storage volume snapshot of your DB instance, backing up the entire DB instance and not just individual databases. You can share a manual snapshot for the purposes of copying the snapshot or restoring a DB instance from it.

If you share a snapshot as public, make sure that none of the data in the snapshot is private or sensitive. When a snapshot is shared publicly, it gives all AWS accounts permission to access the data. This can result in unintended exposure of the data in your Amazon RDS instance.

For more information, see the following resources:
+ [Sharing a DB snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html) in the Amazon RDS documentation
+ [rds-snapshots-public-prohibited](https://docs.aws.amazon.com/config/latest/developerguide/rds-snapshots-public-prohibited.html) in the AWS Config documentation
+ [RDS snapshot should be private](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-1) in the Security Hub CSPM documentation

## Block public access to Amazon RDS, Amazon Redshift, and AWS DMS resources
<a name="block-public-access-instances"></a>

You can configure Amazon RDS DB instances, Amazon Redshift clusters, and AWS Database Migration Service (AWS DMS) replication instances to be publicly accessible. If the `publiclyAccessible` field value is `true`, then these resources are publicly accessible. Allowing public access can result in unnecessary traffic, exposure, or data leaks. We recommend that you don't allow public access to these resources.

We recommend that you enable AWS Config rules or Security Hub CSPM controls to detect whether Amazon RDS DB instances, AWS DMS replication instances, or Amazon Redshift clusters allow public access.

**Note**
The public access settings for AWS DMS replication instances can't be modified after the instance has been provisioned. To change the public access setting, delete the current instance and then recreate it. When you recreate it, don't select the **Publicly accessible** option.

For more information, see the following resources:
+ [AWS DMS replication instances should not be public](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-1) in the Security Hub CSPM documentation
+ [RDS DB Instances should prohibit public access](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-2) in the Security Hub CSPM documentation
+ [Amazon Redshift clusters should prohibit public access](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-1) in the Security Hub CSPM documentation
+ [rds-instance-public-access-check](https://docs.aws.amazon.com/config/latest/developerguide/rds-instance-public-access-check.html) in the AWS Config documentation
+ [dms-replication-not-public](https://docs.aws.amazon.com/config/latest/developerguide/dms-replication-not-public.html) in the AWS Config documentation
+ [redshift-cluster-public-access-check](https://docs.aws.amazon.com/config/latest/developerguide/redshift-cluster-public-access-check.html) in the AWS Config documentation
+ [Modifying an Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html) in the Amazon RDS documentation
+ [Modifying a cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-clusters-console.html#modify-cluster) in the Amazon Redshift documentation

## Block public access to Amazon S3 buckets
<a name="block-public-access-s3"></a>

It's an Amazon S3 security best practice to ensure that your buckets are not publicly accessible. Unless you explicitly require anyone on the internet to be able to read or write to your bucket, make sure that your bucket is not public. This helps protect the integrity and security of the data. You can use AWS Config rules and Security Hub CSPM controls to confirm that your Amazon S3 buckets are compliant with this best practice.

For more information, see the following resources:
+ [Amazon S3 security best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html#security-best-practices-prevent) in the Amazon S3 documentation
+ [S3 Block Public Access setting should be enabled](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-1) in the Security Hub CSPM documentation
+ [S3 buckets should prohibit public read access](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-2) in the Security Hub CSPM documentation
+ [S3 buckets should prohibit public write access](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-3) in the Security Hub CSPM documentation
+ [s3-bucket-public-read-prohibited rule](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-public-read-prohibited.html) in the AWS Config documentation
+ [s3-bucket-public-write-prohibited](https://docs.aws.amazon.com/config/latest/developerguide/s3-bucket-public-write-prohibited.html) in the AWS Config documentation

## Require MFA to delete data in critical Amazon S3 buckets
<a name="mfa-delete-s3-data"></a>

When working with [S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html) in Amazon S3 buckets, you can optionally add another layer of security by configuring a bucket to enable MFA (multi-factor authentication) delete. When you do this, the bucket owner must include two forms of authentication in any request to delete a version or change the versioning state of the bucket. We recommend that you enable this feature for buckets that contain data that's critical to your organization. This can prevent accidental bucket and data deletions.

For more information, see the following resources:
+ [Configuring MFA delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html) in the Amazon S3 documentation

## Configure Amazon OpenSearch Service domains in a VPC
<a name="opensearch-domains-vpc"></a>

Amazon OpenSearch Service is a managed service that helps you deploy, operate, and scale OpenSearch clusters in the AWS Cloud. Amazon OpenSearch Service supports OpenSearch and legacy Elasticsearch open source software (OSS). Amazon OpenSearch Service domains that are deployed within a VPC can communicate with VPC resources over the private AWS network, without the need to traverse the public internet. This configuration improves your security posture by restricting access to the data in transit. We recommend that you don't attach Amazon OpenSearch Service domains to public subnets and that the VPC is configured according to best practices.

For more information, see the following resources:
+ [Launching your Amazon OpenSearch Service domains within a VPC](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vpc.html) in the Amazon OpenSearch Service documentation
+ [opensearch-in-vpc-only](https://docs.aws.amazon.com/config/latest/developerguide/opensearch-in-vpc-only.html) in the AWS Config documentation
+ [OpenSearch domains should be in a VPC](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-2) in the Security Hub CSPM documentation

## Configure alerts for AWS KMS key deletion
<a name="kms-key-deletion"></a>

AWS Key Management Service (AWS KMS) keys cannot be recovered after they have been deleted. If a KMS key is delete, data that is still encrypted under that key is permanently unrecoverable. If you need to retain access to the data, before you delete the key, you must decrypt the data or reencrypt it with a new KMS key. You should delete a KMS key only when you are sure that you don't need to use it anymore.

We recommend that you configure an Amazon CloudWatch alarm that notifies you if someone initiates deletion of a KMS key. Because it is destructive and potentially dangerous to delete a KMS key, AWS KMS requires that you set a waiting period and schedule deletion in 7–30 days. This provides an opportunity to review the scheduled deletion and cancel it, if necessary.

For more information, see the following resources:
+ [Scheduling and canceling key deletion](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-scheduling-key-deletion.html#deleting-keys-scheduling-key-deletion-console) in the AWS KMS documentation
+ [Creating an alarm that detects use of a KMS key pending deletion](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-creating-cloudwatch-alarm.html) in the AWS KMS documentation
+ [AWS KMS keys should not be deleted unintentionally](https://docs.aws.amazon.com/securityhub/latest/userguide/kms-controls.html#kms-3) in the Security Hub CSPM documentation

## Block public access to AWS KMS keys
<a name="block-public-access-keys"></a>

[Key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) are the primary way to control access to AWS KMS keys. Every KMS key has exactly one key policy. Allowing anonymous access to KMS keys can lead to a sensitive data leak. We recommend that you identify any publicly accessible KMS keys and update their access policies in order to prevent unsigned requests made to these resources.

For more information, see the following resources:
+ [Security best practices for AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html) in the AWS KMS documentation
+ [Changing a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html) in the AWS KMS documentation
+ [Determining access to AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/determining-access.html) in the AWS KMS documentation

## Configure load balancer listeners to use secure protocols
<a name="load-balancer-listeners"></a>

[Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) automatically distributes incoming application traffic across multiple targets. You configure your load balancer to accept incoming traffic by specifying one or more *listeners*. A listener is a process that checks for connection requests, using the protocol and port that you configure. Each type of load balancer supports different protocols and ports:
+ [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) make routing decisions at the application layer and use HTTP or HTTPS protocols.
+ [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) make routing decisions at the transport layer and use TCP, TLS, UDP, or TCP\_UDP protocols.
+ [Classic Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/introduction.html) make routing decisions at either the transport layer (by using TCP or SSL protocols) or at the application layer (by using HTTP or HTTPS protocols).

We recommend that you always use HTTPS or TLS protocols. These protocols make sure that the load balancer is responsible for encrypting and decrypting the traffic between the client and the target.

For more information, see the following resources:
+ [Listeners for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html) in the Elastic Load Balancing documentation
+ [Listeners for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-listener-config.html) in the Elastic Load Balancing documentation
+ [Listeners for your Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html) in the Elastic Load Balancing documentation
+ [Ensure AWS load balancers use secure listener protocols](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/ensure-aws-load-balancers-use-secure-listener-protocols-https-ssl-tls.html) in AWS Prescriptive Guidance
+ [elb-tls-https-listeners-only](https://docs.aws.amazon.com/config/latest/developerguide/elb-tls-https-listeners-only.html) in the AWS Config documentation
+ [Classic Load Balancer listeners should be configured with HTTPS or TLS termination](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-3) in the Security Hub CSPM documentation
+ [Application Load Balancer should be configured to redirect all HTTP requests to HTTPS](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-1) in the Security Hub CSPM documentation

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
