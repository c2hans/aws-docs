---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_AnnotationEntry.html
---

# AnnotationEntry
<a name="API_AnnotationEntry"></a>

Describes a single annotation attached to an object, including its name, last modified time, size, ETag, checksum algorithm, and replication status. Returned in the response from `ListObjectAnnotations`.

## Contents
<a name="API_AnnotationEntry_Contents"></a>

 ** AnnotationName **   <a name="AmazonS3-Type-AnnotationEntry-AnnotationName"></a>
The name of the annotation.
Type: String
Required: Yes

 ** LastModified **   <a name="AmazonS3-Type-AnnotationEntry-LastModified"></a>
The date and time the annotation was last modified.
Type: Timestamp
Required: Yes

 ** Size **   <a name="AmazonS3-Type-AnnotationEntry-Size"></a>
The size of the annotation payload, in bytes.
Type: Long
Required: Yes

 ** ChecksumAlgorithm **   <a name="AmazonS3-Type-AnnotationEntry-ChecksumAlgorithm"></a>
The checksum algorithm used for the annotation.
Type: Array of strings
Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME | SHA512 | MD5 | XXHASH64 | XXHASH3 | XXHASH128`
Required: No

 ** ETag **   <a name="AmazonS3-Type-AnnotationEntry-ETag"></a>
The entity tag of the annotation.
Type: String
Required: No

 ** ReplicationStatus **   <a name="AmazonS3-Type-AnnotationEntry-ReplicationStatus"></a>
The replication status of the annotation.
Type: String
Valid Values: `COMPLETE | PENDING | FAILED | REPLICA | COMPLETED`
Required: No

## See Also
<a name="API_AnnotationEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/AnnotationEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/AnnotationEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/AnnotationEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
