---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_IdleRecommendation.html
---

# IdleRecommendation
<a name="API_IdleRecommendation"></a>

Describes an Idle resource recommendation.

## Contents
<a name="API_IdleRecommendation_Contents"></a>

 ** accountId **   <a name="computeoptimizer-Type-IdleRecommendation-accountId"></a>
The AWS account ID of the idle resource.
Type: String
Required: No

 ** finding **   <a name="computeoptimizer-Type-IdleRecommendation-finding"></a>
The finding classification of an idle resource.
Type: String
Valid Values: `Idle | Unattached | Unused`
Required: No

 ** findingDescription **   <a name="computeoptimizer-Type-IdleRecommendation-findingDescription"></a>
A summary of the findings for the resource.
Type: String
Required: No

 ** lastRefreshTimestamp **   <a name="computeoptimizer-Type-IdleRecommendation-lastRefreshTimestamp"></a>
The timestamp of when the idle resource recommendation was last generated.
Type: Timestamp
Required: No

 ** lookBackPeriodInDays **   <a name="computeoptimizer-Type-IdleRecommendation-lookBackPeriodInDays"></a>
The number of days the idle resource utilization metrics were analyzed.
Type: Double
Required: No

 ** resourceArn **   <a name="computeoptimizer-Type-IdleRecommendation-resourceArn"></a>
The ARN of the current idle resource.
Type: String
Required: No

 ** resourceId **   <a name="computeoptimizer-Type-IdleRecommendation-resourceId"></a>
The unique identifier for the resource.
Type: String
Required: No

 ** resourceType **   <a name="computeoptimizer-Type-IdleRecommendation-resourceType"></a>
The type of resource that is idle.
Type: String
Valid Values: `EC2Instance | AutoScalingGroup | EBSVolume | ECSService | RDSDBInstance | NatGateway | DynamoDBTable | ElastiCacheCluster | MemoryDBCluster | DocumentDBCluster | WorkSpaces | SageMakerEndpoint`
Required: No

 ** savingsOpportunity **   <a name="computeoptimizer-Type-IdleRecommendation-savingsOpportunity"></a>
The savings opportunity for the idle resource.
Type: [IdleSavingsOpportunity](API_IdleSavingsOpportunity.md) object
Required: No

 ** savingsOpportunityAfterDiscounts **   <a name="computeoptimizer-Type-IdleRecommendation-savingsOpportunityAfterDiscounts"></a>
The savings opportunity for the idle resource after any applying discounts.
Type: [IdleSavingsOpportunityAfterDiscounts](API_IdleSavingsOpportunityAfterDiscounts.md) object
Required: No

 ** tags **   <a name="computeoptimizer-Type-IdleRecommendation-tags"></a>
A list of tags assigned to your idle resource recommendations.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** utilizationMetrics **   <a name="computeoptimizer-Type-IdleRecommendation-utilizationMetrics"></a>
An array of objects that describe the utilization metrics of the idle resource.
Type: Array of [IdleUtilizationMetric](API_IdleUtilizationMetric.md) objects
Required: No

## See Also
<a name="API_IdleRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/IdleRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/IdleRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/IdleRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
