---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VisaAmexDerivationOutputs.html
---

# VisaAmexDerivationOutputs
<a name="API_VisaAmexDerivationOutputs"></a>

The attributes values used for Amex and Visa derivation methods.

## Contents
<a name="API_VisaAmexDerivationOutputs_Contents"></a>

 ** AuthorizationRequestKeyArn **   <a name="paymentcryptographydata-Type-VisaAmexDerivationOutputs-AuthorizationRequestKeyArn"></a>
The `keyArn` of the issuer master key for cryptogram (IMK-AC) used by the operation.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`
Required: Yes

 ** AuthorizationRequestKeyCheckValue **   <a name="paymentcryptographydata-Type-VisaAmexDerivationOutputs-AuthorizationRequestKeyCheckValue"></a>
The key check value (KCV) of the issuer master key for cryptogram (IMK-AC) used by the operation.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** CurrentPinPekArn **   <a name="paymentcryptographydata-Type-VisaAmexDerivationOutputs-CurrentPinPekArn"></a>
The `keyArn` of the current PIN PEK.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`
Required: No

 ** CurrentPinPekKeyCheckValue **   <a name="paymentcryptographydata-Type-VisaAmexDerivationOutputs-CurrentPinPekKeyCheckValue"></a>
The key check value (KCV) of the current PIN PEK.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 16.
Pattern: `[0-9a-fA-F]+`
Required: No

## See Also
<a name="API_VisaAmexDerivationOutputs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/VisaAmexDerivationOutputs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/VisaAmexDerivationOutputs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/VisaAmexDerivationOutputs)
