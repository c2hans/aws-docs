---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-bodysectionrepeatconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template BodySectionRepeatConfiguration
<a name="aws-properties-quicksight-template-bodysectionrepeatconfiguration"></a>

Describes the configurations that are required to declare a section as repeating.

## Syntax
<a name="aws-properties-quicksight-template-bodysectionrepeatconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-bodysectionrepeatconfiguration-syntax.json"></a>

```
{
  "[DimensionConfigurations](#cfn-quicksight-template-bodysectionrepeatconfiguration-dimensionconfigurations)" : {{[ BodySectionRepeatDimensionConfiguration, ... ]}},
  "[NonRepeatingVisuals](#cfn-quicksight-template-bodysectionrepeatconfiguration-nonrepeatingvisuals)" : {{[ String, ... ]}},
  "[PageBreakConfiguration](#cfn-quicksight-template-bodysectionrepeatconfiguration-pagebreakconfiguration)" : {{BodySectionRepeatPageBreakConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-bodysectionrepeatconfiguration-syntax.yaml"></a>

```
  [DimensionConfigurations](#cfn-quicksight-template-bodysectionrepeatconfiguration-dimensionconfigurations): {{
    - BodySectionRepeatDimensionConfiguration}}
  [NonRepeatingVisuals](#cfn-quicksight-template-bodysectionrepeatconfiguration-nonrepeatingvisuals): {{
    - String}}
  [PageBreakConfiguration](#cfn-quicksight-template-bodysectionrepeatconfiguration-pagebreakconfiguration): {{
    BodySectionRepeatPageBreakConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-bodysectionrepeatconfiguration-properties"></a>

`DimensionConfigurations`  <a name="cfn-quicksight-template-bodysectionrepeatconfiguration-dimensionconfigurations"></a>
List of `BodySectionRepeatDimensionConfiguration` values that describe the dataset column and constraints for the column used to repeat the contents of a section.
*Required*: No
*Type*: Array of [BodySectionRepeatDimensionConfiguration](aws-properties-quicksight-template-bodysectionrepeatdimensionconfiguration.md)
*Minimum*: `0`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NonRepeatingVisuals`  <a name="cfn-quicksight-template-bodysectionrepeatconfiguration-nonrepeatingvisuals"></a>
List of visuals to exclude from repetition in repeating sections. The visuals will render identically, and ignore the repeating configurations in all repeating instances.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `512 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PageBreakConfiguration`  <a name="cfn-quicksight-template-bodysectionrepeatconfiguration-pagebreakconfiguration"></a>
Page break configuration to apply for each repeating instance.
*Required*: No
*Type*: [BodySectionRepeatPageBreakConfiguration](aws-properties-quicksight-template-bodysectionrepeatpagebreakconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
