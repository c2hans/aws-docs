---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DerivationMethodAttributes.html
---

# DerivationMethodAttributes
<a name="API_DerivationMethodAttributes"></a>

Parameters to derive the payment card specific confidentiality and integrity keys.

## Contents
<a name="API_DerivationMethodAttributes_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Amex **   <a name="paymentcryptographydata-Type-DerivationMethodAttributes-Amex"></a>
Parameters to derive the confidentiality and integrity keys for a payment card using Amex derivation method.
Type: [AmexAttributes](API_AmexAttributes.md) object
Required: No

 ** Emv2000 **   <a name="paymentcryptographydata-Type-DerivationMethodAttributes-Emv2000"></a>
Parameters to derive the confidentiality and integrity keys for a payment card using Emv2000 derivation method.
Type: [Emv2000Attributes](API_Emv2000Attributes.md) object
Required: No

 ** EmvCommon **   <a name="paymentcryptographydata-Type-DerivationMethodAttributes-EmvCommon"></a>
Parameters to derive the confidentiality and integrity keys for a payment card using Emv common derivation method.
Type: [EmvCommonAttributes](API_EmvCommonAttributes.md) object
Required: No

 ** Mastercard **   <a name="paymentcryptographydata-Type-DerivationMethodAttributes-Mastercard"></a>
Parameters to derive the confidentiality and integrity keys for a payment card using Mastercard derivation method.
Type: [MasterCardAttributes](API_MasterCardAttributes.md) object
Required: No

 ** Visa **   <a name="paymentcryptographydata-Type-DerivationMethodAttributes-Visa"></a>
Parameters to derive the confidentiality and integrity keys for a a payment card using Visa derivation method.
Type: [VisaAttributes](API_VisaAttributes.md) object
Required: No

## See Also
<a name="API_DerivationMethodAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/DerivationMethodAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/DerivationMethodAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/DerivationMethodAttributes)
