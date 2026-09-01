---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_S3TablesDestinationDescription.html
---

# S3TablesDestinationDescription
<a name="API_S3TablesDestinationDescription"></a>

The configuration for delivery to streaming tables on Apache Iceberg. Returned in [ChannelDescription](API_ChannelDescription.md).

## Contents
<a name="API_S3TablesDestinationDescription_Contents"></a>

 ** DataFreshnessInSeconds **   <a name="Streams-Type-S3TablesDestinationDescription-DataFreshnessInSeconds"></a>
The maximum age, in seconds, of undelivered data.
Type: Integer
Required: Yes

 ** DeadLetterQueueS3Configuration **   <a name="Streams-Type-S3TablesDestinationDescription-DeadLetterQueueS3Configuration"></a>
The dead-letter queue configuration for records that cannot be delivered.
Type: [DeadLetterQueueS3Configuration](API_DeadLetterQueueS3Configuration.md) object
Required: Yes

 ** S3TablesConfigurationList **   <a name="Streams-Type-S3TablesDestinationDescription-S3TablesConfigurationList"></a>
The list of streaming table configurations.
Type: Array of [S3TablesConfiguration](API_S3TablesConfiguration.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10000 items.
Required: Yes

## See Also
<a name="API_S3TablesDestinationDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/S3TablesDestinationDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/S3TablesDestinationDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/S3TablesDestinationDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
