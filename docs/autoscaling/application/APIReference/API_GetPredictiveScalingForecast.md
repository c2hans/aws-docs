---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_GetPredictiveScalingForecast.html
---

# GetPredictiveScalingForecast
<a name="API_GetPredictiveScalingForecast"></a>

Retrieves the forecast data for a predictive scaling policy.

Load forecasts are predictions of the hourly load values using historical load data from CloudWatch and an analysis of historical trends. Capacity forecasts are represented as predicted values for the minimum capacity that is needed on an hourly basis, based on the hourly load forecast.

A minimum of 24 hours of data is required to create the initial forecasts. However, having a full 14 days of historical data results in more accurate forecasts.

## Request Syntax
<a name="API_GetPredictiveScalingForecast_RequestSyntax"></a>

```
{
   "EndTime": {{number}},
   "PolicyName": "{{string}}",
   "ResourceId": "{{string}}",
   "ScalableDimension": "{{string}}",
   "ServiceNamespace": "{{string}}",
   "StartTime": {{number}}
}
```

## Request Parameters
<a name="API_GetPredictiveScalingForecast_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndTime](#API_GetPredictiveScalingForecast_RequestSyntax) **   <a name="autoscaling-GetPredictiveScalingForecast-request-EndTime"></a>
 The exclusive end time of the time range for the forecast data to get. The maximum time duration between the start and end time is 30 days.
Type: Timestamp
Required: Yes

 ** [PolicyName](#API_GetPredictiveScalingForecast_RequestSyntax) **   <a name="autoscaling-GetPredictiveScalingForecast-request-PolicyName"></a>
The name of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `\p{Print}+`
Required: Yes

 ** [ResourceId](#API_GetPredictiveScalingForecast_RequestSyntax) **   <a name="autoscaling-GetPredictiveScalingForecast-request-ResourceId"></a>
 The identifier of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** [ScalableDimension](#API_GetPredictiveScalingForecast_RequestSyntax) **   <a name="autoscaling-GetPredictiveScalingForecast-request-ScalableDimension"></a>
 The scalable dimension.
Type: String
Valid Values: `ecs:service:DesiredCount | ec2:spot-fleet-request:TargetCapacity | elasticmapreduce:instancegroup:InstanceCount | appstream:fleet:DesiredCapacity | dynamodb:table:ReadCapacityUnits | dynamodb:table:WriteCapacityUnits | dynamodb:index:ReadCapacityUnits | dynamodb:index:WriteCapacityUnits | rds:cluster:ReadReplicaCount | sagemaker:variant:DesiredInstanceCount | custom-resource:ResourceType:Property | comprehend:document-classifier-endpoint:DesiredInferenceUnits | comprehend:entity-recognizer-endpoint:DesiredInferenceUnits | lambda:function:ProvisionedConcurrency | cassandra:table:ReadCapacityUnits | cassandra:table:WriteCapacityUnits | kafka:broker-storage:VolumeSize | elasticache:cache-cluster:Nodes | elasticache:replication-group:NodeGroups | elasticache:replication-group:Replicas | neptune:cluster:ReadReplicaCount | sagemaker:variant:DesiredProvisionedConcurrency | sagemaker:inference-component:DesiredCopyCount | workspaces:workspacespool:DesiredUserSessions`
Required: Yes

 ** [ServiceNamespace](#API_GetPredictiveScalingForecast_RequestSyntax) **   <a name="autoscaling-GetPredictiveScalingForecast-request-ServiceNamespace"></a>
 The namespace of the AWS service that provides the resource. For a resource provided by your own application or service, use `custom-resource` instead.
Type: String
Valid Values: `ecs | elasticmapreduce | ec2 | appstream | dynamodb | rds | sagemaker | custom-resource | comprehend | lambda | cassandra | kafka | elasticache | neptune | workspaces`
Required: Yes

 ** [StartTime](#API_GetPredictiveScalingForecast_RequestSyntax) **   <a name="autoscaling-GetPredictiveScalingForecast-request-StartTime"></a>
 The inclusive start time of the time range for the forecast data to get. At most, the date and time can be one year before the current date and time
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_GetPredictiveScalingForecast_ResponseSyntax"></a>

```
{
   "CapacityForecast": {
      "Timestamps": [ number ],
      "Values": [ number ]
   },
   "LoadForecast": [
      {
         "MetricSpecification": {
            "CustomizedCapacityMetricSpecification": {
               "MetricDataQueries": [
                  {
                     "Expression": "string",
                     "Id": "string",
                     "Label": "string",
                     "MetricStat": {
                        "Metric": {
                           "Dimensions": [
                              {
                                 "Name": "string",
                                 "Value": "string"
                              }
                           ],
                           "MetricName": "string",
                           "Namespace": "string"
                        },
                        "Stat": "string",
                        "Unit": "string"
                     },
                     "ReturnData": boolean
                  }
               ]
            },
            "CustomizedLoadMetricSpecification": {
               "MetricDataQueries": [
                  {
                     "Expression": "string",
                     "Id": "string",
                     "Label": "string",
                     "MetricStat": {
                        "Metric": {
                           "Dimensions": [
                              {
                                 "Name": "string",
                                 "Value": "string"
                              }
                           ],
                           "MetricName": "string",
                           "Namespace": "string"
                        },
                        "Stat": "string",
                        "Unit": "string"
                     },
                     "ReturnData": boolean
                  }
               ]
            },
            "CustomizedScalingMetricSpecification": {
               "MetricDataQueries": [
                  {
                     "Expression": "string",
                     "Id": "string",
                     "Label": "string",
                     "MetricStat": {
                        "Metric": {
                           "Dimensions": [
                              {
                                 "Name": "string",
                                 "Value": "string"
                              }
                           ],
                           "MetricName": "string",
                           "Namespace": "string"
                        },
                        "Stat": "string",
                        "Unit": "string"
                     },
                     "ReturnData": boolean
                  }
               ]
            },
            "PredefinedLoadMetricSpecification": {
               "PredefinedMetricType": "string",
               "ResourceLabel": "string"
            },
            "PredefinedMetricPairSpecification": {
               "PredefinedMetricType": "string",
               "ResourceLabel": "string"
            },
            "PredefinedScalingMetricSpecification": {
               "PredefinedMetricType": "string",
               "ResourceLabel": "string"
            },
            "TargetValue": number
         },
         "Timestamps": [ number ],
         "Values": [ number ]
      }
   ],
   "UpdateTime": number
}
```

## Response Elements
<a name="API_GetPredictiveScalingForecast_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CapacityForecast](#API_GetPredictiveScalingForecast_ResponseSyntax) **   <a name="autoscaling-GetPredictiveScalingForecast-response-CapacityForecast"></a>
 The capacity forecast.
Type: [CapacityForecast](API_CapacityForecast.md) object

 ** [LoadForecast](#API_GetPredictiveScalingForecast_ResponseSyntax) **   <a name="autoscaling-GetPredictiveScalingForecast-response-LoadForecast"></a>
 The load forecast.
Type: Array of [LoadForecast](API_LoadForecast.md) objects

 ** [UpdateTime](#API_GetPredictiveScalingForecast_ResponseSyntax) **   <a name="autoscaling-GetPredictiveScalingForecast-response-UpdateTime"></a>
 The time the forecast was made.
Type: Timestamp

## Errors
<a name="API_GetPredictiveScalingForecast_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an internal error.
HTTP Status Code: 400

 ** ValidationException **
An exception was thrown for a validation issue. Review the available parameters for the API request.
HTTP Status Code: 400

## See Also
<a name="API_GetPredictiveScalingForecast_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/application-autoscaling-2016-02-06/GetPredictiveScalingForecast)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/application-autoscaling-2016-02-06/GetPredictiveScalingForecast)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/GetPredictiveScalingForecast)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/application-autoscaling-2016-02-06/GetPredictiveScalingForecast)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/GetPredictiveScalingForecast)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/application-autoscaling-2016-02-06/GetPredictiveScalingForecast)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/application-autoscaling-2016-02-06/GetPredictiveScalingForecast)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/application-autoscaling-2016-02-06/GetPredictiveScalingForecast)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/application-autoscaling-2016-02-06/GetPredictiveScalingForecast)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/GetPredictiveScalingForecast)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
