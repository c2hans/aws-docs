---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostOptimizationHub_GetRecommendation.html
---

# GetRecommendation
<a name="API_CostOptimizationHub_GetRecommendation"></a>

Returns both the current and recommended resource configuration and the estimated cost impact for a recommendation.

The `recommendationId` is only valid for up to a maximum of 24 hours as recommendations are refreshed daily. To retrieve the `recommendationId`, use the `ListRecommendations` API.

## Request Syntax
<a name="API_CostOptimizationHub_GetRecommendation_RequestSyntax"></a>

```
{
   "recommendationId": "{{string}}"
}
```

## Request Parameters
<a name="API_CostOptimizationHub_GetRecommendation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [recommendationId](#API_CostOptimizationHub_GetRecommendation_RequestSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-request-recommendationId"></a>
The ID for the recommendation.
Type: String
Required: Yes

## Response Syntax
<a name="API_CostOptimizationHub_GetRecommendation_ResponseSyntax"></a>

```
{
   "accountId": "string",
   "actionType": "string",
   "costCalculationLookbackPeriodInDays": number,
   "currencyCode": "string",
   "currentResourceDetails": { ... },
   "currentResourceType": "string",
   "estimatedMonthlyCost": number,
   "estimatedMonthlySavings": number,
   "estimatedSavingsOverCostCalculationLookbackPeriod": number,
   "estimatedSavingsPercentage": number,
   "implementationEffort": "string",
   "lastRefreshTimestamp": number,
   "recommendationId": "string",
   "recommendationLookbackPeriodInDays": number,
   "recommendedResourceDetails": { ... },
   "recommendedResourceType": "string",
   "region": "string",
   "resourceArn": "string",
   "resourceId": "string",
   "restartNeeded": boolean,
   "rollbackPossible": boolean,
   "source": "string",
   "tags": [
      {
         "key": "string",
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CostOptimizationHub_GetRecommendation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountId](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-accountId"></a>
The account to which the recommendation applies.
Type: String

 ** [actionType](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-actionType"></a>
The type of action you can take by adopting the recommendation.
Type: String
Valid Values: `Rightsize | Stop | Upgrade | PurchaseSavingsPlans | PurchaseReservedInstances | MigrateToGraviton | Delete | ScaleIn`

 ** [costCalculationLookbackPeriodInDays](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-costCalculationLookbackPeriodInDays"></a>
The lookback period used to calculate cost impact for a recommendation.
Type: Integer

 ** [currencyCode](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-currencyCode"></a>
The currency code used for the recommendation.
Type: String

 ** [currentResourceDetails](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-currentResourceDetails"></a>
The details for the resource.
Type: [ResourceDetails](API_CostOptimizationHub_ResourceDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [currentResourceType](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-currentResourceType"></a>
The type of resource.
Type: String
Valid Values: `Ec2Instance | LambdaFunction | EbsVolume | EcsService | Ec2AutoScalingGroup | Ec2InstanceSavingsPlans | ComputeSavingsPlans | SageMakerSavingsPlans | Ec2ReservedInstances | RdsReservedInstances | OpenSearchReservedInstances | RedshiftReservedInstances | ElastiCacheReservedInstances | RdsDbInstanceStorage | RdsDbInstance | AuroraDbClusterStorage | DynamoDbReservedCapacity | MemoryDbReservedInstances | NatGateway | DynamoDBTable | ElastiCacheCluster | MemoryDBCluster | DocumentDBCluster | WorkSpaces | SageMakerEndpoint`

 ** [estimatedMonthlyCost](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-estimatedMonthlyCost"></a>
The estimated monthly cost of the current resource. For Reserved Instances and Savings Plans, it refers to the cost for eligible usage.
Type: Double

 ** [estimatedMonthlySavings](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-estimatedMonthlySavings"></a>
The estimated monthly savings amount for the recommendation.
Type: Double

 ** [estimatedSavingsOverCostCalculationLookbackPeriod](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-estimatedSavingsOverCostCalculationLookbackPeriod"></a>
The estimated savings amount over the lookback period used to calculate cost impact for a recommendation.
Type: Double

 ** [estimatedSavingsPercentage](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-estimatedSavingsPercentage"></a>
The estimated savings percentage relative to the total cost over the cost calculation lookback period.
Type: Double

 ** [implementationEffort](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-implementationEffort"></a>
The effort required to implement the recommendation.
Type: String
Valid Values: `VeryLow | Low | Medium | High | VeryHigh`

 ** [lastRefreshTimestamp](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-lastRefreshTimestamp"></a>
The time when the recommendation was last generated.
Type: Timestamp

 ** [recommendationId](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-recommendationId"></a>
The ID for the recommendation.
Type: String

 ** [recommendationLookbackPeriodInDays](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-recommendationLookbackPeriodInDays"></a>
The lookback period that's used to generate the recommendation.
Type: Integer

 ** [recommendedResourceDetails](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-recommendedResourceDetails"></a>
The details about the recommended resource.
Type: [ResourceDetails](API_CostOptimizationHub_ResourceDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [recommendedResourceType](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-recommendedResourceType"></a>
The resource type of the recommendation.
Type: String
Valid Values: `Ec2Instance | LambdaFunction | EbsVolume | EcsService | Ec2AutoScalingGroup | Ec2InstanceSavingsPlans | ComputeSavingsPlans | SageMakerSavingsPlans | Ec2ReservedInstances | RdsReservedInstances | OpenSearchReservedInstances | RedshiftReservedInstances | ElastiCacheReservedInstances | RdsDbInstanceStorage | RdsDbInstance | AuroraDbClusterStorage | DynamoDbReservedCapacity | MemoryDbReservedInstances | NatGateway | DynamoDBTable | ElastiCacheCluster | MemoryDBCluster | DocumentDBCluster | WorkSpaces | SageMakerEndpoint`

 ** [region](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-region"></a>
The AWS Region of the resource.
Type: String

 ** [resourceArn](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-resourceArn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String

 ** [resourceId](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-resourceId"></a>
The unique identifier for the resource. This is the same as the Amazon Resource Name (ARN), if available.
Type: String

 ** [restartNeeded](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-restartNeeded"></a>
Whether or not implementing the recommendation requires a restart.
Type: Boolean

 ** [rollbackPossible](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-rollbackPossible"></a>
Whether or not implementing the recommendation can be rolled back.
Type: Boolean

 ** [source](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-source"></a>
The source of the recommendation.
Type: String
Valid Values: `ComputeOptimizer | CostExplorer`

 ** [tags](#API_CostOptimizationHub_GetRecommendation_ResponseSyntax) **   <a name="awscostmanagement-CostOptimizationHub_GetRecommendation-response-tags"></a>
A list of tags associated with the resource for which the recommendation exists.
Type: Array of [Tag](API_CostOptimizationHub_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

## Errors
<a name="API_CostOptimizationHub_GetRecommendation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to use this operation with the given parameters.
HTTP Status Code: 400

 ** InternalServerException **
An error on the server occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified Amazon Resource Name (ARN) in the request doesn't exist.
 ** resourceId **
The identifier of the resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fields **
The list of fields that are invalid.
 ** reason **
The reason for the validation exception.
HTTP Status Code: 400

## See Also
<a name="API_CostOptimizationHub_GetRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cost-optimization-hub-2022-07-26/GetRecommendation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cost-optimization-hub-2022-07-26/GetRecommendation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cost-optimization-hub-2022-07-26/GetRecommendation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cost-optimization-hub-2022-07-26/GetRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cost-optimization-hub-2022-07-26/GetRecommendation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cost-optimization-hub-2022-07-26/GetRecommendation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cost-optimization-hub-2022-07-26/GetRecommendation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cost-optimization-hub-2022-07-26/GetRecommendation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cost-optimization-hub-2022-07-26/GetRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cost-optimization-hub-2022-07-26/GetRecommendation)
