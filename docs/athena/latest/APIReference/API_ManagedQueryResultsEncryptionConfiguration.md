---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_ManagedQueryResultsEncryptionConfiguration.html
---

# ManagedQueryResultsEncryptionConfiguration
<a name="API_ManagedQueryResultsEncryptionConfiguration"></a>

If you encrypt query and calculation results in Athena owned storage, this field indicates the encryption option (for example, SSE\_KMS or CSE\_KMS) and key information.

## Contents
<a name="API_ManagedQueryResultsEncryptionConfiguration_Contents"></a>

 ** KmsKey **   <a name="athena-Type-ManagedQueryResultsEncryptionConfiguration-KmsKey"></a>
The ARN of an AWS KMS key for encrypting managed query results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:kms:([a-z0-9\-]+):\d{12}:key/?[a-zA-Z_0-9+=,.@\-_/]+$|^arn:aws[a-z\-]*:kms:([a-z0-9\-]+):\d{12}:alias/?[a-zA-Z_0-9+=,.@\-_/]+$|^alias/[a-zA-Z0-9/_-]+$|[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## See Also
<a name="API_ManagedQueryResultsEncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/ManagedQueryResultsEncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/ManagedQueryResultsEncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/ManagedQueryResultsEncryptionConfiguration)
