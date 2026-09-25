---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_ReEncryptionAttributes.html
---

# ReEncryptionAttributes
<a name="API_ReEncryptionAttributes"></a>

Parameters that are required to perform reencryption operation.

## Contents
<a name="API_ReEncryptionAttributes_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Asymmetric **   <a name="paymentcryptographydata-Type-ReEncryptionAttributes-Asymmetric"></a>
Specifies the parameters required to encrypt data using an asymmetric key pair. You must specify a `PaddingType`.
Type: [AsymmetricEncryptionAttributes](API_AsymmetricEncryptionAttributes.md) object
Required: No

 ** Dukpt **   <a name="paymentcryptographydata-Type-ReEncryptionAttributes-Dukpt"></a>
Specifies the parameters required to encrypt data using DUKPT.
Type: [DukptEncryptionAttributes](API_DukptEncryptionAttributes.md) object
Required: No

 ** Symmetric **   <a name="paymentcryptographydata-Type-ReEncryptionAttributes-Symmetric"></a>
Specifies the parameters required to encrypt data using symmetric keys.
Type: [SymmetricEncryptionAttributes](API_SymmetricEncryptionAttributes.md) object
Required: No

## See Also
<a name="API_ReEncryptionAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/ReEncryptionAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/ReEncryptionAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/ReEncryptionAttributes)
