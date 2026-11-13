---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-snapshot-snapshotsourcedescription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Snapshot SnapshotSourceDescription
<a name="aws-properties-kinesisanalyticsv2-snapshot-snapshotsourcedescription"></a>

Describes the source of an enhanced snapshot. For a snapshot that was created from an application, `SourceApplicationDescription` is present. For an imported snapshot, `S3PrefixLocation` is present.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-snapshot-snapshotsourcedescription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-snapshot-snapshotsourcedescription-syntax.json"></a>

```
{
  "[S3PrefixLocation](#cfn-kinesisanalyticsv2-snapshot-snapshotsourcedescription-s3prefixlocation)" : {{S3PrefixLocation}},
  "[SourceApplicationDescription](#cfn-kinesisanalyticsv2-snapshot-snapshotsourcedescription-sourceapplicationdescription)" : {{SourceApplicationDescription}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-snapshot-snapshotsourcedescription-syntax.yaml"></a>

```
  [S3PrefixLocation](#cfn-kinesisanalyticsv2-snapshot-snapshotsourcedescription-s3prefixlocation): {{
    S3PrefixLocation}}
  [SourceApplicationDescription](#cfn-kinesisanalyticsv2-snapshot-snapshotsourcedescription-sourceapplicationdescription): {{
    SourceApplicationDescription}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-snapshot-snapshotsourcedescription-properties"></a>

`S3PrefixLocation`  <a name="cfn-kinesisanalyticsv2-snapshot-snapshotsourcedescription-s3prefixlocation"></a>
The Amazon S3 location that the snapshot was imported from. This field is present only if `SnapshotInitiatorOperation` is `ImportSnapshot`.
*Required*: No
*Type*: [S3PrefixLocation](aws-properties-kinesisanalyticsv2-snapshot-s3prefixlocation.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceApplicationDescription`  <a name="cfn-kinesisanalyticsv2-snapshot-snapshotsourcedescription-sourceapplicationdescription"></a>
Describes the application that the snapshot was created from. This field is not present for imported snapshots.
*Required*: No
*Type*: [SourceApplicationDescription](aws-properties-kinesisanalyticsv2-snapshot-sourceapplicationdescription.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
