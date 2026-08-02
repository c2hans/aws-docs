---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_RecipientInfo.html
---

# RecipientInfo
<a name="API_RecipientInfo"></a>

Contains information about the party that receives the response from the API operation.

This data type is designed to support AWS Nitro Enclaves and AWS NitroTPM, which lets you create an attested environment in Amazon EC2. For information about the interaction between AWS KMS and AWS Nitro Enclaves or AWS NitroTPM, see [Cryptographic attestation support in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/cryptographic-attestation.html) in the * AWS Key Management Service Developer Guide*.

## Contents
<a name="API_RecipientInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AttestationDocument **   <a name="KMS-Type-RecipientInfo-AttestationDocument"></a>
The attestation document for an AWS Nitro Enclave or a NitroTPM. This document includes the enclave's public key.
Type: Base64-encoded binary data object
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: No

 ** KeyEncryptionAlgorithm **   <a name="KMS-Type-RecipientInfo-KeyEncryptionAlgorithm"></a>
The encryption algorithm that AWS KMS should use with the public key for an AWS Nitro Enclave or NitroTPM to encrypt plaintext values for the response. The only valid value is `RSAES_OAEP_SHA_256`.
Type: String
Valid Values: `RSAES_OAEP_SHA_256`
Required: No

## See Also
<a name="API_RecipientInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/RecipientInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/RecipientInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/RecipientInfo)
