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
  "[IcebergTableInput](#cfn-glue-table-iceberginput-icebergtableinput)" : {{IcebergTableInput}},
  "[MetadataOperation](#cfn-glue-table-iceberginput-metadataoperation)" : {{Json}},
  "[Version](#cfn-glue-table-iceberginput-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-glue-table-iceberginput-syntax.yaml"></a>

```
  [IcebergTableInput](#cfn-glue-table-iceberginput-icebergtableinput): {{
    IcebergTableInput}}
  [MetadataOperation](#cfn-glue-table-iceberginput-metadataoperation): {{Json}}
  [Version](#cfn-glue-table-iceberginput-version): {{String}}
```

## Properties
<a name="aws-properties-glue-table-iceberginput-properties"></a>

`IcebergTableInput`  <a name="cfn-glue-table-iceberginput-icebergtableinput"></a>
Property description not available.
*Required*: No
*Type*: [IcebergTableInput](aws-properties-glue-table-icebergtableinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetadataOperation`  <a name="cfn-glue-table-iceberginput-metadataoperation"></a>
A required metadata operation. Can only be set to CREATE.
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-glue-table-iceberginput-version"></a>
The table version for the Iceberg table. Defaults to 2.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
