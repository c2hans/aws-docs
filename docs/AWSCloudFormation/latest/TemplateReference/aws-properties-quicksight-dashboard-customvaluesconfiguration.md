---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-customvaluesconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard CustomValuesConfiguration
<a name="aws-properties-quicksight-dashboard-customvaluesconfiguration"></a>

The configuration of custom values for the destination parameter in `DestinationParameterValueConfiguration`.

## Syntax
<a name="aws-properties-quicksight-dashboard-customvaluesconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-customvaluesconfiguration-syntax.json"></a>

```
{
  "[CustomValues](#cfn-quicksight-dashboard-customvaluesconfiguration-customvalues)" : {{CustomParameterValues}},
  "[IncludeNullValue](#cfn-quicksight-dashboard-customvaluesconfiguration-includenullvalue)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-customvaluesconfiguration-syntax.yaml"></a>

```
  [CustomValues](#cfn-quicksight-dashboard-customvaluesconfiguration-customvalues): {{
    CustomParameterValues}}
  [IncludeNullValue](#cfn-quicksight-dashboard-customvaluesconfiguration-includenullvalue): {{Boolean}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-customvaluesconfiguration-properties"></a>

`CustomValues`  <a name="cfn-quicksight-dashboard-customvaluesconfiguration-customvalues"></a>
Property description not available.
*Required*: Yes
*Type*: [CustomParameterValues](aws-properties-quicksight-dashboard-customparametervalues.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeNullValue`  <a name="cfn-quicksight-dashboard-customvaluesconfiguration-includenullvalue"></a>
Includes the null value in custom action parameter values.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
