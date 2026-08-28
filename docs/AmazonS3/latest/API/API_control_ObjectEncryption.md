---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_ObjectEncryption.html
---

# ObjectEncryption
<a name="API_control_ObjectEncryption"></a>

The updated server-side encryption type for this object. The `UpdateObjectEncryption` operation supports the SSE-KMS encryption type.

Valid Values: `SSEKMS`

## Contents
<a name="API_control_ObjectEncryption_Contents"></a>

 ** SSEKMS **   <a name="AmazonS3-Type-control_ObjectEncryption-SSEKMS"></a>
Specifies to update the object encryption type to server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS).
Type: [S3UpdateObjectEncryptionSSEKMS](API_control_S3UpdateObjectEncryptionSSEKMS.md) data type
Required: No

## See Also
<a name="API_control_ObjectEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ObjectEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ObjectEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ObjectEncryption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
