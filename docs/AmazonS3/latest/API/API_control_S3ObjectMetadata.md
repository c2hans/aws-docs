---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3ObjectMetadata.html
---

# S3ObjectMetadata
<a name="API_control_S3ObjectMetadata"></a>

## Contents
<a name="API_control_S3ObjectMetadata_Contents"></a>

 ** CacheControl **   <a name="AmazonS3-Type-control_S3ObjectMetadata-CacheControl"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ContentDisposition **   <a name="AmazonS3-Type-control_S3ObjectMetadata-ContentDisposition"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ContentEncoding **   <a name="AmazonS3-Type-control_S3ObjectMetadata-ContentEncoding"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ContentLanguage **   <a name="AmazonS3-Type-control_S3ObjectMetadata-ContentLanguage"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ContentLength **   <a name="AmazonS3-Type-control_S3ObjectMetadata-ContentLength"></a>
 *This member has been deprecated.*

Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** ContentMD5 **   <a name="AmazonS3-Type-control_S3ObjectMetadata-ContentMD5"></a>
 *This member has been deprecated.*

Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ContentType **   <a name="AmazonS3-Type-control_S3ObjectMetadata-ContentType"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** HttpExpiresDate **   <a name="AmazonS3-Type-control_S3ObjectMetadata-HttpExpiresDate"></a>

Type: Timestamp
Required: No

 ** RequesterCharged **   <a name="AmazonS3-Type-control_S3ObjectMetadata-RequesterCharged"></a>
 *This member has been deprecated.*

Type: Boolean
Required: No

 ** SSEAlgorithm **   <a name="AmazonS3-Type-control_S3ObjectMetadata-SSEAlgorithm"></a>
The server-side encryption algorithm used when storing objects in Amazon S3.
 **Directory buckets ** - For directory buckets, there are only two supported options for server-side encryption: server-side encryption with Amazon S3 managed keys (SSE-S3) (`AES256`) and server-side encryption with AWS KMS keys (SSE-KMS) (`KMS`). For more information, see [Protecting data with server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-serv-side-encryption.html) in the *Amazon S3 User Guide*. For [the Copy operation in Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops), see [S3CopyObjectOperation](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_S3CopyObjectOperation.html).
Type: String
Valid Values: `AES256 | KMS`
Required: No

 ** UserMetadata **   <a name="AmazonS3-Type-control_S3ObjectMetadata-UserMetadata"></a>

Type: String to string map
Map Entries: Maximum number of 8192 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_control_S3ObjectMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3ObjectMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3ObjectMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3ObjectMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
