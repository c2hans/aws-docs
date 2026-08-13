---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-exportsnapshotrecord-diskinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::ExportSnapshotRecord DiskInfo
<a name="aws-properties-lightsail-exportsnapshotrecord-diskinfo"></a>

Describes a disk.

## Syntax
<a name="aws-properties-lightsail-exportsnapshotrecord-diskinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-exportsnapshotrecord-diskinfo-syntax.json"></a>

```
{
  "[IsSystemDisk](#cfn-lightsail-exportsnapshotrecord-diskinfo-issystemdisk)" : {{Boolean}},
  "[Path](#cfn-lightsail-exportsnapshotrecord-diskinfo-path)" : {{String}},
  "[SizeInGb](#cfn-lightsail-exportsnapshotrecord-diskinfo-sizeingb)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lightsail-exportsnapshotrecord-diskinfo-syntax.yaml"></a>

```
  [IsSystemDisk](#cfn-lightsail-exportsnapshotrecord-diskinfo-issystemdisk): {{Boolean}}
  [Path](#cfn-lightsail-exportsnapshotrecord-diskinfo-path): {{String}}
  [SizeInGb](#cfn-lightsail-exportsnapshotrecord-diskinfo-sizeingb): {{Integer}}
```

## Properties
<a name="aws-properties-lightsail-exportsnapshotrecord-diskinfo-properties"></a>

`IsSystemDisk`  <a name="cfn-lightsail-exportsnapshotrecord-diskinfo-issystemdisk"></a>
A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-lightsail-exportsnapshotrecord-diskinfo-path"></a>
The disk path.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SizeInGb`  <a name="cfn-lightsail-exportsnapshotrecord-diskinfo-sizeingb"></a>
The size of the disk in GB (`32`).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
