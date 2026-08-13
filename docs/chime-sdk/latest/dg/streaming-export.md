---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html
---

# Streaming messaging data in Amazon Chime SDK messaging
<a name="streaming-export"></a>

You can configure an `AppInstance` to receive data, such as messages and channel events, in the form of a stream. You can then react to that data in real time. Currently, Amazon Chime SDK messaging only accepts Kinesis streams as stream destinations. You must have these prerequisites to use Kinesis streams with this feature:
+ Kinesis streams must be in the same AWS account as the `AppInstance`.
+ A stream must be in the same region as the `AppInstance`.
+ Stream names have a prefix that starts with `chime-messaging-`.
+ You must configure at least two shards. Each shard can receive data up to 1MB per second, so scale your stream accordingly.
+ You must enable server-side encryption (SSE).

**To configure a Kinesis stream**

1. Create one or more Kinesis streams using the prerequisites in the previous section, then get the ARN. Ensure the caller has Kinesis permissions in addition to Amazon Chime permissions.

   The following examples show how to use the AWS CLI to create a Kinesis stream with two shards, and how to enable SSE.

   `aws kinesis create-stream --stream-name {{chime-messaging-unique-name}} --shard-count {{2}}`

   `aws kinesis start-stream-encryption --stream-name {{chime-messaging-unique-name}} --encryption-type KMS --key-id "{{alias}}/aws/kinesis"`

1. Configure streaming by calling the [PutMessagingStreamingConfigurations](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_PutMessagingStreamingConfigurations.html) API.

   You can configure one or both of two data types, and you can choose the same stream or separate streams for them.

   The following examples show how to use the AWS CLI to configure an `appinstance` to stream the `ChannelMessage` and `Channel` data types.

   ```
   aws chime-sdk-messaging put-messaging-streaming-configurations --app-instance-arn {{app_instance_arn}} \
   --streaming-configurations DataType=ChannelMessage,ResourceArn={{kinesis_data_stream_arn}}
   ```

   ```
   aws chime-sdk-messaging put-messaging-streaming-configurations --app-instance-arn {{app_instance_arn}} \
   --streaming-configurations DataType=Channel,ResourceArn={{kinesis_data_stream_arn}}
   ```

   The data types have the following scopes:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/chime-sdk/latest/dg/streaming-export.html)

1. Start reading the data from your configured Kinesis stream.
**Note**
Any events sent before you configure streaming are not sent to your Kinesis stream.

**Data format**
Kinesis outputs records in JSON format with the following fields: `EventType` and `Payload`. The payload format depends on the `EventType`. The following table lists the event types and their corresponding payload formats.

<table>
<thead>
  <tr><th>EventType</th><th>Payload format</th><th></th></tr>
</thead>
<tbody>
  <tr><td><code>CREATE_CHANNEL_MESSAGE</code></td><td rowspan="4"> <a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMessage.html">https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMessage.html</a> </td><td></td></tr>
  <tr><td><code>REDACT_CHANNEL_MESSAGE</code></td><td></td></tr>
  <tr><td><code>UPDATE_CHANNEL_MESSAGE</code></td><td></td></tr>
  <tr><td><code>DELETE_CHANNEL_MESSAGE</code></td><td></td></tr>
  <tr><td></td><td></td><td></td></tr>
  <tr><td><code>CREATE_CHANNEL</code></td><td rowspan="4"> <a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_Channel.html">https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_Channel.html</a> </td><td></td></tr>
  <tr><td><code>UPDATE_CHANNEL</code></td><td></td></tr>
  <tr><td><code>DELETE_CHANNEL</code></td><td></td></tr>
  <tr><td><code>UPDATE_CHANNEL_EXPIRATION_SETTINGS</code></td><td></td></tr>
  <tr><td></td><td></td><td></td></tr>
  <tr><td><code>CREATE_CHANNEL_MEMBERSHIP</code></td><td rowspan="2"> <a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMembership.html">https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelMembership.html</a> </td><td></td></tr>
  <tr><td><code>DELETE_CHANNEL_MEMBERSHIP</code></td><td></td></tr>
  <tr><td></td><td></td><td></td></tr>
  <tr><td><code>CREATE_CHANNEL_BAN</code></td><td rowspan="2"> <a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelBan.html">https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelBan.html</a> </td><td></td></tr>
  <tr><td><code>DELETE_CHANNEL_BAN</code></td><td></td></tr>
  <tr><td></td><td></td><td></td></tr>
  <tr><td><code>CREATE_CHANNEL_MODERATOR</code></td><td rowspan="2"> <a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelModerator.html">https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ChannelModerator.html</a> </td><td></td></tr>
  <tr><td><code>DELETE_CHANNEL_MODERATOR</code></td><td></td></tr>
  <tr><td><code>CREATE_SUB_CHANNEL</code></td><td rowspan="2"><a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListSubChannels.html#API_messaging-chime_ListSubChannels_RequestSyntax">https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_ListSubChannels.html#API_messaging-chime_ListSubChannels_RequestSyntax</a><br /><a href="https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SubChannelSummary.html#chimesdk-Type-messaging-chime_SubChannelSummary-SubChannelId">https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SubChannelSummary.html#chimesdk-Type-messaging-chime_SubChannelSummary-SubChannelId</a></td><td></td></tr>
  <tr><td><code>DELETE_SUB_CHANNEL</code></td><td></td></tr>
</tbody>
</table>
