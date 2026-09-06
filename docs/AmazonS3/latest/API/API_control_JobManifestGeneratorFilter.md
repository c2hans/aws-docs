---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_JobManifestGeneratorFilter.html
---

# JobManifestGeneratorFilter
<a name="API_control_JobManifestGeneratorFilter"></a>

The filter used to describe a set of objects for the job's manifest.

## Contents
<a name="API_control_JobManifestGeneratorFilter_Contents"></a>

 ** CreatedAfter **   <a name="AmazonS3-Type-control_JobManifestGeneratorFilter-CreatedAfter"></a>
If provided, the generated manifest includes only source bucket objects that were created after this time.
Type: Timestamp
Required: No

 ** CreatedBefore **   <a name="AmazonS3-Type-control_JobManifestGeneratorFilter-CreatedBefore"></a>
If provided, the generated manifest includes only source bucket objects that were created before this time.
Type: Timestamp
Required: No

 ** EligibleForReplication **   <a name="AmazonS3-Type-control_JobManifestGeneratorFilter-EligibleForReplication"></a>
Include objects in the generated manifest only if they are eligible for replication according to the Replication configuration on the source bucket.
Type: Boolean
Required: No

 ** KeyNameConstraint **   <a name="AmazonS3-Type-control_JobManifestGeneratorFilter-KeyNameConstraint"></a>
If provided, the generated manifest includes only source bucket objects whose object keys match the string constraints specified for `MatchAnyPrefix`, `MatchAnySuffix`, and `MatchAnySubstring`.
Type: [KeyNameConstraint](API_control_KeyNameConstraint.md) data type
Required: No

 ** MatchAnyObjectEncryption **   <a name="AmazonS3-Type-control_JobManifestGeneratorFilter-MatchAnyObjectEncryption"></a>
If provided, the generated object list includes only source bucket objects with the indicated server-side encryption type (SSE-S3, SSE-KMS, DSSE-KMS, SSE-C, or NOT-SSE).
Type: Array of [ObjectEncryptionFilter](API_control_ObjectEncryptionFilter.md) data types
Array Members: Fixed number of 1 item.
Required: No

 ** MatchAnyStorageClass **   <a name="AmazonS3-Type-control_JobManifestGeneratorFilter-MatchAnyStorageClass"></a>
If provided, the generated manifest includes only source bucket objects that are stored with the specified storage class.
Type: Array of strings
Valid Values: `STANDARD | STANDARD_IA | ONEZONE_IA | GLACIER | INTELLIGENT_TIERING | DEEP_ARCHIVE | GLACIER_IR`
Required: No

 ** ObjectReplicationStatuses **   <a name="AmazonS3-Type-control_JobManifestGeneratorFilter-ObjectReplicationStatuses"></a>
If provided, the generated manifest includes only source bucket objects that have one of the specified Replication statuses.
Type: Array of strings
Valid Values: `COMPLETED | FAILED | REPLICA | NONE`
Required: No

 ** ObjectSizeGreaterThanBytes **   <a name="AmazonS3-Type-control_JobManifestGeneratorFilter-ObjectSizeGreaterThanBytes"></a>
If provided, the generated manifest includes only source bucket objects whose file size is greater than the specified number of bytes.
Type: Long
Required: No

 ** ObjectSizeLessThanBytes **   <a name="AmazonS3-Type-control_JobManifestGeneratorFilter-ObjectSizeLessThanBytes"></a>
If provided, the generated manifest includes only source bucket objects whose file size is less than the specified number of bytes.
Type: Long
Required: No

## See Also
<a name="API_control_JobManifestGeneratorFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/JobManifestGeneratorFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/JobManifestGeneratorFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/JobManifestGeneratorFilter)
