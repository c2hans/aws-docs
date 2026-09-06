---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_ContractAccount.html
---

# ContractAccount
<a name="API_billing_ContractAccount"></a>

An account that is covered by the Enterprise Support contract.

## Contents
<a name="API_billing_ContractAccount_Contents"></a>

 ** accountId **   <a name="awscostmanagement-Type-billing_ContractAccount-accountId"></a>
The account ID.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** isGdn **   <a name="awscostmanagement-Type-billing_ContractAccount-isGdn"></a>
When true, Support charges are calculated on charges before private discounts. When false, they are calculated after private discounts.
Type: Boolean
Required: Yes

## See Also
<a name="API_billing_ContractAccount_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/ContractAccount)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/ContractAccount)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/ContractAccount)
