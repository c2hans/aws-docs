---
source_url: https://docs.aws.amazon.com/polly/latest/APIReference/API_CustomerManagedEncryption.html
---

# CustomerManagedEncryption

The customer managed key that encrypts your custom voice. If you don't specify a key, Amazon Polly encrypts the voice with an AWS owned key.

## Contents
<a name="API_CustomerManagedEncryption_Contents"></a>

 ** KmsKeyArn **   <a name="polly-Type-CustomerManagedEncryption-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of the key. The key must be a symmetric encryption key in the same AWS Region as the voice. To create the voice, you need `kms:DescribeKey`, `kms:GenerateDataKey`, and `kms:Decrypt` permissions on the key. To synthesize speech with the voice, you need `kms:Decrypt` permission on the key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws(-(cn|iso(-b)?|us-gov|eusc))?:kms:[a-z0-9_-]{1,50}:\d{12}:key/[a-zA-Z0-9-]+$`
Required: Yes

 ** EncryptionContext **   <a name="polly-Type-CustomerManagedEncryption-EncryptionContext"></a>
The key-value pairs that Amazon Polly includes as the encryption context when it encrypts or decrypts the voice with the key. You can use these pairs in key policy conditions. Don't use keys that start with `aws:`, which are reserved.
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_CustomerManagedEncryption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/polly-2016-06-10/CustomerManagedEncryption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/polly-2016-06-10/CustomerManagedEncryption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/polly-2016-06-10/CustomerManagedEncryption)
