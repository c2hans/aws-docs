---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticache-snapshot-nodesnapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElastiCache::Snapshot NodeSnapshot
<a name="aws-properties-elasticache-snapshot-nodesnapshot"></a>

Represents an individual cache node in a snapshot of a cluster.

## Syntax
<a name="aws-properties-elasticache-snapshot-nodesnapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticache-snapshot-nodesnapshot-syntax.json"></a>

```
{
  "[CacheClusterId](#cfn-elasticache-snapshot-nodesnapshot-cacheclusterid)" : {{String}},
  "[CacheNodeCreateTime](#cfn-elasticache-snapshot-nodesnapshot-cachenodecreatetime)" : {{String}},
  "[CacheNodeId](#cfn-elasticache-snapshot-nodesnapshot-cachenodeid)" : {{String}},
  "[CacheSize](#cfn-elasticache-snapshot-nodesnapshot-cachesize)" : {{String}},
  "[NodeGroupId](#cfn-elasticache-snapshot-nodesnapshot-nodegroupid)" : {{String}},
  "[SnapshotCreateTime](#cfn-elasticache-snapshot-nodesnapshot-snapshotcreatetime)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticache-snapshot-nodesnapshot-syntax.yaml"></a>

```
  [CacheClusterId](#cfn-elasticache-snapshot-nodesnapshot-cacheclusterid): {{String}}
  [CacheNodeCreateTime](#cfn-elasticache-snapshot-nodesnapshot-cachenodecreatetime): {{String}}
  [CacheNodeId](#cfn-elasticache-snapshot-nodesnapshot-cachenodeid): {{String}}
  [CacheSize](#cfn-elasticache-snapshot-nodesnapshot-cachesize): {{String}}
  [NodeGroupId](#cfn-elasticache-snapshot-nodesnapshot-nodegroupid): {{String}}
  [SnapshotCreateTime](#cfn-elasticache-snapshot-nodesnapshot-snapshotcreatetime): {{String}}
```

## Properties
<a name="aws-properties-elasticache-snapshot-nodesnapshot-properties"></a>

`CacheClusterId`  <a name="cfn-elasticache-snapshot-nodesnapshot-cacheclusterid"></a>
A unique identifier for the source cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CacheNodeCreateTime`  <a name="cfn-elasticache-snapshot-nodesnapshot-cachenodecreatetime"></a>
The date and time when the cache node was created in the source cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CacheNodeId`  <a name="cfn-elasticache-snapshot-nodesnapshot-cachenodeid"></a>
The cache node identifier for the node in the source cluster.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CacheSize`  <a name="cfn-elasticache-snapshot-nodesnapshot-cachesize"></a>
The size of the cache on the source cache node.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NodeGroupId`  <a name="cfn-elasticache-snapshot-nodesnapshot-nodegroupid"></a>
A unique identifier for the source node group (shard).
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotCreateTime`  <a name="cfn-elasticache-snapshot-nodesnapshot-snapshotcreatetime"></a>
The date and time when the source node's metadata and cache data set was obtained for the snapshot.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
