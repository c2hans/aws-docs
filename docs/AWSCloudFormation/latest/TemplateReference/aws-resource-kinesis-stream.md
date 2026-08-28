---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesis-stream.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Kinesis::Stream
<a name="aws-resource-kinesis-stream"></a>

Creates a Kinesis stream that captures and transports data records that are emitted from data sources. For information about creating streams, see [CreateStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_CreateStream.html) in the Amazon Kinesis API Reference.

## Syntax
<a name="aws-resource-kinesis-stream-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-kinesis-stream-syntax.json"></a>

```
{
  "Type" : "AWS::Kinesis::Stream",
  "Properties" : {
      "[DesiredShardLevelMetrics](#cfn-kinesis-stream-desiredshardlevelmetrics)" : {{[ String, ... ]}},
      "[MaxRecordSizeInKiB](#cfn-kinesis-stream-maxrecordsizeinkib)" : {{Integer}},
      "[Name](#cfn-kinesis-stream-name)" : {{String}},
      "[RetentionPeriodHours](#cfn-kinesis-stream-retentionperiodhours)" : {{Integer}},
      "[ShardCount](#cfn-kinesis-stream-shardcount)" : {{Integer}},
      "[StreamEncryption](#cfn-kinesis-stream-streamencryption)" : {{StreamEncryption}},
      "[StreamModeDetails](#cfn-kinesis-stream-streammodedetails)" : {{StreamModeDetails}},
      "[Tags](#cfn-kinesis-stream-tags)" : {{[ Tag, ... ]}},
      "[WarmThroughputMiBps](#cfn-kinesis-stream-warmthroughputmibps)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-kinesis-stream-syntax.yaml"></a>

```
Type: AWS::Kinesis::Stream
Properties:
  [DesiredShardLevelMetrics](#cfn-kinesis-stream-desiredshardlevelmetrics): {{
    - String}}
  [MaxRecordSizeInKiB](#cfn-kinesis-stream-maxrecordsizeinkib): {{Integer}}
  [Name](#cfn-kinesis-stream-name): {{String}}
  [RetentionPeriodHours](#cfn-kinesis-stream-retentionperiodhours): {{Integer}}
  [ShardCount](#cfn-kinesis-stream-shardcount): {{Integer}}
  [StreamEncryption](#cfn-kinesis-stream-streamencryption): {{
    StreamEncryption}}
  [StreamModeDetails](#cfn-kinesis-stream-streammodedetails): {{
    StreamModeDetails}}
  [Tags](#cfn-kinesis-stream-tags): {{
    - Tag}}
  [WarmThroughputMiBps](#cfn-kinesis-stream-warmthroughputmibps): {{Integer}}
```

## Properties
<a name="aws-resource-kinesis-stream-properties"></a>

`DesiredShardLevelMetrics`  <a name="cfn-kinesis-stream-desiredshardlevelmetrics"></a>
A list of shard-level metrics in properties to enable enhanced monitoring mode.
*Required*: No
*Type*: Array of String
*Maximum*: `7`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxRecordSizeInKiB`  <a name="cfn-kinesis-stream-maxrecordsizeinkib"></a>
The maximum record size of a single record in kibibyte (KiB) that you can write to, and read from a stream.
*Required*: No
*Type*: Integer
*Minimum*: `1024`
*Maximum*: `10240`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-kinesis-stream-name"></a>
The name of the Kinesis stream. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the stream name. For more information, see [Name Type](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html).
If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RetentionPeriodHours`  <a name="cfn-kinesis-stream-retentionperiodhours"></a>
The number of hours for the data records that are stored in shards to remain accessible. The default value is 24. For more information about the stream retention period, see [Changing the Data Retention Period](https://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html) in the Amazon Kinesis Developer Guide.
*Required*: No
*Type*: Integer
*Minimum*: `24`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShardCount`  <a name="cfn-kinesis-stream-shardcount"></a>
The number of shards that the stream uses. For greater provisioned throughput, increase the number of shards.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamEncryption`  <a name="cfn-kinesis-stream-streamencryption"></a>
When specified, enables or updates server-side encryption using an AWS KMS key for a specified stream. Removing this property from your stack template and updating your stack disables encryption.
*Required*: No
*Type*: [StreamEncryption](aws-properties-kinesis-stream-streamencryption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamModeDetails`  <a name="cfn-kinesis-stream-streammodedetails"></a>
 Specifies the capacity mode to which you want to set your data stream. Currently, in Kinesis Data Streams, you can choose between an **on-demand** capacity mode and a **provisioned** capacity mode for your data streams.
*Required*: No
*Type*: [StreamModeDetails](aws-properties-kinesis-stream-streammodedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-kinesis-stream-tags"></a>
An arbitrary set of tags (key–value pairs) to associate with the Kinesis stream. For information about constraints for this property, see [Tag Restrictions](https://docs.aws.amazon.com/streams/latest/dev/tagging.html#tagging-restrictions) in the *Amazon Kinesis Developer Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-kinesis-stream-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WarmThroughputMiBps`  <a name="cfn-kinesis-stream-warmthroughputmibps"></a>
The target warm throughput in MB/s that the stream should be scaled to handle. This represents the throughput capacity that will be immediately available for write operations.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-kinesis-stream-return-values"></a>

### Ref
<a name="aws-resource-kinesis-stream-return-values-ref"></a>

 When you specify an AWS::Kinesis::Stream resource as an argument to the `Ref` function, AWS CloudFormation returns the stream name (physical ID).

For more information about using the Ref function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-kinesis-stream-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for the `Arn` attribute.

For more information about using Fn::GetAtt, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-kinesis-stream-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon resource name (ARN) of the Kinesis stream, such as `arn:aws:kinesis:us-east-2:123456789012:stream/mystream`.

## Examples
<a name="aws-resource-kinesis-stream--examples"></a>

### Create a Stream
<a name="aws-resource-kinesis-stream--examples--Create_a_Stream"></a>

The following example creates a `Stream` resource that uses three shards, sets a seven-day retention period, and specifies the KMS key for server-side encryption.

#### JSON
<a name="aws-resource-kinesis-stream--examples--Create_a_Stream--json"></a>

```
"MyStream": {
    "Type": "AWS::Kinesis::Stream",
    "Properties": {
        "Name": "MyKinesisStream",
        "RetentionPeriodHours" : 168,
        "ShardCount": 3,
        "StreamEncryption": {
            "EncryptionType": "KMS",
            "KeyId": "!Ref myKey"
            },
        "Tags": [ {
            "Key": "Environment",
            "Value": "Production" } ]
        }
}
```

#### YAML
<a name="aws-resource-kinesis-stream--examples--Create_a_Stream--yaml"></a>

```
MyStream:
    Type: AWS::Kinesis::Stream
    Properties:
        Name: MyKinesisStream
        RetentionPeriodHours: 168
        ShardCount: 3
        StreamEncryption:
            EncryptionType: KMS
            KeyId: !Ref myKey
        Tags:
            -
                Key: Environment Value:
                Production
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
