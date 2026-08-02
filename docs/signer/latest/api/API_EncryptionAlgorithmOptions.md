---
source_url: https://docs.aws.amazon.com/signer/latest/api/API_EncryptionAlgorithmOptions.html
---

# EncryptionAlgorithmOptions
<a name="API_EncryptionAlgorithmOptions"></a>

The encryption algorithm options that are available to a code-signing job.

## Contents
<a name="API_EncryptionAlgorithmOptions_Contents"></a>

 ** allowedValues **   <a name="signer-Type-EncryptionAlgorithmOptions-allowedValues"></a>
The set of accepted encryption algorithms that are allowed in a code-signing job.
Type: Array of strings
Valid Values: `RSA | ECDSA`
Required: Yes

 ** defaultValue **   <a name="signer-Type-EncryptionAlgorithmOptions-defaultValue"></a>
The default encryption algorithm that is used by a code-signing job.
Type: String
Valid Values: `RSA | ECDSA`
Required: Yes

## See Also
<a name="API_EncryptionAlgorithmOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signer-2017-08-25/EncryptionAlgorithmOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signer-2017-08-25/EncryptionAlgorithmOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signer-2017-08-25/EncryptionAlgorithmOptions)
