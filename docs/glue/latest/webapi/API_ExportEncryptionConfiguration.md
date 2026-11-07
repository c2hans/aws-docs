---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ExportEncryptionConfiguration.html
---

# ExportEncryptionConfiguration
<a name="API_ExportEncryptionConfiguration"></a>

The encryption configuration for exported data catalog metadata.

## Contents
<a name="API_ExportEncryptionConfiguration_Contents"></a>

 ** KmsKeyArn **   <a name="Glue-Type-ExportEncryptionConfiguration-KmsKeyArn"></a>
The ARN of the KMS key used to encrypt the exported data.
Type: String
Pattern: `arn:aws[-a-z0-9]*:kms:[-a-z0-9]*:[0-9]{12}:key/.+`
Required: No

 ** SseAlgorithm **   <a name="Glue-Type-ExportEncryptionConfiguration-SseAlgorithm"></a>
The server-side encryption algorithm used for the exported data. Valid values are `AES256` and `aws:kms`.
Type: String
Required: No

## See Also
<a name="API_ExportEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ExportEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ExportEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ExportEncryptionConfiguration)
