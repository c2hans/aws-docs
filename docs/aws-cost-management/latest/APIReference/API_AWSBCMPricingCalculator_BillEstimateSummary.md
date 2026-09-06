---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillEstimateSummary.html
---

# BillEstimateSummary
<a name="API_AWSBCMPricingCalculator_BillEstimateSummary"></a>

 Provides a summary of a bill estimate.

## Contents
<a name="API_AWSBCMPricingCalculator_BillEstimateSummary_Contents"></a>

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateSummary-id"></a>
 The unique identifier of the bill estimate.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** billInterval **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateSummary-billInterval"></a>
 The time period covered by the bill estimate.
Type: [BillInterval](API_AWSBCMPricingCalculator_BillInterval.md) object
Required: No

 ** createdAt **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateSummary-createdAt"></a>
 The timestamp when the bill estimate was created.
Type: Timestamp
Required: No

 ** expiresAt **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateSummary-expiresAt"></a>
 The timestamp when the bill estimate will expire.
Type: Timestamp
Required: No

 ** name **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateSummary-name"></a>
 The name of the bill estimate.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** status **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillEstimateSummary-status"></a>
 The current status of the bill estimate.
Type: String
Valid Values: `IN_PROGRESS | COMPLETE | FAILED`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BillEstimateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BillEstimateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BillEstimateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BillEstimateSummary)
