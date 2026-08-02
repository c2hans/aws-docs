---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_IdleRecommendationError.html
---

# IdleRecommendationError
<a name="API_IdleRecommendationError"></a>

Returns of list of resources that doesn't have idle recommendations.

## Contents
<a name="API_IdleRecommendationError_Contents"></a>

 ** code **   <a name="computeoptimizer-Type-IdleRecommendationError-code"></a>
The error code.
Type: String
Required: No

 ** identifier **   <a name="computeoptimizer-Type-IdleRecommendationError-identifier"></a>
The ID of the error.
Type: String
Required: No

 ** message **   <a name="computeoptimizer-Type-IdleRecommendationError-message"></a>
The error message.
Type: String
Required: No

 ** resourceType **   <a name="computeoptimizer-Type-IdleRecommendationError-resourceType"></a>
The type of resource associated with the error.
Type: String
Valid Values: `EC2Instance | AutoScalingGroup | EBSVolume | ECSService | RDSDBInstance | NatGateway | DynamoDBTable | ElastiCacheCluster | MemoryDBCluster | DocumentDBCluster | WorkSpaces | SageMakerEndpoint`
Required: No

## See Also
<a name="API_IdleRecommendationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/IdleRecommendationError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/IdleRecommendationError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/IdleRecommendationError)
