---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-memorydb-snapshot-clusterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MemoryDB::Snapshot ClusterConfiguration
<a name="aws-properties-memorydb-snapshot-clusterconfiguration"></a>

A list of cluster configuration options.

## Syntax
<a name="aws-properties-memorydb-snapshot-clusterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-memorydb-snapshot-clusterconfiguration-syntax.json"></a>

```
{
  "[Description](#cfn-memorydb-snapshot-clusterconfiguration-description)" : {{String}},
  "[Engine](#cfn-memorydb-snapshot-clusterconfiguration-engine)" : {{String}},
  "[EngineVersion](#cfn-memorydb-snapshot-clusterconfiguration-engineversion)" : {{String}},
  "[MaintenanceWindow](#cfn-memorydb-snapshot-clusterconfiguration-maintenancewindow)" : {{String}},
  "[Name](#cfn-memorydb-snapshot-clusterconfiguration-name)" : {{String}},
  "[NodeType](#cfn-memorydb-snapshot-clusterconfiguration-nodetype)" : {{String}},
  "[NumShards](#cfn-memorydb-snapshot-clusterconfiguration-numshards)" : {{Integer}},
  "[ParameterGroupName](#cfn-memorydb-snapshot-clusterconfiguration-parametergroupname)" : {{String}},
  "[Port](#cfn-memorydb-snapshot-clusterconfiguration-port)" : {{Integer}},
  "[SnapshotRetentionLimit](#cfn-memorydb-snapshot-clusterconfiguration-snapshotretentionlimit)" : {{Integer}},
  "[SnapshotWindow](#cfn-memorydb-snapshot-clusterconfiguration-snapshotwindow)" : {{String}},
  "[SubnetGroupName](#cfn-memorydb-snapshot-clusterconfiguration-subnetgroupname)" : {{String}},
  "[TopicArn](#cfn-memorydb-snapshot-clusterconfiguration-topicarn)" : {{String}},
  "[VpcId](#cfn-memorydb-snapshot-clusterconfiguration-vpcid)" : {{String}}
}
```

### YAML
<a name="aws-properties-memorydb-snapshot-clusterconfiguration-syntax.yaml"></a>

```
  [Description](#cfn-memorydb-snapshot-clusterconfiguration-description): {{String}}
  [Engine](#cfn-memorydb-snapshot-clusterconfiguration-engine): {{String}}
  [EngineVersion](#cfn-memorydb-snapshot-clusterconfiguration-engineversion): {{String}}
  [MaintenanceWindow](#cfn-memorydb-snapshot-clusterconfiguration-maintenancewindow): {{String}}
  [Name](#cfn-memorydb-snapshot-clusterconfiguration-name): {{String}}
  [NodeType](#cfn-memorydb-snapshot-clusterconfiguration-nodetype): {{String}}
  [NumShards](#cfn-memorydb-snapshot-clusterconfiguration-numshards): {{Integer}}
  [ParameterGroupName](#cfn-memorydb-snapshot-clusterconfiguration-parametergroupname): {{String}}
  [Port](#cfn-memorydb-snapshot-clusterconfiguration-port): {{Integer}}
  [SnapshotRetentionLimit](#cfn-memorydb-snapshot-clusterconfiguration-snapshotretentionlimit): {{Integer}}
  [SnapshotWindow](#cfn-memorydb-snapshot-clusterconfiguration-snapshotwindow): {{String}}
  [SubnetGroupName](#cfn-memorydb-snapshot-clusterconfiguration-subnetgroupname): {{String}}
  [TopicArn](#cfn-memorydb-snapshot-clusterconfiguration-topicarn): {{String}}
  [VpcId](#cfn-memorydb-snapshot-clusterconfiguration-vpcid): {{String}}
```

## Properties
<a name="aws-properties-memorydb-snapshot-clusterconfiguration-properties"></a>

`Description`  <a name="cfn-memorydb-snapshot-clusterconfiguration-description"></a>
The description of the cluster configuration
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Engine`  <a name="cfn-memorydb-snapshot-clusterconfiguration-engine"></a>
The name of the engine used by the cluster configuration.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EngineVersion`  <a name="cfn-memorydb-snapshot-clusterconfiguration-engineversion"></a>
The Redis OSS engine version used by the cluster
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaintenanceWindow`  <a name="cfn-memorydb-snapshot-clusterconfiguration-maintenancewindow"></a>
The specified maintenance window for the cluster
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-memorydb-snapshot-clusterconfiguration-name"></a>
The name of the cluster
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodeType`  <a name="cfn-memorydb-snapshot-clusterconfiguration-nodetype"></a>
The node type used for the cluster
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NumShards`  <a name="cfn-memorydb-snapshot-clusterconfiguration-numshards"></a>
The number of shards in the cluster
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ParameterGroupName`  <a name="cfn-memorydb-snapshot-clusterconfiguration-parametergroupname"></a>
The name of parameter group used by the cluster
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-memorydb-snapshot-clusterconfiguration-port"></a>
The port used by the cluster
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotRetentionLimit`  <a name="cfn-memorydb-snapshot-clusterconfiguration-snapshotretentionlimit"></a>
The snapshot retention limit set by the cluster
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotWindow`  <a name="cfn-memorydb-snapshot-clusterconfiguration-snapshotwindow"></a>
The snapshot window set by the cluster
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetGroupName`  <a name="cfn-memorydb-snapshot-clusterconfiguration-subnetgroupname"></a>
The name of the subnet group used by the cluster
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopicArn`  <a name="cfn-memorydb-snapshot-clusterconfiguration-topicarn"></a>
The Amazon Resource Name (ARN) of the SNS notification topic for the cluster
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcId`  <a name="cfn-memorydb-snapshot-clusterconfiguration-vpcid"></a>
The ID of the VPC the cluster belongs to
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
