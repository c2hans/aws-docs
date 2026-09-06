---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_SessionKeyDerivation.html
---

# SessionKeyDerivation
<a name="API_SessionKeyDerivation"></a>

Parameters to derive a session key for Authorization Response Cryptogram (ARQC) verification.

## Contents
<a name="API_SessionKeyDerivation_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Amex **   <a name="paymentcryptographydata-Type-SessionKeyDerivation-Amex"></a>
Parameters to derive session key for an Amex payment card for ARQC verification.
Type: [SessionKeyAmex](API_SessionKeyAmex.md) object
Required: No

 ** Emv2000 **   <a name="paymentcryptographydata-Type-SessionKeyDerivation-Emv2000"></a>
Parameters to derive session key for an Emv2000 payment card for ARQC verification.
Type: [SessionKeyEmv2000](API_SessionKeyEmv2000.md) object
Required: No

 ** EmvCommon **   <a name="paymentcryptographydata-Type-SessionKeyDerivation-EmvCommon"></a>
Parameters to derive session key for an Emv common payment card for ARQC verification.
Type: [SessionKeyEmvCommon](API_SessionKeyEmvCommon.md) object
Required: No

 ** Mastercard **   <a name="paymentcryptographydata-Type-SessionKeyDerivation-Mastercard"></a>
Parameters to derive session key for a Mastercard payment card for ARQC verification.
Type: [SessionKeyMastercard](API_SessionKeyMastercard.md) object
Required: No

 ** Visa **   <a name="paymentcryptographydata-Type-SessionKeyDerivation-Visa"></a>
Parameters to derive session key for a Visa payment cardfor ARQC verification.
Type: [SessionKeyVisa](API_SessionKeyVisa.md) object
Required: No

## See Also
<a name="API_SessionKeyDerivation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/SessionKeyDerivation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/SessionKeyDerivation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/SessionKeyDerivation)
