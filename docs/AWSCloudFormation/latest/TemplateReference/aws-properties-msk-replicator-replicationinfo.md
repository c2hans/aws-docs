---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-replicator-replicationinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator ReplicationInfo
<a name="aws-properties-msk-replicator-replicationinfo"></a>

Specifies configuration for replication between a source and target Kafka cluster.

## Syntax
<a name="aws-properties-msk-replicator-replicationinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-replicator-replicationinfo-syntax.json"></a>

```
{
  "[ConsumerGroupReplication](#cfn-msk-replicator-replicationinfo-consumergroupreplication)" : {{ConsumerGroupReplication}},
  "[SourceKafkaClusterArn](#cfn-msk-replicator-replicationinfo-sourcekafkaclusterarn)" : {{String}},
  "[SourceKafkaClusterId](#cfn-msk-replicator-replicationinfo-sourcekafkaclusterid)" : {{String}},
  "[TargetCompressionType](#cfn-msk-replicator-replicationinfo-targetcompressiontype)" : {{String}},
  "[TargetKafkaClusterArn](#cfn-msk-replicator-replicationinfo-targetkafkaclusterarn)" : {{String}},
  "[TargetKafkaClusterId](#cfn-msk-replicator-replicationinfo-targetkafkaclusterid)" : {{String}},
  "[TopicReplication](#cfn-msk-replicator-replicationinfo-topicreplication)" : {{TopicReplication}}
}
```

### YAML
<a name="aws-properties-msk-replicator-replicationinfo-syntax.yaml"></a>

```
  [ConsumerGroupReplication](#cfn-msk-replicator-replicationinfo-consumergroupreplication): {{
    ConsumerGroupReplication}}
  [SourceKafkaClusterArn](#cfn-msk-replicator-replicationinfo-sourcekafkaclusterarn): {{String}}
  [SourceKafkaClusterId](#cfn-msk-replicator-replicationinfo-sourcekafkaclusterid): {{String}}
  [TargetCompressionType](#cfn-msk-replicator-replicationinfo-targetcompressiontype): {{String}}
  [TargetKafkaClusterArn](#cfn-msk-replicator-replicationinfo-targetkafkaclusterarn): {{String}}
  [TargetKafkaClusterId](#cfn-msk-replicator-replicationinfo-targetkafkaclusterid): {{String}}
  [TopicReplication](#cfn-msk-replicator-replicationinfo-topicreplication): {{
    TopicReplication}}
```

## Properties
<a name="aws-properties-msk-replicator-replicationinfo-properties"></a>

`ConsumerGroupReplication`  <a name="cfn-msk-replicator-replicationinfo-consumergroupreplication"></a>
Configuration relating to consumer group replication.
*Required*: Yes
*Type*: [ConsumerGroupReplication](aws-properties-msk-replicator-consumergroupreplication.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceKafkaClusterArn`  <a name="cfn-msk-replicator-replicationinfo-sourcekafkaclusterarn"></a>
The ARN of the source Kafka cluster.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws|aws-us-gov|aws-cn):kafka:.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceKafkaClusterId`  <a name="cfn-msk-replicator-replicationinfo-sourcekafkaclusterid"></a>
The cluster ID of the source Apache Kafka cluster. Specify either sourceKafkaClusterArn or sourceKafkaClusterId, but not both.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetCompressionType`  <a name="cfn-msk-replicator-replicationinfo-targetcompressiontype"></a>
The compression type to use when producing records to target cluster.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | GZIP | SNAPPY | LZ4 | ZSTD`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetKafkaClusterArn`  <a name="cfn-msk-replicator-replicationinfo-targetkafkaclusterarn"></a>
The ARN of the target Kafka cluster.
*Required*: No
*Type*: String
*Pattern*: `arn:(aws|aws-us-gov|aws-cn):kafka:.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TargetKafkaClusterId`  <a name="cfn-msk-replicator-replicationinfo-targetkafkaclusterid"></a>
The cluster ID of the target Apache Kafka cluster. Specify either targetKafkaClusterArn or targetKafkaClusterId, but not both.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TopicReplication`  <a name="cfn-msk-replicator-replicationinfo-topicreplication"></a>
Configuration relating to topic replication.
*Required*: Yes
*Type*: [TopicReplication](aws-properties-msk-replicator-topicreplication.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
