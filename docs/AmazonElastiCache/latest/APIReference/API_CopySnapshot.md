---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_CopySnapshot.html
---

# CopySnapshot
<a name="API_CopySnapshot"></a>

Makes a copy of an existing snapshot.

**Note**
This operation is valid for Valkey or Redis OSS only.

**Important**
Users or groups that have permissions to use the `CopySnapshot` operation can create their own Amazon S3 buckets and copy snapshots to it. To control access to your snapshots, use an IAM policy to control who has the ability to use the `CopySnapshot` operation. For more information about using IAM to control the use of ElastiCache operations, see [Exporting Snapshots](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html) and [Authentication & Access Control](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/IAM.html).

You could receive the following error messages.

**Error Messages**
+  **Error Message:** The S3 bucket %s is outside of the region.

   **Solution:** Create an Amazon S3 bucket in the same region as your snapshot. For more information, see [Step 1: Create an Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-create-s3-bucket) in the ElastiCache User Guide.
+  **Error Message:** The S3 bucket %s does not exist.

   **Solution:** Create an Amazon S3 bucket in the same region as your snapshot. For more information, see [Step 1: Create an Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-create-s3-bucket) in the ElastiCache User Guide.
+  **Error Message:** The S3 bucket %s is not owned by the authenticated user.

   **Solution:** Create an Amazon S3 bucket in the same region as your snapshot. For more information, see [Step 1: Create an Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-create-s3-bucket) in the ElastiCache User Guide.
+  **Error Message:** The authenticated user does not have sufficient permissions to perform the desired activity.

   **Solution:** Contact your system administrator to get the needed permissions.
+  **Error Message:** The S3 bucket %s already contains an object with key %s.

   **Solution:** Give the `TargetSnapshotName` a new and unique value. If exporting a snapshot, you could alternatively create a new Amazon S3 bucket and use this same value for `TargetSnapshotName`.
+  **Error Message: ** ElastiCache has not been granted READ permissions %s on the S3 Bucket.

   **Solution:** Add List and Read permissions on the bucket. For more information, see [Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-grant-access) in the ElastiCache User Guide.
+  **Error Message: ** ElastiCache has not been granted WRITE permissions %s on the S3 Bucket.

   **Solution:** Add Upload/Delete permissions on the bucket. For more information, see [Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-grant-access) in the ElastiCache User Guide.
+  **Error Message: ** ElastiCache has not been granted READ\_ACP permissions %s on the S3 Bucket.

   **Solution:** Add View Permissions on the bucket. For more information, see [Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-grant-access) in the ElastiCache User Guide.

## Request Parameters
<a name="API_CopySnapshot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** SourceSnapshotName **
The name of an existing snapshot from which to make a copy.
Type: String
Required: Yes

 ** TargetSnapshotName **
A name for the snapshot copy. ElastiCache does not permit overwriting a snapshot, therefore this name must be unique within its context - ElastiCache or an Amazon S3 bucket if exporting. This value is stored as a lowercase string.
Type: String
Required: Yes

 ** KmsKeyId **
The ID of the KMS key used to encrypt the target snapshot.
Type: String
Required: No

 **Tags.Tag.N**
A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** TargetBucket **
The Amazon S3 bucket to which the snapshot is exported. This parameter is used only when exporting a snapshot for external access.
When using this parameter to export a snapshot, be sure Amazon ElastiCache has the needed permissions to this S3 bucket. For more information, see [Step 2: Grant ElastiCache Access to Your Amazon S3 Bucket](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html#backups-exporting-grant-access) in the *Amazon ElastiCache User Guide*.
For more information, see [Exporting a Snapshot](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/backups-exporting.html) in the *Amazon ElastiCache User Guide*.
Type: String
Required: No

## Response Elements
<a name="API_CopySnapshot_ResponseElements"></a>

The following element is returned by the service.

 ** Snapshot **
Represents a copy of an entire Valkey or Redis OSS cluster as of the time when the snapshot was taken.
Type: [Snapshot](API_Snapshot.md) object

## Errors
<a name="API_CopySnapshot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterCombination **
Two or more incompatible parameters were specified.
 ** message **
Two or more parameters that must not be used together were used together.
HTTP Status Code: 400

 ** InvalidParameterValue **
The value for a parameter is invalid.
 ** message **
A parameter value is invalid.
HTTP Status Code: 400

 ** InvalidSnapshotState **
The current state of the snapshot does not allow the requested operation to occur.
HTTP Status Code: 400

 ** SnapshotAlreadyExistsFault **
You already have a snapshot with the given name.
HTTP Status Code: 400

 ** SnapshotNotFoundFault **
The requested snapshot name does not refer to an existing snapshot.
HTTP Status Code: 404

 ** SnapshotQuotaExceededFault **
The request cannot be processed because it would exceed the maximum number of snapshots.
HTTP Status Code: 400

 ** TagQuotaPerResourceExceeded **
The request cannot be processed because it would cause the resource to have more than the allowed number of tags. The maximum number of tags permitted on a resource is 50.
HTTP Status Code: 400

## Examples
<a name="API_CopySnapshot_Examples"></a>

### Snapshot copy
<a name="API_CopySnapshot_Example_1"></a>

The following example makes a copy of the snapshot `automatic.my-redis-primary-2016-04-27-03-15` named `my-snapshot-copy`.

#### Sample Request
<a name="API_CopySnapshot_Example_1_Request"></a>

```
https://elasticache.us-west-2.amazonaws.com/
    ?Action=CopySnapshot
    &SourceSnapshotName=automatic.my-redis-primary-2016-04-27-03-15
    &TargetSnapshotName=my-snapshot-copy
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20141201T220302Z
    &Version=2015-02-02
    &X-Amz-Algorithm=AWS4-HMAC-SHA256
    &X-Amz-Date=20141201T220302Z
    &X-Amz-SignedHeaders=Host
    &X-Amz-Expires=20141201T220302Z
    &X-Amz-Credential=<credential>
    &X-Amz-Signature=<signature>
```

## See Also
<a name="API_CopySnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticache-2015-02-02/CopySnapshot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticache-2015-02-02/CopySnapshot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/CopySnapshot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticache-2015-02-02/CopySnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/CopySnapshot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticache-2015-02-02/CopySnapshot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticache-2015-02-02/CopySnapshot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticache-2015-02-02/CopySnapshot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticache-2015-02-02/CopySnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/CopySnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
