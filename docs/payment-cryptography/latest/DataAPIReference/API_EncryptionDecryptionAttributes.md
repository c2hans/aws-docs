---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EncryptionDecryptionAttributes.html
---

# EncryptionDecryptionAttributes
<a name="API_EncryptionDecryptionAttributes"></a>

Parameters that are required to perform encryption and decryption operations.

## Contents
<a name="API_EncryptionDecryptionAttributes_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Asymmetric **   <a name="paymentcryptographydata-Type-EncryptionDecryptionAttributes-Asymmetric"></a>
Parameters for plaintext encryption using asymmetric keys.
Type: [AsymmetricEncryptionAttributes](API_AsymmetricEncryptionAttributes.md) object
Required: No

 ** Dukpt **   <a name="paymentcryptographydata-Type-EncryptionDecryptionAttributes-Dukpt"></a>
Parameters that are required to encrypt plaintext data using DUKPT.
Type: [DukptEncryptionAttributes](API_DukptEncryptionAttributes.md) object
Required: No

 ** Emv **   <a name="paymentcryptographydata-Type-EncryptionDecryptionAttributes-Emv"></a>
Parameters for plaintext encryption using EMV keys.
Type: [EmvEncryptionAttributes](API_EmvEncryptionAttributes.md) object
Required: No

 ** Symmetric **   <a name="paymentcryptographydata-Type-EncryptionDecryptionAttributes-Symmetric"></a>
Parameters that are required to perform encryption and decryption using symmetric keys.
Type: [SymmetricEncryptionAttributes](API_SymmetricEncryptionAttributes.md) object
Required: No

## See Also
<a name="API_EncryptionDecryptionAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/EncryptionDecryptionAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/EncryptionDecryptionAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/EncryptionDecryptionAttributes)
