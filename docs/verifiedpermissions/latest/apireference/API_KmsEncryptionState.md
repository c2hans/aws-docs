---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_KmsEncryptionState.html
---

# KmsEncryptionState
<a name="API_KmsEncryptionState"></a>

A structure that contains the AWS KMS encryption configuration for the policy store. The encryption state shows what customer-managed KMS key is being used to encrypt all resources within the policy store, and any user-defined context key-value pairs added during encryption processes.

This data type is used as a field that is part of the [EncryptionState](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EncryptionState.html) type.

## Contents
<a name="API_KmsEncryptionState_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** encryptionContext **   <a name="verifiedpermissions-Type-KmsEncryptionState-encryptionContext"></a>
User-defined, additional context added to encryption processes.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 8192 items.
Key Length Constraints: Minimum length of 1.
Value Length Constraints: Minimum length of 1.
Required: Yes

 ** key **   <a name="verifiedpermissions-Type-KmsEncryptionState-key"></a>
The customer-managed KMS key [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) being used for encryption processes.
Type: String
Pattern: `[a-zA-Z0-9:/_-]+`
Required: Yes

## See Also
<a name="API_KmsEncryptionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/KmsEncryptionState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/KmsEncryptionState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/KmsEncryptionState)
