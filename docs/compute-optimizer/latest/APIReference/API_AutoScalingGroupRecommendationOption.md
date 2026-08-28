---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_AutoScalingGroupRecommendationOption.html
---

# AutoScalingGroupRecommendationOption
<a name="API_AutoScalingGroupRecommendationOption"></a>

Describes a recommendation option for an Auto Scaling group.

## Contents
<a name="API_AutoScalingGroupRecommendationOption_Contents"></a>

 ** configuration **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendationOption-configuration"></a>
An array of objects that describe an Auto Scaling group configuration.
Type: [AutoScalingGroupConfiguration](API_AutoScalingGroupConfiguration.md) object
Required: No

 ** instanceGpuInfo **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendationOption-instanceGpuInfo"></a>
 Describes the GPU accelerator settings for the recommended instance type of the Auto Scaling group.
Type: [GpuInfo](API_GpuInfo.md) object
Required: No

 ** migrationEffort **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendationOption-migrationEffort"></a>
The level of effort required to migrate from the current instance type to the recommended instance type.
For example, the migration effort is `Low` if Amazon EMR is the inferred workload type and an AWS Graviton instance type is recommended. The migration effort is `Medium` if a workload type couldn't be inferred but an AWS Graviton instance type is recommended. The migration effort is `VeryLow` if both the current and recommended instance types are of the same CPU architecture.
Type: String
Valid Values: `VeryLow | Low | Medium | High`
Required: No

 ** performanceRisk **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendationOption-performanceRisk"></a>
The performance risk of the Auto Scaling group configuration recommendation.
Performance risk indicates the likelihood of the recommended instance type not meeting the resource needs of your workload. Compute Optimizer calculates an individual performance risk score for each specification of the recommended instance, including CPU, memory, EBS throughput, EBS IOPS, disk throughput, disk IOPS, network throughput, and network PPS. The performance risk of the recommended instance is calculated as the maximum performance risk score across the analyzed resource specifications.
The value ranges from `0` - `4`, with `0` meaning that the recommended resource is predicted to always provide enough hardware capability. The higher the performance risk is, the more likely you should validate whether the recommendation will meet the performance requirements of your workload before migrating your resource.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 4.
Required: No

 ** projectedUtilizationMetrics **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendationOption-projectedUtilizationMetrics"></a>
An array of objects that describe the projected utilization metrics of the Auto Scaling group recommendation option.
The `Cpu` and `Memory` metrics are the only projected utilization metrics returned. Additionally, the `Memory` metric is returned only for resources that have the unified CloudWatch agent installed on them. For more information, see [Enabling Memory Utilization with the CloudWatch Agent](https://docs.aws.amazon.com/compute-optimizer/latest/ug/metrics.html#cw-agent).
Type: Array of [UtilizationMetric](API_UtilizationMetric.md) objects
Required: No

 ** rank **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendationOption-rank"></a>
The rank of the Auto Scaling group recommendation option.
The top recommendation option is ranked as `1`.
Type: Integer
Required: No

 ** savingsOpportunity **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendationOption-savingsOpportunity"></a>
An object that describes the savings opportunity for the Auto Scaling group recommendation option. Savings opportunity includes the estimated monthly savings amount and percentage.
Type: [SavingsOpportunity](API_SavingsOpportunity.md) object
Required: No

 ** savingsOpportunityAfterDiscounts **   <a name="computeoptimizer-Type-AutoScalingGroupRecommendationOption-savingsOpportunityAfterDiscounts"></a>
 An object that describes the savings opportunity for the Auto Scaling group recommendation option that includes Savings Plans and Reserved Instances discounts. Savings opportunity includes the estimated monthly savings and percentage.
Type: [AutoScalingGroupSavingsOpportunityAfterDiscounts](API_AutoScalingGroupSavingsOpportunityAfterDiscounts.md) object
Required: No

## See Also
<a name="API_AutoScalingGroupRecommendationOption_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/AutoScalingGroupRecommendationOption)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/AutoScalingGroupRecommendationOption)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/AutoScalingGroupRecommendationOption)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
