---
source_url: https://docs.aws.amazon.com/eventbridgev2/latest/APIReference/API_EncryptionConfiguration.html
---

# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

Encryption configuration for an event bus.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** KmsKeyIdentifier **   <a name="eventbridgev2-Type-EncryptionConfiguration-KmsKeyIdentifier"></a>
Identifier of the AWS KMS customer managed key used to encrypt events: a key ID, key ARN, alias name, or alias ARN. When absent, events are encrypted with an AWS owned key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9_\-/:]*`
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridgev2-2025-05-15/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridgev2-2025-05-15/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridgev2-2025-05-15/EncryptionConfiguration)
