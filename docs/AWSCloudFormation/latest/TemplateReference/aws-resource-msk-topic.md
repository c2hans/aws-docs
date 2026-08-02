---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-msk-topic.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Topic
<a name="aws-resource-msk-topic"></a>

Creates a new MSK topic.

## Syntax
<a name="aws-resource-msk-topic-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-msk-topic-syntax.json"></a>

```
{
  "Type" : "AWS::MSK::Topic",
  "Properties" : {
      "[ClusterArn](#cfn-msk-topic-clusterarn)" : {{String}},
      "[Configs](#cfn-msk-topic-configs)" : {{String}},
      "[PartitionCount](#cfn-msk-topic-partitioncount)" : {{Integer}},
      "[ReplicationFactor](#cfn-msk-topic-replicationfactor)" : {{Integer}},
      "[TopicName](#cfn-msk-topic-topicname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-msk-topic-syntax.yaml"></a>

```
Type: AWS::MSK::Topic
Properties:
  [ClusterArn](#cfn-msk-topic-clusterarn): {{String}}
  [Configs](#cfn-msk-topic-configs): {{String}}
  [PartitionCount](#cfn-msk-topic-partitioncount): {{Integer}}
  [ReplicationFactor](#cfn-msk-topic-replicationfactor): {{Integer}}
  [TopicName](#cfn-msk-topic-topicname): {{String}}
```

## Properties
<a name="aws-resource-msk-topic-properties"></a>

`ClusterArn`  <a name="cfn-msk-topic-clusterarn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the cluster.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configs`  <a name="cfn-msk-topic-configs"></a>
Topic configurations encoded as a Base64 string.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PartitionCount`  <a name="cfn-msk-topic-partitioncount"></a>
The number of partitions for the topic.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicationFactor`  <a name="cfn-msk-topic-replicationfactor"></a>
The replication factor for the topic.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TopicName`  <a name="cfn-msk-topic-topicname"></a>
The name of the topic to create.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-msk-topic-return-values"></a>

### Ref
<a name="aws-resource-msk-topic-return-values-ref"></a>

When you provide the logical ID of this resource to the `Ref` intrinsic function, `Ref` returns the topic ARN.

### Fn::GetAtt
<a name="aws-resource-msk-topic-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

####
<a name="aws-resource-msk-topic-return-values-fn--getatt-fn--getatt"></a>

`TopicArn`  <a name="TopicArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the topic.
