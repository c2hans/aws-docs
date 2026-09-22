---
source_url: https://docs.aws.amazon.com/transcribe/latest/APIReference/API_EncryptionConfiguration.html
---

# EncryptionConfiguration
<a name="API_EncryptionConfiguration"></a>

The encryption configuration for your custom resource. Specify a customer managed AWS KMS key, and optionally an encryption context, to encrypt your custom vocabulary, custom vocabulary filter, or custom language model artifacts at rest. If you do not provide a key, your artifacts are encrypted with an AWS owned key.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** KMSKey **   <a name="transcribe-Type-EncryptionConfiguration-KMSKey"></a>
The Amazon Resource Name (ARN) of the AWS KMS key you want to use to encrypt your resource artifacts. Only full AWS KMS key ARN format is supported.
 AWS KMS key ARNs have the format `arn:partition:kms:region:account:key/key-id`. For example: `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`.
For more information, see [KMS key ARNs](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`
Required: Yes

 ** KMSEncryptionContext **   <a name="transcribe-Type-EncryptionConfiguration-KMSEncryptionContext"></a>
A map of plain text, non-secret key:value pairs, known as encryption context pairs, that provide an added layer of security for your data. For more information, see [KMS encryption context](https://docs.aws.amazon.com/transcribe/latest/dg/key-management.html#kms-context).
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 2000.
Key Pattern: `^[\x20-\x7E]+$`
Value Length Constraints: Minimum length of 1. Maximum length of 2000.
Value Pattern: `^[\x20-\x7E]+$`
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transcribe-2017-10-26/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transcribe-2017-10-26/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transcribe-2017-10-26/EncryptionConfiguration)
