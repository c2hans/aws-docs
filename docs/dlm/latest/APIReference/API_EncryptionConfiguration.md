---
source_url: https://docs.aws.amazon.com/dlm/latest/APIReference/API_EncryptionConfiguration.html
---

# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

 **[Event-based policies only]** Specifies the encryption settings for cross-Region snapshot copies created by event-based policies.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** Encrypted **   <a name="dlm-Type-EncryptionConfiguration-Encrypted"></a>
To encrypt a copy of an unencrypted snapshot when encryption by default is not enabled, enable encryption using this parameter. Copies of encrypted snapshots are encrypted, even if this parameter is false or when encryption by default is not enabled.
Type: Boolean
Required: Yes

 ** CmkArn **   <a name="dlm-Type-EncryptionConfiguration-CmkArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key to use for EBS encryption. If this parameter is not specified, the default KMS key for the account is used.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws(-[a-z]{1,4}){0,2}:kms:([a-z]+-){2,3}\d:\d+:key/.*`
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dlm-2018-01-12/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dlm-2018-01-12/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dlm-2018-01-12/EncryptionConfiguration)
