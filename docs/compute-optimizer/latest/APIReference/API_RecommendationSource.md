---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_RecommendationSource.html
---

# RecommendationSource
<a name="API_RecommendationSource"></a>

Describes the source of a recommendation, such as an Amazon EC2 instance or Auto Scaling group.

## Contents
<a name="API_RecommendationSource_Contents"></a>

 ** recommendationSourceArn **   <a name="computeoptimizer-Type-RecommendationSource-recommendationSourceArn"></a>
The Amazon Resource Name (ARN) of the recommendation source.
Type: String
Required: No

 ** recommendationSourceType **   <a name="computeoptimizer-Type-RecommendationSource-recommendationSourceType"></a>
The resource type of the recommendation source.
Type: String
Valid Values: `Ec2Instance | AutoScalingGroup | EbsVolume | LambdaFunction | EcsService | License | RdsDBInstance | RdsDBInstanceStorage | AuroraDBClusterStorage | NatGateway | DynamoDBTable | ElastiCacheCluster | MemoryDBCluster | DocumentDBCluster | WorkSpaces | SageMakerEndpoint`
Required: No

## See Also
<a name="API_RecommendationSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/RecommendationSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/RecommendationSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/RecommendationSource)
