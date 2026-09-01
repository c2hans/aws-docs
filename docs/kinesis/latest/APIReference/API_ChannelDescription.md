---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ChannelDescription.html
---

# ChannelDescription
<a name="API_ChannelDescription"></a>

Describes the configuration and current status of a channel.

## Contents
<a name="API_ChannelDescription_Contents"></a>

 ** ChannelARN **   <a name="Streams-Type-ChannelDescription-ChannelARN"></a>
The Amazon Resource Name (ARN) of the channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:channel/\S+`
Required: Yes

 ** ChannelCreationTimestamp **   <a name="Streams-Type-ChannelDescription-ChannelCreationTimestamp"></a>
The time at which the channel was created.
Type: Timestamp
Required: Yes

 ** ChannelId **   <a name="Streams-Type-ChannelDescription-ChannelId"></a>
The unique identifier of the channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** ChannelName **   <a name="Streams-Type-ChannelDescription-ChannelName"></a>
The name of the channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** ChannelStatus **   <a name="Streams-Type-ChannelDescription-ChannelStatus"></a>
The current status of the channel. Valid values:
+  `CREATING` - The channel is being created.
+  `ACTIVE` - The channel is ready to deliver records.
+  `UPDATING` - The channel configuration is being updated.
+  `DELETING` - The channel is being deleted.
+  `FAILED` - See `ChannelStatusReason` for the failure cause.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | FAILED`
Required: Yes

 ** LoggingConfiguration **   <a name="Streams-Type-ChannelDescription-LoggingConfiguration"></a>
The Amazon CloudWatch Logs configuration for the channel.
Type: [ChannelLoggingConfiguration](API_ChannelLoggingConfiguration.md) object
Required: Yes

 ** ServiceExecutionRoleARN **   <a name="Streams-Type-ChannelDescription-ServiceExecutionRoleARN"></a>
The Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis Data Streams assumes to write records to the destination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[-a-z0-9]*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** StreamConfigurationList **   <a name="Streams-Type-ChannelDescription-StreamConfigurationList"></a>
The source stream configuration for the channel.
Type: Array of [ChannelStreamDescription](API_ChannelStreamDescription.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10000 items.
Required: Yes

 ** ChannelStatusReason **   <a name="Streams-Type-ChannelDescription-ChannelStatusReason"></a>
A message describing the reason for a `FAILED` status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** EncryptionConfiguration **   <a name="Streams-Type-ChannelDescription-EncryptionConfiguration"></a>
The AWS KMS key configuration that Amazon Kinesis Data Streams uses to encrypt data delivered to the channel's destination.
Type: [ChannelEncryptionConfiguration](API_ChannelEncryptionConfiguration.md) object
Required: No

 ** S3DestinationConfiguration **   <a name="Streams-Type-ChannelDescription-S3DestinationConfiguration"></a>
The configuration for delivery to a general purpose Amazon S3 bucket. Present only when the channel destination is a general purpose Amazon S3 bucket.
Type: [S3DestinationDescription](API_S3DestinationDescription.md) object
Required: No

 ** S3TablesDestinationConfiguration **   <a name="Streams-Type-ChannelDescription-S3TablesDestinationConfiguration"></a>
The configuration for delivery to streaming tables on Apache Iceberg in Amazon S3 Tables. Present only when the channel destination is a streaming table.
Type: [S3TablesDestinationDescription](API_S3TablesDestinationDescription.md) object
Required: No

## See Also
<a name="API_ChannelDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/ChannelDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/ChannelDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/ChannelDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
