---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-snapshot-importsourceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Snapshot ImportSourceConfiguration
<a name="aws-properties-kinesisanalyticsv2-snapshot-importsourceconfiguration"></a>

Describes the source of the savepoint data to import.

## Syntax
<a name="aws-properties-kinesisanalyticsv2-snapshot-importsourceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-snapshot-importsourceconfiguration-syntax.json"></a>

```
{
  "[ImportRoleArn](#cfn-kinesisanalyticsv2-snapshot-importsourceconfiguration-importrolearn)" : {{String}},
  "[SourceEncryptionConfiguration](#cfn-kinesisanalyticsv2-snapshot-importsourceconfiguration-sourceencryptionconfiguration)" : {{SnapshotEncryptionConfigurationDescription}},
  "[SourceS3PrefixLocation](#cfn-kinesisanalyticsv2-snapshot-importsourceconfiguration-sources3prefixlocation)" : {{S3PrefixLocation}},
  "[SourceType](#cfn-kinesisanalyticsv2-snapshot-importsourceconfiguration-sourcetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-snapshot-importsourceconfiguration-syntax.yaml"></a>

```
  [ImportRoleArn](#cfn-kinesisanalyticsv2-snapshot-importsourceconfiguration-importrolearn): {{String}}
  [SourceEncryptionConfiguration](#cfn-kinesisanalyticsv2-snapshot-importsourceconfiguration-sourceencryptionconfiguration): {{
    SnapshotEncryptionConfigurationDescription}}
  [SourceS3PrefixLocation](#cfn-kinesisanalyticsv2-snapshot-importsourceconfiguration-sources3prefixlocation): {{
    S3PrefixLocation}}
  [SourceType](#cfn-kinesisanalyticsv2-snapshot-importsourceconfiguration-sourcetype): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-snapshot-importsourceconfiguration-properties"></a>

`ImportRoleArn`  <a name="cfn-kinesisanalyticsv2-snapshot-importsourceconfiguration-importrolearn"></a>
The ARN of the IAM role that Managed Service for Apache Flink assumes to read the savepoint data from the source location. For information about the permissions that this role requires, see [Import and export](https://docs.aws.amazon.com/managed-flink/latest/java/snapshots-import-export.html).
*Required*: Yes
*Type*: String
*Pattern*: `^arn:`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceEncryptionConfiguration`  <a name="cfn-kinesisanalyticsv2-snapshot-importsourceconfiguration-sourceencryptionconfiguration"></a>
The encryption configuration of the savepoint data at the source location. If you don't specify this parameter, Managed Service for Apache Flink uses a key of type `AWS_OWNED_KEY`. If you specify a KMS key, you must specify the key ARN.
*Required*: No
*Type*: [SnapshotEncryptionConfigurationDescription](aws-properties-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceS3PrefixLocation`  <a name="cfn-kinesisanalyticsv2-snapshot-importsourceconfiguration-sources3prefixlocation"></a>
The Amazon S3 bucket and key prefix that contain the savepoint data to import. The bucket must be owned by your account and must be in the same Region as the request.
*Required*: Yes
*Type*: [S3PrefixLocation](aws-properties-kinesisanalyticsv2-snapshot-s3prefixlocation.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceType`  <a name="cfn-kinesisanalyticsv2-snapshot-importsourceconfiguration-sourcetype"></a>
The type of the source location. The only supported value is `S3`.
*Required*: Yes
*Type*: String
*Allowed values*: `S3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
