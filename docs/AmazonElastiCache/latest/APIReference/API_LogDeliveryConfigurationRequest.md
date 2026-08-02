---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_LogDeliveryConfigurationRequest.html
---

# LogDeliveryConfigurationRequest
<a name="API_LogDeliveryConfigurationRequest"></a>

Specifies the destination, format and type of the logs.

## Contents
<a name="API_LogDeliveryConfigurationRequest_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DestinationDetails **
Configuration details of either a CloudWatch Logs destination or Kinesis Data Firehose destination.
Type: [DestinationDetails](API_DestinationDetails.md) object
Required: No

 ** DestinationType **
Specify either `cloudwatch-logs` or `kinesis-firehose` as the destination type.
Type: String
Valid Values: `cloudwatch-logs | kinesis-firehose`
Required: No

 ** Enabled **
Specify if log delivery is enabled. Default `true`.
Type: Boolean
Required: No

 ** LogFormat **
Specifies either JSON or TEXT
Type: String
Valid Values: `text | json`
Required: No

 ** LogType **
Refers to [slow-log](https://redis.io/commands/slowlog) or engine-log..
Type: String
Valid Values: `slow-log | engine-log`
Required: No

## See Also
<a name="API_LogDeliveryConfigurationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/LogDeliveryConfigurationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/LogDeliveryConfigurationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/LogDeliveryConfigurationRequest)
