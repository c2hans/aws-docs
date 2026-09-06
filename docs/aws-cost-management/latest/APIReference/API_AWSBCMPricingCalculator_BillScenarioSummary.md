---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AWSBCMPricingCalculator_BillScenarioSummary.html
---

# BillScenarioSummary
<a name="API_AWSBCMPricingCalculator_BillScenarioSummary"></a>

 Provides a summary of a bill scenario.

## Contents
<a name="API_AWSBCMPricingCalculator_BillScenarioSummary_Contents"></a>

 ** id **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioSummary-id"></a>
 The unique identifier of the bill scenario.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** billInterval **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioSummary-billInterval"></a>
 The time period covered by the bill scenario.
Type: [BillInterval](API_AWSBCMPricingCalculator_BillInterval.md) object
Required: No

 ** costCategoryGroupSharingPreferenceArn **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioSummary-costCategoryGroupSharingPreferenceArn"></a>
The arn of the cost category used in the reserved and prioritized group sharing.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:ce::[0-9]{12}:costcategory/[a-f0-9-]{36}`
Required: No

 ** createdAt **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioSummary-createdAt"></a>
 The timestamp when the bill scenario was created.
Type: Timestamp
Required: No

 ** expiresAt **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioSummary-expiresAt"></a>
 The timestamp when the bill scenario will expire.
Type: Timestamp
Required: No

 ** failureMessage **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioSummary-failureMessage"></a>
 An error message if the bill scenario creation or processing failed.
Type: String
Required: No

 ** groupSharingPreference **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioSummary-groupSharingPreference"></a>
The setting for the reserved instance and savings plan group sharing used in this estimate.
Type: String
Valid Values: `OPEN | PRIORITIZED | RESTRICTED`
Required: No

 ** name **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioSummary-name"></a>
 The name of the bill scenario.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** status **   <a name="awscostmanagement-Type-AWSBCMPricingCalculator_BillScenarioSummary-status"></a>
 The current status of the bill scenario.
Type: String
Valid Values: `READY | LOCKED | FAILED | STALE`
Required: No

## See Also
<a name="API_AWSBCMPricingCalculator_BillScenarioSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-pricing-calculator-2024-06-19/BillScenarioSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-pricing-calculator-2024-06-19/BillScenarioSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-pricing-calculator-2024-06-19/BillScenarioSummary)
