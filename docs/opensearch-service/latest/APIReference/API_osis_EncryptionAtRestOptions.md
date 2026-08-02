---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_EncryptionAtRestOptions.html
---

# EncryptionAtRestOptions
<a name="API_osis_EncryptionAtRestOptions"></a>

Options to control how OpenSearch encrypts buffer data.

## Contents
<a name="API_osis_EncryptionAtRestOptions_Contents"></a>

 ** KmsKeyArn **   <a name="opensearchservice-Type-osis_EncryptionAtRestOptions-KmsKeyArn"></a>
The ARN of the KMS key used to encrypt buffer data. By default, data is encrypted using an AWS owned key.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 2048.
Required: Yes

## See Also
<a name="API_osis_EncryptionAtRestOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/EncryptionAtRestOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/EncryptionAtRestOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/EncryptionAtRestOptions)
