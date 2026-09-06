---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetContainerServiceMetricData.html
---

# GetContainerServiceMetricData
<a name="API_GetContainerServiceMetricData"></a>

Returns the data points of a specific metric of your Amazon Lightsail container service.

Metrics report the utilization of your resources. Monitor and collect metric data regularly to maintain the reliability, availability, and performance of your resources.

## Request Syntax
<a name="API_GetContainerServiceMetricData_RequestSyntax"></a>

```
{
   "endTime": {{number}},
   "metricName": "{{string}}",
   "period": {{number}},
   "serviceName": "{{string}}",
   "startTime": {{number}},
   "statistics": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_GetContainerServiceMetricData_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [endTime](#API_GetContainerServiceMetricData_RequestSyntax) **   <a name="Lightsail-GetContainerServiceMetricData-request-endTime"></a>
The end time of the time period.
Type: Timestamp
Required: Yes

 ** [metricName](#API_GetContainerServiceMetricData_RequestSyntax) **   <a name="Lightsail-GetContainerServiceMetricData-request-metricName"></a>
The metric for which you want to return information.
Valid container service metric names are listed below, along with the most useful statistics to include in your request, and the published unit value.
+  `CPUUtilization` - The average percentage of compute units that are currently in use across all nodes of the container service. This metric identifies the processing power required to run containers on each node of the container service.

  Statistics: The most useful statistics are `Maximum` and `Average`.

  Unit: The published unit is `Percent`.
+  `MemoryUtilization` - The average percentage of available memory that is currently in use across all nodes of the container service. This metric identifies the memory required to run containers on each node of the container service.

  Statistics: The most useful statistics are `Maximum` and `Average`.

  Unit: The published unit is `Percent`.
Type: String
Valid Values: `CPUUtilization | MemoryUtilization`
Required: Yes

 ** [period](#API_GetContainerServiceMetricData_RequestSyntax) **   <a name="Lightsail-GetContainerServiceMetricData-request-period"></a>
The granularity, in seconds, of the returned data points.
All container service metric data is available in 5-minute (300 seconds) granularity.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 86400.
Required: Yes

 ** [serviceName](#API_GetContainerServiceMetricData_RequestSyntax) **   <a name="Lightsail-GetContainerServiceMetricData-request-serviceName"></a>
The name of the container service for which to get metric data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `^[a-z0-9]{1,2}|[a-z0-9][a-z0-9-]+[a-z0-9]$`
Required: Yes

 ** [startTime](#API_GetContainerServiceMetricData_RequestSyntax) **   <a name="Lightsail-GetContainerServiceMetricData-request-startTime"></a>
The start time of the time period.
Type: Timestamp
Required: Yes

 ** [statistics](#API_GetContainerServiceMetricData_RequestSyntax) **   <a name="Lightsail-GetContainerServiceMetricData-request-statistics"></a>
The statistic for the metric.
The following statistics are available:
+  `Minimum` - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.
+  `Maximum` - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.
+  `Sum` - All values submitted for the matching metric added together. You can use this statistic to determine the total volume of a metric.
+  `Average` - The value of `Sum` / `SampleCount` during the specified period. By comparing this statistic with the `Minimum` and `Maximum` values, you can determine the full scope of a metric and how close the average use is to the `Minimum` and `Maximum` values. This comparison helps you to know when to increase or decrease your resources.
+  `SampleCount` - The count, or number, of data points used for the statistical calculation.
Type: Array of strings
Valid Values: `Minimum | Maximum | Sum | Average | SampleCount`
Required: Yes

## Response Syntax
<a name="API_GetContainerServiceMetricData_ResponseSyntax"></a>

```
{
   "metricData": [
      {
         "average": number,
         "maximum": number,
         "minimum": number,
         "sampleCount": number,
         "sum": number,
         "timestamp": number,
         "unit": "string"
      }
   ],
   "metricName": "string"
}
```

## Response Elements
<a name="API_GetContainerServiceMetricData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [metricData](#API_GetContainerServiceMetricData_ResponseSyntax) **   <a name="Lightsail-GetContainerServiceMetricData-response-metricData"></a>
An array of objects that describe the metric data returned.
Type: Array of [MetricDatapoint](API_MetricDatapoint.md) objects

 ** [metricName](#API_GetContainerServiceMetricData_ResponseSyntax) **   <a name="Lightsail-GetContainerServiceMetricData-response-metricName"></a>
The name of the metric returned.
Type: String
Valid Values: `CPUUtilization | MemoryUtilization`

## Errors
<a name="API_GetContainerServiceMetricData_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Lightsail throws this exception when the user cannot be authenticated or uses invalid credentials to access a resource.
HTTP Status Code: 400

 ** InvalidInputException **
Lightsail throws this exception when user input does not conform to the validation rules of an input field.
Domain and distribution APIs are only available in the N. Virginia (`us-east-1`) AWS Region. Please set your AWS Region configuration to `us-east-1` to create, view, or edit these resources.
HTTP Status Code: 400

 ** NotFoundException **
Lightsail throws this exception when it cannot find a resource.
HTTP Status Code: 400

 ** RegionSetupInProgressException **
Lightsail throws this exception when an operation is performed on resources in an opt-in Region that is currently being set up.
 ** docs **
 [Regions and Availability Zones for Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-regions-and-availability-zones-in-amazon-lightsail.html)
 ** tip **
Opt-in Regions typically take a few minutes to finish setting up before you can work with them. Wait a few minutes and try again.
HTTP Status Code: 400

 ** ServiceException **
A general service exception.
HTTP Status Code: 500

 ** UnauthenticatedException **
Lightsail throws this exception when the user has not been authenticated.
HTTP Status Code: 400

## See Also
<a name="API_GetContainerServiceMetricData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetContainerServiceMetricData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetContainerServiceMetricData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetContainerServiceMetricData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetContainerServiceMetricData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetContainerServiceMetricData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetContainerServiceMetricData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetContainerServiceMetricData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetContainerServiceMetricData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetContainerServiceMetricData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetContainerServiceMetricData)
