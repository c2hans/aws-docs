---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-glue-table-opentableformatinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Glue::Table OpenTableFormatInput
<a name="aws-properties-glue-table-opentableformatinput"></a>

Specifies an `OpenTableFormatInput` structure when creating an open format table.

## Syntax
<a name="aws-properties-glue-table-opentableformatinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-glue-table-opentableformatinput-syntax.json"></a>

```
{
  "[IcebergInput](#cfn-glue-table-opentableformatinput-iceberginput)" : {{IcebergInput}}
}
```

### YAML
<a name="aws-properties-glue-table-opentableformatinput-syntax.yaml"></a>

```
  [IcebergInput](#cfn-glue-table-opentableformatinput-iceberginput): {{
    IcebergInput}}
```

## Properties
<a name="aws-properties-glue-table-opentableformatinput-properties"></a>

`IcebergInput`  <a name="cfn-glue-table-opentableformatinput-iceberginput"></a>
Specifies an `IcebergInput` structure that defines an Apache Iceberg metadata table.
*Required*: No
*Type*: [IcebergInput](aws-properties-glue-table-iceberginput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
