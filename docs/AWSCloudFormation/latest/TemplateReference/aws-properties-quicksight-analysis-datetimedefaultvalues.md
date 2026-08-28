---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-datetimedefaultvalues.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis DateTimeDefaultValues
<a name="aws-properties-quicksight-analysis-datetimedefaultvalues"></a>

The default values of the `DateTimeParameterDeclaration`.

## Syntax
<a name="aws-properties-quicksight-analysis-datetimedefaultvalues-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-datetimedefaultvalues-syntax.json"></a>

```
{
  "[DynamicValue](#cfn-quicksight-analysis-datetimedefaultvalues-dynamicvalue)" : {{DynamicDefaultValue}},
  "[RollingDate](#cfn-quicksight-analysis-datetimedefaultvalues-rollingdate)" : {{RollingDateConfiguration}},
  "[StaticValues](#cfn-quicksight-analysis-datetimedefaultvalues-staticvalues)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-datetimedefaultvalues-syntax.yaml"></a>

```
  [DynamicValue](#cfn-quicksight-analysis-datetimedefaultvalues-dynamicvalue): {{
    DynamicDefaultValue}}
  [RollingDate](#cfn-quicksight-analysis-datetimedefaultvalues-rollingdate): {{
    RollingDateConfiguration}}
  [StaticValues](#cfn-quicksight-analysis-datetimedefaultvalues-staticvalues): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-datetimedefaultvalues-properties"></a>

`DynamicValue`  <a name="cfn-quicksight-analysis-datetimedefaultvalues-dynamicvalue"></a>
The dynamic value of the `DataTimeDefaultValues`. Different defaults are displayed according to users, groups, and values mapping.
*Required*: No
*Type*: [DynamicDefaultValue](aws-properties-quicksight-analysis-dynamicdefaultvalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RollingDate`  <a name="cfn-quicksight-analysis-datetimedefaultvalues-rollingdate"></a>
The rolling date of the `DataTimeDefaultValues`. The date is determined from the dataset based on input expression.
*Required*: No
*Type*: [RollingDateConfiguration](aws-properties-quicksight-analysis-rollingdateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StaticValues`  <a name="cfn-quicksight-analysis-datetimedefaultvalues-staticvalues"></a>
The static values of the `DataTimeDefaultValues`.
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `50000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
