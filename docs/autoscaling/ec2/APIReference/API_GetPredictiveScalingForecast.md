---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_GetPredictiveScalingForecast.html
---

# GetPredictiveScalingForecast
<a name="API_GetPredictiveScalingForecast"></a>

Retrieves the forecast data for a predictive scaling policy.

Load forecasts are predictions of the hourly load values using historical load data from CloudWatch and an analysis of historical trends. Capacity forecasts are represented as predicted values for the minimum capacity that is needed on an hourly basis, based on the hourly load forecast.

A minimum of 24 hours of data is required to create the initial forecasts. However, having a full 14 days of historical data results in more accurate forecasts.

For more information, see [Predictive scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Request Parameters
<a name="API_GetPredictiveScalingForecast_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AutoScalingGroupName **
The name of the Auto Scaling group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** EndTime **
The exclusive end time of the time range for the forecast data to get. The maximum time duration between the start and end time is 30 days.
Although this parameter can accept a date and time that is more than two days in the future, the availability of forecast data has limits. Amazon EC2 Auto Scaling only issues forecasts for periods of two days in advance.
Type: Timestamp
Required: Yes

 ** PolicyName **
The name of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** StartTime **
The inclusive start time of the time range for the forecast data to get. At most, the date and time can be one year before the current date and time.
Type: Timestamp
Required: Yes

## Response Elements
<a name="API_GetPredictiveScalingForecast_ResponseElements"></a>

The following elements are returned by the service.

 ** CapacityForecast **
The capacity forecast.
Type: [CapacityForecast](API_CapacityForecast.md) object

 **LoadForecast.member.N**
The load forecast.
Type: Array of [LoadForecast](API_LoadForecast.md) objects

 ** UpdateTime **
The time the forecast was made.
Type: Timestamp

## Errors
<a name="API_GetPredictiveScalingForecast_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceContention **
You already have a pending update to an Amazon EC2 Auto Scaling resource (for example, an Auto Scaling group, instance, or load balancer).
 ** message **

HTTP Status Code: 500

## Examples
<a name="API_GetPredictiveScalingForecast_Examples"></a>

### Example
<a name="API_GetPredictiveScalingForecast_Example_1"></a>

This example illustrates one usage of GetPredictiveScalingForecast.

#### Sample Request
<a name="API_GetPredictiveScalingForecast_Example_1_Request"></a>

```
https://autoscaling.amazonaws.com/?Action=GetPredictiveScalingForecast
&AutoScalingGroupName=my-asg
&PolicyName=cpu40-predictive-scaling-policy
&StartTime=2021-04-29T08:00:00Z
&EndTIme=2021-05-29T08:00:00Z
&Version=2011-01-01
&AUTHPARAMS
```

## See Also
<a name="API_GetPredictiveScalingForecast_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/autoscaling-2011-01-01/GetPredictiveScalingForecast)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/GetPredictiveScalingForecast)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/GetPredictiveScalingForecast)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/autoscaling-2011-01-01/GetPredictiveScalingForecast)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/GetPredictiveScalingForecast)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/autoscaling-2011-01-01/GetPredictiveScalingForecast)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/autoscaling-2011-01-01/GetPredictiveScalingForecast)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/GetPredictiveScalingForecast)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/GetPredictiveScalingForecast)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/autoscaling-2011-01-01/GetPredictiveScalingForecast)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
