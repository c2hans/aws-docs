---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-categoryfilterconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis CategoryFilterConfiguration
<a name="aws-properties-quicksight-analysis-categoryfilterconfiguration"></a>

The configuration for a `CategoryFilter`.

This is a union type structure. For this structure to be valid, only one of the attributes can be defined.

## Syntax
<a name="aws-properties-quicksight-analysis-categoryfilterconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-categoryfilterconfiguration-syntax.json"></a>

```
{
  "[CustomFilterConfiguration](#cfn-quicksight-analysis-categoryfilterconfiguration-customfilterconfiguration)" : {{CustomFilterConfiguration}},
  "[CustomFilterListConfiguration](#cfn-quicksight-analysis-categoryfilterconfiguration-customfilterlistconfiguration)" : {{CustomFilterListConfiguration}},
  "[FilterListConfiguration](#cfn-quicksight-analysis-categoryfilterconfiguration-filterlistconfiguration)" : {{FilterListConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-categoryfilterconfiguration-syntax.yaml"></a>

```
  [CustomFilterConfiguration](#cfn-quicksight-analysis-categoryfilterconfiguration-customfilterconfiguration): {{
    CustomFilterConfiguration}}
  [CustomFilterListConfiguration](#cfn-quicksight-analysis-categoryfilterconfiguration-customfilterlistconfiguration): {{
    CustomFilterListConfiguration}}
  [FilterListConfiguration](#cfn-quicksight-analysis-categoryfilterconfiguration-filterlistconfiguration): {{
    FilterListConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-analysis-categoryfilterconfiguration-properties"></a>

`CustomFilterConfiguration`  <a name="cfn-quicksight-analysis-categoryfilterconfiguration-customfilterconfiguration"></a>
A custom filter that filters based on a single value. This filter can be partially matched.
*Required*: No
*Type*: [CustomFilterConfiguration](aws-properties-quicksight-analysis-customfilterconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomFilterListConfiguration`  <a name="cfn-quicksight-analysis-categoryfilterconfiguration-customfilterlistconfiguration"></a>
A list of custom filter values. In the Quick Sight console, this filter type is called a custom filter list.
*Required*: No
*Type*: [CustomFilterListConfiguration](aws-properties-quicksight-analysis-customfilterlistconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FilterListConfiguration`  <a name="cfn-quicksight-analysis-categoryfilterconfiguration-filterlistconfiguration"></a>
A list of filter configurations. In the Quick Sight console, this filter type is called a filter list.
*Required*: No
*Type*: [FilterListConfiguration](aws-properties-quicksight-analysis-filterlistconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
