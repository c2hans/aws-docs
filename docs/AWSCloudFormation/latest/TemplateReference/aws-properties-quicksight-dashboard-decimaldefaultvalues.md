---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-decimaldefaultvalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard DecimalDefaultValues
<a name="aws-properties-quicksight-dashboard-decimaldefaultvalues"></a>

The default values of the `DecimalParameterDeclaration`.

## Syntax
<a name="aws-properties-quicksight-dashboard-decimaldefaultvalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-decimaldefaultvalues-syntax.json"></a>

```
{
  "[DynamicValue](#cfn-quicksight-dashboard-decimaldefaultvalues-dynamicvalue)" : {{DynamicDefaultValue}},
  "[StaticValues](#cfn-quicksight-dashboard-decimaldefaultvalues-staticvalues)" : {{[ Number, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-decimaldefaultvalues-syntax.yaml"></a>

```
  [DynamicValue](#cfn-quicksight-dashboard-decimaldefaultvalues-dynamicvalue): {{
    DynamicDefaultValue}}
  [StaticValues](#cfn-quicksight-dashboard-decimaldefaultvalues-staticvalues): {{
    - Number}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-decimaldefaultvalues-properties"></a>

`DynamicValue`  <a name="cfn-quicksight-dashboard-decimaldefaultvalues-dynamicvalue"></a>
The dynamic value of the `DecimalDefaultValues`. Different defaults are displayed according to users, groups, and values mapping.
*Required*: No
*Type*: [DynamicDefaultValue](aws-properties-quicksight-dashboard-dynamicdefaultvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticValues`  <a name="cfn-quicksight-dashboard-decimaldefaultvalues-staticvalues"></a>
The static values of the `DecimalDefaultValues`.
*Required*: No
*Type*: Array of Number
*Minimum*: `0`
*Maximum*: `50000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
