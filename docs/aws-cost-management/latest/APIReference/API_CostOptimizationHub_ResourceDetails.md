---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_ResourceDetails.html
---

# ResourceDetails
<a name="API_CostOptimizationHub_ResourceDetails"></a>

Contains detailed information about the specified resource.

## Contents
<a name="API_CostOptimizationHub_ResourceDetails_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** auroraDbClusterStorage **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-auroraDbClusterStorage"></a>
The Aurora DB cluster storage recommendation details.
Type: [AuroraDbClusterStorage](API_CostOptimizationHub_AuroraDbClusterStorage.md) object
Required: No

 ** computeSavingsPlans **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-computeSavingsPlans"></a>
The Compute Savings Plans recommendation details.
Type: [ComputeSavingsPlans](API_CostOptimizationHub_ComputeSavingsPlans.md) object
Required: No

 ** documentDbCluster **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-documentDbCluster"></a>
The Amazon DocumentDB cluster recommendation details.
Type: [DocumentDbCluster](API_CostOptimizationHub_DocumentDbCluster.md) object
Required: No

 ** dynamoDbReservedCapacity **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-dynamoDbReservedCapacity"></a>
The DynamoDB reserved capacity recommendation details.
Type: [DynamoDbReservedCapacity](API_CostOptimizationHub_DynamoDbReservedCapacity.md) object
Required: No

 ** dynamoDbTable **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-dynamoDbTable"></a>
The DynamoDB table recommendation details.
Type: [DynamoDbTable](API_CostOptimizationHub_DynamoDbTable.md) object
Required: No

 ** ebsVolume **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-ebsVolume"></a>
The Amazon Elastic Block Store volume recommendation details.
Type: [EbsVolume](API_CostOptimizationHub_EbsVolume.md) object
Required: No

 ** ec2AutoScalingGroup **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-ec2AutoScalingGroup"></a>
The EC2 Auto Scaling group recommendation details.
Type: [Ec2AutoScalingGroup](API_CostOptimizationHub_Ec2AutoScalingGroup.md) object
Required: No

 ** ec2Instance **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-ec2Instance"></a>
The EC2 instance recommendation details.
Type: [Ec2Instance](API_CostOptimizationHub_Ec2Instance.md) object
Required: No

 ** ec2InstanceSavingsPlans **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-ec2InstanceSavingsPlans"></a>
The EC2 instance Savings Plans recommendation details.
Type: [Ec2InstanceSavingsPlans](API_CostOptimizationHub_Ec2InstanceSavingsPlans.md) object
Required: No

 ** ec2ReservedInstances **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-ec2ReservedInstances"></a>
The EC2 reserved instances recommendation details.
Type: [Ec2ReservedInstances](API_CostOptimizationHub_Ec2ReservedInstances.md) object
Required: No

 ** ecsService **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-ecsService"></a>
The ECS service recommendation details.
Type: [EcsService](API_CostOptimizationHub_EcsService.md) object
Required: No

 ** elastiCacheCluster **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-elastiCacheCluster"></a>
The ElastiCache cluster recommendation details.
Type: [ElastiCacheCluster](API_CostOptimizationHub_ElastiCacheCluster.md) object
Required: No

 ** elastiCacheReservedInstances **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-elastiCacheReservedInstances"></a>
The ElastiCache reserved instances recommendation details.
Type: [ElastiCacheReservedInstances](API_CostOptimizationHub_ElastiCacheReservedInstances.md) object
Required: No

 ** lambdaFunction **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-lambdaFunction"></a>
The Lambda function recommendation details.
Type: [LambdaFunction](API_CostOptimizationHub_LambdaFunction.md) object
Required: No

 ** memoryDbCluster **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-memoryDbCluster"></a>
The MemoryDB cluster recommendation details.
Type: [MemoryDbCluster](API_CostOptimizationHub_MemoryDbCluster.md) object
Required: No

 ** memoryDbReservedInstances **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-memoryDbReservedInstances"></a>
The MemoryDB reserved instances recommendation details.
Type: [MemoryDbReservedInstances](API_CostOptimizationHub_MemoryDbReservedInstances.md) object
Required: No

 ** natGateway **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-natGateway"></a>
The NAT Gateway recommendation details.
Type: [NatGateway](API_CostOptimizationHub_NatGateway.md) object
Required: No

 ** openSearchReservedInstances **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-openSearchReservedInstances"></a>
The OpenSearch reserved instances recommendation details.
Type: [OpenSearchReservedInstances](API_CostOptimizationHub_OpenSearchReservedInstances.md) object
Required: No

 ** rdsDbInstance **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-rdsDbInstance"></a>
The DB instance recommendation details.
Type: [RdsDbInstance](API_CostOptimizationHub_RdsDbInstance.md) object
Required: No

 ** rdsDbInstanceStorage **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-rdsDbInstanceStorage"></a>
The DB instance storage recommendation details.
Type: [RdsDbInstanceStorage](API_CostOptimizationHub_RdsDbInstanceStorage.md) object
Required: No

 ** rdsReservedInstances **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-rdsReservedInstances"></a>
The RDS reserved instances recommendation details.
Type: [RdsReservedInstances](API_CostOptimizationHub_RdsReservedInstances.md) object
Required: No

 ** redshiftReservedInstances **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-redshiftReservedInstances"></a>
The Redshift reserved instances recommendation details.
Type: [RedshiftReservedInstances](API_CostOptimizationHub_RedshiftReservedInstances.md) object
Required: No

 ** sageMakerEndpoint **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-sageMakerEndpoint"></a>
The SageMaker endpoint recommendation details.
Type: [SageMakerEndpoint](API_CostOptimizationHub_SageMakerEndpoint.md) object
Required: No

 ** sageMakerSavingsPlans **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-sageMakerSavingsPlans"></a>
The SageMaker AI Savings Plans recommendation details.
Type: [SageMakerSavingsPlans](API_CostOptimizationHub_SageMakerSavingsPlans.md) object
Required: No

 ** workSpaces **   <a name="awscostmanagement-Type-CostOptimizationHub_ResourceDetails-workSpaces"></a>
The WorkSpaces recommendation details.
Type: [WorkSpaces](API_CostOptimizationHub_WorkSpaces.md) object
Required: No

## See Also
<a name="API_CostOptimizationHub_ResourceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/ResourceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/ResourceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/ResourceDetails)
