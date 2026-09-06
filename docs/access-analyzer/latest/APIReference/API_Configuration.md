---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_Configuration.html
---

# Configuration
<a name="API_Configuration"></a>

Access control configuration structures for your resource. You specify the configuration as a type-value pair. You can specify only one type of access control configuration.

## Contents
<a name="API_Configuration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** dynamodbStream **   <a name="accessanalyzer-Type-Configuration-dynamodbStream"></a>
The access control configuration is for a DynamoDB stream.
Type: [DynamodbStreamConfiguration](API_DynamodbStreamConfiguration.md) object
Required: No

 ** dynamodbTable **   <a name="accessanalyzer-Type-Configuration-dynamodbTable"></a>
The access control configuration is for a DynamoDB table or index.
Type: [DynamodbTableConfiguration](API_DynamodbTableConfiguration.md) object
Required: No

 ** ebsSnapshot **   <a name="accessanalyzer-Type-Configuration-ebsSnapshot"></a>
The access control configuration is for an Amazon EBS volume snapshot.
Type: [EbsSnapshotConfiguration](API_EbsSnapshotConfiguration.md) object
Required: No

 ** ecrRepository **   <a name="accessanalyzer-Type-Configuration-ecrRepository"></a>
The access control configuration is for an Amazon ECR repository.
Type: [EcrRepositoryConfiguration](API_EcrRepositoryConfiguration.md) object
Required: No

 ** efsFileSystem **   <a name="accessanalyzer-Type-Configuration-efsFileSystem"></a>
The access control configuration is for an Amazon EFS file system.
Type: [EfsFileSystemConfiguration](API_EfsFileSystemConfiguration.md) object
Required: No

 ** iamRole **   <a name="accessanalyzer-Type-Configuration-iamRole"></a>
The access control configuration is for an IAM role.
Type: [IamRoleConfiguration](API_IamRoleConfiguration.md) object
Required: No

 ** kmsKey **   <a name="accessanalyzer-Type-Configuration-kmsKey"></a>
The access control configuration is for a KMS key.
Type: [KmsKeyConfiguration](API_KmsKeyConfiguration.md) object
Required: No

 ** rdsDbClusterSnapshot **   <a name="accessanalyzer-Type-Configuration-rdsDbClusterSnapshot"></a>
The access control configuration is for an Amazon RDS DB cluster snapshot.
Type: [RdsDbClusterSnapshotConfiguration](API_RdsDbClusterSnapshotConfiguration.md) object
Required: No

 ** rdsDbSnapshot **   <a name="accessanalyzer-Type-Configuration-rdsDbSnapshot"></a>
The access control configuration is for an Amazon RDS DB snapshot.
Type: [RdsDbSnapshotConfiguration](API_RdsDbSnapshotConfiguration.md) object
Required: No

 ** s3Bucket **   <a name="accessanalyzer-Type-Configuration-s3Bucket"></a>
The access control configuration is for an Amazon S3 bucket.
Type: [S3BucketConfiguration](API_S3BucketConfiguration.md) object
Required: No

 ** s3ExpressDirectoryBucket **   <a name="accessanalyzer-Type-Configuration-s3ExpressDirectoryBucket"></a>
The access control configuration is for an Amazon S3 directory bucket.
Type: [S3ExpressDirectoryBucketConfiguration](API_S3ExpressDirectoryBucketConfiguration.md) object
Required: No

 ** secretsManagerSecret **   <a name="accessanalyzer-Type-Configuration-secretsManagerSecret"></a>
The access control configuration is for a Secrets Manager secret.
Type: [SecretsManagerSecretConfiguration](API_SecretsManagerSecretConfiguration.md) object
Required: No

 ** snsTopic **   <a name="accessanalyzer-Type-Configuration-snsTopic"></a>
The access control configuration is for an Amazon SNS topic
Type: [SnsTopicConfiguration](API_SnsTopicConfiguration.md) object
Required: No

 ** sqsQueue **   <a name="accessanalyzer-Type-Configuration-sqsQueue"></a>
The access control configuration is for an Amazon SQS queue.
Type: [SqsQueueConfiguration](API_SqsQueueConfiguration.md) object
Required: No

## See Also
<a name="API_Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/Configuration)
