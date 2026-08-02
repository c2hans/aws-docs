---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_Filter.html
---

# Filter
<a name="API_CostOptimizationHub_Filter"></a>

Describes a filter that returns a more specific list of recommendations. Filters recommendations by different dimensions.

## Contents
<a name="API_CostOptimizationHub_Filter_Contents"></a>

 ** accountIds **   <a name="awscostmanagement-Type-CostOptimizationHub_Filter-accountIds"></a>
The account to which the recommendation applies.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `[0-9]{12}`
Required: No

 ** actionTypes **   <a name="awscostmanagement-Type-CostOptimizationHub_Filter-actionTypes"></a>
The type of action you can take by adopting the recommendation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Valid Values: `Rightsize | Stop | Upgrade | PurchaseSavingsPlans | PurchaseReservedInstances | MigrateToGraviton | Delete | ScaleIn`
Required: No

 ** implementationEfforts **   <a name="awscostmanagement-Type-CostOptimizationHub_Filter-implementationEfforts"></a>
The effort required to implement the recommendation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Valid Values: `VeryLow | Low | Medium | High | VeryHigh`
Required: No

 ** recommendationIds **   <a name="awscostmanagement-Type-CostOptimizationHub_Filter-recommendationIds"></a>
The IDs for the recommendations.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** regions **   <a name="awscostmanagement-Type-CostOptimizationHub_Filter-regions"></a>
The AWS Region of the resource.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** resourceArns **   <a name="awscostmanagement-Type-CostOptimizationHub_Filter-resourceArns"></a>
The Amazon Resource Name (ARN) of the recommendation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** resourceIds **   <a name="awscostmanagement-Type-CostOptimizationHub_Filter-resourceIds"></a>
The resource ID of the recommendation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** resourceTypes **   <a name="awscostmanagement-Type-CostOptimizationHub_Filter-resourceTypes"></a>
The resource type of the recommendation.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Valid Values: `Ec2Instance | LambdaFunction | EbsVolume | EcsService | Ec2AutoScalingGroup | Ec2InstanceSavingsPlans | ComputeSavingsPlans | SageMakerSavingsPlans | Ec2ReservedInstances | RdsReservedInstances | OpenSearchReservedInstances | RedshiftReservedInstances | ElastiCacheReservedInstances | RdsDbInstanceStorage | RdsDbInstance | AuroraDbClusterStorage | DynamoDbReservedCapacity | MemoryDbReservedInstances | NatGateway | DynamoDBTable | ElastiCacheCluster | MemoryDBCluster | DocumentDBCluster | WorkSpaces | SageMakerEndpoint`
Required: No

 ** restartNeeded **   <a name="awscostmanagement-Type-CostOptimizationHub_Filter-restartNeeded"></a>
Whether or not implementing the recommendation requires a restart.
Type: Boolean
Required: No

 ** rollbackPossible **   <a name="awscostmanagement-Type-CostOptimizationHub_Filter-rollbackPossible"></a>
Whether or not implementing the recommendation can be rolled back.
Type: Boolean
Required: No

 ** tags **   <a name="awscostmanagement-Type-CostOptimizationHub_Filter-tags"></a>
A list of tags assigned to the recommendation.
Type: Array of [Tag](API_CostOptimizationHub_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## See Also
<a name="API_CostOptimizationHub_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/Filter)
