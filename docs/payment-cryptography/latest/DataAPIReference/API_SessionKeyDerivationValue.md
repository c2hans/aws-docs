---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_SessionKeyDerivationValue.html
---

# SessionKeyDerivationValue
<a name="API_SessionKeyDerivationValue"></a>

Parameters to derive session key value using a MAC EMV algorithm.

## Contents
<a name="API_SessionKeyDerivationValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** ApplicationCryptogram **   <a name="paymentcryptographydata-Type-SessionKeyDerivationValue-ApplicationCryptogram"></a>
The cryptogram provided by the terminal during transaction processing.
Type: String
Length Constraints: Fixed length of 16.
Pattern: `[0-9a-fA-F]+`
Required: No

 ** ApplicationTransactionCounter **   <a name="paymentcryptographydata-Type-SessionKeyDerivationValue-ApplicationTransactionCounter"></a>
The transaction counter that is provided by the terminal during transaction processing.
Type: String
Length Constraints: Fixed length of 4.
Pattern: `[0-9a-fA-F]+`
Required: No

## See Also
<a name="API_SessionKeyDerivationValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-data-2022-02-03/SessionKeyDerivationValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-data-2022-02-03/SessionKeyDerivationValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-data-2022-02-03/SessionKeyDerivationValue)
