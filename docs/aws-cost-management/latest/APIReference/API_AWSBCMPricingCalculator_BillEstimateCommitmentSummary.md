---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillEstimateCommitmentSummary.html
---

# BillEstimateCommitmentSummary
<a name="API_AWSBCMPricingCalculator_BillEstimateCommitmentSummary"></a>

 Provides a summary of commitment-related information for a bill estimate.

## Contents
<a name="API_AWSBCMPricingCalculator_BillEstimateCommitmentSummary_Contents"></a>

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateCommitmentSummary-id"></a>
 The unique identifier of the commitment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** monthlyPayment **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateCommitmentSummary-monthlyPayment"></a>
 The monthly payment amount for this commitment, if applicable.
Type: [CostAmount](API_AWSBCMPricingCalculator_CostAmount.md) object
Required: No

 ** offeringId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateCommitmentSummary-offeringId"></a>
 The identifier of the specific offering associated with this commitment.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** paymentOption **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateCommitmentSummary-paymentOption"></a>
 The payment option chosen for this commitment (e.g., All Upfront, Partial Upfront, No Upfront).
Type: String
Required: No

 ** purchaseAgreementType **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateCommitmentSummary-purchaseAgreementType"></a>
 The type of purchase agreement (e.g., Reserved Instance, Savings Plan).
Type: String
Valid Values: `SAVINGS_PLANS | RESERVED_INSTANCE`
Required: No

 ** region **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateCommitmentSummary-region"></a>
 The AWS region associated with this commitment.
Type: String
Required: No

 ** termLength **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateCommitmentSummary-termLength"></a>
 The length of the commitment term.
Type: String
Required: No

 ** upfrontPayment **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateCommitmentSummary-upfrontPayment"></a>
 The upfront payment amount for this commitment, if applicable.
Type: [CostAmount](API_AWSBCMPricingCalculator_CostAmount.md) object
Required: No

 ** usageAccountId **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateCommitmentSummary-usageAccountId"></a>
 The AWS account ID associated with this commitment.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BillEstimateCommitmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BillEstimateCommitmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BillEstimateCommitmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BillEstimateCommitmentSummary)
