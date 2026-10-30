---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ContractDetails.html
---

# ContractDetails
<a name="API_billing_ContractDetails"></a>

The details of a contract returned by `GetContractInformation`. This is a union in which exactly one member is set, corresponding to the contract type. For a private pricing addendum, the `privatePricingAddendum` member is set. Check which member is present to determine the contract type.

## Contents
<a name="API_billing_ContractDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** privatePricingAddendum **   <a name="awscostmanagement-Type-billing_ContractDetails-privatePricingAddendum"></a>
The details of a private pricing addendum contract. This member is set when the contract is a private pricing addendum.
Type: [PrivatePricingAddendum](API_billing_PrivatePricingAddendum.md) object
Required: No

## See Also
<a name="API_billing_ContractDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/ContractDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/ContractDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/ContractDetails)
