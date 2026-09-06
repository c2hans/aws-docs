---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_EncryptionSetting.html
---

# EncryptionSetting
<a name="API_EncryptionSetting"></a>

The object representing the passwords that were used to encrypt the data related to the bot recommendation, as well as the AWS KMS key ARN used to encrypt the associated metadata.

## Contents
<a name="API_EncryptionSetting_Contents"></a>

 ** associatedTranscriptsPassword **   <a name="lexv2-Type-EncryptionSetting-associatedTranscriptsPassword"></a>
The password used to encrypt the associated transcript file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** botLocaleExportPassword **   <a name="lexv2-Type-EncryptionSetting-botLocaleExportPassword"></a>
The password used to encrypt the recommended bot recommendation file.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** kmsKeyArn **   <a name="lexv2-Type-EncryptionSetting-kmsKeyArn"></a>
The AWS KMS key ARN used to encrypt the metadata associated with the bot recommendation.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:[\w\-]+:kms:[\w\-]+:[\d]{12}:(?:key\/[\w\-]+|alias\/[a-zA-Z0-9:\/_\-]{1,256})$`
Required: No

## See Also
<a name="API_EncryptionSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/EncryptionSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/EncryptionSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/EncryptionSetting)
