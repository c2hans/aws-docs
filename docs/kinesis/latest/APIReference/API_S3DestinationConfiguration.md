---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_S3DestinationConfiguration.html
---

# S3DestinationConfiguration
<a name="API_S3DestinationConfiguration"></a>

The configuration for delivery to a general purpose Amazon S3 bucket. Used in [CreateChannel](API_CreateChannel.md).

## Contents
<a name="API_S3DestinationConfiguration_Contents"></a>

 ** StorageConfiguration **   <a name="Streams-Type-S3DestinationConfiguration-StorageConfiguration"></a>
The Amazon S3 storage configuration for the channel.
Type: [S3StorageConfiguration](API_S3StorageConfiguration.md) object
Required: Yes

 ** DataFreshnessInSeconds **   <a name="Streams-Type-S3DestinationConfiguration-DataFreshnessInSeconds"></a>
The maximum age, in seconds, of undelivered data before the channel delivers it to the destination. The default value is 300 seconds.
Type: Integer
Required: No

 ** DeadLetterQueueS3Configuration **   <a name="Streams-Type-S3DestinationConfiguration-DeadLetterQueueS3Configuration"></a>
The dead-letter queue configuration for records that cannot be delivered. Optional for general purpose Amazon S3 destinations. If not specified, it defaults to the destination bucket with an error prefix.
Type: [DeadLetterQueueS3Configuration](API_DeadLetterQueueS3Configuration.md) object
Required: No

## See Also
<a name="API_S3DestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/S3DestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/S3DestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/S3DestinationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
