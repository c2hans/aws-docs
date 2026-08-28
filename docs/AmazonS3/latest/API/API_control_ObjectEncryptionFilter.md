---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ObjectEncryptionFilter.html
---

# ObjectEncryptionFilter
<a name="API_control_ObjectEncryptionFilter"></a>

An optional filter for the S3JobManifestGenerator that identifies the subset of objects by encryption type.

## Contents
<a name="API_control_ObjectEncryptionFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** DSSEKMS **   <a name="AmazonS3-Type-control_ObjectEncryptionFilter-DSSEKMS"></a>
Filters for objects that are encrypted by dual-layer server-side encryption with AWS Key Management Service (KMS) keys (DSSE-KMS).
Type: [DSSEKMSFilter](API_control_DSSEKMSFilter.md) data type
Required: No

 ** NOTSSE **   <a name="AmazonS3-Type-control_ObjectEncryptionFilter-NOTSSE"></a>
Filters for objects that are not encrypted by server-side encryption.
Type: [NotSSEFilter](API_control_NotSSEFilter.md) data type
Required: No

 ** SSEC **   <a name="AmazonS3-Type-control_ObjectEncryptionFilter-SSEC"></a>
Filters for objects that are encrypted by server-side encryption with customer-provided keys (SSE-C).
Type: [SSECFilter](API_control_SSECFilter.md) data type
Required: No

 ** SSEKMS **   <a name="AmazonS3-Type-control_ObjectEncryptionFilter-SSEKMS"></a>
Filters for objects that are encrypted by server-side encryption with AWS Key Management Service (KMS) keys (SSE-KMS).
Type: [SSEKMSFilter](API_control_SSEKMSFilter.md) data type
Required: No

 ** SSES3 **   <a name="AmazonS3-Type-control_ObjectEncryptionFilter-SSES3"></a>
Filters for objects that are encrypted by server-side encryption with Amazon S3 managed keys (SSE-S3).
Type: [SSES3Filter](API_control_SSES3Filter.md) data type
Required: No

## See Also
<a name="API_control_ObjectEncryptionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ObjectEncryptionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ObjectEncryptionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ObjectEncryptionFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
