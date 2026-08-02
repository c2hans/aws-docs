---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-bucket-inventorytableconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::Bucket InventoryTableConfiguration
<a name="aws-properties-s3-bucket-inventorytableconfiguration"></a>

 The inventory table configuration for an S3 Metadata configuration.

**Note**
If you've disabled your inventory table configuration and now want to re-enable it, you must first manually delete the old inventory table from your AWS managed table bucket. Otherwise, the newly re-enabled inventory table configuration will enter a failed state because the inventory table already exists in the table bucket.

## Syntax
<a name="aws-properties-s3-bucket-inventorytableconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-bucket-inventorytableconfiguration-syntax.json"></a>

```
{
  "[ConfigurationState](#cfn-s3-bucket-inventorytableconfiguration-configurationstate)" : {{String}},
  "[EncryptionConfiguration](#cfn-s3-bucket-inventorytableconfiguration-encryptionconfiguration)" : {{MetadataTableEncryptionConfiguration}},
  "[TableArn](#cfn-s3-bucket-inventorytableconfiguration-tablearn)" : {{String}},
  "[TableName](#cfn-s3-bucket-inventorytableconfiguration-tablename)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-bucket-inventorytableconfiguration-syntax.yaml"></a>

```
  [ConfigurationState](#cfn-s3-bucket-inventorytableconfiguration-configurationstate): {{String}}
  [EncryptionConfiguration](#cfn-s3-bucket-inventorytableconfiguration-encryptionconfiguration): {{
    MetadataTableEncryptionConfiguration}}
  [TableArn](#cfn-s3-bucket-inventorytableconfiguration-tablearn): {{String}}
  [TableName](#cfn-s3-bucket-inventorytableconfiguration-tablename): {{String}}
```

## Properties
<a name="aws-properties-s3-bucket-inventorytableconfiguration-properties"></a>

`ConfigurationState`  <a name="cfn-s3-bucket-inventorytableconfiguration-configurationstate"></a>
 The configuration state of the inventory table, indicating whether the inventory table is enabled or disabled.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionConfiguration`  <a name="cfn-s3-bucket-inventorytableconfiguration-encryptionconfiguration"></a>
 The encryption configuration for the inventory table.
*Required*: No
*Type*: [MetadataTableEncryptionConfiguration](aws-properties-s3-bucket-metadatatableencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableArn`  <a name="cfn-s3-bucket-inventorytableconfiguration-tablearn"></a>
 The Amazon Resource Name (ARN) for the inventory table.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TableName`  <a name="cfn-s3-bucket-inventorytableconfiguration-tablename"></a>
 The name of the inventory table.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
