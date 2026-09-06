---
source_url: https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_DestinationConfiguration.html
---

# DestinationConfiguration
<a name="API_DestinationConfiguration"></a>

A complex type that describes a location where chat logs will be stored. Each member represents the configuration of one log destination. For logging, you define only one type of destination (for CloudWatch Logs, Kinesis Firehose, or S3).

## Contents
<a name="API_DestinationConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cloudWatchLogs **   <a name="ivs-Type-DestinationConfiguration-cloudWatchLogs"></a>
An Amazon CloudWatch Logs destination configuration where chat activity will be logged.
Type: [CloudWatchLogsDestinationConfiguration](API_CloudWatchLogsDestinationConfiguration.md) object
Required: No

 ** firehose **   <a name="ivs-Type-DestinationConfiguration-firehose"></a>
An Amazon Kinesis Data Firehose destination configuration where chat activity will be logged.
Type: [FirehoseDestinationConfiguration](API_FirehoseDestinationConfiguration.md) object
Required: No

 ** s3 **   <a name="ivs-Type-DestinationConfiguration-s3"></a>
An Amazon S3 destination configuration where chat activity will be logged.
Type: [S3DestinationConfiguration](API_S3DestinationConfiguration.md) object
Required: No

## See Also
<a name="API_DestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivschat-2020-07-14/DestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivschat-2020-07-14/DestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivschat-2020-07-14/DestinationConfiguration)
