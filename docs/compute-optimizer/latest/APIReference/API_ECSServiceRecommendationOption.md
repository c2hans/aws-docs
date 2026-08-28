---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_ECSServiceRecommendationOption.html
---

# ECSServiceRecommendationOption
<a name="API_ECSServiceRecommendationOption"></a>

 Describes the recommendation options for an Amazon ECS service.

## Contents
<a name="API_ECSServiceRecommendationOption_Contents"></a>

 ** containerRecommendations **   <a name="computeoptimizer-Type-ECSServiceRecommendationOption-containerRecommendations"></a>
 The CPU and memory size recommendations for the containers within the task of your Amazon ECS service.
Type: Array of [ContainerRecommendation](API_ContainerRecommendation.md) objects
Required: No

 ** cpu **   <a name="computeoptimizer-Type-ECSServiceRecommendationOption-cpu"></a>
 The CPU size of the Amazon ECS service recommendation option.
Type: Integer
Required: No

 ** memory **   <a name="computeoptimizer-Type-ECSServiceRecommendationOption-memory"></a>
 The memory size of the Amazon ECS service recommendation option.
Type: Integer
Required: No

 ** projectedUtilizationMetrics **   <a name="computeoptimizer-Type-ECSServiceRecommendationOption-projectedUtilizationMetrics"></a>
 An array of objects that describe the projected utilization metrics of the Amazon ECS service recommendation option.
Type: Array of [ECSServiceProjectedUtilizationMetric](API_ECSServiceProjectedUtilizationMetric.md) objects
Required: No

 ** savingsOpportunity **   <a name="computeoptimizer-Type-ECSServiceRecommendationOption-savingsOpportunity"></a>
Describes the savings opportunity for recommendations of a given resource type or for the recommendation option of an individual resource.
Savings opportunity represents the estimated monthly savings you can achieve by implementing a given Compute Optimizer recommendation.
Savings opportunity data requires that you opt in to Cost Explorer, as well as activate **Receive Amazon EC2 resource recommendations** in the Cost Explorer preferences page. That creates a connection between Cost Explorer and Compute Optimizer. With this connection, Cost Explorer generates savings estimates considering the price of existing resources, the price of recommended resources, and historical usage data. Estimated monthly savings reflects the projected dollar savings associated with each of the recommendations generated. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [Optimizing your cost with Rightsizing Recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html) in the *Cost Management User Guide*.
Type: [SavingsOpportunity](API_SavingsOpportunity.md) object
Required: No

 ** savingsOpportunityAfterDiscounts **   <a name="computeoptimizer-Type-ECSServiceRecommendationOption-savingsOpportunityAfterDiscounts"></a>
 Describes the savings opportunity for Amazon ECS service recommendations or for the recommendation option.
Savings opportunity represents the estimated monthly savings after applying Savings Plans discounts. You can achieve this by implementing a given Compute Optimizer recommendation.
Type: [ECSSavingsOpportunityAfterDiscounts](API_ECSSavingsOpportunityAfterDiscounts.md) object
Required: No

## See Also
<a name="API_ECSServiceRecommendationOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/ECSServiceRecommendationOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/ECSServiceRecommendationOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/ECSServiceRecommendationOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
