---
source_url: https://docs.aws.amazon.com/kinesis/latest/APIReference/API_ChannelSummary.html
---

# ChannelSummary
<a name="API_ChannelSummary"></a>

A summary of a channel, returned by [ListChannels](API_ListChannels.md).

## Contents
<a name="API_ChannelSummary_Contents"></a>

 ** ChannelARN **   <a name="Streams-Type-ChannelSummary-ChannelARN"></a>
The Amazon Resource Name (ARN) of the channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws.*:kinesis:.*:\d{12}:channel/\S+`
Required: Yes

 ** ChannelCreationTimestamp **   <a name="Streams-Type-ChannelSummary-ChannelCreationTimestamp"></a>
The time at which the channel was created.
Type: Timestamp
Required: Yes

 ** ChannelDestinationType **   <a name="Streams-Type-ChannelSummary-ChannelDestinationType"></a>
The destination type of the channel. Valid values:
+  `S3` - Delivery to a general purpose Amazon S3 bucket.
+  `S3_TABLES` - Delivery to streaming tables on Apache Iceberg.
Type: String
Valid Values: `S3 | S3_TABLES`
Required: Yes

 ** ChannelId **   <a name="Streams-Type-ChannelSummary-ChannelId"></a>
The unique identifier of the channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** ChannelName **   <a name="Streams-Type-ChannelSummary-ChannelName"></a>
The name of the channel.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** ChannelStatus **   <a name="Streams-Type-ChannelSummary-ChannelStatus"></a>
The current status of the channel. Valid values:
+  `CREATING` - The channel is being created.
+  `ACTIVE` - The channel is ready to deliver records.
+  `UPDATING` - The channel configuration is being updated.
+  `DELETING` - The channel is being deleted.
+  `FAILED` - See `ChannelStatusReason` for the failure cause.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | FAILED`
Required: Yes

 ** Streams **   <a name="Streams-Type-ChannelSummary-Streams"></a>
The source streams associated with the channel.
Type: Array of [ChannelStreamIdentifier](API_ChannelStreamIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10000 items.
Required: Yes

 ** ChannelStatusReason **   <a name="Streams-Type-ChannelSummary-ChannelStatusReason"></a>
A message describing the reason for a `FAILED` status.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_ChannelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesis-2013-12-02/ChannelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesis-2013-12-02/ChannelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesis-2013-12-02/ChannelSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Kinesis Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query kinesis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
