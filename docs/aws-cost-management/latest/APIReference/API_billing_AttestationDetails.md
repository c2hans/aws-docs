---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_AttestationDetails.html
---

# AttestationDetails
<a name="API_billing_AttestationDetails"></a>

The details of an investment attestation submission, including the value being attested and how the resulting investment is distributed.

## Contents
<a name="API_billing_AttestationDetails_Contents"></a>

 ** attestationValue **   <a name="awscostmanagement-Type-billing_AttestationDetails-attestationValue"></a>
The value being attested, expressed as either a monetary amount or one or more quantities. Exactly one form is set.
Type: [AttestationValue](API_billing_AttestationValue.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** investmentDistributions **   <a name="awscostmanagement-Type-billing_AttestationDetails-investmentDistributions"></a>
The distribution of the resulting investment across the eligible investment accounts on the contract. If you omit this value, the full investment is allocated to the single eligible investment account on the contract. This value is required when multiple investment accounts are eligible. When you provide this value, the sum of all distributions must equal the resulting monetary investment value (the attested amount, or the value computed from the attested quantities using the investment multipliers). The list contains at most 200 distributions.
Type: Array of [InvestmentDistribution](API_billing_InvestmentDistribution.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## See Also
<a name="API_billing_AttestationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/AttestationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/AttestationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/AttestationDetails)
