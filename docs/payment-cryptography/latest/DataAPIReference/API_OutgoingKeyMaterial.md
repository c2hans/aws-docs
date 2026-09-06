---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_OutgoingKeyMaterial.html
---

# OutgoingKeyMaterial
<a name="API_OutgoingKeyMaterial"></a>

Parameter information of the outgoing TR31WrappedKeyBlock containing the transaction key.

## Contents
<a name="API_OutgoingKeyMaterial_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Tr31KeyBlock **   <a name="paymentcryptographydata-Type-OutgoingKeyMaterial-Tr31KeyBlock"></a>
Parameter information of the TR31WrappedKeyBlock containing the transaction key wrapped using a KEK.
Type: [OutgoingTr31KeyBlock](API_OutgoingTr31KeyBlock.md) object
Required: No

## See Also
<a name="API_OutgoingKeyMaterial_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/OutgoingKeyMaterial)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/OutgoingKeyMaterial)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/OutgoingKeyMaterial)
