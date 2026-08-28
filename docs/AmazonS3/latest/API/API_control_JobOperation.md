---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobOperation.html
---

# JobOperation
<a name="API_control_JobOperation"></a>

The operation that you want this job to perform on every object listed in the manifest. For more information about the available operations, see [Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-operations.html) in the *Amazon S3 User Guide*.

## Contents
<a name="API_control_JobOperation_Contents"></a>

 ** LambdaInvoke **   <a name="AmazonS3-Type-control_JobOperation-LambdaInvoke"></a>
Directs the specified job to invoke an AWS Lambda function on every object in the manifest.
Type: [LambdaInvokeOperation](API_control_LambdaInvokeOperation.md) data type
Required: No

 ** S3ComputeObjectChecksum **   <a name="AmazonS3-Type-control_JobOperation-S3ComputeObjectChecksum"></a>
Directs the specified job to compute checksum values for every object in the manifest.
Type: [S3ComputeObjectChecksumOperation](API_control_S3ComputeObjectChecksumOperation.md) data type
Required: No

 ** S3DeleteObjectTagging **   <a name="AmazonS3-Type-control_JobOperation-S3DeleteObjectTagging"></a>
Directs the specified job to execute a DELETE Object tagging call on every object in the manifest.
This functionality is not supported by directory buckets.
Type: [S3DeleteObjectTaggingOperation](API_control_S3DeleteObjectTaggingOperation.md) data type
Required: No

 ** S3InitiateRestoreObject **   <a name="AmazonS3-Type-control_JobOperation-S3InitiateRestoreObject"></a>
Directs the specified job to initiate restore requests for every archived object in the manifest.
This functionality is not supported by directory buckets.
Type: [S3InitiateRestoreObjectOperation](API_control_S3InitiateRestoreObjectOperation.md) data type
Required: No

 ** S3PutObjectAcl **   <a name="AmazonS3-Type-control_JobOperation-S3PutObjectAcl"></a>
Directs the specified job to run a `PutObjectAcl` call on every object in the manifest.
This functionality is not supported by directory buckets.
Type: [S3SetObjectAclOperation](API_control_S3SetObjectAclOperation.md) data type
Required: No

 ** S3PutObjectCopy **   <a name="AmazonS3-Type-control_JobOperation-S3PutObjectCopy"></a>
Directs the specified job to run a PUT Copy object call on every object in the manifest.
Type: [S3CopyObjectOperation](API_control_S3CopyObjectOperation.md) data type
Required: No

 ** S3PutObjectLegalHold **   <a name="AmazonS3-Type-control_JobOperation-S3PutObjectLegalHold"></a>
Contains the configuration for an S3 Object Lock legal hold operation that an S3 Batch Operations job passes to every object to the underlying `PutObjectLegalHold` API operation. For more information, see [Using S3 Object Lock legal hold with S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-legal-hold.html) in the *Amazon S3 User Guide*.
This functionality is not supported by directory buckets.
Type: [S3SetObjectLegalHoldOperation](API_control_S3SetObjectLegalHoldOperation.md) data type
Required: No

 ** S3PutObjectRetention **   <a name="AmazonS3-Type-control_JobOperation-S3PutObjectRetention"></a>
Contains the configuration parameters for the Object Lock retention action for an S3 Batch Operations job. Batch Operations passes every object to the underlying `PutObjectRetention` API operation. For more information, see [Using S3 Object Lock retention with S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-retention-date.html) in the *Amazon S3 User Guide*.
This functionality is not supported by directory buckets.
Type: [S3SetObjectRetentionOperation](API_control_S3SetObjectRetentionOperation.md) data type
Required: No

 ** S3PutObjectTagging **   <a name="AmazonS3-Type-control_JobOperation-S3PutObjectTagging"></a>
Directs the specified job to run a PUT Object tagging call on every object in the manifest.
This functionality is not supported by directory buckets.
Type: [S3SetObjectTaggingOperation](API_control_S3SetObjectTaggingOperation.md) data type
Required: No

 ** S3ReplicateObject **   <a name="AmazonS3-Type-control_JobOperation-S3ReplicateObject"></a>
Directs the specified job to invoke `ReplicateObject` on every object in the job's manifest.
This functionality is not supported by directory buckets.
Type: [S3ReplicateObjectOperation](API_control_S3ReplicateObjectOperation.md) data type
Required: No

 ** S3UpdateObjectEncryption **   <a name="AmazonS3-Type-control_JobOperation-S3UpdateObjectEncryption"></a>
Updates the server-side encryption type of an existing encrypted object in a general purpose bucket. You can use the `UpdateObjectEncryption` operation to change encrypted objects from server-side encryption with Amazon S3 managed keys (SSE-S3) to server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), or to apply S3 Bucket Keys. You can also use the `UpdateObjectEncryption` operation to change the customer-managed KMS key used to encrypt your data so that you can comply with custom key-rotation standards.
Type: [S3UpdateObjectEncryptionOperation](API_control_S3UpdateObjectEncryptionOperation.md) data type
Required: No

## See Also
<a name="API_control_JobOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
