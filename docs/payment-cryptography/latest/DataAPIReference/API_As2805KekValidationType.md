---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_As2805KekValidationType.html
---

# As2805KekValidationType
<a name="API_As2805KekValidationType"></a>

Parameter information for generating a random key for KEK validation to perform node-to-node initialization.

## Contents
<a name="API_As2805KekValidationType_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** KekValidationRequest **   <a name="paymentcryptographydata-Type-As2805KekValidationType-KekValidationRequest"></a>
Parameter information for generating a KEK validation request during node-to-node initialization.
Type: [KekValidationRequest](API_KekValidationRequest.md) object
Required: No

 ** KekValidationResponse **   <a name="paymentcryptographydata-Type-As2805KekValidationType-KekValidationResponse"></a>
Parameter information for generating a KEK validation response during node-to-node initialization.
Type: [KekValidationResponse](API_KekValidationResponse.md) object
Required: No

## See Also
<a name="API_As2805KekValidationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/As2805KekValidationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/As2805KekValidationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/As2805KekValidationType)
