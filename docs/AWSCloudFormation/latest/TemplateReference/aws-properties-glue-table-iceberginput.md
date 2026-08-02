---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-table-iceberginput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Table IcebergInput
<a name="aws-properties-glue-table-iceberginput"></a>

Specifies an input structure that defines an Apache Iceberg metadata table.

## Syntax
<a name="aws-properties-glue-table-iceberginput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-table-iceberginput-syntax.json"></a>

```
{
  "[MetadataOperation](#cfn-glue-table-iceberginput-metadataoperation)" : {{String}},
  "[Version](#cfn-glue-table-iceberginput-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-table-iceberginput-syntax.yaml"></a>

```
  [MetadataOperation](#cfn-glue-table-iceberginput-metadataoperation): {{String}}
  [Version](#cfn-glue-table-iceberginput-version): {{String}}
```

## Properties
<a name="aws-properties-glue-table-iceberginput-properties"></a>

`MetadataOperation`  <a name="cfn-glue-table-iceberginput-metadataoperation"></a>
A required metadata operation. Can only be set to CREATE.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-glue-table-iceberginput-version"></a>
The table version for the Iceberg table. Defaults to 2.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
