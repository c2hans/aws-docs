---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-journaltableconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket JournalTableConfiguration
<a name="aws-properties-s3-bucket-journaltableconfiguration"></a>

 The journal table configuration for an S3 Metadata configuration. The journal table is required for each metadata table configuration and cannot be disabled.

**Note**
The journal configuration will enter a failed state if a journal table already exists in the table bucket. The journal table of a previous configuration must be deleted before a new journal table can be created successfully.

## Syntax
<a name="aws-properties-s3-bucket-journaltableconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-journaltableconfiguration-syntax.json"></a>

```
{
  "[EncryptionConfiguration](#cfn-s3-bucket-journaltableconfiguration-encryptionconfiguration)" : {{MetadataTableEncryptionConfiguration}},
  "[RecordExpiration](#cfn-s3-bucket-journaltableconfiguration-recordexpiration)" : {{RecordExpiration}},
  "[TableArn](#cfn-s3-bucket-journaltableconfiguration-tablearn)" : {{String}},
  "[TableName](#cfn-s3-bucket-journaltableconfiguration-tablename)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-journaltableconfiguration-syntax.yaml"></a>

```
  [EncryptionConfiguration](#cfn-s3-bucket-journaltableconfiguration-encryptionconfiguration): {{
    MetadataTableEncryptionConfiguration}}
  [RecordExpiration](#cfn-s3-bucket-journaltableconfiguration-recordexpiration): {{
    RecordExpiration}}
  [TableArn](#cfn-s3-bucket-journaltableconfiguration-tablearn): {{String}}
  [TableName](#cfn-s3-bucket-journaltableconfiguration-tablename): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-journaltableconfiguration-properties"></a>

`EncryptionConfiguration`  <a name="cfn-s3-bucket-journaltableconfiguration-encryptionconfiguration"></a>
 The encryption configuration for the journal table.
*Required*: No
*Type*: [MetadataTableEncryptionConfiguration](aws-properties-s3-bucket-metadatatableencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RecordExpiration`  <a name="cfn-s3-bucket-journaltableconfiguration-recordexpiration"></a>
 The journal table record expiration settings for the journal table.
*Required*: Yes
*Type*: [RecordExpiration](aws-properties-s3-bucket-recordexpiration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableArn`  <a name="cfn-s3-bucket-journaltableconfiguration-tablearn"></a>
 The Amazon Resource Name (ARN) for the journal table.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableName`  <a name="cfn-s3-bucket-journaltableconfiguration-tablename"></a>
 The name of the journal table.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
