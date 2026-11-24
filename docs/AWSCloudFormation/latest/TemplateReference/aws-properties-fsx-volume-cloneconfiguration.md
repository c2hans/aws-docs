---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-volume-cloneconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::Volume CloneConfiguration

Describes the parent volume, and the snapshot if one was specified, that an FSx for ONTAP volume clone was created from.

## Syntax
<a name="aws-properties-fsx-volume-cloneconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-volume-cloneconfiguration-syntax.json"></a>

```json
{
  "[ParentVolumeId](#cfn-fsx-volume-cloneconfiguration-parentvolumeid)" : {{String}},
  "[SnapshotId](#cfn-fsx-volume-cloneconfiguration-snapshotid)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-volume-cloneconfiguration-syntax.yaml"></a>

```yaml
  [ParentVolumeId](#cfn-fsx-volume-cloneconfiguration-parentvolumeid): {{String}}
  [SnapshotId](#cfn-fsx-volume-cloneconfiguration-snapshotid): {{String}}
```

## Properties
<a name="aws-properties-fsx-volume-cloneconfiguration-properties"></a>

`ParentVolumeId`  <a name="cfn-fsx-volume-cloneconfiguration-parentvolumeid"></a>
The ID of the parent volume that the clone was created from.
*Required*: Yes
*Type*: String
*Pattern*: `^(fsvol-[0-9a-f]{17,})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotId`  <a name="cfn-fsx-volume-cloneconfiguration-snapshotid"></a>
The ID of the snapshot of the parent volume that the clone was created from, if you specified one when you created the clone.
*Required*: No
*Type*: String
*Pattern*: `^((fs)?volsnap-[0-9a-f]{8,})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
