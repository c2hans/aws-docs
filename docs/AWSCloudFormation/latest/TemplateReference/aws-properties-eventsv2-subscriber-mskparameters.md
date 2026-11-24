---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-mskparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber MskParameters

Parameters for producing events to an Amazon Managed Streaming for Apache Kafka (Amazon MSK) cluster, used when TargetArn is an Amazon MSK cluster ARN.

## Syntax
<a name="aws-properties-eventsv2-subscriber-mskparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-mskparameters-syntax.json"></a>

```json
{
  "[Acks](#cfn-eventsv2-subscriber-mskparameters-acks)" : {{String}},
  "[ClientId](#cfn-eventsv2-subscriber-mskparameters-clientid)" : {{String}},
  "[Compression](#cfn-eventsv2-subscriber-mskparameters-compression)" : {{String}},
  "[Connectivity](#cfn-eventsv2-subscriber-mskparameters-connectivity)" : {{String}},
  "[Headers](#cfn-eventsv2-subscriber-mskparameters-headers)" : {{[ MskHeader, ... ]}},
  "[PartitionKey](#cfn-eventsv2-subscriber-mskparameters-partitionkey)" : {{String}},
  "[TopicName](#cfn-eventsv2-subscriber-mskparameters-topicname)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-mskparameters-syntax.yaml"></a>

```yaml
  [Acks](#cfn-eventsv2-subscriber-mskparameters-acks): {{String}}
  [ClientId](#cfn-eventsv2-subscriber-mskparameters-clientid): {{String}}
  [Compression](#cfn-eventsv2-subscriber-mskparameters-compression): {{String}}
  [Connectivity](#cfn-eventsv2-subscriber-mskparameters-connectivity): {{String}}
  [Headers](#cfn-eventsv2-subscriber-mskparameters-headers): {{
    - MskHeader}}
  [PartitionKey](#cfn-eventsv2-subscriber-mskparameters-partitionkey): {{String}}
  [TopicName](#cfn-eventsv2-subscriber-mskparameters-topicname): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-mskparameters-properties"></a>

`Acks`  <a name="cfn-eventsv2-subscriber-mskparameters-acks"></a>
Producer acknowledgement mode. ALL waits for all in-sync replicas. LEADER waits for the partition leader only. Defaults to ALL.
*Required*: No
*Type*: String
*Allowed values*: `ALL | LEADER`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ClientId`  <a name="cfn-eventsv2-subscriber-mskparameters-clientid"></a>
Producer client.id passed to the Kafka broker. A literal, not a JSONata expression.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Compression`  <a name="cfn-eventsv2-subscriber-mskparameters-compression"></a>
Producer compression codec applied to the record batch. Defaults to NONE.
*Required*: No
*Type*: String
*Allowed values*: `NONE | GZIP | SNAPPY | LZ4 | ZSTD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Connectivity`  <a name="cfn-eventsv2-subscriber-mskparameters-connectivity"></a>
Specifies how the service connects to the Amazon MSK cluster. PUBLIC connects through the cluster's public access. PRIVATE connects through the cluster's multi-VPC private connectivity. You must turn on the chosen connectivity path, with IAM access control, on the cluster.
*Required*: Yes
*Type*: String
*Allowed values*: `PUBLIC | PRIVATE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Headers`  <a name="cfn-eventsv2-subscriber-mskparameters-headers"></a>
Kafka record headers attached to each produced record.
*Required*: No
*Type*: Array of [MskHeader](aws-properties-eventsv2-subscriber-mskheader.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PartitionKey`  <a name="cfn-eventsv2-subscriber-mskparameters-partitionkey"></a>
Kafka record key. Accepts a literal or a JSONata expression; the resolved value selects the destination partition.
*Required*: No
*Type*: String
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicName`  <a name="cfn-eventsv2-subscriber-mskparameters-topicname"></a>
Name of the Kafka topic events are produced to. Accepts a literal or a JSONata expression.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `8192`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
