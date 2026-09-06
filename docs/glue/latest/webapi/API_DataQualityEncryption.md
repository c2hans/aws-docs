---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityEncryption.html
---

# DataQualityEncryption
<a name="API_DataQualityEncryption"></a>

Specifies how Data Quality assets in your account should be encrypted.

## Contents
<a name="API_DataQualityEncryption_Contents"></a>

 ** DataQualityEncryptionMode **   <a name="Glue-Type-DataQualityEncryption-DataQualityEncryptionMode"></a>
The encryption mode to use for encrypting Data Quality assets. These assets include data quality rulesets, results, statistics, anomaly detection models and observations.
Valid values are `SSEKMS` for encryption using a customer-managed KMS key, or `DISABLED`.
Type: String
Valid Values: `DISABLED | SSE-KMS`
Required: No

 ** KmsKeyArn **   <a name="Glue-Type-DataQualityEncryption-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.
Type: String
Pattern: `^$|arn:aws[a-z0-9-]*:kms:.*`
Required: No

## See Also
<a name="API_DataQualityEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityEncryption)
