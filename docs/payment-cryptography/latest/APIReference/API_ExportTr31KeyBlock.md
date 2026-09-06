---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ExportTr31KeyBlock.html
---

# ExportTr31KeyBlock
<a name="API_ExportTr31KeyBlock"></a>

Parameter information for key material export using symmetric TR-31 key exchange method.

## Contents
<a name="API_ExportTr31KeyBlock_Contents"></a>

 ** WrappingKeyIdentifier **   <a name="paymentcryptography-Type-ExportTr31KeyBlock-WrappingKeyIdentifier"></a>
The `KeyARN` of the the wrapping key. This key encrypts or wraps the key under export for TR-31 key block generation.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

 ** KeyBlockHeaders **   <a name="paymentcryptography-Type-ExportTr31KeyBlock-KeyBlockHeaders"></a>
Optional metadata for export associated with the key material. This data is signed but transmitted in clear text.
Type: [KeyBlockHeaders](API_KeyBlockHeaders.md) object
Required: No

## See Also
<a name="API_ExportTr31KeyBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ExportTr31KeyBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ExportTr31KeyBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ExportTr31KeyBlock)
