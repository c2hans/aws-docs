---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesis-channel.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Channel
<a name="aws-resource-kinesis-channel"></a>

Creates a channel that delivers records from a Kinesis data stream to a destination. A channel reads records from the specified stream and writes them to streaming tables on Apache Iceberg (Amazon S3 Tables) or to a general purpose Amazon S3 bucket.

You must specify either `S3DestinationConfiguration` or `S3TablesDestinationConfiguration`, but not both.

To use this operation, you must have permission to pass the specified service execution IAM role to Amazon Kinesis Data Streams (the `iam:PassRole` permission on that role).

Creating a channel is an asynchronous operation. Upon receiving the request, Amazon Kinesis Data Streams returns immediately with the channel in the `CREATING` state. After provisioning is complete, Amazon Kinesis Data Streams sets the state to `ACTIVE`. You can use DescribeChannel to check the current state.

This operation is only supported for data streams with the on-demand capacity mode.

This operation has a call limit of 5 transactions per second (TPS) for each AWS account. Exceeding 5 TPS results in a `LimitExceededException`.

## Syntax
<a name="aws-resource-kinesis-channel-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-kinesis-channel-syntax.json"></a>

```
{
  "Type" : "AWS::Kinesis::Channel",
  "Properties" : {
      "[ChannelName](#cfn-kinesis-channel-channelname)" : {{String}},
      "[EncryptionConfiguration](#cfn-kinesis-channel-encryptionconfiguration)" : {{EncryptionConfiguration}},
      "[LoggingConfiguration](#cfn-kinesis-channel-loggingconfiguration)" : {{LoggingConfiguration}},
      "[S3DestinationConfiguration](#cfn-kinesis-channel-s3destinationconfiguration)" : {{S3DestinationConfiguration}},
      "[S3TablesDestinationConfiguration](#cfn-kinesis-channel-s3tablesdestinationconfiguration)" : {{S3TablesDestinationConfiguration}},
      "[ServiceExecutionRoleARN](#cfn-kinesis-channel-serviceexecutionrolearn)" : {{String}},
      "[StreamConfigurationList](#cfn-kinesis-channel-streamconfigurationlist)" : {{[ StreamConfiguration, ... ]}},
      "[Tags](#cfn-kinesis-channel-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-kinesis-channel-syntax.yaml"></a>

```
Type: AWS::Kinesis::Channel
Properties:
  [ChannelName](#cfn-kinesis-channel-channelname): {{String}}
  [EncryptionConfiguration](#cfn-kinesis-channel-encryptionconfiguration): {{
    EncryptionConfiguration}}
  [LoggingConfiguration](#cfn-kinesis-channel-loggingconfiguration): {{
    LoggingConfiguration}}
  [S3DestinationConfiguration](#cfn-kinesis-channel-s3destinationconfiguration): {{
    S3DestinationConfiguration}}
  [S3TablesDestinationConfiguration](#cfn-kinesis-channel-s3tablesdestinationconfiguration): {{
    S3TablesDestinationConfiguration}}
  [ServiceExecutionRoleARN](#cfn-kinesis-channel-serviceexecutionrolearn): {{String}}
  [StreamConfigurationList](#cfn-kinesis-channel-streamconfigurationlist): {{
    - StreamConfiguration}}
  [Tags](#cfn-kinesis-channel-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-kinesis-channel-properties"></a>

`ChannelName`  <a name="cfn-kinesis-channel-channelname"></a>
The name of the channel.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionConfiguration`  <a name="cfn-kinesis-channel-encryptionconfiguration"></a>
The AWS KMS key configuration that Amazon Kinesis Data Streams uses to encrypt data delivered to the channel's destination.
*Required*: No
*Type*: [EncryptionConfiguration](aws-properties-kinesis-channel-encryptionconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LoggingConfiguration`  <a name="cfn-kinesis-channel-loggingconfiguration"></a>
The Amazon CloudWatch Logs configuration for the channel.
*Required*: No
*Type*: [LoggingConfiguration](aws-properties-kinesis-channel-loggingconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3DestinationConfiguration`  <a name="cfn-kinesis-channel-s3destinationconfiguration"></a>
The configuration for delivery to a general purpose Amazon S3 bucket. Present only when the channel destination is a general purpose Amazon S3 bucket.
*Required*: No
*Type*: [S3DestinationConfiguration](aws-properties-kinesis-channel-s3destinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3TablesDestinationConfiguration`  <a name="cfn-kinesis-channel-s3tablesdestinationconfiguration"></a>
The configuration for delivery to streaming tables on Apache Iceberg in Amazon S3 Tables. Present only when the channel destination is a streaming table.
*Required*: No
*Type*: [S3TablesDestinationConfiguration](aws-properties-kinesis-channel-s3tablesdestinationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceExecutionRoleARN`  <a name="cfn-kinesis-channel-serviceexecutionrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that Amazon Kinesis Data Streams assumes to write records to the destination.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:iam::\d{12}:role/[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`StreamConfigurationList`  <a name="cfn-kinesis-channel-streamconfigurationlist"></a>
The source stream configuration for the channel.
*Required*: Yes
*Type*: Array of [StreamConfiguration](aws-properties-kinesis-channel-streamconfiguration.md)
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-kinesis-channel-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-kinesis-channel-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-kinesis-channel-return-values"></a>

### Ref
<a name="aws-resource-kinesis-channel-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-kinesis-channel-return-values-fn--getatt"></a>

####
<a name="aws-resource-kinesis-channel-return-values-fn--getatt-fn--getatt"></a>

`ChannelARN`  <a name="ChannelARN-fn::getatt"></a>
The Amazon Resource Name (ARN) of the channel.

`ChannelCreationTimestamp`  <a name="ChannelCreationTimestamp-fn::getatt"></a>
The time at which the channel was created.

`ChannelId`  <a name="ChannelId-fn::getatt"></a>
The unique identifier of the channel.

`ChannelStatus`  <a name="ChannelStatus-fn::getatt"></a>
The current status of the channel. Valid values:
+ `CREATING` - The channel is being created.
+ `ACTIVE` - The channel is ready to deliver records.
+ `UPDATING` - The channel configuration is being updated.
+ `DELETING` - The channel is being deleted.
+ `FAILED` - See `ChannelStatusReason` for the failure cause.
