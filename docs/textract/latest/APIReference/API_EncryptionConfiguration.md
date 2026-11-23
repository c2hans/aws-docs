---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_EncryptionConfiguration.html
---

# EncryptionConfiguration

Specifies the AWS Key Management Service (AWS KMS) key and encryption context used to encrypt a resource at rest. When omitted, Amazon Textract encrypts the resource using an AWS owned key.

## Contents
<a name="API_EncryptionConfiguration_Contents"></a>

 ** KmsKeyId **   <a name="Textract-Type-EncryptionConfiguration-KmsKeyId"></a>
The identifier of the AWS KMS key to use for encryption. This can be a key ID, key ARN, alias name, or alias ARN.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^([A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2047})?$`
Required: Yes

 ** KmsEncryptionContext **   <a name="Textract-Type-EncryptionConfiguration-KmsEncryptionContext"></a>
A set of key-value pairs that Amazon Textract includes as the AWS KMS encryption context when encrypting and decrypting the resource.
On `UpdateProject` and `UpdateBlueprint`, this member is the one exception to replacing a supplied configuration whole. If you omit it, the stored encryption context is kept. To clear a custom encryption context, specify an empty map (`{}`).
Type: String to string map
Map Entries: Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 2000.
Key Pattern: `^.*\S.*$`
Value Length Constraints: Minimum length of 1. Maximum length of 2000.
Value Pattern: `^.*\S.*$`
Required: No

## See Also
<a name="API_EncryptionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/EncryptionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/EncryptionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/EncryptionConfiguration)
