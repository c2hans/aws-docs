---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe PipeSourceSelfManagedKafkaParameters
<a name="aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters"></a>

The parameters for using a self-managed Apache Kafka stream as a source.

A *self managed* cluster refers to any Apache Kafka cluster not hosted by AWS. This includes both clusters you manage yourself, as well as those hosted by a third-party provider, such as [Confluent Cloud](https://www.confluent.io/), [CloudKarafka](https://www.cloudkarafka.com/), or [Redpanda](https://redpanda.com/). For more information, see [Apache Kafka streams as a source](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-kafka.html) in the *Amazon EventBridge User Guide*.

## Syntax
<a name="aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters-syntax.json"></a>

```
{
  "[AdditionalBootstrapServers](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-additionalbootstrapservers)" : {{[ String, ... ]}},
  "[BatchSize](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-batchsize)" : {{Integer}},
  "[ConsumerGroupID](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-consumergroupid)" : {{String}},
  "[Credentials](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-credentials)" : {{SelfManagedKafkaAccessConfigurationCredentials}},
  "[MaximumBatchingWindowInSeconds](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-maximumbatchingwindowinseconds)" : {{Integer}},
  "[ServerRootCaCertificate](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-serverrootcacertificate)" : {{String}},
  "[StartingPosition](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-startingposition)" : {{String}},
  "[TopicName](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-topicname)" : {{String}},
  "[Vpc](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-vpc)" : {{SelfManagedKafkaAccessConfigurationVpc}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters-syntax.yaml"></a>

```
  [AdditionalBootstrapServers](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-additionalbootstrapservers): {{
    - String}}
  [BatchSize](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-batchsize): {{Integer}}
  [ConsumerGroupID](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-consumergroupid): {{String}}
  [Credentials](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-credentials): {{
    SelfManagedKafkaAccessConfigurationCredentials}}
  [MaximumBatchingWindowInSeconds](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-maximumbatchingwindowinseconds): {{Integer}}
  [ServerRootCaCertificate](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-serverrootcacertificate): {{String}}
  [StartingPosition](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-startingposition): {{String}}
  [TopicName](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-topicname): {{String}}
  [Vpc](#cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-vpc): {{
    SelfManagedKafkaAccessConfigurationVpc}}
```

## Properties
<a name="aws-properties-pipes-pipe-pipesourceselfmanagedkafkaparameters-properties"></a>

`AdditionalBootstrapServers`  <a name="cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-additionalbootstrapservers"></a>
An array of server URLs.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `300 | 2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BatchSize`  <a name="cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-batchsize"></a>
The maximum number of records to include in each batch.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConsumerGroupID`  <a name="cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-consumergroupid"></a>
The name of the destination queue to consume.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-\/*:_+=.@-]*$`
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Credentials`  <a name="cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-credentials"></a>
The credentials needed to access the resource.
*Required*: No
*Type*: [SelfManagedKafkaAccessConfigurationCredentials](aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationcredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumBatchingWindowInSeconds`  <a name="cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-maximumbatchingwindowinseconds"></a>
The maximum length of a time to wait for events.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `300`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerRootCaCertificate`  <a name="cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-serverrootcacertificate"></a>
The ARN of the Secrets Manager secret used for certification.
*Required*: No
*Type*: String
*Pattern*: `^(^arn:aws([a-z]|\-)*:secretsmanager:([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}):(\d{12}):secret:.+)$`
*Minimum*: `1`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StartingPosition`  <a name="cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-startingposition"></a>
The position in a stream from which to start reading.
*Required*: No
*Type*: String
*Allowed values*: `TRIM_HORIZON | LATEST`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TopicName`  <a name="cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-topicname"></a>
The name of the topic that the pipe will read from.
*Required*: Yes
*Type*: String
*Pattern*: `^[^.]([a-zA-Z0-9\-_.]+)$`
*Minimum*: `1`
*Maximum*: `249`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Vpc`  <a name="cfn-pipes-pipe-pipesourceselfmanagedkafkaparameters-vpc"></a>
This structure specifies the VPC subnets and security groups for the stream, and whether a public IP address is to be used.
*Required*: No
*Type*: [SelfManagedKafkaAccessConfigurationVpc](aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
