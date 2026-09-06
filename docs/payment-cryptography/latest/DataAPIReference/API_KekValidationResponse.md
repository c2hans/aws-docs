---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_KekValidationResponse.html
---

# KekValidationResponse
<a name="API_KekValidationResponse"></a>

Parameter information for generating a KEK validation response during node-to-node initialization.

## Contents
<a name="API_KekValidationResponse_Contents"></a>

 ** RandomKeySend **   <a name="paymentcryptographydata-Type-KekValidationResponse-RandomKeySend"></a>
The random key send value received from the initiating node to generate a KEK validation response.
Type: String
Length Constraints: Minimum length of 16. Maximum length of 48.
Pattern: `(?:[0-9a-fA-F]{16}|[0-9a-fA-F]{32}|[0-9a-fA-F]{48})`
Required: Yes

## See Also
<a name="API_KekValidationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/KekValidationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/KekValidationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/KekValidationResponse)
