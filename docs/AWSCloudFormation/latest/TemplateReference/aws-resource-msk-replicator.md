---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-msk-replicator.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Replicator
<a name="aws-resource-msk-replicator"></a>

Creates the replicator.

Note: Enhanced consumer offset syncing is only supported when the `topicNameConfiguration` type is `IDENTICAL`.

## Syntax
<a name="aws-resource-msk-replicator-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-msk-replicator-syntax.json"></a>

```
{
  "Type" : "AWS::MSK::Replicator",
  "Properties" : {
      "[Description](#cfn-msk-replicator-description)" : {{String}},
      "[KafkaClusters](#cfn-msk-replicator-kafkaclusters)" : {{[ KafkaCluster, ... ]}},
      "[LogDelivery](#cfn-msk-replicator-logdelivery)" : {{LogDelivery}},
      "[ReplicationInfoList](#cfn-msk-replicator-replicationinfolist)" : {{[ ReplicationInfo, ... ]}},
      "[ReplicatorName](#cfn-msk-replicator-replicatorname)" : {{String}},
      "[ServiceExecutionRoleArn](#cfn-msk-replicator-serviceexecutionrolearn)" : {{String}},
      "[Tags](#cfn-msk-replicator-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-msk-replicator-syntax.yaml"></a>

```
Type: AWS::MSK::Replicator
Properties:
  [Description](#cfn-msk-replicator-description): {{String}}
  [KafkaClusters](#cfn-msk-replicator-kafkaclusters): {{
    - KafkaCluster}}
  [LogDelivery](#cfn-msk-replicator-logdelivery): {{
    LogDelivery}}
  [ReplicationInfoList](#cfn-msk-replicator-replicationinfolist): {{
    - ReplicationInfo}}
  [ReplicatorName](#cfn-msk-replicator-replicatorname): {{String}}
  [ServiceExecutionRoleArn](#cfn-msk-replicator-serviceexecutionrolearn): {{String}}
  [Tags](#cfn-msk-replicator-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-msk-replicator-properties"></a>

`Description`  <a name="cfn-msk-replicator-description"></a>
A summary description of the replicator.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KafkaClusters`  <a name="cfn-msk-replicator-kafkaclusters"></a>
Kafka Clusters to use in setting up sources / targets for replication.
*Required*: Yes
*Type*: Array of [KafkaCluster](aws-properties-msk-replicator-kafkacluster.md)
*Minimum*: `2`
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LogDelivery`  <a name="cfn-msk-replicator-logdelivery"></a>
Configuration for delivering replicator logs to customer destinations.
*Required*: No
*Type*: [LogDelivery](aws-properties-msk-replicator-logdelivery.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicationInfoList`  <a name="cfn-msk-replicator-replicationinfolist"></a>
A list of replication configurations, where each configuration targets a given source cluster to target cluster replication flow.
*Required*: Yes
*Type*: Array of [ReplicationInfo](aws-properties-msk-replicator-replicationinfo.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicatorName`  <a name="cfn-msk-replicator-replicatorname"></a>
The name of the replicator. Alpha-numeric characters with '-' are allowed.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9A-Za-z][0-9A-Za-z-]{0,}$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceExecutionRoleArn`  <a name="cfn-msk-replicator-serviceexecutionrolearn"></a>
The ARN of the IAM role used by the replicator to access resources in the customer's account (e.g source and target clusters)
*Required*: Yes
*Type*: String
*Pattern*: `arn:(aws|aws-us-gov|aws-cn):iam:.*`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-msk-replicator-tags"></a>
List of tags to attach to created Replicator.
*Required*: No
*Type*: Array of [Tag](aws-properties-msk-replicator-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-msk-replicator-return-values"></a>

### Ref
<a name="aws-resource-msk-replicator-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-msk-replicator-return-values-fn--getatt"></a>

####
<a name="aws-resource-msk-replicator-return-values-fn--getatt-fn--getatt"></a>

`CurrentVersion`  <a name="CurrentVersion-fn::getatt"></a>
The current version number of the replicator.

`ReplicatorArn`  <a name="ReplicatorArn-fn::getatt"></a>
Amazon Resource Name (ARN) for the created replicator.
