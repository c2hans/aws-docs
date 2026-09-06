---
source_url: https://docs.aws.amazon.com/autoscaling/plans/APIReference/API_GetScalingPlanResourceForecastData.html
---

# GetScalingPlanResourceForecastData
<a name="API_GetScalingPlanResourceForecastData"></a>

Retrieves the forecast data for a scalable resource.

Capacity forecasts are represented as predicted values, or data points, that are calculated using historical data points from a specified CloudWatch load metric. Data points are available for up to 56 days.

## Request Syntax
<a name="API_GetScalingPlanResourceForecastData_RequestSyntax"></a>

```
{
   "EndTime": {{number}},
   "ForecastDataType": "{{string}}",
   "ResourceId": "{{string}}",
   "ScalableDimension": "{{string}}",
   "ScalingPlanName": "{{string}}",
   "ScalingPlanVersion": {{number}},
   "ServiceNamespace": "{{string}}",
   "StartTime": {{number}}
}
```

## Request Parameters
<a name="API_GetScalingPlanResourceForecastData_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EndTime](#API_GetScalingPlanResourceForecastData_RequestSyntax) **   <a name="autoscaling-GetScalingPlanResourceForecastData-request-EndTime"></a>
The exclusive end time of the time range for the forecast data to get. The maximum time duration between the start and end time is seven days.
Although this parameter can accept a date and time that is more than two days in the future, the availability of forecast data has limits. AWS Auto Scaling only issues forecasts for periods of two days in advance.
Type: Timestamp
Required: Yes

 ** [ForecastDataType](#API_GetScalingPlanResourceForecastData_RequestSyntax) **   <a name="autoscaling-GetScalingPlanResourceForecastData-request-ForecastDataType"></a>
The type of forecast data to get.
+  `LoadForecast`: The load metric forecast.
+  `CapacityForecast`: The capacity forecast.
+  `ScheduledActionMinCapacity`: The minimum capacity for each scheduled scaling action. This data is calculated as the larger of two values: the capacity forecast or the minimum capacity in the scaling instruction.
+  `ScheduledActionMaxCapacity`: The maximum capacity for each scheduled scaling action. The calculation used is determined by the predictive scaling maximum capacity behavior setting in the scaling instruction.
Type: String
Valid Values: `CapacityForecast | LoadForecast | ScheduledActionMinCapacity | ScheduledActionMaxCapacity`
Required: Yes

 ** [ResourceId](#API_GetScalingPlanResourceForecastData_RequestSyntax) **   <a name="autoscaling-GetScalingPlanResourceForecastData-request-ResourceId"></a>
The ID of the resource. This string consists of a prefix (`autoScalingGroup`) followed by the name of a specified Auto Scaling group (`my-asg`). Example: `autoScalingGroup/my-asg`.
Type: String
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** [ScalableDimension](#API_GetScalingPlanResourceForecastData_RequestSyntax) **   <a name="autoscaling-GetScalingPlanResourceForecastData-request-ScalableDimension"></a>
The scalable dimension for the resource. The only valid value is `autoscaling:autoScalingGroup:DesiredCapacity`.
Type: String
Valid Values: `autoscaling:autoScalingGroup:DesiredCapacity`
Required: Yes

 ** [ScalingPlanName](#API_GetScalingPlanResourceForecastData_RequestSyntax) **   <a name="autoscaling-GetScalingPlanResourceForecastData-request-ScalingPlanName"></a>
The name of the scaling plan.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{Print}&&[^|:/]]+`
Required: Yes

 ** [ScalingPlanVersion](#API_GetScalingPlanResourceForecastData_RequestSyntax) **   <a name="autoscaling-GetScalingPlanResourceForecastData-request-ScalingPlanVersion"></a>
The version number of the scaling plan. Currently, the only valid value is `1`.
Type: Long
Required: Yes

 ** [ServiceNamespace](#API_GetScalingPlanResourceForecastData_RequestSyntax) **   <a name="autoscaling-GetScalingPlanResourceForecastData-request-ServiceNamespace"></a>
The namespace of the AWS service. The only valid value is `autoscaling`.
Type: String
Valid Values: `autoscaling`
Required: Yes

 ** [StartTime](#API_GetScalingPlanResourceForecastData_RequestSyntax) **   <a name="autoscaling-GetScalingPlanResourceForecastData-request-StartTime"></a>
The inclusive start time of the time range for the forecast data to get. The date and time can be at most 56 days before the current date and time.
Type: Timestamp
Required: Yes

## Response Syntax
<a name="API_GetScalingPlanResourceForecastData_ResponseSyntax"></a>

```
{
   "Datapoints": [
      {
         "Timestamp": number,
         "Value": number
      }
   ]
}
```

## Response Elements
<a name="API_GetScalingPlanResourceForecastData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Datapoints](#API_GetScalingPlanResourceForecastData_ResponseSyntax) **   <a name="autoscaling-GetScalingPlanResourceForecastData-response-Datapoints"></a>
The data points to return.
Type: Array of [Datapoint](API_Datapoint.md) objects

## Errors
<a name="API_GetScalingPlanResourceForecastData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
The service encountered an internal error.
HTTP Status Code: 400

 ** ValidationException **
An exception was thrown for a validation issue. Review the parameters provided.
HTTP Status Code: 400

## See Also
<a name="API_GetScalingPlanResourceForecastData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-plans-2018-01-06/GetScalingPlanResourceForecastData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-plans-2018-01-06/GetScalingPlanResourceForecastData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-plans-2018-01-06/GetScalingPlanResourceForecastData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-plans-2018-01-06/GetScalingPlanResourceForecastData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-plans-2018-01-06/GetScalingPlanResourceForecastData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-plans-2018-01-06/GetScalingPlanResourceForecastData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-plans-2018-01-06/GetScalingPlanResourceForecastData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-plans-2018-01-06/GetScalingPlanResourceForecastData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-plans-2018-01-06/GetScalingPlanResourceForecastData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-plans-2018-01-06/GetScalingPlanResourceForecastData)
