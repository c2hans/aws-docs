---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_EncryptionAtRest.html
---

# EncryptionAtRest
<a name="API_EncryptionAtRest"></a>

Specifies the encryption-at-rest configuration for the Data Catalog.

## Contents
<a name="API_EncryptionAtRest_Contents"></a>

 ** CatalogEncryptionMode **   <a name="Glue-Type-EncryptionAtRest-CatalogEncryptionMode"></a>
The encryption-at-rest mode for encrypting Data Catalog data.
Type: String
Valid Values: `DISABLED | SSE-KMS | SSE-KMS-WITH-SERVICE-ROLE`
Required: Yes

 ** CatalogEncryptionServiceRole **   <a name="Glue-Type-EncryptionAtRest-CatalogEncryptionServiceRole"></a>
The role that AWS Glue assumes to encrypt and decrypt the Data Catalog objects on the caller's behalf.
Type: String
Pattern: `^arn:aws(-(cn|us-gov|iso(-[bef])?))?:iam::[0-9]{12}:role/.+`
Required: No

 ** SseAwsKmsKeyId **   <a name="Glue-Type-EncryptionAtRest-SseAwsKmsKeyId"></a>
The ID of the AWS KMS key to use for encryption at rest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_EncryptionAtRest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/EncryptionAtRest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/EncryptionAtRest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/EncryptionAtRest)
