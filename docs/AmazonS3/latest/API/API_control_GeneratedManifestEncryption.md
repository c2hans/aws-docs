---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GeneratedManifestEncryption.html
---

# GeneratedManifestEncryption
<a name="API_control_GeneratedManifestEncryption"></a>

The encryption configuration to use when storing the generated manifest.

## Contents
<a name="API_control_GeneratedManifestEncryption_Contents"></a>

 ** SSEKMS **   <a name="AmazonS3-Type-control_GeneratedManifestEncryption-SSEKMS"></a>
Configuration details on how SSE-KMS is used to encrypt generated manifest objects.
Type: [SSEKMSEncryption](API_control_SSEKMSEncryption.md) data type
Required: No

 ** SSES3 **   <a name="AmazonS3-Type-control_GeneratedManifestEncryption-SSES3"></a>
Specifies the use of SSE-S3 to encrypt generated manifest objects.
Type: [SSES3Encryption](API_control_SSES3Encryption.md) data type
Required: No

## See Also
<a name="API_control_GeneratedManifestEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GeneratedManifestEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GeneratedManifestEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GeneratedManifestEncryption)
