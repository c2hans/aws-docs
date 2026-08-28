---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RecommendationSummary.html
---

# RecommendationSummary
<a name="API_RecommendationSummary"></a>

A summary of a recommendation.

## Contents
<a name="API_RecommendationSummary_Contents"></a>

 ** accountId **   <a name="computeoptimizer-Type-RecommendationSummary-accountId"></a>
The AWS account ID of the recommendation summary.
Type: String
Required: No

 ** aggregatedSavingsOpportunity **   <a name="computeoptimizer-Type-RecommendationSummary-aggregatedSavingsOpportunity"></a>
Describes the savings opportunity for recommendations of a given resource type or for the recommendation option of an individual resource.
Savings opportunity represents the estimated monthly savings you can achieve by implementing a given Compute Optimizer recommendation.
Savings opportunity data requires that you opt in to Cost Explorer, as well as activate **Receive Amazon EC2 resource recommendations** in the Cost Explorer preferences page. That creates a connection between Cost Explorer and Compute Optimizer. With this connection, Cost Explorer generates savings estimates considering the price of existing resources, the price of recommended resources, and historical usage data. Estimated monthly savings reflects the projected dollar savings associated with each of the recommendations generated. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [Optimizing your cost with Rightsizing Recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html) in the *Cost Management User Guide*.
Type: [SavingsOpportunity](API_SavingsOpportunity.md) object
Required: No

 ** currentPerformanceRiskRatings **   <a name="computeoptimizer-Type-RecommendationSummary-currentPerformanceRiskRatings"></a>
An object that describes the performance risk ratings for a given resource type.
Type: [CurrentPerformanceRiskRatings](API_CurrentPerformanceRiskRatings.md) object
Required: No

 ** idleSavingsOpportunity **   <a name="computeoptimizer-Type-RecommendationSummary-idleSavingsOpportunity"></a>
Describes the savings opportunity for recommendations of a given resource type or for the recommendation option of an individual resource.
Savings opportunity represents the estimated monthly savings you can achieve by implementing a given Compute Optimizer recommendation.
Savings opportunity data requires that you opt in to Cost Explorer, as well as activate **Receive Amazon EC2 resource recommendations** in the Cost Explorer preferences page. That creates a connection between Cost Explorer and Compute Optimizer. With this connection, Cost Explorer generates savings estimates considering the price of existing resources, the price of recommended resources, and historical usage data. Estimated monthly savings reflects the projected dollar savings associated with each of the recommendations generated. For more information, see [Enabling Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-enable.html) and [Optimizing your cost with Rightsizing Recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html) in the *Cost Management User Guide*.
Type: [SavingsOpportunity](API_SavingsOpportunity.md) object
Required: No

 ** idleSummaries **   <a name="computeoptimizer-Type-RecommendationSummary-idleSummaries"></a>
 Describes the findings summary of the idle resources.
Type: Array of [IdleSummary](API_IdleSummary.md) objects
Required: No

 ** inferredWorkloadSavings **   <a name="computeoptimizer-Type-RecommendationSummary-inferredWorkloadSavings"></a>
 An array of objects that describes the estimated monthly saving amounts for the instances running on the specified `inferredWorkloadTypes`. The array contains the top five savings opportunites for the instances that run inferred workload types.
Type: Array of [InferredWorkloadSaving](API_InferredWorkloadSaving.md) objects
Required: No

 ** recommendationResourceType **   <a name="computeoptimizer-Type-RecommendationSummary-recommendationResourceType"></a>
The resource type that the recommendation summary applies to.
Type: String
Valid Values: `Ec2Instance | AutoScalingGroup | EbsVolume | LambdaFunction | EcsService | License | RdsDBInstance | RdsDBInstanceStorage | AuroraDBClusterStorage | NatGateway | DynamoDBTable | ElastiCacheCluster | MemoryDBCluster | DocumentDBCluster | WorkSpaces | SageMakerEndpoint`
Required: No

 ** savingsOpportunity **   <a name="computeoptimizer-Type-RecommendationSummary-savingsOpportunity"></a>
An object that describes the savings opportunity for a given resource type. Savings opportunity includes the estimated monthly savings amount and percentage.
Type: [SavingsOpportunity](API_SavingsOpportunity.md) object
Required: No

 ** summaries **   <a name="computeoptimizer-Type-RecommendationSummary-summaries"></a>
An array of objects that describe a recommendation summary.
Type: Array of [Summary](API_Summary.md) objects
Required: No

## See Also
<a name="API_RecommendationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/RecommendationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/RecommendationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/RecommendationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
