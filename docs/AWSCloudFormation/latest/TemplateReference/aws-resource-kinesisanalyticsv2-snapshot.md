---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-kinesisanalyticsv2-snapshot.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Snapshot
<a name="aws-resource-kinesisanalyticsv2-snapshot"></a>

Creates an enhanced snapshot of the state data of a running Managed Service for Apache Flink application. The application must be in the `RUNNING` status, use Apache Flink version 1.20 or later, and use the `ENHANCED_SNAPSHOTS` snapshot mode.

This operation is asynchronous. The response returns the snapshot ARN with the `CREATING` status. To check the status of the snapshot, use `DescribeSnapshot`. To track the progress of the operation, use `DescribeSnapshotOperation`.

An application can have only one `CreateSnapshot` operation in progress at a time. For information about limits, see [Managed Service for Apache Flink Quotas](https://docs.aws.amazon.com/managed-flink/latest/java/limits.html). For more information about snapshots, see [Enhanced Snapshots](https://docs.aws.amazon.com/managed-flink/latest/java/how-snapshots.html).

## Syntax
<a name="aws-resource-kinesisanalyticsv2-snapshot-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-kinesisanalyticsv2-snapshot-syntax.json"></a>

```
{
  "Type" : "AWS::KinesisAnalyticsV2::Snapshot",
  "Properties" : {
      "[ApplicationName](#cfn-kinesisanalyticsv2-snapshot-applicationname)" : {{String}},
      "[ImportSourceConfiguration](#cfn-kinesisanalyticsv2-snapshot-importsourceconfiguration)" : {{ImportSourceConfiguration}},
      "[SnapshotDescription](#cfn-kinesisanalyticsv2-snapshot-snapshotdescription)" : {{String}},
      "[SnapshotEncryptionConfigurationDescription](#cfn-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription)" : {{SnapshotEncryptionConfigurationDescription}},
      "[SnapshotFormat](#cfn-kinesisanalyticsv2-snapshot-snapshotformat)" : {{String}},
      "[SnapshotName](#cfn-kinesisanalyticsv2-snapshot-snapshotname)" : {{String}},
      "[Tags](#cfn-kinesisanalyticsv2-snapshot-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-kinesisanalyticsv2-snapshot-syntax.yaml"></a>

```
Type: AWS::KinesisAnalyticsV2::Snapshot
Properties:
  [ApplicationName](#cfn-kinesisanalyticsv2-snapshot-applicationname): {{String}}
  [ImportSourceConfiguration](#cfn-kinesisanalyticsv2-snapshot-importsourceconfiguration): {{
    ImportSourceConfiguration}}
  [SnapshotDescription](#cfn-kinesisanalyticsv2-snapshot-snapshotdescription): {{String}}
  [SnapshotEncryptionConfigurationDescription](#cfn-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription): {{
    SnapshotEncryptionConfigurationDescription}}
  [SnapshotFormat](#cfn-kinesisanalyticsv2-snapshot-snapshotformat): {{String}}
  [SnapshotName](#cfn-kinesisanalyticsv2-snapshot-snapshotname): {{String}}
  [Tags](#cfn-kinesisanalyticsv2-snapshot-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-kinesisanalyticsv2-snapshot-properties"></a>

`ApplicationName`  <a name="cfn-kinesisanalyticsv2-snapshot-applicationname"></a>
The name of the application.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ImportSourceConfiguration`  <a name="cfn-kinesisanalyticsv2-snapshot-importsourceconfiguration"></a>
Describes the source of the savepoint data to import.
*Required*: No
*Type*: [ImportSourceConfiguration](aws-properties-kinesisanalyticsv2-snapshot-importsourceconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotDescription`  <a name="cfn-kinesisanalyticsv2-snapshot-snapshotdescription"></a>
The summary description of the snapshot.
*Required*: No
*Type*: String
*Pattern*: `^[^\u0000-\u001F\u007F]*$`
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotEncryptionConfigurationDescription`  <a name="cfn-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription"></a>
Describes the encryption settings of data at rest for the snapshot.
*Required*: No
*Type*: [SnapshotEncryptionConfigurationDescription](aws-properties-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotFormat`  <a name="cfn-kinesisanalyticsv2-snapshot-snapshotformat"></a>
The format of the snapshot.
*Required*: No
*Type*: String
*Allowed values*: `CANONICAL`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SnapshotName`  <a name="cfn-kinesisanalyticsv2-snapshot-snapshotname"></a>
The name of the enhanced snapshot.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-kinesisanalyticsv2-snapshot-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-kinesisanalyticsv2-snapshot-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-kinesisanalyticsv2-snapshot-return-values"></a>

### Ref
<a name="aws-resource-kinesisanalyticsv2-snapshot-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-kinesisanalyticsv2-snapshot-return-values-fn--getatt"></a>

####
<a name="aws-resource-kinesisanalyticsv2-snapshot-return-values-fn--getatt-fn--getatt"></a>

`RuntimeEnvironment`  <a name="RuntimeEnvironment-fn::getatt"></a>
The Flink runtime of the application that the snapshot was created from. This field is not present for imported snapshots.

`SnapshotArn`  <a name="SnapshotArn-fn::getatt"></a>
The ARN of the enhanced snapshot.

`SnapshotCreationTimestamp`  <a name="SnapshotCreationTimestamp-fn::getatt"></a>
The timestamp that indicates when the snapshot was created.

`SnapshotInitiator`  <a name="SnapshotInitiator-fn::getatt"></a>
Indicates who initiated the snapshot. `USER` indicates a snapshot that you created or imported. `SYSTEM` indicates a snapshot that Managed Service for Apache Flink created.

`SnapshotInitiatorOperation`  <a name="SnapshotInitiatorOperation-fn::getatt"></a>
The operation that created the snapshot.

`SnapshotSizeInBytes`  <a name="SnapshotSizeInBytes-fn::getatt"></a>
The size of the snapshot, in bytes. The value is `0` until the snapshot status is `READY`.

`SnapshotSourceDescription.S3PrefixLocation.BucketARN`  <a name="SnapshotSourceDescription.S3PrefixLocation.BucketARN-fn::getatt"></a>
The ARN of the Amazon S3 bucket.

`SnapshotSourceDescription.S3PrefixLocation.KeyPrefix`  <a name="SnapshotSourceDescription.S3PrefixLocation.KeyPrefix-fn::getatt"></a>
The key prefix in the Amazon S3 bucket that you specified in the request.

`SnapshotSourceDescription.SourceApplicationDescription.ApplicationCreationTimestamp`  <a name="SnapshotSourceDescription.SourceApplicationDescription.ApplicationCreationTimestamp-fn::getatt"></a>
Property description not available.

`SnapshotSourceDescription.SourceApplicationDescription.ApplicationName`  <a name="SnapshotSourceDescription.SourceApplicationDescription.ApplicationName-fn::getatt"></a>
The name of the application.

`SnapshotSourceDescription.SourceApplicationDescription.ApplicationVersionId`  <a name="SnapshotSourceDescription.SourceApplicationDescription.ApplicationVersionId-fn::getatt"></a>
The current application version ID when the snapshot was created.

`SnapshotStatus`  <a name="SnapshotStatus-fn::getatt"></a>
The status of the enhanced snapshot.
