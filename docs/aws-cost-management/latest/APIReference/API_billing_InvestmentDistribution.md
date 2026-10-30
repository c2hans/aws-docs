---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_billing_InvestmentDistribution.html
---

# InvestmentDistribution
<a name="API_billing_InvestmentDistribution"></a>

An allocation of an investment disbursement to a specific recipient account. The account is the target account that receives the investment, not your account.

## Contents
<a name="API_billing_InvestmentDistribution_Contents"></a>

 ** accountId **   <a name="awscostmanagement-Type-billing_InvestmentDistribution-accountId"></a>
The recipient AWS account ID that receives this portion of the investment. This must be one of the eligible investment accounts on the contract.
Type: String
Pattern: `[0-9]{12}`
Required: Yes

 ** investmentAmount **   <a name="awscostmanagement-Type-billing_InvestmentDistribution-investmentAmount"></a>
The monetary value allocated to the recipient account.
Type: [Amount](API_billing_Amount.md) object
Required: Yes

## See Also
<a name="API_billing_InvestmentDistribution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billing-2023-09-07/InvestmentDistribution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billing-2023-09-07/InvestmentDistribution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billing-2023-09-07/InvestmentDistribution)
