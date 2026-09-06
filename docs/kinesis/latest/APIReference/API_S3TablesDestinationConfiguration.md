---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_S3TablesDestinationConfiguration.html
---

# S3TablesDestinationConfiguration
<a name="API_S3TablesDestinationConfiguration"></a>

The configuration for delivery to streaming tables on Apache Iceberg. Used in [CreateChannel](API_CreateChannel.md).

## Contents
<a name="API_S3TablesDestinationConfiguration_Contents"></a>

 ** DeadLetterQueueS3Configuration **   <a name="Streams-Type-S3TablesDestinationConfiguration-DeadLetterQueueS3Configuration"></a>
The dead-letter queue configuration for records that cannot be delivered. Required for streaming table destinations.
Type: [DeadLetterQueueS3Configuration](API_DeadLetterQueueS3Configuration.md) object
Required: Yes

 ** S3TablesConfigurationList **   <a name="Streams-Type-S3TablesDestinationConfiguration-S3TablesConfigurationList"></a>
The list of streaming table configurations. Currently, one table is supported per channel.
Type: Array of [S3TablesConfiguration](API_S3TablesConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10000 items.
Required: Yes

 ** DataFreshnessInSeconds **   <a name="Streams-Type-S3TablesDestinationConfiguration-DataFreshnessInSeconds"></a>
The maximum age, in seconds, of undelivered data before the channel delivers it to the destination. The default value is 300 seconds.
Type: Integer
Required: No

## See Also
<a name="API_S3TablesDestinationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/S3TablesDestinationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/S3TablesDestinationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/S3TablesDestinationConfiguration)
