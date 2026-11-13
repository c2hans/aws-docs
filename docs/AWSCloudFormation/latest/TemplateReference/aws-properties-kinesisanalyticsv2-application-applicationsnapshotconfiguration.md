---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Application ApplicationSnapshotConfiguration
<a name="aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration"></a>

Describes whether snapshots are enabled for a Managed Service for Apache Flink application.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration-syntax.json"></a>

```
{
  "[SnapshotMode](#cfn-kinesisanalyticsv2-application-applicationsnapshotconfiguration-snapshotmode)" : {{String}},
  "[SnapshotsEnabled](#cfn-kinesisanalyticsv2-application-applicationsnapshotconfiguration-snapshotsenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration-syntax.yaml"></a>

```
  [SnapshotMode](#cfn-kinesisanalyticsv2-application-applicationsnapshotconfiguration-snapshotmode): {{String}}
  [SnapshotsEnabled](#cfn-kinesisanalyticsv2-application-applicationsnapshotconfiguration-snapshotsenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration-properties"></a>

`SnapshotMode`  <a name="cfn-kinesisanalyticsv2-application-applicationsnapshotconfiguration-snapshotmode"></a>
Specifies the snapshot mode for a Managed Service for Apache Flink application. To use enhanced snapshots, specify `ENHANCED_SNAPSHOTS`. If you don't specify this parameter, the application uses `APPLICATION_SNAPSHOTS_LEGACY`. For more information, see [Enhanced Snapshots](https://docs.aws.amazon.com/managed-flink/latest/java/how-snapshots.html).
To use `ENHANCED_SNAPSHOTS`, the application must use Apache Flink version 1.20 or later.
*Required*: No
*Type*: String
*Allowed values*: `APPLICATION_SNAPSHOTS_LEGACY | ENHANCED_SNAPSHOTS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnapshotsEnabled`  <a name="cfn-kinesisanalyticsv2-application-applicationsnapshotconfiguration-snapshotsenabled"></a>
Describes whether snapshots are enabled for a Managed Service for Apache Flink application.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-kinesisanalyticsv2-application-applicationsnapshotconfiguration--seealso"></a>
+ [ApplicationSnapshotConfiguration](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationSnapshotConfiguration.html) in the *Amazon Kinesis Data Analytics API Reference*
