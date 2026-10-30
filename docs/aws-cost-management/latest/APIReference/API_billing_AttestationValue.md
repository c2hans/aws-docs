---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_AttestationValue.html
---

# AttestationValue
<a name="API_billing_AttestationValue"></a>

The value being attested. This is a union in which exactly one member is set. Set `attestationAmount` to attest a monetary amount directly, or set `attestationQuantities` to attest one or more quantities that are converted to a value using the investment's multipliers.

## Contents
<a name="API_billing_AttestationValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** attestationAmount **   <a name="awscostmanagement-Type-billing_AttestationValue-attestationAmount"></a>
The value attested as a monetary amount. This form is valid only when the investment has no multiplier.
Type: [Amount](API_billing_Amount.md) object
Required: No

 ** attestationQuantities **   <a name="awscostmanagement-Type-billing_AttestationValue-attestationQuantities"></a>
The value attested as one or more quantities, each with its own unit. The list contains at most 50 quantities.
Type: Array of [AttestationQuantity](API_billing_AttestationQuantity.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_billing_AttestationValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/AttestationValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/AttestationValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/AttestationValue)
