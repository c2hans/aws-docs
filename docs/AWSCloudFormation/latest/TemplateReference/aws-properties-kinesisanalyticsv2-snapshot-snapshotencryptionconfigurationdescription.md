---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::KinesisAnalyticsV2::Snapshot SnapshotEncryptionConfigurationDescription
<a name="aws-properties-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription"></a>

<a name="aws-properties-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription-description"></a>The `SnapshotEncryptionConfigurationDescription` property type specifies Property description not available. for an [AWS::KinesisAnalyticsV2::Snapshot](aws-resource-kinesisanalyticsv2-snapshot.md).

## Syntax
<a name="aws-properties-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription-syntax.json"></a>

```
{
  "[KeyId](#cfn-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription-keyid)" : {{String}},
  "[KeyType](#cfn-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription-keytype)" : {{String}}
}
```

### YAML
<a name="aws-properties-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription-syntax.yaml"></a>

```
  [KeyId](#cfn-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription-keyid): {{String}}
  [KeyType](#cfn-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription-keytype): {{String}}
```

## Properties
<a name="aws-properties-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription-properties"></a>

`KeyId`  <a name="cfn-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription-keyid"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KeyType`  <a name="cfn-kinesisanalyticsv2-snapshot-snapshotencryptionconfigurationdescription-keytype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `AWS_OWNED_KEY | CUSTOMER_MANAGED_KEY`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
