---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-memorydb-snapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MemoryDB::Snapshot
<a name="aws-resource-memorydb-snapshot"></a>

Represents a copy of an entire cluster as of the time when the snapshot was taken.

## Syntax
<a name="aws-resource-memorydb-snapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-memorydb-snapshot-syntax.json"></a>

```
{
  "Type" : "AWS::MemoryDB::Snapshot",
  "Properties" : {
      "[ClusterName](#cfn-memorydb-snapshot-clustername)" : {{String}},
      "[KmsKeyId](#cfn-memorydb-snapshot-kmskeyid)" : {{String}},
      "[SnapshotName](#cfn-memorydb-snapshot-snapshotname)" : {{String}},
      "[Tags](#cfn-memorydb-snapshot-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-memorydb-snapshot-syntax.yaml"></a>

```
Type: AWS::MemoryDB::Snapshot
Properties:
  [ClusterName](#cfn-memorydb-snapshot-clustername): {{String}}
  [KmsKeyId](#cfn-memorydb-snapshot-kmskeyid): {{String}}
  [SnapshotName](#cfn-memorydb-snapshot-snapshotname): {{String}}
  [Tags](#cfn-memorydb-snapshot-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-memorydb-snapshot-properties"></a>

`ClusterName`  <a name="cfn-memorydb-snapshot-clustername"></a>
The user-supplied name of the cluster. This identifier is a unique key that identifies a cluster.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-memorydb-snapshot-kmskeyid"></a>
The ID of the KMS key used to encrypt the snapshot.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotName`  <a name="cfn-memorydb-snapshot-snapshotname"></a>
The name of the snapshot
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-memorydb-snapshot-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-memorydb-snapshot-tag.md)
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-memorydb-snapshot-return-values"></a>

### Ref
<a name="aws-resource-memorydb-snapshot-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-memorydb-snapshot-return-values-fn--getatt"></a>

####
<a name="aws-resource-memorydb-snapshot-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN (Amazon Resource Name) of the snapshot.

`DataTiering`  <a name="DataTiering-fn::getatt"></a>
Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes. For more information, see [Data tiering](https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html).

`Source`  <a name="Source-fn::getatt"></a>
Indicates whether the snapshot is from an automatic backup (automated) or was created manually (manual).

`Status`  <a name="Status-fn::getatt"></a>
The status of the snapshot. Valid values: creating \| available \| restoring \| copying \| deleting.
