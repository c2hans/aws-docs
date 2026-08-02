---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-volume-originsnapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::Volume OriginSnapshot
<a name="aws-properties-fsx-volume-originsnapshot"></a>

The configuration object that specifies the snapshot to use as the origin of the data for the volume.

## Syntax
<a name="aws-properties-fsx-volume-originsnapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-volume-originsnapshot-syntax.json"></a>

```
{
  "[CopyStrategy](#cfn-fsx-volume-originsnapshot-copystrategy)" : {{String}},
  "[SnapshotARN](#cfn-fsx-volume-originsnapshot-snapshotarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-fsx-volume-originsnapshot-syntax.yaml"></a>

```
  [CopyStrategy](#cfn-fsx-volume-originsnapshot-copystrategy): {{String}}
  [SnapshotARN](#cfn-fsx-volume-originsnapshot-snapshotarn): {{String}}
```

## Properties
<a name="aws-properties-fsx-volume-originsnapshot-properties"></a>

`CopyStrategy`  <a name="cfn-fsx-volume-originsnapshot-copystrategy"></a>
Specifies the strategy used when copying data from the snapshot to the new volume.
+ `CLONE` - The new volume references the data in the origin snapshot. Cloning a snapshot is faster than copying data from the snapshot to a new volume and doesn't consume disk throughput. However, the origin snapshot can't be deleted if there is a volume using its copied data.
+ `FULL_COPY` - Copies all data from the snapshot to the new volume.

  Specify this option to create the volume from a snapshot on another FSx for OpenZFS file system.
The `INCREMENTAL_COPY` option is only for updating an existing volume by using a snapshot from another FSx for OpenZFS file system. For more information, see [CopySnapshotAndUpdateVolume](https://docs.aws.amazon.com/fsx/latest/APIReference/API_CopySnapshotAndUpdateVolume.html).
*Required*: Yes
*Type*: String
*Allowed values*: `CLONE | FULL_COPY | INCREMENTAL_COPY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotARN`  <a name="cfn-fsx-volume-originsnapshot-snapshotarn"></a>
Specifies the snapshot to use when creating an OpenZFS volume from a snapshot.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
