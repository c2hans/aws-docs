---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html
---

# Required permissions for Amazon S3 API operations
<a name="using-with-s3-policy-actions"></a>

**Note**
This page is about Amazon S3 policy actions for general purpose buckets. To learn more about Amazon S3 policy actions for directory buckets, see [Actions for directory buckets](s3-express-security-iam.md#s3-express-security-iam-actions).

To perform an S3 API operation, you must have the right permissions. This page maps S3 API operations to the required permissions. To grant permissions to perform an S3 API operation, you must compose a valid policy (such as an S3 bucket policy or IAM identity-based policy), and specify corresponding actions in the `Action` element of the policy. These actions are called policy actions. Not every S3 API operation is represented by a single permission (a single policy action), and some permissions (some policy actions) are required for many different API operations.

When you compose policies, you must specify the `Resource` element based on the correct resource type required by the corresponding Amazon S3 policy actions. This page categorizes permissions to S3 API operations by the resource types. For more information about the resource types, see [ Resource types defined by Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html#amazons3-resources-for-iam-policies) in the *Service Authorization Reference*. For a full list of Amazon S3 policy actions, resources, and condition keys for use in policies, see [ Actions, resources, and condition keys for Amazon S3](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html) in the *Service Authorization Reference*. For a complete list of Amazon S3 API operations, see [Amazon S3 API Actions](https://docs.aws.amazon.com//AmazonS3/latest/API/API_Operations.html) in the *Amazon Simple Storage Service API Reference*.

For more information on how to address the HTTP `403 Forbidden` errors in S3, see [Troubleshoot access denied (403 Forbidden) errors in Amazon S3](troubleshoot-403-errors.md). For more information on the IAM features to use with S3, see [How Amazon S3 works with IAM](security_iam_service-with-iam.md). For more information on S3 security best practices, see [Security best practices for Amazon S3](security-best-practices.md).

**Topics**
+ [Bucket operations and permissions](#using-with-s3-policy-actions-related-to-buckets)
+ [Object operations and permissions](#using-with-s3-policy-actions-related-to-objects)
+ [Access point for general purpose buckets operations and permissions](#using-with-s3-policy-actions-related-to-accesspoint)
+ [Object Lambda Access Point operations and permissions](#using-with-s3-policy-actions-related-to-olap)
+ [Multi-Region Access Point operations and permissions](#using-with-s3-policy-actions-related-to-mrap)
+ [Batch job operations and permissions](#using-with-s3-policy-actions-related-to-batchops)
+ [S3 Storage Lens configuration operations and permissions](#using-with-s3-policy-actions-related-to-lens)
+ [S3 Storage Lens groups operations and permissions](#using-with-s3-policy-actions-related-to-lens-groups)
+ [S3 Access Grants instance operations and permissions](#using-with-s3-policy-actions-related-to-s3ag-instances)
+ [S3 Access Grants location operations and permissions](#using-with-s3-policy-actions-related-to-s3ag-locations)
+ [S3 Access Grants grant operations and permissions](#using-with-s3-policy-actions-related-to-s3ag-grants)
+ [Account operations and permissions](#using-with-s3-policy-actions-related-to-accounts)

## Bucket operations and permissions
<a name="using-with-s3-policy-actions-related-to-buckets"></a>

Bucket operations are S3 API operations that operate on the bucket resource type. You must specify S3 policy actions for bucket operations in bucket policies or IAM identity-based policies.

In the policies, the `Resource` element must be the bucket Amazon Resource Name (ARN). For more information about the `Resource` element format and example policies, see [Bucket operations](security_iam_service-with-iam.md#using-with-s3-actions-related-to-buckets).

**Note**
To grant permissions to bucket operations in access point policies, note the following:
Permissions granted for bucket operations in an access point policy are effective only if the underlying bucket allows the same permissions. When you use an access point, you must delegate access control from the bucket to the access point or add the same permissions in the access point policy to the underlying bucket's policy.
In access point policies that grant permissions to bucket operations, the `Resource` element must be the `accesspoint` ARN. For more information about the `Resource` element format and example policies, see [Bucket operations in policies for access points for general purpose buckets](security_iam_service-with-iam.md#bucket-operations-ap). For more information about access point policies, see [Configuring IAM policies for using access points](access-points-policies.md).
Not all bucket operations are supported by access points. For more information, see [Access points compatibility with S3 operations](access-points-service-api-support.md#access-points-operations-support).

The following is the mapping of bucket operations and required policy actions.

| API operations | Policy actions | Description of policy actions |
| --- | --- | --- |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html) | (Required) `s3:CreateBucket` | Required to create a new s3 bucket. |
|  | (Conditionally required) `s3:PutBucketAcl` | Required if you want to use access control list (ACL) to specify permissions on a bucket when you make a `CreateBucket` request. |
|  | (Conditionally required) `s3:PutBucketObjectLockConfiguration`, `s3:PutBucketVersioning` | Required if you want to enable Object Lock when you create a bucket. |
|  | (Conditionally required) `s3:PutBucketOwnershipControls` | Required if you want to specify S3 Object Ownership when you create a bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataConfiguration.html) (V2 API operation. The IAM policy action name is the same for the V1 and V2 API operations.) | (Required) `s3:CreateBucketMetadataTableConfiguration`, `s3tables:CreateTableBucket`, `s3tables:CreateNamespace`, `s3tables:CreateTable`, `s3tables:GetTable`, `s3tables:PutTablePolicy`, `s3tables:PutTableEncryption`, `kms:DescribeKey` | Required to create a metadata table configuration on a general purpose bucket. <br />To create your AWS managed table bucket and the metadata tables that are specified in your metadata table configuration, you must have the specified `s3tables` permissions.<br />If you want to encrypt your metadata tables with server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), you need additional permissions in your KMS key policy. For more information, see [Setting up permissions for configuring metadata tables](metadata-tables-permissions.md).<br />If you also want to integrate your AWS managed table bucket with AWS analytics services so that you can query your metadata table, you need additional permissions. For more information, see [Integrating Amazon S3 Tables with AWS analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html). |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataTableConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucketMetadataTableConfiguration.html) (V1 API operation) | (Required) `s3:CreateBucketMetadataTableConfiguration`, `s3tables:CreateNamespace`, `s3tables:CreateTable`, `s3tables:GetTable`, `s3tables:PutTablePolicy` | Required to create a metadata table configuration on a general purpose bucket. <br />To create the metadata table in the table bucket that's specified in your metadata table configuration, you must have the specified `s3tables` permissions.<br />If you want to encrypt your metadata tables with server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), you need additional permissions. For more information, see [Setting up permissions for configuring metadata tables](metadata-tables-permissions.md).<br />If you also want to integrate your table bucket with AWS analytics services so that you can query your metadata table, you need additional permissions. For more information, see [Integrating Amazon S3 Tables with AWS analytics services](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-integrating-aws.html). |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html) | (Required) `s3:DeleteBucket` | Required to delete an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketAnalyticsConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketAnalyticsConfiguration.html) | (Required) `s3:PutAnalyticsConfiguration` | Required to delete an S3 analytics configuration from an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketCors.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketCors.html) | (Required) `s3:PutBucketCORS` | Required to delete the cross-origin resource sharing (CORS) configuration for an bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketEncryption.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketEncryption.html) | (Required) `s3:PutEncryptionConfiguration` | Required to reset the default encryption configuration for an S3 bucket as server-side encryption with Amazon S3 managed keys (SSE-S3). |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketIntelligentTieringConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketIntelligentTieringConfiguration.html) | (Required) `s3:PutIntelligentTieringConfiguration` | Required to delete the existing S3 Intelligent-Tiering configuration from an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketInventoryConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketInventoryConfiguration.html) | (Required) `s3:PutInventoryConfiguration` | Required to delete an S3 Inventory configuration from an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketLifecycle.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketLifecycle.html) | (Required) `s3:PutLifecycleConfiguration` | Required to delete the S3 Lifecycle configuration for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataTableConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataTableConfiguration.html) (V2 API operation. The IAM policy action name is the same for the V1 and V2 API operations.) | (Required) `s3:DeleteBucketMetadataTableConfiguration` | Required to delete a metadata table configuration from a general purpose bucket.  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataTableConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetadataTableConfiguration.html) (V1 API operation) | (Required) `s3:DeleteBucketMetadataTableConfiguration` | Required to delete a metadata table configuration from a general purpose bucket.  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetricsConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketMetricsConfiguration.html) | (Required) `s3:PutMetricsConfiguration` | Required to delete a metrics configuration for the Amazon CloudWatch request metrics from an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketOwnershipControls.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketOwnershipControls.html)  | (Required) `s3:PutBucketOwnershipControls` | Required to remove the Object Ownership setting for an S3 bucket. After removal, the Object Ownership setting becomes `Object writer`. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html) | (Required) `s3:DeleteBucketPolicy` | Required to delete the policy of an S3 bucket.  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketReplication.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketReplication.html) | (Required) `s3:PutReplicationConfiguration` | Required to delete the replication configuration of an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html) | (Required) `s3:PutBucketTagging` | Required to delete tags from an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketWebsite.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketWebsite.html) | (Required) `s3:DeleteBucketWebsite` | Required to remove the website configuration for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeletePublicAccessBlock.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeletePublicAccessBlock.html) (Bucket-level) | (Required) `s3:PutBucketPublicAccessBlock` | Required to remove the block public access configuration for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAccelerateConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAccelerateConfiguration.html) | (Required) `s3:GetAccelerateConfiguration` | Required to use the accelerate subresource to return the Amazon S3 Transfer Acceleration state of a bucket, which is either Enabled or Suspended. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAcl.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAcl.html) | (Required) `s3:GetBucketAcl` | Required to return the access control list (ACL) of an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAnalyticsConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAnalyticsConfiguration.html) | (Required) `s3:GetAnalyticsConfiguration` | Required to return an analytics configuration that's identified by the analytics configuration ID from an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketCors.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketCors.html) | (Required) `s3:GetBucketCORS` | Required to return the cross-origin resource sharing (CORS) configuration for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html) | (Required) `s3:GetEncryptionConfiguration` | Required to return the default encryption configuration for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketIntelligentTieringConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketIntelligentTieringConfiguration.html) | (Required) `s3:GetIntelligentTieringConfiguration` | Required to get the S3 Intelligent-Tiering configuration of an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketInventoryConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketInventoryConfiguration.html) | (Required) `s3:GetInventoryConfiguration` | Required to return an inventory configuration that's identified by the inventory configuration ID from the bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycle.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycle.html) | (Required) `s3:GetLifecycleConfiguration` | Required to return the S3 Lifecycle configuration of the bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLocation.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLocation.html) | (Required) `s3:GetBucketLocation` | Required to return the AWS Region that an S3 bucket resides in. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLogging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLogging.html) | (Required) `s3:GetBucketLogging` | Required to return the logging status of an S3 bucket and the permissions that users have to view and modify that status. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataTableConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataTableConfiguration.html) (V2 API operation. The IAM policy action name is the same for the V1 and V2 API operations.) | (Required) `s3:GetBucketMetadataTableConfiguration` | Required to retrieve a metadata table configuration for a general purpose bucket.  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataTableConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetadataTableConfiguration.html) (V1 API operation) | (Required) `s3:GetBucketMetadataTableConfiguration` | Required to retrieve a metadata table configuration for a general purpose bucket.  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetricsConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketMetricsConfiguration.html) | (Required) `s3:GetMetricsConfiguration` | Required to get a metrics configuration that's specified by the metrics configuration ID from the bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotificationConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketNotificationConfiguration.html) | (Required) `s3:GetBucketNotification` | Required to return the notification configuration of an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketOwnershipControls.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketOwnershipControls.html) | (Required) `s3:GetBucketOwnershipControls` | Required to retrieve the Object Ownership setting for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html) | (Required) `s3:GetBucketPolicy` | Required to return the policy of an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicyStatus.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicyStatus.html) | (Required) `s3:GetBucketPolicyStatus` | Required to retrieve the policy status for an S3 bucket, indicating whether the bucket is public. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketReplication.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketReplication.html) | (Required) `s3:GetReplicationConfiguration` | Required to return the replication configuration of an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketRequestPayment.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketRequestPayment.html) | (Required) `s3:GetBucketRequestPayment` | Required to return the request payment configuration for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html) | (Required) `s3:GetBucketVersioning` | Required to return the versioning state of an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html) | (Required) `s3:GetBucketTagging` | Required to return the tag set that's associated with an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketWebsite.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketWebsite.html) | (Required) `s3:GetBucketWebsite` | Required to return the website configuration for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLockConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLockConfiguration.html) | (Required) `s3:GetBucketObjectLockConfiguration` | Required to get the Object Lock configuration for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html) (Bucket-level) | (Required) `s3:GetBucketPublicAccessBlock` | Required to retrieve the block public access configuration for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadBucket.html) | (Required) `s3:ListBucket` | Required to determine if a bucket exists and if you have permission to access it. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketAnalyticsConfigurations.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketAnalyticsConfigurations.html) | (Required) `s3:GetAnalyticsConfiguration` | Required to list the analytics configurations for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketIntelligentTieringConfigurations.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketIntelligentTieringConfigurations.html) | (Required) `s3:GetIntelligentTieringConfiguration` | Required to list the S3 Intelligent-Tiering configurations of an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketInventoryConfigurations.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketInventoryConfigurations.html) | (Required) `s3:GetInventoryConfiguration` | Required to return a list of inventory configurations for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketMetricsConfigurations.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBucketMetricsConfigurations.html) | (Required) `s3:GetMetricsConfiguration` | Required to list the metrics configurations for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html) | (Required) `s3:ListBucket` | Required to list some or all (up to 1,000) of the objects in an S3 bucket. |
|  | (Conditionally required) `s3:GetObjectAcl` | Required if you want to display object owner information. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html) | (Required) `s3:ListBucket` | Required to list some or all (up to 1,000) of the objects in an S3 bucket. |
|  | (Conditionally required) `s3:GetObjectAcl` | Required if you want to display object owner information. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html) | (Required) `s3:ListBucketVersions` | Required to get metadata about all the versions of objects in an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAccelerateConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAccelerateConfiguration.html) | (Required) `s3:PutAccelerateConfiguration` | Required to set the accelerate configuration of an existing bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAcl.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAcl.html) | (Required) `s3:PutBucketAcl` | Required to use access control lists (ACLs) to set the permissions on an existing bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAnalyticsConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAnalyticsConfiguration.html) | (Required) `s3:PutAnalyticsConfiguration` | Required to set an analytics configuration for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketCors.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketCors.html) | (Required) `s3:PutBucketCORS` | Required to set the cross-origin resource sharing (CORS) configuration for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html) | (Required) `s3:PutEncryptionConfiguration` | Required to configure the default encryption for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketIntelligentTieringConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketIntelligentTieringConfiguration.html) | (Required) `s3:PutIntelligentTieringConfiguration` | Required to put the S3 Intelligent-Tiering configuration to an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketInventoryConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketInventoryConfiguration.html) | (Required) `s3:PutInventoryConfiguration` | Required to add an inventory configuration to an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycle.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLifecycle.html) | (Required) `s3:PutLifecycleConfiguration` | Required to create a new S3 Lifecycle configuration or replace an existing lifecycle configuration for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLogging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLogging.html) | (Required) `s3:PutBucketLogging` | Required to set the logging parameters for an S3 bucket and specify permissions for who can view and modify the logging parameters. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketMetricsConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketMetricsConfiguration.html) | (Required) `s3:PutMetricsConfiguration` | Required to set or update a metrics configuration for the Amazon CloudWatch request metrics of an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotificationConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketNotificationConfiguration.html) | (Required) `s3:PutBucketNotification` | Required to enable notifications of specified events for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketOwnershipControls.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketOwnershipControls.html) | (Required) `s3:PutBucketOwnershipControls` | Required to create or modify the Object Ownership setting for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketPolicy.html) | (Required) `s3:PutBucketPolicy` | Required to apply an S3 bucket policy to a bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketReplication.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketReplication.html) | (Required) `s3:PutReplicationConfiguration` | Required to create a new replication configuration or replace an existing one for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketRequestPayment.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketRequestPayment.html) | (Required) `s3:PutBucketRequestPayment` | Required to set the request payment configuration for a bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html) | (Required) `s3:PutBucketTagging` | Required to add a set of tags to an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketVersioning.html) | (Required) `s3:PutBucketVersioning` | Required to set the versioning state of an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketWebsite.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketWebsite.html) | (Required) `s3:PutBucketWebsite` | Required to configure a bucket as a website and set the configuration of the website. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLockConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLockConfiguration.html) | (Required) `s3:PutBucketObjectLockConfiguration` | Required to put Object Lock configuration on an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html) (Bucket-level) | (Required) `s3:PutBucketPublicAccessBlock` | Required to create or modify the block public access configuration for an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataInventoryTableConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataInventoryTableConfiguration.html) | (Required) `s3:UpdateBucketMetadataInventoryTableConfiguration`, `s3tables:CreateTableBucket`, `s3tables:CreateNamespace`, `s3tables:CreateTable`, `s3tables:GetTable`, `s3tables:PutTablePolicy`, `s3tables:PutTableEncryption`, `kms:DescribeKey` | Required to enable or disable an inventory table for a metadata table configuration on a general purpose bucket.<br />If you want to encrypt your inventory table with server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), you need additional permissions in your KMS key policy. For more information, see [Setting up permissions for configuring metadata tables](metadata-tables-permissions.md). |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataJournalTableConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateBucketMetadataJournalTableConfiguration.html) | (Required) `s3:UpdateBucketMetadataJournalTableConfiguration` | Required to enable or disable journal table record expiration for a metadata table configuration on a general purpose bucket. |

## Object operations and permissions
<a name="using-with-s3-policy-actions-related-to-objects"></a>

Object operations are S3 API operations that operate on the object resource type. You must specify S3 policy actions for object operations in resource-based policies (such as bucket policies, access point policies, Multi-Region Access Point policies, VPC endpoint policies) or IAM identity-based policies.

In the policies, the `Resource` element must be the object ARN. For more information about the `Resource` element format and example policies, see [Object operations](security_iam_service-with-iam.md#using-with-s3-actions-related-to-objects).

**Note**
AWS KMS policy actions (`kms:GenerateDataKey` and `kms:Decrypt`) are only applicable for the AWS KMS resource type and must be specified in IAM identity-based policies and AWS KMS resource-based policies (AWS KMS key policies). You can't specify AWS KMS policy actions in S3 resource-based policies, such as S3 bucket policies.
When you use access points to control access to object operations, you can use access point policies. To grant permissions to object operations in access point policies, note the following:
In access point policies that grant permissions to object operations, the `Resource` element must be the ARNs for objects accessed through an access point. For more information about the `Resource` element format and example policies, see [Object operations in access point policies](security_iam_service-with-iam.md#object-operations-ap).
Not all object operations are supported by access points. For more information, see [Access points compatibility with S3 operations](access-points-service-api-support.md#access-points-operations-support).
Not all object operations are supported by Multi-Region Access Points. For more information, see [Multi-Region Access Point compatibility with S3 operations](MrapOperations.md#mrap-operations-support).

The following is the mapping of object operations and required policy actions.

| API operations | Policy actions | Description of policy actions |
| --- | --- | --- |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html) | (Required) `s3:AbortMultipartUpload` | Required to abort a multipart upload. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html) | (Required) `s3:PutObject` | Required to complete a multipart upload. |
|  | (Conditionally required) `kms:Decrypt` | Required if you want to complete a multipart upload for an AWS KMS customer managed key encrypted object.  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) | For source object: | For source object: |
|  | (Required) Either `s3:GetObject` or `s3:GetObjectVersion` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)  |
|  | (Conditionally required) `kms:Decrypt` | Required if you want to copy an AWS KMS customer managed key encrypted object from the source bucket.  |
|  | For destination object: | For destination object: |
|  | (Required) `s3:PutObject` | Required to put the copied object in the destination bucket. |
|  | (Conditionally required) `s3:PutObjectAcl` | Required if you want to put the copied object with the object access control list (ACL) to the destination bucket when you make a `CopyObject` request. |
|  | (Conditionally required) `s3:PutObjectTagging` | Required if you want to put the copied object with object tagging to the destination bucket when you make a `CopyObject` request. |
|  | (Conditionally required) `kms:GenerateDataKey` | Required if you want to encrypt the copied object with an AWS KMS customer managed key and put it to the destination bucket.  |
|  | (Conditionally required) `s3:PutObjectRetention` | Required if you want to set an Object Lock retention configuration for the new object. |
|  | (Conditionally required) `s3:PutObjectLegalHold` | Required if you want to place an Object Lock legal hold on the new object. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html) | (Required) `s3:PutObject` | Required to create multipart upload. |
|  | (Conditionally required) `s3:PutObjectAcl` | Required if you want to set the object access control list (ACL) permissions for the uploaded object. |
|  | (Conditionally required) `s3:PutObjectTagging` | Required if you want to add object tagging(s) to the uploaded object. |
|  | (Conditionally required) `kms:GenerateDataKey` | Required if you want to use an AWS KMS customer managed key to encrypt an object when you initiate a multipart upload.  |
|  | (Conditionally required) `s3:PutObjectRetention` | Required if you want to set an Object Lock retention configuration for the uploaded object. |
|  | (Conditionally required) `s3:PutObjectLegalHold` | Required if you want to apply an Object Lock legal hold to the uploaded object. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html) | (Required) Either `s3:DeleteObject` or `s3:DeleteObjectVersion` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)  |
|  | (Conditionally required) `s3:BypassGovernanceRetention` | Required if you want to delete an object that's protected by governance mode for Object Lock retention. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html) | (Required) Either `s3:DeleteObject` or `s3:DeleteObjectVersion` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)  |
|  | (Conditionally required) `s3:BypassGovernanceRetention` | Required if you want to delete objects that are protected by governance mode for Object Lock retention. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html) | (Required) Either `s3:DeleteObjectTagging` or `s3:DeleteObjectVersionTagging` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) | (Required) Either `s3:GetObject` or `s3:GetObjectVersion` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)  |
|  | (Conditionally required) `kms:Decrypt` | Required if you want to get and decrypt an AWS KMS customer managed key encrypted object.  |
|  | (Conditionally required) `s3:GetObjectTagging` | Required if you want to get the tag-set of an object when you make a `GetObject` request. |
|  | (Conditionally required) `s3:GetObjectLegalHold` | Required if you want to get an object's current Object Lock legal hold status. |
|  | (Conditionally required) `s3:GetObjectRetention` | Required if you want to retrieve the Object Lock retention settings for an object. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html) | (Required) Either `s3:GetObjectAcl` or `s3:GetObjectVersionAcl` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html) | (Required) Either `s3:GetObject` or `s3:GetObjectVersion` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)  |
|  | (Conditionally required) `kms:Decrypt` | Required if you want to retrieve attributes related to an AWS KMS customer managed key encrypted object.  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLegalHold.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectLegalHold.html) | (Required) `s3:GetObjectLegalHold` | Required to get an object's current Object Lock legal hold status. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectRetention.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectRetention.html) | (Required) `s3:GetObjectRetention` | Required to retrieve the Object Lock retention settings for an object. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html) | (Required) Either `s3:GetObjectTagging` or `s3:GetObjectVersionTagging` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTorrent.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTorrent.html) | (Required) `s3:GetObject` | Required to return torrent files of an object. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html) | (Required) `s3:GetObject` | Required to retrieve metadata from an object without returning the object itself. |
|  | (Conditionally required) `s3:GetObjectLegalHold` | Required if you want to get an object's current Object Lock legal hold status. |
|  | (Conditionally required) `s3:GetObjectRetention` | Required if you want to retrieve the Object Lock retention settings for an object. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html) | (Required) `s3:ListBucketMultipartUploads` | Required to list in-progress multipart uploads in a bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html) | (Required) `s3:ListMultipartUploadParts` | Required to list the parts that have been uploaded for a specific multipart upload. |
|  | (Conditionally required) `kms:Decrypt` | Required if you want to list parts of an AWS KMS customer managed key encrypted multipart upload.  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) | (Required) `s3:PutObject` | Required to put an object. |
|  | (Conditionally required) `s3:PutObjectAcl` | Required if you want to put the object access control list (ACL) when you make a `PutObject` request. |
|  | (Conditionally required) `s3:PutObjectTagging` | Required if you want to put object tagging when you make a `PutObject` request. |
|  | (Conditionally required) `kms:GenerateDataKey` | Required if you want to encrypt an object with an AWS KMS customer managed key.  |
|  | (Conditionally required) `s3:PutObjectRetention` | Required if you want to set an Object Lock retention configuration on an object. |
|  | (Conditionally required) `s3:PutObjectLegalHold` | Required if you want to apply an Object Lock legal hold configuration to a specified object. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html) | (Required) Either `s3:PutObjectAcl` or `s3:PutObjectVersionAcl` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLegalHold.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectLegalHold.html) | (Required) `s3:PutObjectLegalHold` | Required to apply an Object Lock legal hold configuration to an object. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectRetention.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectRetention.html) | (Required) `s3:PutObjectRetention` | Required to apply an Object Lock retention configuration to an object. |
|  | (Conditionally required) `s3:BypassGovernanceRetention` | Required if you want to bypass the governance mode of an Object Lock retention configuration. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html) | (Required) Either `s3:PutObjectTagging` or `s3:PutObjectVersionTagging` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_RestoreObject.html) | (Required) `s3:RestoreObject` | Required to restore a copy of an archived object. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_SelectObjectContent.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_SelectObjectContent.html) | (Required) `s3:GetObject` | Required to filter the contents of an S3 object based on a simple structured query language (SQL) statement. |
|  | (Conditionally required) `kms:Decrypt` | Required if you want to filter the contents of an S3 object that's encrypted with an AWS KMS customer managed key. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateObjectEncryption.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UpdateObjectEncryption.html) | (Required) `s3:UpdateObjectEncryption`, `kms:Encrypt`, `kms:Decrypt`, `kms:GenerateDataKey`, `kms:ReEncrypt*`  | Required if you want to change encrypted objects between server-side encryption with Amazon S3 managed encryption (SSE-S3) and server-side encryption with AWS Key Management Service (AWS KMS) encryption keys (SSE-KMS). You can also use the `UpdateObjectEncryption` operation to apply S3 Bucket Keys to reduce AWS KMS request costs or change the customer-managed KMS key that's used to encrypt your data so that you can comply with custom key-rotation standards. |
|  | (Conditionally required) `organizations:DescribeAccount` | If you're using AWS Organizations, to use the `UpdateObjectEncryption` operation with customer-managed KMS keys from other AWS accounts within your organization, you must have the `organizations:DescribeAccount` permission.  You must also request the ability to use AWS KMS keys owned by other member accounts within your organization by contacting AWS Support.  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html) | (Required) `s3:PutObject` | Required to upload a part in a multipart upload. |
|  | (Conditionally required) `kms:GenerateDataKey` | Required if you want to put an upload part and encrypt it with an AWS KMS customer managed key. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPartCopy.html) | For source object: | For source object: |
|  | (Required) Either `s3:GetObject` or `s3:GetObjectVersion` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-policy-actions.html)  |
|  | (Conditionally required) `kms:Decrypt` | Required if you want to copy an AWS KMS customer managed key encrypted object from the source bucket.  |
|  | For destination part: | For destination part: |
|  | (Required) `s3:PutObject` | Required to upload a multipart upload part to the destination bucket. |
|  | (Conditionally required) `kms:GenerateDataKey` | Required if you want to encrypt a part with an AWS KMS customer managed key when you upload the part to the destination bucket.  |

## Access point for general purpose buckets operations and permissions
<a name="using-with-s3-policy-actions-related-to-accesspoint"></a>

Access point operations are S3 API operations that operate on the `accesspoint` resource type. You must specify S3 policy actions for access point operations in IAM identity-based policies, not in bucket policies or access point policies.

In the policies, the `Resource` element must be the `accesspoint` ARN. For more information about the `Resource` element format and example policies, see [Access point for general purpose bucket operations](security_iam_service-with-iam.md#using-with-s3-actions-related-to-accesspoint).

**Note**
If you want to use access points to control access to bucket or object operations, note the following:
For using access points to control access to bucket operations, see [Bucket operations in policies for access points for general purpose buckets](security_iam_service-with-iam.md#bucket-operations-ap).
For using access points to control access to object operations, see [Object operations in access point policies](security_iam_service-with-iam.md#object-operations-ap).
For more information about how to configure access point policies, see [Configuring IAM policies for using access points](access-points-policies.md).

The following is the mapping of access point operations and required policy actions.

| API operations | Policy actions | Description of policy actions |
| --- | --- | --- |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPoint.html) | (Required) `s3:CreateAccessPoint` | Required to create an access point that's associated with an S3 bucket. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPoint.html) | (Required) `s3:DeleteAccessPoint` | Required to delete an access point. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicy.html) | (Required) `s3:DeleteAccessPointPolicy` | Required to delete an access point policy. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html) | (Required) `s3:GetAccessPointPolicy` | Required to retrieve an access point policy. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyStatus.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyStatus.html) | (Required) `s3:GetAccessPointPolicyStatus` | Required to retrieve the information on whether the specified access point currently has a policy that allows public access. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicy.html) | (Required) `s3:PutAccessPointPolicy` | Required to put an access point policy. |

## Object Lambda Access Point operations and permissions
<a name="using-with-s3-policy-actions-related-to-olap"></a>

Object Lambda Access Point operations are S3 API operations that operate on the `objectlambdaaccesspoint` resource type. For more information about how to configure policies for Object Lambda Access Point operations, see [Configuring IAM policies for Object Lambda Access Points](olap-policies.md).

The following is the mapping of Object Lambda Access Point operations and required policy actions.

| API operations | Policy actions | Description of policy actions |
| --- | --- | --- |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPointForObjectLambda.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessPointForObjectLambda.html) | (Required) `s3:CreateAccessPointForObjectLambda` | Required to create an Object Lambda Access Point. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointForObjectLambda.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointForObjectLambda.html) | (Required) `s3:DeleteAccessPointForObjectLambda` | Required to delete a specified Object Lambda Access Point. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicyForObjectLambda.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicyForObjectLambda.html) | (Required) `s3:DeleteAccessPointPolicyForObjectLambda` | Required to delete the policy on a specified Object Lambda Access Point. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointConfigurationForObjectLambda.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointConfigurationForObjectLambda.html) | (Required) `s3:GetAccessPointConfigurationForObjectLambda` | Required to retrieve the configuration of the Object Lambda Access Point. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetAccessPointForObjectLambda.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetAccessPointForObjectLambda.html) | (Required) `s3:GetAccessPointForObjectLambda` | Required to retrieve information about the Object Lambda Access Point. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetAccessPointPolicyForObjectLambda.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetAccessPointPolicyForObjectLambda.html) | (Required) `s3:GetAccessPointPolicyForObjectLambda` | Required to return the access point policy that's associated with the specified Object Lambda Access Point. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetAccessPointPolicyStatusForObjectLambda.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetAccessPointPolicyStatusForObjectLambda.html) | (Required) `s3:GetAccessPointPolicyStatusForObjectLambda` | Required to return the policy status for a specific Object Lambda Access Point policy. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutAccessPointConfigurationForObjectLambda.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutAccessPointConfigurationForObjectLambda.html) | (Required) `s3:PutAccessPointConfigurationForObjectLambda` | Required to set the configuration of the Object Lambda Access Point. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutAccessPointPolicyForObjectLambda.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutAccessPointPolicyForObjectLambda.html) | (Required) `s3:PutAccessPointPolicyForObjectLambda` | Required to associate an access policy with a specified Object Lambda Access Point. |

## Multi-Region Access Point operations and permissions
<a name="using-with-s3-policy-actions-related-to-mrap"></a>

Multi-Region Access Point operations are S3 API operations that operate on the `multiregionaccesspoint` resource type. For more information about how to configure policies for Multi-Region Access Point operations, see [Multi-Region Access Point policy examples](MultiRegionAccessPointPermissions.md#MultiRegionAccessPointPolicyExamples).

The following is the mapping of Multi-Region Access Point operations and required policy actions.

| API operations | Policy actions | Description of policy actions |
| --- | --- | --- |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateMultiRegionAccessPoint.html) | (Required) `s3:CreateMultiRegionAccessPoint` | Required to create a Multi-Region Access Point and associate it with S3 buckets. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteMultiRegionAccessPoint.html) | (Required) `s3:DeleteMultiRegionAccessPoint` | Required to delete a Multi-Region Access Point. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeMultiRegionAccessPointOperation.html) | (Required) `s3:DescribeMultiRegionAccessPointOperation` | Required to retrieve the status of an asynchronous request to manage a Multi-Region Access Point. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPoint.html) | (Required) `s3:GetMultiRegionAccessPoint` | Required to return configuration information about the specified Multi-Region Access Point. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicy.html) | (Required) `s3:GetMultiRegionAccessPointPolicy` | Required to return the access control policy of the specified Multi-Region Access Point. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicyStatus.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointPolicyStatus.html) | (Required) `s3:GetMultiRegionAccessPointPolicyStatus` | Required to return the policy status for a specific Multi-Region Access Point about whether the specified Multi-Region Access Point has an access control policy that allows public access. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointRoutes.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetMultiRegionAccessPointRoutes.html) | (Required) `s3:GetMultiRegionAccessPointRoutes` | Required to return the routing configuration for a Multi-Region Access Point. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPointPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPointPolicy.html) | (Required) `s3:PutMultiRegionAccessPointPolicy` | Required to update the access control policy of the specified Multi-Region Access Point. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SubmitMultiRegionAccessPointRoutes.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_SubmitMultiRegionAccessPointRoutes.html) | (Required) `s3:SubmitMultiRegionAccessPointRoutes` | Required to submit an updated route configuration for a Multi-Region Access Point. |

## Batch job operations and permissions
<a name="using-with-s3-policy-actions-related-to-batchops"></a>

(Batch Operations) job operations are S3 API operations that operate on the `job` resource type. You must specify S3 policy actions for job operations in IAM identity-based policies, not in bucket policies.

In the policies, the `Resource` element must be the `job` ARN. For more information about the `Resource` element format and example policies, see [Batch job operations](security_iam_service-with-iam.md#using-with-s3-actions-related-to-batchops).

The following is the mapping of batch job operations and required policy actions.

| API operations | Policy actions | Description of policy actions |
| --- | --- | --- |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteJobTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteJobTagging.html) | (Required) `s3:DeleteJobTagging` | Required to remove tags from an existing S3 Batch Operations job. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DescribeJob.html) | (Required) `s3:DescribeJob` | Required to retrieve the configuration parameters and status for a Batch Operations job. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetJobTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetJobTagging.html) | (Required) `s3:GetJobTagging` | Required to return the tag set of an existing S3 Batch Operations job. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutJobTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutJobTagging.html) | (Required) `s3:PutJobTagging` | Required to put or replace tags on an existing S3 Batch Operations job. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobPriority.html) | (Required) `s3:UpdateJobPriority` | Required to update the priority of an existing job. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateJobStatus.html) | (Required) `s3:UpdateJobStatus` | Required to update the status for the specified job. |

## S3 Storage Lens configuration operations and permissions
<a name="using-with-s3-policy-actions-related-to-lens"></a>

S3 Storage Lens configuration operations are S3 API operations that operate on the `storagelensconfiguration` resource type. For more information about how to configure S3 Storage Lens configuration operations, see [Setting Amazon S3 Storage Lens permissions](storage_lens_iam_permissions.md).

The following is the mapping of S3 Storage Lens configuration operations and required policy actions.

| API operations | Policy actions | Description of policy actions |
| --- | --- | --- |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensConfiguration.html) | (Required) `s3:DeleteStorageLensConfiguration` | Required to delete the S3 Storage Lens configuration. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensConfigurationTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensConfigurationTagging.html) | (Required) `s3:DeleteStorageLensConfigurationTagging` | Required to delete the S3 Storage Lens configuration tags. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensConfiguration.html) | (Required) `s3:GetStorageLensConfiguration` | Required to get the S3 Storage Lens configuration. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensConfigurationTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensConfigurationTagging.html) | (Required) `s3:GetStorageLensConfigurationTagging` | Required to get the tags of S3 Storage Lens configuration. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutStorageLensConfigurationTagging.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutStorageLensConfigurationTagging.html) | (Required) `s3:PutStorageLensConfigurationTagging` | Required to put or replace tags on an existing S3 Storage Lens configuration. |

## S3 Storage Lens groups operations and permissions
<a name="using-with-s3-policy-actions-related-to-lens-groups"></a>

S3 Storage Lens groups operations are S3 API operations that operate on the `storagelensgroup` resource type. For more information about how to configure S3 Storage Lens groups permissions, see [Storage Lens groups permissions](storage-lens-groups.md#storage-lens-group-permissions).

The following is the mapping of S3 Storage Lens groups operations and required policy actions.

| API operations | Policy actions | Description of policy actions |
| --- | --- | --- |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensGroup.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteStorageLensGroup.html) | (Required) `s3:DeleteStorageLensGroup` | Required to delete an existing S3 Storage Lens group. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensGroup.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetStorageLensGroup.html) | (Required) `s3:GetStorageLensGroup` | Required to retrieve the S3 Storage Lens group configuration details. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateStorageLensGroup.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateStorageLensGroup.html) | (Required) `s3:UpdateStorageLensGroup` | Required to update the existing S3 Storage Lens group. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateStorageLensGroup.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateStorageLensGroup.html) | (Required) `s3:CreateStorageLensGroup` | Required to create a new Storage Lens group. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateStorageLensGroup.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateStorageLensGroup.html), [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html) | (Required) `s3:CreateStorageLensGroup`, `s3:TagResource` | Required to create a new Storage Lens group with tags. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensGroups.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensGroups.html) | (Required) `s3:ListStorageLensGroups` | Required to list all Storage Lens groups in your home Region. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListTagsForResource.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListTagsForResource.html) | (Required) `s3:ListTagsForResource` | Required to list the tags that were added to your Storage Lens group. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_TagResource.html) | (Required) `s3:TagResource` | Required to add or update a Storage Lens group tag for an existing Storage Lens group. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UntagResource.html) | (Required) `s3:UntagResource` | Required to delete a tag from a Storage Lens group. |

## S3 Access Grants instance operations and permissions
<a name="using-with-s3-policy-actions-related-to-s3ag-instances"></a>

S3 Access Grants instance operations are S3 API operations that operate on the `accessgrantsinstance` resource type. An S3 Access Grants instance is a logical container for your access grants. For more information on working with S3 Access Grants instances, see [Working with S3 Access Grants instances](access-grants-instance.md).

The following is the mapping of the S3 Access Grants instance configuration operations and required policy actions.

| API operations | Policy actions | Description of policy actions |
| --- | --- | --- |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AssociateAccessGrantsIdentityCenter.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_AssociateAccessGrantsIdentityCenter.html) | (Required) `s3:AssociateAccessGrantsIdentityCenter` | Required to associate an AWS IAM Identity Center instance with your S3 Access Grants instance, thus enabling you to create access grants for users and groups in your corporate identity directory. You must also have the following permissions: <br />`sso:CreateApplication`, `sso:PutApplicationGrant`, and `sso:PutApplicationAuthenticationMethod`. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrantsInstance.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrantsInstance.html) | (Required) `s3:CreateAccessGrantsInstance` | Required to create an S3 Access Grants instance (`accessgrantsinstance` resource) which is a container for your individual access grants. <br />To associate an AWS IAM Identity Center instance with your S3 Access Grants instance, you must also have the `sso:DescribeInstance`, `sso:CreateApplication`, `sso:PutApplicationGrant`, and `sso:PutApplicationAuthenticationMethod` permissions. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsInstance.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsInstance.html) | (Required) `s3:DeleteAccessGrantsInstance` | Required to delete an S3 Access Grants instance (`accessgrantsinstance` resource) from an AWS Region in your account.  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsInstanceResourcePolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsInstanceResourcePolicy.html) | (Required) `s3:DeleteAccessGrantsInstanceResourcePolicy` | Required to delete a resource policy for your S3 Access Grants instance.  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DissociateAccessGrantsIdentityCenter.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DissociateAccessGrantsIdentityCenter.html) | (Required) `s3:DissociateAccessGrantsIdentityCenter` | Required to disassociate an AWS IAM Identity Center instance from your S3 Access Grants instance. You must also have the following permissions:<br />`sso:DeleteApplication` |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstance.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstance.html) | (Required) `s3:GetAccessGrantsInstance` | Required to retrieve the S3 Access Grants instance for an AWS Region in your account. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstanceForPrefix.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstanceForPrefix.html) | (Required) `s3:GetAccessGrantsInstanceForPrefix` | Required to retrieve the S3 Access Grants instance that contains a particular prefix. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstanceResourcePolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsInstanceResourcePolicy.html) | (Required) `s3:GetAccessGrantsInstanceResourcePolicy` | Required to return the resource policy of your S3 Access Grants instance. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantsInstances.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantsInstances.html) | (Required) `s3:ListAccessGrantsInstances` | Required to return a list of the S3 Access Grants instances in your account. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessGrantsInstanceResourcePolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessGrantsInstanceResourcePolicy.html) | (Required) `s3:PutAccessGrantsInstanceResourcePolicy` | Required to update the resource policy of the S3 Access Grants instance. |

## S3 Access Grants location operations and permissions
<a name="using-with-s3-policy-actions-related-to-s3ag-locations"></a>

S3 Access Grants location operations are S3 API operations that operate on the `accessgrantslocation` resource type. For more information on working with S3 Access Grants locations, see [Working with S3 Access Grants locations](access-grants-location.md).

The following is the mapping of the S3 Access Grants location configuration operations and required policy actions.

| API operations | Policy actions | Description of policy actions |
| --- | --- | --- |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrantsLocation.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrantsLocation.html) | (Required) `s3:CreateAccessGrantsLocation` | Required to register a location in your S3 Access Grants instance (create an `accessgrantslocation` resource). You must also have the following permission for the specified IAM role: <br />`iam:PassRole` |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsLocation.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrantsLocation.html) | (Required) `s3:DeleteAccessGrantsLocation` | Required to remove a registered location from your S3 Access Grants instance.  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsLocation.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrantsLocation.html) | (Required) `s3:GetAccessGrantsLocation` | Required to retrieve the details of a particular location registered in your S3 Access Grants instance. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantsLocations.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrantsLocations.html) | (Required) `s3:ListAccessGrantsLocations` | Required to return a list of the locations registered in your S3 Access Grants instance. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateAccessGrantsLocation.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_UpdateAccessGrantsLocation.html) | (Required) `s3:UpdateAccessGrantsLocation` | Required to update the IAM role of a registered location in your S3 Access Grants instance. |

## S3 Access Grants grant operations and permissions
<a name="using-with-s3-policy-actions-related-to-s3ag-grants"></a>

S3 Access Grants grant operations are S3 API operations that operate on the `accessgrant` resource type. For more information on working with individual grants using S3 Access Grants, see [Working with grants in S3 Access Grants](access-grants-grant.md).

The following is the mapping of the S3 Access Grants grant configuration operations and required policy actions.

| API operations | Policy actions | Description of policy actions |
| --- | --- | --- |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrant.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateAccessGrant.html) | (Required) `s3:CreateAccessGrant` | Required to create an individual grant (`accessgrant` resource) for a user or group in your S3 Access Grants instance. You must also have the following permissions:<br />For any directory identity — `sso:DescribeInstance` and `sso:DescribeApplication`<br />For directory users — `identitystore:DescribeUser` |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrant.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessGrant.html) | (Required) `s3:DeleteAccessGrant` | Required to delete an individual access grant (`accessgrant` resource) from your S3 Access Grants instance.  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrant.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessGrant.html) | (Required) `s3:GetAccessGrant` | Required to get the details about an individual access grant in your S3 Access Grants instance.  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrants.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessGrants.html) | (Required) `s3:ListAccessGrants` | Required to return a list of individual access grants in your S3 Access Grants instance.  |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListCallerAccessGrants.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListCallerAccessGrants.html) | (Required) `s3:ListCallerAccessGrants` | Required to list the access grants that grant the caller access to Amazon S3 data through S3 Access Grants.  |

## Account operations and permissions
<a name="using-with-s3-policy-actions-related-to-accounts"></a>

Account operations are S3 API operations that operate on the account level. Account isn't a resource type defined by Amazon S3. You must specify S3 policy actions for account operations in IAM identity-based policies, not in bucket policies.

In the policies, the `Resource` element must be `"*"`. For more information about example policies, see [Account operations](security_iam_service-with-iam.md#using-with-s3-actions-related-to-accounts).

The following is the mapping of account operations and required policy actions.

| API operations | Policy actions | Description of policy actions |
| --- | --- | --- |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateJob.html) | (Required) `s3:CreateJob` | Required to create a new S3 Batch Operations job. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateStorageLensGroup.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateStorageLensGroup.html) | (Required) `s3:CreateStorageLensGroup` | Required to create a new S3 Storage Lens group and associate it with the specified AWS account ID. |
|  | (Conditionally required) `s3:TagResource` | Required if you want to create an S3 Storage Lens group with AWS resource tags. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeletePublicAccessBlock.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeletePublicAccessBlock.html) (Account-level) | (Required) `s3:PutAccountPublicAccessBlock` | Required to remove the block public access configuration from an AWS account. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPoint.html) | (Required) `s3:GetAccessPoint` | Required to retrieve configuration information about the specified access point. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicy.html) (Account-level) | (Required) `s3:GetAccountPublicAccessBlock` | Required to retrieve the block public access configuration for an AWS account. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPoints.html) | (Required) `s3:ListAccessPoints` | Required to list access points of an S3 bucket that are owned by an AWS account. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForObjectLambda.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListAccessPointsForObjectLambda.html) | (Required) `s3:ListAccessPointsForObjectLambda` | Required to list the Object Lambda Access Points. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html) | (Required) `s3:ListAllMyBuckets` | Required to return a list of all buckets that are owned by the authenticated sender of the request. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListJobs.html) | (Required) `s3:ListJobs` | Required to list current jobs and jobs that have ended recently. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListMultiRegionAccessPoints.html) | (Required) `s3:ListMultiRegionAccessPoints` | Required to return a list of the Multi-Region Access Points that are currently associated with the specified AWS account. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensConfigurations.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensConfigurations.html) | (Required) `s3:ListStorageLensConfigurations` | Required to get a list of S3 Storage Lens configurations for an AWS account. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensGroups.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ListStorageLensGroups.html) | (Required) `s3:ListStorageLensGroups` | Required to list all the S3 Storage Lens groups in the specified home AWS Region. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html) (Account-level) | (Required) `s3:PutAccountPublicAccessBlock` | Required to create or modify the block public access configuration for an AWS account. |
| [https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutStorageLensConfiguration.html](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutStorageLensConfiguration.html) | (Required) `s3:PutStorageLensConfiguration` | Required to put an S3 Storage Lens configuration. |
