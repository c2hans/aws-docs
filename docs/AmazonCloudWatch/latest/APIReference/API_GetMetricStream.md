---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStream.html
---

# GetMetricStream
<a name="API_GetMetricStream"></a>

Returns information about the metric stream that you specify.

## Request Syntax
<a name="API_GetMetricStream_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMetricStream_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_GetMetricStream_RequestSyntax) **   <a name="ACW-GetMetricStream-request-Name"></a>
The name of the metric stream to retrieve information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_GetMetricStream_ResponseSyntax"></a>

```
{
   "Arn": "string",
   "CreationDate": number,
   "ExcludeFilters": [
      {
         "MetricNames": [ "string" ],
         "Namespace": "string"
      }
   ],
   "FirehoseArn": "string",
   "IncludeFilters": [
      {
         "MetricNames": [ "string" ],
         "Namespace": "string"
      }
   ],
   "IncludeLinkedAccountsMetrics": boolean,
   "LastUpdateDate": number,
   "Name": "string",
   "OutputFormat": "string",
   "RoleArn": "string",
   "State": "string",
   "StatisticsConfigurations": [
      {
         "AdditionalStatistics": [ "string" ],
         "IncludeMetrics": [
            {
               "MetricName": "string",
               "Namespace": "string"
            }
         ]
      }
   ]
}
```

## Response Elements
<a name="API_GetMetricStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_GetMetricStream_ResponseSyntax) **   <a name="ACW-GetMetricStream-response-Arn"></a>
The ARN of the metric stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [CreationDate](#API_GetMetricStream_ResponseSyntax) **   <a name="ACW-GetMetricStream-response-CreationDate"></a>
The date that the metric stream was created.
Type: Timestamp

 ** [ExcludeFilters](#API_GetMetricStream_ResponseSyntax) **   <a name="ACW-GetMetricStream-response-ExcludeFilters"></a>
If this array of metric namespaces is present, then these namespaces are the only metric namespaces that are not streamed by this metric stream. In this case, all other metric namespaces in the account are streamed by this metric stream.
Type: Array of [MetricStreamFilter](API_MetricStreamFilter.md) objects

 ** [FirehoseArn](#API_GetMetricStream_ResponseSyntax) **   <a name="ACW-GetMetricStream-response-FirehoseArn"></a>
The ARN of the Amazon Kinesis Data Firehose delivery stream that is used by this metric stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [IncludeFilters](#API_GetMetricStream_ResponseSyntax) **   <a name="ACW-GetMetricStream-response-IncludeFilters"></a>
If this array of metric namespaces is present, then these namespaces are the only metric namespaces that are streamed by this metric stream.
Type: Array of [MetricStreamFilter](API_MetricStreamFilter.md) objects

 ** [IncludeLinkedAccountsMetrics](#API_GetMetricStream_ResponseSyntax) **   <a name="ACW-GetMetricStream-response-IncludeLinkedAccountsMetrics"></a>
If this is `true` and this metric stream is in a monitoring account, then the stream includes metrics from source accounts that the monitoring account is linked to.
Type: Boolean

 ** [LastUpdateDate](#API_GetMetricStream_ResponseSyntax) **   <a name="ACW-GetMetricStream-response-LastUpdateDate"></a>
The date of the most recent update to the metric stream's configuration.
Type: Timestamp

 ** [Name](#API_GetMetricStream_ResponseSyntax) **   <a name="ACW-GetMetricStream-response-Name"></a>
The name of the metric stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [OutputFormat](#API_GetMetricStream_ResponseSyntax) **   <a name="ACW-GetMetricStream-response-OutputFormat"></a>
The output format for the stream. Valid values are `json`, `opentelemetry1.0`, and `opentelemetry0.7`. For more information about metric stream output formats, see [Metric streams output formats](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Valid Values: `json | opentelemetry0.7 | opentelemetry1.0`

 ** [RoleArn](#API_GetMetricStream_ResponseSyntax) **   <a name="ACW-GetMetricStream-response-RoleArn"></a>
The ARN of the IAM role that is used by this metric stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [State](#API_GetMetricStream_ResponseSyntax) **   <a name="ACW-GetMetricStream-response-State"></a>
The state of the metric stream. The possible values are `running` and `stopped`.
Type: String

 ** [StatisticsConfigurations](#API_GetMetricStream_ResponseSyntax) **   <a name="ACW-GetMetricStream-response-StatisticsConfigurations"></a>
Each entry in this array displays information about one or more metrics that include additional statistics in the metric stream. For more information about the additional statistics, see [ CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html).
Type: Array of [MetricStreamStatisticsConfiguration](API_MetricStreamStatisticsConfiguration.md) objects

## Errors
<a name="API_GetMetricStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
Request processing has failed due to some unknown error, exception, or failure.
 ** Message **

HTTP Status Code: 500

 ** InvalidParameterCombination **
Parameters were used together that cannot be used together.
 ** message **

HTTP Status Code: 400

 ** InvalidParameterValue **
The value of an input parameter is bad or out-of-range.
 ** message **

HTTP Status Code: 400

 ** MissingParameter **
An input parameter that is required is missing.
 ** message **

HTTP Status Code: 400

 ** ResourceNotFoundException **
The named resource does not exist.
HTTP Status Code: 404

## See Also
<a name="API_GetMetricStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/GetMetricStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetMetricStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetMetricStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/GetMetricStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetMetricStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/GetMetricStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/GetMetricStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/GetMetricStream)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetMetricStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetMetricStream)
