---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Recommendation.html
---

# Recommendation
<a name="API_CostOptimizationHub_Recommendation"></a>

Describes a recommendation.

## Contents
<a name="API_CostOptimizationHub_Recommendation_Contents"></a>

 ** accountId **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-accountId"></a>
The account to which the recommendation applies.
Type: String
Required: No

 ** actionType **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-actionType"></a>
The type of tasks that can be carried out by this action.
Type: String
Required: No

 ** currencyCode **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-currencyCode"></a>
The currency code used for the recommendation.
Type: String
Required: No

 ** currentResourceSummary **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-currentResourceSummary"></a>
Describes the current resource.
Type: String
Required: No

 ** currentResourceType **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-currentResourceType"></a>
The current resource type.
Type: String
Required: No

 ** estimatedMonthlyCost **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-estimatedMonthlyCost"></a>
The estimated monthly cost of the current resource. For Reserved Instances and Savings Plans, it refers to the cost for eligible usage.
Type: Double
Required: No

 ** estimatedMonthlySavings **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-estimatedMonthlySavings"></a>
The estimated monthly savings amount for the recommendation.
Type: Double
Required: No

 ** estimatedSavingsPercentage **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-estimatedSavingsPercentage"></a>
The estimated savings percentage relative to the total cost over the cost calculation lookback period.
Type: Double
Required: No

 ** implementationEffort **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-implementationEffort"></a>
The effort required to implement the recommendation.
Type: String
Required: No

 ** lastRefreshTimestamp **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-lastRefreshTimestamp"></a>
The time when the recommendation was last generated.
Type: Timestamp
Required: No

 ** recommendationId **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-recommendationId"></a>
The ID for the recommendation.
Type: String
Required: No

 ** recommendationLookbackPeriodInDays **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-recommendationLookbackPeriodInDays"></a>
The lookback period that's used to generate the recommendation.
Type: Integer
Required: No

 ** recommendedResourceSummary **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-recommendedResourceSummary"></a>
Describes the recommended resource.
Type: String
Required: No

 ** recommendedResourceType **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-recommendedResourceType"></a>
The recommended resource type.
Type: String
Required: No

 ** region **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-region"></a>
The AWS Region of the resource.
Type: String
Required: No

 ** resourceArn **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-resourceArn"></a>
The Amazon Resource Name (ARN) for the recommendation.
Type: String
Required: No

 ** resourceId **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-resourceId"></a>
The resource ID for the recommendation.
Type: String
Required: No

 ** restartNeeded **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-restartNeeded"></a>
Whether or not implementing the recommendation requires a restart.
Type: Boolean
Required: No

 ** rollbackPossible **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-rollbackPossible"></a>
Whether or not implementing the recommendation can be rolled back.
Type: Boolean
Required: No

 ** source **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-source"></a>
The source of the recommendation.
Type: String
Valid Values: `ComputeOptimizer | CostExplorer`
Required: No

 ** tags **   <a name="awscostmanagement-Type-CostOptimizationHub_Recommendation-tags"></a>
A list of tags assigned to the recommendation.
Type: Array of [Tag](API_CostOptimizationHub_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## See Also
<a name="API_CostOptimizationHub_Recommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/Recommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/Recommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/Recommendation)
