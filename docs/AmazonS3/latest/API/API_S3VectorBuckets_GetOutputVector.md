---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_S3VectorBuckets_GetOutputVector.html
---

# GetOutputVector
<a name="API_S3VectorBuckets_GetOutputVector"></a>

The attributes of a vector returned by the `GetVectors` operation.

## Contents
<a name="API_S3VectorBuckets_GetOutputVector_Contents"></a>

 ** key **   <a name="AmazonS3-Type-S3VectorBuckets_GetOutputVector-key"></a>
The name of the vector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** data **   <a name="AmazonS3-Type-S3VectorBuckets_GetOutputVector-data"></a>
The vector data of the vector.
Type: [VectorData](API_S3VectorBuckets_VectorData.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** metadata **   <a name="AmazonS3-Type-S3VectorBuckets_GetOutputVector-metadata"></a>
Metadata about the vector.
Type: JSON value
Required: No

## See Also
<a name="API_S3VectorBuckets_GetOutputVector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3vectors-2025-07-15/GetOutputVector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3vectors-2025-07-15/GetOutputVector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3vectors-2025-07-15/GetOutputVector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
