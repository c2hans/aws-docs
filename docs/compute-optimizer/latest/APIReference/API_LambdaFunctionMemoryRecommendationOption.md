---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_LambdaFunctionMemoryRecommendationOption.html
---

# LambdaFunctionMemoryRecommendationOption
<a name="API_LambdaFunctionMemoryRecommendationOption"></a>

Describes a recommendation option for an AWS Lambda function.

## Contents
<a name="API_LambdaFunctionMemoryRecommendationOption_Contents"></a>

 ** memorySize **   <a name="computeoptimizer-Type-LambdaFunctionMemoryRecommendationOption-memorySize"></a>
The memory size, in MB, of the function recommendation option.
Type: Integer
Required: No

 ** projectedUtilizationMetrics **   <a name="computeoptimizer-Type-LambdaFunctionMemoryRecommendationOption-projectedUtilizationMetrics"></a>
An array of objects that describe the projected utilization metrics of the function recommendation option.
Type: Array of [LambdaFunctionMemoryProjectedMetric](API_LambdaFunctionMemoryProjectedMetric.md) objects
Required: No

 ** rank **   <a name="computeoptimizer-Type-LambdaFunctionMemoryRecommendationOption-rank"></a>
The rank of the function recommendation option.
The top recommendation option is ranked as `1`.
Type: Integer
Required: No

 ** savingsOpportunity **   <a name="computeoptimizer-Type-LambdaFunctionMemoryRecommendationOption-savingsOpportunity"></a>
An object that describes the savings opportunity for the Lambda function recommendation option. Savings opportunity includes the estimated monthly savings amount and percentage.
Type: [SavingsOpportunity](API_SavingsOpportunity.md) object
Required: No

 ** savingsOpportunityAfterDiscounts **   <a name="computeoptimizer-Type-LambdaFunctionMemoryRecommendationOption-savingsOpportunityAfterDiscounts"></a>
 An object that describes the savings opportunity for the Lambda recommendation option which includes Saving Plans discounts. Savings opportunity includes the estimated monthly savings and percentage.
Type: [LambdaSavingsOpportunityAfterDiscounts](API_LambdaSavingsOpportunityAfterDiscounts.md) object
Required: No

## See Also
<a name="API_LambdaFunctionMemoryRecommendationOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/LambdaFunctionMemoryRecommendationOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/LambdaFunctionMemoryRecommendationOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/LambdaFunctionMemoryRecommendationOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
