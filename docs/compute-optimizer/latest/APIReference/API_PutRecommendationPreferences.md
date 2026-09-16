---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_PutRecommendationPreferences.html
---

# PutRecommendationPreferences
<a name="API_PutRecommendationPreferences"></a>

Creates a new recommendation preference or updates an existing recommendation preference, such as enhanced infrastructure metrics.

For more information, see [Activating enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the * AWS Compute Optimizer User Guide*.

## Request Syntax
<a name="API_PutRecommendationPreferences_RequestSyntax"></a>

```
{
   "enhancedInfrastructureMetrics": "{{string}}",
   "externalMetricsPreference": {
      "source": "{{string}}"
   },
   "inferredWorkloadTypes": "{{string}}",
   "lookBackPeriod": "{{string}}",
   "preferredResources": [
      {
         "excludeList": [ "{{string}}" ],
         "includeList": [ "{{string}}" ],
         "name": "{{string}}"
      }
   ],
   "resourceType": "{{string}}",
   "savingsEstimationMode": "{{string}}",
   "scope": {
      "name": "{{string}}",
      "value": "{{string}}"
   },
   "utilizationPreferences": [
      {
         "metricName": "{{string}}",
         "metricParameters": {
            "headroom": "{{string}}",
            "threshold": "{{string}}"
         }
      }
   ]
}
```

## Request Parameters
<a name="API_PutRecommendationPreferences_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [enhancedInfrastructureMetrics](#API_PutRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-PutRecommendationPreferences-request-enhancedInfrastructureMetrics"></a>
The status of the enhanced infrastructure metrics recommendation preference to create or update.
Specify the `Active` status to activate the preference, or specify `Inactive` to deactivate the preference.
For more information, see [Enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the * AWS Compute Optimizer User Guide*.
Type: String
Valid Values: `Active | Inactive`
Required: No

 ** [externalMetricsPreference](#API_PutRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-PutRecommendationPreferences-request-externalMetricsPreference"></a>
The provider of the external metrics recommendation preference to create or update.
Specify a valid provider in the `source` field to activate the preference. To delete this preference, see the [DeleteRecommendationPreferences](API_DeleteRecommendationPreferences.md) action.
This preference can only be set for the `Ec2Instance` resource type.
For more information, see [External metrics ingestion](https://docs.aws.amazon.com/compute-optimizer/latest/ug/external-metrics-ingestion.html) in the * AWS Compute Optimizer User Guide*.
Type: [ExternalMetricsPreference](API_ExternalMetricsPreference.md) object
Required: No

 ** [inferredWorkloadTypes](#API_PutRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-PutRecommendationPreferences-request-inferredWorkloadTypes"></a>
The status of the inferred workload types recommendation preference to create or update.
The inferred workload type feature is active by default. To deactivate it, create a recommendation preference.
Specify the `Inactive` status to deactivate the feature, or specify `Active` to activate it.
For more information, see [Inferred workload types](https://docs.aws.amazon.com/compute-optimizer/latest/ug/inferred-workload-types.html) in the * AWS Compute Optimizer User Guide*.
Type: String
Valid Values: `Active | Inactive`
Required: No

 ** [lookBackPeriod](#API_PutRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-PutRecommendationPreferences-request-lookBackPeriod"></a>
 The preference to control the number of days the utilization metrics of the AWS resource are analyzed. When this preference isn't specified, we use the default value `DAYS_14`.
You can only set this preference for the Amazon EC2 instance, Auto Scaling group, Amazon EBS volume, Amazon ECS service on Fargate, Amazon RDS DB instance, and Aurora DB cluster storage resource types.
+ Lookback period preferences for Amazon EC2 instances, Amazon EBS volumes, Amazon ECS services, Amazon RDS DB instances, and Aurora DB cluster storage resource types can be set at the organization, account, and resource levels.
+ Auto Scaling group lookback preferences can only be set at the resource level.
+ Amazon EBS volume lookback preferences can be set at the organization, account, and resource levels.
+ Amazon ECS service on Fargate lookback preferences can be set at the organization, account, and resource levels.
+ Amazon RDS DB instance lookback preferences can be set at the organization, account, and resource levels.
+ Aurora DB cluster storage lookback preferences can be set at the organization, account, and resource levels.
+ Changing the lookback period for Amazon EBS volumes to 14 days does not affect the 32-day lookback period used to determine whether an Amazon EBS volume is unattached.
Type: String
Valid Values: `DAYS_14 | DAYS_32 | DAYS_93`
Required: No

 ** [preferredResources](#API_PutRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-PutRecommendationPreferences-request-preferredResources"></a>
 The preference to control which resource type values are considered when generating rightsizing recommendations. You can specify this preference as a combination of include and exclude lists. You must specify either an `includeList` or `excludeList`. If the preference is an empty set of resource type values, an error occurs.
You can only set this preference for the Amazon EC2 instance, Auto Scaling group, Amazon EBS volume, Amazon ECS service, Amazon RDS DB instance, and Aurora DB cluster storage resource types.
Type: Array of [PreferredResource](API_PreferredResource.md) objects
Required: No

 ** [resourceType](#API_PutRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-PutRecommendationPreferences-request-resourceType"></a>
The target resource type of the recommendation preference to create.
The `Ec2Instance` option encompasses standalone instances and instances that are part of Auto Scaling groups. The `AutoScalingGroup` option encompasses only instances that are part of an Auto Scaling group.
Type: String
Valid Values: `Ec2Instance | AutoScalingGroup | EbsVolume | EcsService | RdsDBInstance | AuroraDBClusterStorage`
Required: Yes

 ** [savingsEstimationMode](#API_PutRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-PutRecommendationPreferences-request-savingsEstimationMode"></a>
 The status of the savings estimation mode preference to create or update.
Specify the `AfterDiscounts` status to activate the preference, or specify `BeforeDiscounts` to deactivate the preference.
Only the account manager or delegated administrator of your organization can activate this preference.
For more information, see [ Savings estimation mode](https://docs.aws.amazon.com/compute-optimizer/latest/ug/savings-estimation-mode.html) in the * AWS Compute Optimizer User Guide*.
Type: String
Valid Values: `AfterDiscounts | BeforeDiscounts`
Required: No

 ** [scope](#API_PutRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-PutRecommendationPreferences-request-scope"></a>
An object that describes the scope of the recommendation preference to create.
You can create recommendation preferences at the organization level (for management accounts of an organization only), account level, and resource level. For more information, see [Activating enhanced infrastructure metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/enhanced-infrastructure-metrics.html) in the * AWS Compute Optimizer User Guide*.
You cannot create recommendation preferences for Auto Scaling groups at the organization and account levels. You can create recommendation preferences for Auto Scaling groups only at the resource level by specifying a scope name of `ResourceArn` and a scope value of the Auto Scaling group Amazon Resource Name (ARN). This will configure the preference for all instances that are part of the specified Auto Scaling group. You also cannot create recommendation preferences at the resource level for instances that are part of an Auto Scaling group. You can create recommendation preferences at the resource level only for standalone instances.
Type: [Scope](API_Scope.md) object
Required: No

 ** [utilizationPreferences](#API_PutRecommendationPreferences_RequestSyntax) **   <a name="computeoptimizer-PutRecommendationPreferences-request-utilizationPreferences"></a>
 The preference to control the resource’s CPU utilization threshold, CPU utilization headroom, and memory utilization headroom. When this preference isn't specified, we use the following default values.
CPU utilization:
+  `P99_5` for threshold
+  `PERCENT_20` for headroom
Memory utilization:
+  `PERCENT_20` for headroom
+ You can only set CPU and memory utilization preferences for the Amazon EC2 instance resource type.
+ The threshold setting isn’t available for memory utilization.
Type: Array of [UtilizationPreference](API_UtilizationPreference.md) objects
Required: No

## Response Elements
<a name="API_PutRecommendationPreferences_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutRecommendationPreferences_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An internal error has occurred. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterValueException **
The value supplied for the input parameter is out of range or not valid.
HTTP Status Code: 400

 ** MissingAuthenticationToken **
The request must contain either a valid (registered) AWS access key ID or X.509 certificate.
HTTP Status Code: 400

 ** OptInRequiredException **
The account is not opted in to AWS Compute Optimizer.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource that is required for the action doesn't exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The request has failed due to a temporary failure of the server.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_PutRecommendationPreferences_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-2019-11-01/PutRecommendationPreferences)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-2019-11-01/PutRecommendationPreferences)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-2019-11-01/PutRecommendationPreferences)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-2019-11-01/PutRecommendationPreferences)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-2019-11-01/PutRecommendationPreferences)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-2019-11-01/PutRecommendationPreferences)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-2019-11-01/PutRecommendationPreferences)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-2019-11-01/PutRecommendationPreferences)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-2019-11-01/PutRecommendationPreferences)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-2019-11-01/PutRecommendationPreferences)
