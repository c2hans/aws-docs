---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe PipeSourceManagedStreamingKafkaParameters
<a name="aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters"></a>

The parameters for using an MSK stream as a source.

## Syntax
<a name="aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-syntax.json"></a>

```
{
  "[BatchSize](#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-batchsize)" : {{Integer}},
  "[ConsumerGroupID](#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-consumergroupid)" : {{String}},
  "[Credentials](#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-credentials)" : {{MSKAccessCredentials}},
  "[MaximumBatchingWindowInSeconds](#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-maximumbatchingwindowinseconds)" : {{Integer}},
  "[StartingPosition](#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-startingposition)" : {{String}},
  "[TopicName](#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-topicname)" : {{String}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-syntax.yaml"></a>

```
  [BatchSize](#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-batchsize): {{Integer}}
  [ConsumerGroupID](#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-consumergroupid): {{String}}
  [Credentials](#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-credentials): {{
    MSKAccessCredentials}}
  [MaximumBatchingWindowInSeconds](#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-maximumbatchingwindowinseconds): {{Integer}}
  [StartingPosition](#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-startingposition): {{String}}
  [TopicName](#cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-topicname): {{String}}
```

## Properties
<a name="aws-properties-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-properties"></a>

`BatchSize`  <a name="cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-batchsize"></a>
The maximum number of records to include in each batch.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConsumerGroupID`  <a name="cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-consumergroupid"></a>
The name of the destination queue to consume.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-\/*:_+=.@-]*$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Credentials`  <a name="cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-credentials"></a>
The credentials needed to access the resource.
*Required*: No
*Type*: [MSKAccessCredentials](aws-properties-pipes-pipe-mskaccesscredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumBatchingWindowInSeconds`  <a name="cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-maximumbatchingwindowinseconds"></a>
The maximum length of a time to wait for events.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartingPosition`  <a name="cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-startingposition"></a>
The position in a stream from which to start reading.
*Required*: No
*Type*: String
*Allowed values*: `TRIM_HORIZON | LATEST`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TopicName`  <a name="cfn-pipes-pipe-pipesourcemanagedstreamingkafkaparameters-topicname"></a>
The name of the topic that the pipe will read from.
*Required*: Yes
*Type*: String
*Pattern*: `^[^.]([a-zA-Z0-9\-_.]+)$`
*Minimum*: `1`
*Maximum*: `249`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
