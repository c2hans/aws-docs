---
source_url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_LogDeliveryConfiguration.html
---

# LogDeliveryConfiguration
<a name="API_LogDeliveryConfiguration"></a>

Returns the destination, format and type of the logs.

## Contents
<a name="API_LogDeliveryConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DestinationDetails **
Configuration details of either a CloudWatch Logs destination or Kinesis Data Firehose destination.
Type: [DestinationDetails](API_DestinationDetails.md) object
Required: No

 ** DestinationType **
Returns the destination type, either `cloudwatch-logs` or `kinesis-firehose`.
Type: String
Valid Values: `cloudwatch-logs | kinesis-firehose`
Required: No

 ** LogFormat **
Returns the log format, either JSON or TEXT.
Type: String
Valid Values: `text | json`
Required: No

 ** LogType **
Refers to [slow-log](https://redis.io/commands/slowlog) or engine-log.
Type: String
Valid Values: `slow-log | engine-log`
Required: No

 ** Message **
Returns an error message for the log delivery configuration.
Type: String
Required: No

 ** Status **
Returns the log delivery configuration status. Values are one of `enabling` \| `disabling` \| `modifying` \| `active` \| `error`
Type: String
Valid Values: `active | enabling | modifying | disabling | error`
Required: No

## See Also
<a name="API_LogDeliveryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticache-2015-02-02/LogDeliveryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticache-2015-02-02/LogDeliveryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticache-2015-02-02/LogDeliveryConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon ElastiCache. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonElastiCache` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
