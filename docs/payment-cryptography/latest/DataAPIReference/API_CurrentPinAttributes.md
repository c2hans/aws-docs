---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CurrentPinAttributes.html
---

# CurrentPinAttributes
<a name="API_CurrentPinAttributes"></a>

The parameter values of the current PIN to be changed on the EMV chip card.

## Contents
<a name="API_CurrentPinAttributes_Contents"></a>

 ** CurrentEncryptedPinBlock **   <a name="paymentcryptographydata-Type-CurrentPinAttributes-CurrentEncryptedPinBlock"></a>
The encrypted pinblock of the current pin stored on the chip card.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `[0-9a-fA-F]+`
Required: Yes

 ** CurrentPinPekIdentifier **   <a name="paymentcryptographydata-Type-CurrentPinAttributes-CurrentPinPekIdentifier"></a>
The `keyArn` of the current PIN PEK.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

## See Also
<a name="API_CurrentPinAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/CurrentPinAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/CurrentPinAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/CurrentPinAttributes)
