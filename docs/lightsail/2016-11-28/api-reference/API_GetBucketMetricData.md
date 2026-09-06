---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBucketMetricData.html
---

# GetBucketMetricData
<a name="API_GetBucketMetricData"></a>

Returns the data points of a specific metric for an Amazon Lightsail bucket.

Metrics report the utilization of a bucket. View and collect metric data regularly to monitor the number of objects stored in a bucket (including object versions) and the storage space used by those objects.

## Request Syntax
<a name="API_GetBucketMetricData_RequestSyntax"></a>

```
{
   "bucketName": "{{string}}",
   "endTime": {{number}},
   "metricName": "{{string}}",
   "period": {{number}},
   "startTime": {{number}},
   "statistics": [ "{{string}}" ],
   "unit": "{{string}}"
}
```

## Request Parameters
<a name="API_GetBucketMetricData_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [bucketName](#API_GetBucketMetricData_RequestSyntax) **   <a name="Lightsail-GetBucketMetricData-request-bucketName"></a>
The name of the bucket for which to get metric data.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 54.
Pattern: `^[a-z0-9][a-z0-9-]{1,52}[a-z0-9]$`
Required: Yes

 ** [endTime](#API_GetBucketMetricData_RequestSyntax) **   <a name="Lightsail-GetBucketMetricData-request-endTime"></a>
The timestamp indicating the latest data to be returned.
Type: Timestamp
Required: Yes

 ** [metricName](#API_GetBucketMetricData_RequestSyntax) **   <a name="Lightsail-GetBucketMetricData-request-metricName"></a>
The metric for which you want to return information.
Valid bucket metric names are listed below, along with the most useful statistics to include in your request, and the published unit value.
These bucket metrics are reported once per day.
+  ** `BucketSizeBytes` ** - The amount of data in bytes stored in a bucket. This value is calculated by summing the size of all objects in the bucket (including object versions), including the size of all parts for all incomplete multipart uploads to the bucket.

  Statistics: The most useful statistic is `Maximum`.

  Unit: The published unit is `Bytes`.
+  ** `NumberOfObjects` ** - The total number of objects stored in a bucket. This value is calculated by counting all objects in the bucket (including object versions) and the total number of parts for all incomplete multipart uploads to the bucket.

  Statistics: The most useful statistic is `Average`.

  Unit: The published unit is `Count`.
Type: String
Valid Values: `BucketSizeBytes | NumberOfObjects`
Required: Yes

 ** [period](#API_GetBucketMetricData_RequestSyntax) **   <a name="Lightsail-GetBucketMetricData-request-period"></a>
The granularity, in seconds, of the returned data points.
Bucket storage metrics are reported once per day. Therefore, you should specify a period of 86400 seconds, which is the number of seconds in a day.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 86400.
Required: Yes

 ** [startTime](#API_GetBucketMetricData_RequestSyntax) **   <a name="Lightsail-GetBucketMetricData-request-startTime"></a>
The timestamp indicating the earliest data to be returned.
Type: Timestamp
Required: Yes

 ** [statistics](#API_GetBucketMetricData_RequestSyntax) **   <a name="Lightsail-GetBucketMetricData-request-statistics"></a>
The statistic for the metric.
The following statistics are available:
+  `Minimum` - The lowest value observed during the specified period. Use this value to determine low volumes of activity for your application.
+  `Maximum` - The highest value observed during the specified period. Use this value to determine high volumes of activity for your application.
+  `Sum` - The sum of all values submitted for the matching metric. You can use this statistic to determine the total volume of a metric.
+  `Average` - The value of `Sum` / `SampleCount` during the specified period. By comparing this statistic with the `Minimum` and `Maximum` values, you can determine the full scope of a metric and how close the average use is to the `Minimum` and `Maximum` values. This comparison helps you to know when to increase or decrease your resources.
+  `SampleCount` - The count, or number, of data points used for the statistical calculation.
Type: Array of strings
Valid Values: `Minimum | Maximum | Sum | Average | SampleCount`
Required: Yes

 ** [unit](#API_GetBucketMetricData_RequestSyntax) **   <a name="Lightsail-GetBucketMetricData-request-unit"></a>
The unit for the metric data request.
Valid units depend on the metric data being requested. For the valid units with each available metric, see the `metricName` parameter.
Type: String
Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`
Required: Yes

## Response Syntax
<a name="API_GetBucketMetricData_ResponseSyntax"></a>

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
<a name="API_GetBucketMetricData_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [metricData](#API_GetBucketMetricData_ResponseSyntax) **   <a name="Lightsail-GetBucketMetricData-response-metricData"></a>
An array of objects that describe the metric data returned.
Type: Array of [MetricDatapoint](API_MetricDatapoint.md) objects

 ** [metricName](#API_GetBucketMetricData_ResponseSyntax) **   <a name="Lightsail-GetBucketMetricData-response-metricName"></a>
The name of the metric returned.
Type: String
Valid Values: `BucketSizeBytes | NumberOfObjects`

## Errors
<a name="API_GetBucketMetricData_Errors"></a>

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
<a name="API_GetBucketMetricData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lightsail-2016-11-28/GetBucketMetricData)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lightsail-2016-11-28/GetBucketMetricData)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/GetBucketMetricData)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lightsail-2016-11-28/GetBucketMetricData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/GetBucketMetricData)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lightsail-2016-11-28/GetBucketMetricData)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lightsail-2016-11-28/GetBucketMetricData)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lightsail-2016-11-28/GetBucketMetricData)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lightsail-2016-11-28/GetBucketMetricData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/GetBucketMetricData)
