---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_S3DestinationDescription.html
---

# S3DestinationDescription
<a name="API_S3DestinationDescription"></a>

The configuration for delivery to a general purpose Amazon S3 bucket. Returned in [ChannelDescription](API_ChannelDescription.md).

## Contents
<a name="API_S3DestinationDescription_Contents"></a>

 ** DataFreshnessInSeconds **   <a name="Streams-Type-S3DestinationDescription-DataFreshnessInSeconds"></a>
The maximum age, in seconds, of undelivered data.
Type: Integer
Required: Yes

 ** DeadLetterQueueS3Configuration **   <a name="Streams-Type-S3DestinationDescription-DeadLetterQueueS3Configuration"></a>
The dead-letter queue configuration for records that cannot be delivered.
Type: [DeadLetterQueueS3Configuration](API_DeadLetterQueueS3Configuration.md) object
Required: Yes

 ** StorageConfiguration **   <a name="Streams-Type-S3DestinationDescription-StorageConfiguration"></a>
The Amazon S3 storage configuration for the channel.
Type: [S3StorageConfiguration](API_S3StorageConfiguration.md) object
Required: Yes

## See Also
<a name="API_S3DestinationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/S3DestinationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/S3DestinationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/S3DestinationDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
