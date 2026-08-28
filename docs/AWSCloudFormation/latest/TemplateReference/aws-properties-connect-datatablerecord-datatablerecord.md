---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-datatablerecord-datatablerecord.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::DataTableRecord DataTableRecord
<a name="aws-properties-connect-datatablerecord-datatablerecord"></a>

<a name="aws-properties-connect-datatablerecord-datatablerecord-description"></a>The `DataTableRecord` property type specifies Property description not available. for an [AWS::Connect::DataTableRecord](aws-resource-connect-datatablerecord.md).

## Syntax
<a name="aws-properties-connect-datatablerecord-datatablerecord-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-datatablerecord-datatablerecord-syntax.json"></a>

```
{
  "[PrimaryValues](#cfn-connect-datatablerecord-datatablerecord-primaryvalues)" : {{[ Value, ... ]}},
  "[Values](#cfn-connect-datatablerecord-datatablerecord-values)" : {{[ Value, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-datatablerecord-datatablerecord-syntax.yaml"></a>

```
  [PrimaryValues](#cfn-connect-datatablerecord-datatablerecord-primaryvalues): {{
    - Value}}
  [Values](#cfn-connect-datatablerecord-datatablerecord-values): {{
    - Value}}
```

## Properties
<a name="aws-properties-connect-datatablerecord-datatablerecord-properties"></a>

`PrimaryValues`  <a name="cfn-connect-datatablerecord-datatablerecord-primaryvalues"></a>
Property description not available.
*Required*: No
*Type*: Array of [Value](aws-properties-connect-datatablerecord-value.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-connect-datatablerecord-datatablerecord-values"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [Value](aws-properties-connect-datatablerecord-value.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
