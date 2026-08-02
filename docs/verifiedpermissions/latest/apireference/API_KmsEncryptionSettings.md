---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_KmsEncryptionSettings.html
---

# KmsEncryptionSettings
<a name="API_KmsEncryptionSettings"></a>

A structure that contains the KMS encryption configuration for the policy store. The encryption settings determine what customer-managed KMS key will be used to encrypt all resources within the policy store, and any user-defined context key-value pairs to append during encryption processes.

This data type is used as a field that is part of the [EncryptionSettings](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EncryptionSettings.html) type.

## Contents
<a name="API_KmsEncryptionSettings_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** key **   <a name="verifiedpermissions-Type-KmsEncryptionSettings-key"></a>
The customer-managed KMS key [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html), alias or ID to be used for encryption processes.
Users can provide the full KMS key ARN, a KMS key alias, or a KMS key ID, but it will be mapped to the full KMS key ARN after policy store creation, and referenced when encrypting child resources.
Type: String
Pattern: `[a-zA-Z0-9:/_-]+`
Required: Yes

 ** encryptionContext **   <a name="verifiedpermissions-Type-KmsEncryptionSettings-encryptionContext"></a>
User-defined, additional context to be added to encryption processes.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 8192 items.
Key Length Constraints: Minimum length of 1.
Value Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_KmsEncryptionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/KmsEncryptionSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/KmsEncryptionSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/KmsEncryptionSettings)
