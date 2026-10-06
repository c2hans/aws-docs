---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricStream.html
---

# PutMetricStream
<a name="API_PutMetricStream"></a>

Creates or updates a metric stream. Metric streams can automatically stream CloudWatch metrics to AWS destinations, including Amazon S3, and to many third-party solutions.

For more information, see [ Using Metric Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html).

To create a metric stream, you must be signed in to an account that has the `iam:PassRole` permission and either the `CloudWatchFullAccess` policy or the `cloudwatch:PutMetricStream` permission.

When you create or update a metric stream, you choose one of the following:
+ Stream metrics from all metric namespaces in the account.
+ Stream metrics from all metric namespaces in the account, except for the namespaces that you list in `ExcludeFilters`.
+ Stream metrics from only the metric namespaces that you list in `IncludeFilters`.

By default, a metric stream always sends the `MAX`, `MIN`, `SUM`, and `SAMPLECOUNT` statistics for each metric that is streamed. You can use the `StatisticsConfigurations` parameter to have the metric stream send additional statistics in the stream. Streaming additional statistics incurs additional costs. For more information, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/).

When you use `PutMetricStream` to create a new metric stream, the stream is created in the `running` state. If you use it to update an existing stream, the state of the stream is not changed.

If you are using CloudWatch cross-account observability and you create a metric stream in a monitoring account, you can choose whether to include metrics from source accounts in the stream. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).

## Request Syntax
<a name="API_PutMetricStream_RequestSyntax"></a>

```
{
   "ExcludeFilters": [
      {
         "MetricNames": [ "{{string}}" ],
         "Namespace": "{{string}}"
      }
   ],
   "FirehoseArn": "{{string}}",
   "IncludeFilters": [
      {
         "MetricNames": [ "{{string}}" ],
         "Namespace": "{{string}}"
      }
   ],
   "IncludeLinkedAccountsMetrics": {{boolean}},
   "Name": "{{string}}",
   "OutputFormat": "{{string}}",
   "RoleArn": "{{string}}",
   "StatisticsConfigurations": [
      {
         "AdditionalStatistics": [ "{{string}}" ],
         "IncludeMetrics": [
            {
               "MetricName": "{{string}}",
               "Namespace": "{{string}}"
            }
         ]
      }
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutMetricStream_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ExcludeFilters](#API_PutMetricStream_RequestSyntax) **   <a name="ACW-PutMetricStream-request-ExcludeFilters"></a>
If you specify this parameter, the stream sends metrics from all metric namespaces except for the namespaces that you specify here.
You cannot include `ExcludeFilters` and `IncludeFilters` in the same operation.
Type: Array of [MetricStreamFilter](API_MetricStreamFilter.md) objects
Required: No

 ** [FirehoseArn](#API_PutMetricStream_RequestSyntax) **   <a name="ACW-PutMetricStream-request-FirehoseArn"></a>
The ARN of the Amazon Kinesis Data Firehose delivery stream to use for this metric stream. This Amazon Kinesis Data Firehose delivery stream must already exist and must be in the same account as the metric stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [IncludeFilters](#API_PutMetricStream_RequestSyntax) **   <a name="ACW-PutMetricStream-request-IncludeFilters"></a>
If you specify this parameter, the stream sends only the metrics from the metric namespaces that you specify here.
You cannot include `IncludeFilters` and `ExcludeFilters` in the same operation.
Type: Array of [MetricStreamFilter](API_MetricStreamFilter.md) objects
Required: No

 ** [IncludeLinkedAccountsMetrics](#API_PutMetricStream_RequestSyntax) **   <a name="ACW-PutMetricStream-request-IncludeLinkedAccountsMetrics"></a>
If you are creating a metric stream in a monitoring account, specify `true` to include metrics from source accounts in the metric stream.
Type: Boolean
Required: No

 ** [Name](#API_PutMetricStream_RequestSyntax) **   <a name="ACW-PutMetricStream-request-Name"></a>
If you are creating a new metric stream, this is the name for the new stream. The name must be different than the names of other metric streams in this account and Region.
If you are updating a metric stream, specify the name of that stream here.
Valid characters are A-Z, a-z, 0-9, "-" and "\_".
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [OutputFormat](#API_PutMetricStream_RequestSyntax) **   <a name="ACW-PutMetricStream-request-OutputFormat"></a>
The output format for the stream. Valid values are `json`, `opentelemetry1.0`, and `opentelemetry0.7`. For more information about metric stream output formats, see [ Metric streams output formats](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Valid Values: `json | opentelemetry0.7 | opentelemetry1.0`
Required: Yes

 ** [RoleArn](#API_PutMetricStream_RequestSyntax) **   <a name="ACW-PutMetricStream-request-RoleArn"></a>
The ARN of an IAM role that this metric stream will use to access Amazon Kinesis Data Firehose resources. This IAM role must already exist and must be in the same account as the metric stream. This IAM role must include the following permissions:
+ firehose:PutRecord
+ firehose:PutRecordBatch
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [StatisticsConfigurations](#API_PutMetricStream_RequestSyntax) **   <a name="ACW-PutMetricStream-request-StatisticsConfigurations"></a>
By default, a metric stream always sends the `MAX`, `MIN`, `SUM`, and `SAMPLECOUNT` statistics for each metric that is streamed. You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members.
For each entry in this array, you specify one or more metrics and the list of additional statistics to stream for those metrics. The additional statistics that you can stream depend on the stream's `OutputFormat`. If the `OutputFormat` is `json`, you can stream any additional statistic that is supported by CloudWatch, listed in [ CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html). If the `OutputFormat` is `opentelemetry1.0` or `opentelemetry0.7`, you can stream percentile statistics such as p95, p99.9, and so on.
Type: Array of [MetricStreamStatisticsConfiguration](API_MetricStreamStatisticsConfiguration.md) objects
Required: No

 ** [Tags](#API_PutMetricStream_RequestSyntax) **   <a name="ACW-PutMetricStream-request-Tags"></a>
A list of key-value pairs to associate with the metric stream. You can associate as many as 50 tags with a metric stream.
Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.
You can use this parameter only when you are creating a new metric stream. If you are using this operation to update an existing metric stream, any tags you specify in this parameter are ignored. To change the tags of an existing metric stream, use [TagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html) or [UntagResource](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html).
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_PutMetricStream_ResponseSyntax"></a>

```
{
   "Arn": "string"
}
```

## Response Elements
<a name="API_PutMetricStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_PutMetricStream_ResponseSyntax) **   <a name="ACW-PutMetricStream-response-Arn"></a>
The ARN of the metric stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_PutMetricStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
More than one process tried to modify a resource at the same time.
HTTP Status Code: 429

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

## Examples
<a name="API_PutMetricStream_Examples"></a>

### Stream two namespaces with the default statistics
<a name="API_PutMetricStream_Example_1"></a>

The following example creates a metric stream that streams all the metrics from the `AWS/EC2` and `AWS/ELB` namespaces, with only the default statistics.

#### Sample Request
<a name="API_PutMetricStream_Example_1_Request"></a>

```
{
  "Name": "MyMetricStream",
  "FirehoseArn": "arn:aws:firehose:us-east-1:123456789098:stream/MyFirehose",
  "RoleArn": "arn:aws:iam::123456789098:role/MyFirehoseWriteAccessRole",
  "IncludeFilters": [
    {
      "Namespace": "AWS/EC2"
    },
    {
      "Namespace": "AWS/ELB"
    }
  ],
  "OutputFormat": "opentelemetry1.0"
}
```

### In a monitoring account, stream two namespaces with default statistics from all source accounts
<a name="API_PutMetricStream_Example_2"></a>

The following example creates a metric stream that streams all the metrics from the `AWS/EC2` and `AWS/ELB` namespaces from this monitoring account and from all source accounts that it is linked to.

#### Sample Request
<a name="API_PutMetricStream_Example_2_Request"></a>

```
{
  "Name": "MyMetricStream",
  "FirehoseArn": "arn:aws:firehose:us-east-1:123456789098:stream/MyFirehose",
  "RoleArn": "arn:aws:iam::123456789098:role/MyFirehoseWriteAccessRole",
  "IncludeLinkedAccountsMetrics": "true",
  "IncludeFilters": [
    {
      "Namespace": "AWS/EC2"
    },
    {
      "Namespace": "AWS/ELB"
    }
  ],
  "OutputFormat": "opentelemetry1.0"
}
```

### Stream additional statistics
<a name="API_PutMetricStream_Example_3"></a>

The following example creates a metric stream that streams all metrics from the `AWS/EC2` namespace with only the default statistics, and also streams two other metrics with the default statistics and some additional statistics.

#### Sample Request
<a name="API_PutMetricStream_Example_3_Request"></a>

```
{
    "Name": "MyMetricStream",
    "FirehoseArn": "arn:aws:firehose:us-east-1:123456789098:stream/MyFirehose",
    "RoleArn": "arn:aws:iam::123456789098:role/MyFirehoseWriteAccessRole",
    "IncludeFilters": [
        {
            "Namespace": "AWS/EC2"
        }
    ],
    "OutputFormat": "json",
    "StatisticsConfigurations": [
        {
            "IncludeMetrics": [
                {
                    "Namespace": "AWS/ApplicationELB",
                    "MetricName": "TargetResponseTime"
                },
                {
                    "Namespace": "AWS/ELB",
                    "MetricName": "Latency"
                }
            ],
            "AdditionalStatistics": [
                "tm90",
                "p90",
                "p99",
                "p99.9"
            ]
        }
    ]
}
```

## See Also
<a name="API_PutMetricStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/PutMetricStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/PutMetricStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/PutMetricStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/PutMetricStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/PutMetricStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/PutMetricStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/PutMetricStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/PutMetricStream)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/PutMetricStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/PutMetricStream)
