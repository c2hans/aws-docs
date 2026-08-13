---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lightsail::ExportSnapshotRecord ExportSnapshotRecordSourceInfo
<a name="aws-properties-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo"></a>

Describes the source of an export snapshot record.

## Syntax
<a name="aws-properties-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-syntax.json"></a>

```
{
  "[Arn](#cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-arn)" : {{String}},
  "[CreatedAt](#cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-createdat)" : {{String}},
  "[FromResourceArn](#cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-fromresourcearn)" : {{String}},
  "[FromResourceName](#cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-fromresourcename)" : {{String}},
  "[InstanceSnapshotInfo](#cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-instancesnapshotinfo)" : {{InstanceSnapshotInfo}},
  "[Name](#cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-name)" : {{String}},
  "[ResourceType](#cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-resourcetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-syntax.yaml"></a>

```
  [Arn](#cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-arn): {{String}}
  [CreatedAt](#cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-createdat): {{String}}
  [FromResourceArn](#cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-fromresourcearn): {{String}}
  [FromResourceName](#cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-fromresourcename): {{String}}
  [InstanceSnapshotInfo](#cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-instancesnapshotinfo): {{
    InstanceSnapshotInfo}}
  [Name](#cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-name): {{String}}
  [ResourceType](#cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-resourcetype): {{String}}
```

## Properties
<a name="aws-properties-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-properties"></a>

`Arn`  <a name="cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-arn"></a>
The Amazon Resource Name (ARN) of the source instance or disk snapshot.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CreatedAt`  <a name="cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-createdat"></a>
The date when the source instance or disk snapshot was created.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FromResourceArn`  <a name="cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-fromresourcearn"></a>
The Amazon Resource Name (ARN) of the snapshot's source instance or disk.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FromResourceName`  <a name="cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-fromresourcename"></a>
The name of the snapshot's source instance or disk.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceSnapshotInfo`  <a name="cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-instancesnapshotinfo"></a>
A list of objects describing an instance snapshot.
*Required*: No
*Type*: [InstanceSnapshotInfo](aws-properties-lightsail-exportsnapshotrecord-instancesnapshotinfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-name"></a>
The name of the source instance or disk snapshot.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-lightsail-exportsnapshotrecord-exportsnapshotrecordsourceinfo-resourcetype"></a>
The Lightsail resource type (`InstanceSnapshot` or `DiskSnapshot`).
*Required*: No
*Type*: String
*Allowed values*: `InstanceSnapshot | DiskSnapshot`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
