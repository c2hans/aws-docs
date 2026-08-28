---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fsx-filesystem-rootvolumeconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FSx::FileSystem RootVolumeConfiguration
<a name="aws-properties-fsx-filesystem-rootvolumeconfiguration"></a>

The configuration of an Amazon FSx for OpenZFS root volume.

## Syntax
<a name="aws-properties-fsx-filesystem-rootvolumeconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fsx-filesystem-rootvolumeconfiguration-syntax.json"></a>

```
{
  "[CopyTagsToSnapshots](#cfn-fsx-filesystem-rootvolumeconfiguration-copytagstosnapshots)" : {{Boolean}},
  "[DataCompressionType](#cfn-fsx-filesystem-rootvolumeconfiguration-datacompressiontype)" : {{String}},
  "[NfsExports](#cfn-fsx-filesystem-rootvolumeconfiguration-nfsexports)" : {{[ NfsExports, ... ]}},
  "[ReadOnly](#cfn-fsx-filesystem-rootvolumeconfiguration-readonly)" : {{Boolean}},
  "[RecordSizeKiB](#cfn-fsx-filesystem-rootvolumeconfiguration-recordsizekib)" : {{Integer}},
  "[UserAndGroupQuotas](#cfn-fsx-filesystem-rootvolumeconfiguration-userandgroupquotas)" : {{[ UserAndGroupQuotas, ... ]}}
}
```

### YAML
<a name="aws-properties-fsx-filesystem-rootvolumeconfiguration-syntax.yaml"></a>

```
  [CopyTagsToSnapshots](#cfn-fsx-filesystem-rootvolumeconfiguration-copytagstosnapshots): {{Boolean}}
  [DataCompressionType](#cfn-fsx-filesystem-rootvolumeconfiguration-datacompressiontype): {{String}}
  [NfsExports](#cfn-fsx-filesystem-rootvolumeconfiguration-nfsexports): {{
    - NfsExports}}
  [ReadOnly](#cfn-fsx-filesystem-rootvolumeconfiguration-readonly): {{Boolean}}
  [RecordSizeKiB](#cfn-fsx-filesystem-rootvolumeconfiguration-recordsizekib): {{Integer}}
  [UserAndGroupQuotas](#cfn-fsx-filesystem-rootvolumeconfiguration-userandgroupquotas): {{
    - UserAndGroupQuotas}}
```

## Properties
<a name="aws-properties-fsx-filesystem-rootvolumeconfiguration-properties"></a>

`CopyTagsToSnapshots`  <a name="cfn-fsx-filesystem-rootvolumeconfiguration-copytagstosnapshots"></a>
A Boolean value indicating whether tags for the volume should be copied to snapshots of the volume. This value defaults to `false`. If it's set to `true`, all tags for the volume are copied to snapshots where the user doesn't specify tags. If this value is `true` and you specify one or more tags, only the specified tags are copied to snapshots. If you specify one or more tags when creating the snapshot, no tags are copied from the volume, regardless of this value.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataCompressionType`  <a name="cfn-fsx-filesystem-rootvolumeconfiguration-datacompressiontype"></a>
Specifies the method used to compress the data on the volume. The compression type is `NONE` by default.
+ `NONE` - Doesn't compress the data on the volume. `NONE` is the default.
+ `ZSTD` - Compresses the data in the volume using the Zstandard (ZSTD) compression algorithm. Compared to LZ4, Z-Standard provides a better compression ratio to minimize on-disk storage utilization.
+ `LZ4` - Compresses the data in the volume using the LZ4 compression algorithm. Compared to Z-Standard, LZ4 is less compute-intensive and delivers higher write throughput speeds.
*Required*: No
*Type*: String
*Allowed values*: `NONE | ZSTD | LZ4`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NfsExports`  <a name="cfn-fsx-filesystem-rootvolumeconfiguration-nfsexports"></a>
The configuration object for mounting a file system.
*Required*: No
*Type*: [Array](aws-properties-fsx-filesystem-nfsexports.md) of [NfsExports](aws-properties-fsx-filesystem-nfsexports.md)
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReadOnly`  <a name="cfn-fsx-filesystem-rootvolumeconfiguration-readonly"></a>
A Boolean value indicating whether the volume is read-only. Setting this value to `true` can be useful after you have completed changes to a volume and no longer want changes to occur.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecordSizeKiB`  <a name="cfn-fsx-filesystem-rootvolumeconfiguration-recordsizekib"></a>
Specifies the record size of an OpenZFS root volume, in kibibytes (KiB). Valid values are 4, 8, 16, 32, 64, 128, 256, 512, or 1024 KiB. The default is 128 KiB. Most workloads should use the default record size. Database workflows can benefit from a smaller record size, while streaming workflows can benefit from a larger record size. For additional guidance on setting a custom record size, see [ Tips for maximizing performance](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html#performance-tips-zfs) in the *Amazon FSx for OpenZFS User Guide*.
*Required*: No
*Type*: Integer
*Minimum*: `4`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserAndGroupQuotas`  <a name="cfn-fsx-filesystem-rootvolumeconfiguration-userandgroupquotas"></a>
An object specifying how much storage users or groups can use on the volume.
*Required*: No
*Type*: [Array](aws-properties-fsx-filesystem-userandgroupquotas.md) of [UserAndGroupQuotas](aws-properties-fsx-filesystem-userandgroupquotas.md)
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
