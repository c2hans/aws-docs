---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ObjectEncryption.html
---

# ObjectEncryption
<a name="API_ObjectEncryption"></a>

 The updated server-side encryption type for this object. The `UpdateObjectEncryption` operation supports the SSE-S3 and SSE-KMS encryption types.

Valid Values: `SSES3` \| `SSEKMS`

## Contents
<a name="API_ObjectEncryption_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** SSEKMS **   <a name="AmazonS3-Type-ObjectEncryption-SSEKMS"></a>
 Specifies to update the object encryption type to server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS).
Type: [SSEKMSEncryption](API_SSEKMSEncryption.md) data type
Required: No

## See Also
<a name="API_ObjectEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ObjectEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ObjectEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ObjectEncryption)
