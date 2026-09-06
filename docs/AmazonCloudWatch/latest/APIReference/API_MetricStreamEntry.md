---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricStreamEntry.html
---

# MetricStreamEntry
<a name="API_MetricStreamEntry"></a>

This structure contains the configuration information about one metric stream.

## Contents
<a name="API_MetricStreamEntry_Contents"></a>

 ** Arn **   <a name="ACW-Type-MetricStreamEntry-Arn"></a>
The ARN of the metric stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** CreationDate **   <a name="ACW-Type-MetricStreamEntry-CreationDate"></a>
The date that the metric stream was originally created.
Type: Timestamp
Required: No

 ** FirehoseArn **   <a name="ACW-Type-MetricStreamEntry-FirehoseArn"></a>
The ARN of the Kinesis Firehose devlivery stream that is used for this metric stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** LastUpdateDate **   <a name="ACW-Type-MetricStreamEntry-LastUpdateDate"></a>
The date that the configuration of this metric stream was most recently updated.
Type: Timestamp
Required: No

 ** Name **   <a name="ACW-Type-MetricStreamEntry-Name"></a>
The name of the metric stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** OutputFormat **   <a name="ACW-Type-MetricStreamEntry-OutputFormat"></a>
The output format of this metric stream. Valid values are `json`, `opentelemetry1.0`, and `opentelemetry0.7`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Valid Values: `json | opentelemetry0.7 | opentelemetry1.0`
Required: No

 ** State **   <a name="ACW-Type-MetricStreamEntry-State"></a>
The current state of this stream. Valid values are `running` and `stopped`.
Type: String
Required: No

## See Also
<a name="API_MetricStreamEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/MetricStreamEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/MetricStreamEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/MetricStreamEntry)
