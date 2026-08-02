---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillEstimateLineItemSummary.html
---

# BillEstimateLineItemSummary
<a name="API_AWSBCMPricingCalculator_BillEstimateLineItemSummary"></a>

 Provides a summary of a line item in a bill estimate.

## Contents
<a name="API_AWSBCMPricingCalculator_BillEstimateLineItemSummary_Contents"></a>

 ** operation **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateLineItemSummary-operation"></a>
 The specific operation associated with this line item.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** serviceCode **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateLineItemSummary-serviceCode"></a>
 The AWS service code associated with this line item.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** usageType **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateLineItemSummary-usageType"></a>
 The type of usage for this line item.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: Yes

 ** availabilityZone **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateLineItemSummary-availabilityZone"></a>
 The availability zone associated with this line item, if applicable.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 32.
Pattern: `[-a-zA-Z0-9\.\-_:, \/()]*`
Required: No

 ** estimatedCost **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateLineItemSummary-estimatedCost"></a>
 The estimated cost for this line item.
Type: [CostAmount](API_AWSBCMPricingCalculator_CostAmount.md) object
Required: No

 ** estimatedUsageQuantity **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateLineItemSummary-estimatedUsageQuantity"></a>
 The estimated usage quantity for this line item.
Type: [UsageQuantityResult](API_AWSBCMPricingCalculator_UsageQuantityResult.md) object
Required: No

 ** historicalCost **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateLineItemSummary-historicalCost"></a>
 The historical cost for this line item.
Type: [CostAmount](API_AWSBCMPricingCalculator_CostAmount.md) object
Required: No

 ** historicalUsageQuantity **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateLineItemSummary-historicalUsageQuantity"></a>
 The historical usage quantity for this line item.
Type: [UsageQuantityResult](API_AWSBCMPricingCalculator_UsageQuantityResult.md) object
Required: No

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateLineItemSummary-id"></a>
 The unique identifier of this line item.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** lineItemId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateLineItemSummary-lineItemId"></a>
 The line item identifier from the original bill.
Type: String
Required: No

 ** lineItemType **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateLineItemSummary-lineItemType"></a>
 The type of this line item (e.g., Usage, Tax, Credit).
Type: String
Required: No

 ** location **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateLineItemSummary-location"></a>
 The location associated with this line item.
Type: String
Required: No

 ** payerAccountId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateLineItemSummary-payerAccountId"></a>
 The AWS account ID of the payer for this line item.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** savingsPlanArns **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateLineItemSummary-savingsPlanArns"></a>
 The Amazon Resource Names (ARNs) of any Savings Plans applied to this line item.
Type: Array of strings
Required: No

 ** usageAccountId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateLineItemSummary-usageAccountId"></a>
 The AWS account ID associated with the usage for this line item.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BillEstimateLineItemSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BillEstimateLineItemSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BillEstimateLineItemSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BillEstimateLineItemSummary)
