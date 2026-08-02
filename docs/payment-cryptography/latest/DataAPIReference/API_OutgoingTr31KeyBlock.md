---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_OutgoingTr31KeyBlock.html
---

# OutgoingTr31KeyBlock
<a name="API_OutgoingTr31KeyBlock"></a>

Parameter information of the TR31WrappedKeyBlock containing the transaction key wrapped using a KEK.

## Contents
<a name="API_OutgoingTr31KeyBlock_Contents"></a>

 ** WrappingKeyIdentifier **   <a name="paymentcryptographydata-Type-OutgoingTr31KeyBlock-WrappingKeyIdentifier"></a>
The `keyARN` of the KEK used to wrap the transaction key.
Type: String
Length Constraints: Minimum length of 7. Maximum length of 322.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:(key/[0-9a-zA-Z]{16,64}|alias/[a-zA-Z0-9/_-]+)$|^alias/[a-zA-Z0-9/_-]+`
Required: Yes

## See Also
<a name="API_OutgoingTr31KeyBlock_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/OutgoingTr31KeyBlock)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/OutgoingTr31KeyBlock)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/OutgoingTr31KeyBlock)
