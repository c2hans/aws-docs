---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-exportsnapshotrecord-instancesnapshotinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::ExportSnapshotRecord InstanceSnapshotInfo
<a name="aws-properties-lightsail-exportsnapshotrecord-instancesnapshotinfo"></a>

Describes an instance snapshot.

## Syntax
<a name="aws-properties-lightsail-exportsnapshotrecord-instancesnapshotinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-exportsnapshotrecord-instancesnapshotinfo-syntax.json"></a>

```
{
  "[FromBlueprintId](#cfn-lightsail-exportsnapshotrecord-instancesnapshotinfo-fromblueprintid)" : {{String}},
  "[FromBundleId](#cfn-lightsail-exportsnapshotrecord-instancesnapshotinfo-frombundleid)" : {{String}},
  "[FromDiskInfo](#cfn-lightsail-exportsnapshotrecord-instancesnapshotinfo-fromdiskinfo)" : {{[ DiskInfo, ... ]}}
}
```

### YAML
<a name="aws-properties-lightsail-exportsnapshotrecord-instancesnapshotinfo-syntax.yaml"></a>

```
  [FromBlueprintId](#cfn-lightsail-exportsnapshotrecord-instancesnapshotinfo-fromblueprintid): {{String}}
  [FromBundleId](#cfn-lightsail-exportsnapshotrecord-instancesnapshotinfo-frombundleid): {{String}}
  [FromDiskInfo](#cfn-lightsail-exportsnapshotrecord-instancesnapshotinfo-fromdiskinfo): {{
    - DiskInfo}}
```

## Properties
<a name="aws-properties-lightsail-exportsnapshotrecord-instancesnapshotinfo-properties"></a>

`FromBlueprintId`  <a name="cfn-lightsail-exportsnapshotrecord-instancesnapshotinfo-fromblueprintid"></a>
The blueprint ID from which the source instance (`amazon_linux_2023`).
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FromBundleId`  <a name="cfn-lightsail-exportsnapshotrecord-instancesnapshotinfo-frombundleid"></a>
The bundle ID from which the source instance was created (`micro_x_x`).
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FromDiskInfo`  <a name="cfn-lightsail-exportsnapshotrecord-instancesnapshotinfo-fromdiskinfo"></a>
A list of objects describing the disks that were attached to the source instance.
*Required*: No
*Type*: Array of [DiskInfo](aws-properties-lightsail-exportsnapshotrecord-diskinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
