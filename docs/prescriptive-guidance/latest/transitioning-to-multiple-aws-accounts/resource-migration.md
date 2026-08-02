---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/resource-migration.html
---

# Resource migration
<a name="resource-migration"></a>

After migrating from a single AWS account to multi-account architecture, it's common to have production and non-production workloads running in the preexisting account. Migrating these resources to dedicated production and non-production accounts or organizational units helps you manage access and networking for these workloads. The following are some options for migrating common AWS resources into another AWS account.

This section focuses on strategies for replicating data between AWS accounts. You should strive to have your workloads be as stateless as possible to avoid needing to replicate compute resources between accounts. It is also beneficial to manage your resources through infrastructure as code (IaC) so that you can reprovision an environment in a separate AWS account.

This section reviews options for migrating the following data resources:
+ [AWS AppConfig configurations and environments](#aws-appconfig)
+ [AWS Certificate Manager certificates](#aws-certificate-manager)
+ [Amazon CloudFront distributions](#amazon-cloudfront)
+ [AWS CodeArtifact domains and repositories](#aws-codeartifact)
+ [Amazon DynamoDB tables](#amazon-dynamodb)
+ [Amazon EBS volumes](#amazon-ebs)
+ [Amazon EC2 instances or AMIs](#amazon-ec2)
+ [Amazon ECR registries](#amazon-ecr)
+ [Amazon EFS file systems](#amazon-efs)
+ [Amazon ElastiCache (Redis OSS) clusters](#amazon-elasticache)
+ [AWS Elastic Beanstalk environments](#aws-elastic-beanstalk)
+ [Elastic IP addresses](#elastic-ip-addresses)
+ [AWS Lambda layers](#aws-lambda)
+ [Amazon Lightsail](#amazon-lightsail)
+ [Amazon Neptune clusters](#amazon-neptune)
+ [Amazon OpenSearch Service domains](#amazon-opensearch-service)
+ [Amazon RDS snapshots](#amazon-rds)
+ [Amazon Redshift clusters](#amazon-redshift)
+ [Amazon Route 53 domains and hosted zones](#amazon-route-53)
+ [Amazon S3 buckets](#amazon-s3)
+ [Amazon SageMaker Runtime models](#amazon-sagemaker)
+ [AWS WAF web ACLs](#aws-waf)

## AWS AppConfig configurations and environments
<a name="aws-appconfig"></a>

AWS AppConfig doesn't support directly copying its configuration to another AWS account. However, it is a best practice to manage the AWS AppConfig configurations and environments separately from the AWS accounts that are hosting the environments. For more information, see [Cross-account configuration with AWS AppConfig](https://aws.amazon.com/blogs/mt/cross-account-configuration-with-aws-appconfig/) (AWS blog post).

## AWS Certificate Manager certificates
<a name="aws-certificate-manager"></a>

You can't directly export an AWS Certificate Manager (ACM) certificate from one account to another because the AWS Key Management Service (AWS KMS) key used to encrypt the certificate's private key is unique to each Region and account. However, you can simultaneously provision multiple certificates with the same domain name across multiple accounts and Regions. ACM supports validating domain ownership by using DNS (recommended) or email. When you use DNS validation and create a new certificate, ACM generates a unique CNAME record for every domain on the certificate. The CNAME record is unique for each account, and it must be added to the Route 53 hosted zone or DNS provider within 72 hours for the certificate to be properly validated.

## Amazon CloudFront distributions
<a name="amazon-cloudfront"></a>

Amazon CloudFront doesn't support migration of distributions from one AWS account to another AWS account. However, CloudFront does support the migration of an alternate domain name, also known as a *CNAME*, from one distribution to another. For more information, see [How do I resolve the CNAMEAlreadyExists error when I set up a CNAME alias for my CloudFront distribution](https://repost.aws/knowledge-center/resolve-cnamealreadyexists-error) (AWS Knowledge Center).

## AWS CodeArtifact domains and repositories
<a name="aws-codeartifact"></a>

Although an organization can have multiple domains, the recommendation is to have a single production domain that contains all published artifacts. This helps development teams find and share packages across an organization. The AWS account that owns the domain can be different from the account that owns any repositories associated to the domain. You can copy packages between repositories, but they must belong to the same domain. For more information, see [Copy packages between repositories](https://docs.aws.amazon.com/codeartifact/latest/ug/copy-package.html) (CodeArtifact documentation).

## Amazon DynamoDB tables
<a name="amazon-dynamodb"></a>

You can use one of the following services to migrate a Amazon DynamoDB table to a different AWS account:
+ AWS Backup
+ Amazon DynamoDB import and export to Amazon S3
+ Amazon S3 and AWS Glue
+ AWS Data Pipeline
+ Amazon EMR

For more information, see [How can I migrate my Amazon DynamoDB tables from one AWS account to another](https://repost.aws/knowledge-center/dynamodb-cross-account-migration) (AWS Knowledge Center).

## Amazon EBS volumes
<a name="amazon-ebs"></a>

You can take a snapshot of an existing Amazon Elastic Block Store (Amazon EBS) volume, share the snapshot with the target account, and then create a copy of the volume in the target account. This effectively migrates the volume from one account to another. For more information, see [How can I share an encrypted Amazon EBS snapshot or volume with another AWS account](https://repost.aws/knowledge-center/share-ebs-volume) (AWS Knowledge Center).

## Amazon EC2 instances or AMIs
<a name="amazon-ec2"></a>

It is not possible to directly transfer existing Amazon Elastic Compute Cloud (Amazon EC2) instances or Amazon Machine Images (AMIs) to a different AWS account. Instead, you can create a custom AMI in the source account, share the AMI with the target account, launch a new EC2 instance from the shared AMI in the target account, then deregister the shared AMI. For more information, see [How do I transfer an Amazon EC2 instance or AMI to a different AWS account](https://repost.aws/knowledge-center/account-transfer-ec2-instance) (AWS Knowledge Center).

## Amazon ECR registries
<a name="amazon-ecr"></a>

Amazon Elastic Container Registry (Amazon ECR) supports both cross-account and cross-Region replication. You configure replication on the source registry and a registry permissions policy on the target registry. For more information, see [Configuring cross-account replication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-settings-examples.html#registry-settings-examples-crossaccount) (Amazon ECR documentation) and [Allow the root user of a source account to replicate all repositories](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions-examples.html#registry-permissions-examples-all) (Amazon ECR documentation).

## Amazon EFS file systems
<a name="amazon-efs"></a>

Amazon Elastic File System (Amazon EFS) supports cross-account and cross-Region replication. You can configure replication on the source file system. For more information, see [Replicating file systems](https://docs.aws.amazon.com/efs/latest/ug/efs-replication.html) (Amazon EFS documentation).

## Amazon ElastiCache (Redis OSS) clusters
<a name="amazon-elasticache"></a>

You can use a backup of an Amazon ElastiCache (Redis OSS) database cluster to migrate it to a different account. For more information, see [What are best practices for migrating my ElastiCache (Redis OSS) cluster](https://repost.aws/knowledge-center/elasticache-redis-migrate-best-practices) (AWS Knowledge Center).

## AWS Elastic Beanstalk environments
<a name="aws-elastic-beanstalk"></a>

For AWS Elastic Beanstalk, you can use [saved configurations](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environment-configuration-savedconfig.html) (Elastic Beanstalk documentation) to migrate an environment to a different AWS account. For more information, see [How do I migrate my Elastic Beanstalk environment from one AWS account to another AWS account](https://repost.aws/knowledge-center/elastic-beanstalk-migration-accounts) (AWS Knowledge Center).

## Elastic IP addresses
<a name="elastic-ip-addresses"></a>

You can transfer Elastic IP addresses between AWS accounts that are in the same AWS Region. For more information, see [Transfer Elastic IP addresses](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html#transfer-EIPs-intro) (Amazon VPC documentation).

## AWS Lambda layers
<a name="aws-lambda"></a>

By default, an AWS Lambda layer that you create is private to your AWS account. However, you can optionally share the layer with other AWS accounts or make it public. To copy a layer, you reprovision it in another AWS account. For more information, see [Configuring layer permissions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html#configuration-layers-permissions) (Lambda documentation).

## Amazon Lightsail
<a name="amazon-lightsail"></a>

You can create a snapshot of an Amazon Lightsail instance and export the snapshot to an Amazon Machine Image (AMI) and an encrypted snapshot of an Amazon EBS volume. For more information, see [Exporting Amazon Lightsail snapshots to Amazon EC2](https://aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-exporting-snapshots-to-amazon-ec2) (Lightsail documentation). By default, the snapshot is encrypted with an AWS managed key created in AWS Key Management Service (AWS KMS). However, this type of KMS key cannot be shared between AWS accounts. Instead, you manually encrypt a copy of the AMI with a customer managed key that can be used from the target account. For more information, see [Allowing users in other accounts to use a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying-external-accounts.html) (AWS KMS documentation). You can then share the copied AMI with the target AWS account and launch a new EC2 instance for Lightsail from the copied AMI. For more information, see [Launch an instance using the new launch instance wizard](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html#liw-quickly-launch-instance) (Amazon EC2 documentation).

## Amazon Neptune clusters
<a name="amazon-neptune"></a>

You can copy an automated snapshot of the Amazon Neptune database cluster to another AWS account. For more information, see [Copying a database (DB) cluster snapshot](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-copy-snapshot.html) (Neptune documentation).

You can also share a manual snapshot with up to 20 AWS accounts that can directly restore a DB cluster from the snapshot. For more information, see [Sharing a DB Cluster Snapshot](https://docs.aws.amazon.com/neptune/latest/userguide/backup-restore-share-snapshot.html) (Neptune documentation).

## Amazon OpenSearch Service domains
<a name="amazon-opensearch-service"></a>

To copy data between Amazon OpenSearch Service domains, you can use Amazon S3 to create a snapshot of the source domain and then restore the snapshot into a target domain in a different AWS account. For more information, see [How do I restore data from an Amazon OpenSearch Service domain in another AWS account](https://repost.aws/knowledge-center/opensearch-restore-data) (AWS Knowledge Center).

If you have network connectivity between the AWS accounts, you can also use the [cross-cluster replication](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/replication.html) (OpenSearch Service documentation) feature in OpenSearch Service.

## Amazon RDS snapshots
<a name="amazon-rds"></a>

For Amazon Relational Database Service (Amazon RDS), you can share manual snapshots of DB instances or clusters with up to 20 AWS accounts. You can then restore the DB instance or DB cluster from the shared snapshot. For more information, see [How do I share manual Amazon RDS DB snapshots or Aurora DB cluster snapshots with another AWS account](https://repost.aws/knowledge-center/rds-snapshots-share-account) (AWS Knowledge Center).

You can also use AWS Database Migration Service (AWS DMSs) to configure continuous replication between database instances in different accounts. However, this requires network connectivity between the accounts, such as VPC peering or a transit gateway.

## Amazon Redshift clusters
<a name="amazon-redshift"></a>

To migrate an Amazon Redshift cluster to a different AWS account, you create a manual snapshot of the cluster in the source account, share the snapshot with the target AWS account, and then restore the cluster from the snapshot. For more information, see [How do I copy an Amazon Redshift provisioned cluster to a different AWS account](https://repost.aws/knowledge-center/account-transfer-redshift) (AWS Knowledge Center).

## Amazon Route 53 domains and hosted zones
<a name="amazon-route-53"></a>

You can transfer Amazon Route 53 domains between AWS accounts. For more information, see [Transfer a domain to a different AWS account](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-between-aws-accounts.html) (Route 53 documentation).

You can also migrate a Route 53 hosted zone to a different AWS account. For more information about when this is recommended or required, see [Migrate a hosted zone to a different AWS account](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-between-aws-accounts.html#domain-transfer-between-aws-accounts-hosted-zone) (Route 53 documentation). When you migrate a hosted zone, you recreate it in the target AWS account. For instructions, see [Migrating a hosted zone to a different AWS account](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-migrating.html) (Route 53 documentation).

## Amazon S3 buckets
<a name="amazon-s3"></a>

You can use Amazon Simple Storage Service (Amazon S3) Same-Region Replication to copy objects between S3 buckets in the same AWS Region. For more information, see [Replicating objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) (Amazon S3 documentation). Note the following:
+ Change the replica ownership to the AWS account that owns the destination bucket. For instructions, see [Changing the replica owner](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-change-owner.html) (Amazon S3 documentation).
+ Update the bucket owner conditions to reflect the AWS account ID of the target bucket. For more information, see [Verifying bucket ownership with bucket owner condition](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-owner-condition.html) (Amazon S3 documentation).
+ As of April 2023, the **Bucket owner enforced setting** is enabled for newly created buckets, making bucket access control lists (ACLs) and object ACLs ineffective. For more information, see [Amazon S3 Security Changes Are Coming](https://aws.amazon.com/blogs/aws/heads-up-amazon-s3-security-changes-are-coming-in-april-of-2023/) (AWS blog post)
+ You can use [S3 Batch Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-batch-replication-batch.html) (Amazon S3 documentation) to replicate objects that existed before replication was configured.

## Amazon SageMaker models
<a name="amazon-sagemaker"></a>

Amazon SageMaker models are stored in an Amazon S3 bucket during training. By granting access to the S3 bucket from the target account, you can deploy a model stored in the source account to the target account. For more information, see [How can I deploy an Amazon SageMaker model to a different AWS account](https://repost.aws/knowledge-center/sagemaker-cross-account-model) (AWS Knowledge Center).

## AWS WAF web ACLs
<a name="aws-waf"></a>

AWS WAF web access control lists (web ACLs) must reside in the same account as the resources they are associated to, such as Amazon CloudFront distributions, Application Load Balancers, Amazon API Gateway REST APIs, and AWS AppSync GraphQL APIs. You can use AWS Firewall Manager to centrally manage AWS WAF web ACLs across your entire organization in AWS Organizations and across Regions. For more information, see [Getting started with AWS Firewall ManagerAWS WAF policies](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-fms.html) (Firewall Manager documentation).
