---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-snapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::Snapshot
<a name="aws-resource-ec2-snapshot"></a>

Describes a snapshot.

## Syntax
<a name="aws-resource-ec2-snapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-snapshot-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::Snapshot",
  "Properties" : {
      "[Description](#cfn-ec2-snapshot-description)" : {{String}},
      "[Tags](#cfn-ec2-snapshot-tags)" : {{[ TagsItems, ... ]}},
      "[VolumeId](#cfn-ec2-snapshot-volumeid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-snapshot-syntax.yaml"></a>

```
Type: AWS::EC2::Snapshot
Properties:
  [Description](#cfn-ec2-snapshot-description): {{String}}
  [Tags](#cfn-ec2-snapshot-tags): {{
    - TagsItems}}
  [VolumeId](#cfn-ec2-snapshot-volumeid): {{String}}
```

## Properties
<a name="aws-resource-ec2-snapshot-properties"></a>

`Description`  <a name="cfn-ec2-snapshot-description"></a>
The description for the snapshot.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ec2-snapshot-tags"></a>
Any tags assigned to the snapshot.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-ec2-snapshot-tagsitems.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VolumeId`  <a name="cfn-ec2-snapshot-volumeid"></a>
The ID of the volume that was used to create the snapshot. Snapshots created by a copy snapshot operation have an arbitrary volume ID that you should not use for any purpose.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-snapshot-return-values"></a>

### Ref
<a name="aws-resource-ec2-snapshot-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-snapshot-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-snapshot-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Encrypted`  <a name="Encrypted-fn::getatt"></a>
Indicates whether the snapshot is encrypted.

`KmsKeyId`  <a name="KmsKeyId-fn::getatt"></a>
The Amazon Resource Name (ARN) of the AWS KMS key that was used to protect the volume encryption key for the parent volume.

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
The ID of the AWS account that owns the EBS snapshot.

`Progress`  <a name="Progress-fn::getatt"></a>
The progress of the snapshot, as a percentage.

`SnapshotId`  <a name="SnapshotId-fn::getatt"></a>
The ID of the snapshot. Each snapshot receives a unique identifier when it is created.

`StartTime`  <a name="StartTime-fn::getatt"></a>
The time stamp when the snapshot was initiated.

`State`  <a name="State-fn::getatt"></a>
The snapshot state.

`StorageTier`  <a name="StorageTier-fn::getatt"></a>
The storage tier in which the snapshot is stored. `standard` indicates that the snapshot is stored in the standard snapshot storage tier and that it is ready for use. `archive` indicates that the snapshot is currently archived and that it must be restored before it can be used.

`VolumeSize`  <a name="VolumeSize-fn::getatt"></a>
The size of the volume, in GiB.
