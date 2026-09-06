---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-bodysectionrepeatconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard BodySectionRepeatConfiguration
<a name="aws-properties-quicksight-dashboard-bodysectionrepeatconfiguration"></a>

Describes the configurations that are required to declare a section as repeating.

## Syntax
<a name="aws-properties-quicksight-dashboard-bodysectionrepeatconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-bodysectionrepeatconfiguration-syntax.json"></a>

```
{
  "[DimensionConfigurations](#cfn-quicksight-dashboard-bodysectionrepeatconfiguration-dimensionconfigurations)" : {{[ BodySectionRepeatDimensionConfiguration, ... ]}},
  "[NonRepeatingVisuals](#cfn-quicksight-dashboard-bodysectionrepeatconfiguration-nonrepeatingvisuals)" : {{[ String, ... ]}},
  "[PageBreakConfiguration](#cfn-quicksight-dashboard-bodysectionrepeatconfiguration-pagebreakconfiguration)" : {{BodySectionRepeatPageBreakConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-bodysectionrepeatconfiguration-syntax.yaml"></a>

```
  [DimensionConfigurations](#cfn-quicksight-dashboard-bodysectionrepeatconfiguration-dimensionconfigurations): {{
    - BodySectionRepeatDimensionConfiguration}}
  [NonRepeatingVisuals](#cfn-quicksight-dashboard-bodysectionrepeatconfiguration-nonrepeatingvisuals): {{
    - String}}
  [PageBreakConfiguration](#cfn-quicksight-dashboard-bodysectionrepeatconfiguration-pagebreakconfiguration): {{
    BodySectionRepeatPageBreakConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-bodysectionrepeatconfiguration-properties"></a>

`DimensionConfigurations`  <a name="cfn-quicksight-dashboard-bodysectionrepeatconfiguration-dimensionconfigurations"></a>
List of `BodySectionRepeatDimensionConfiguration` values that describe the dataset column and constraints for the column used to repeat the contents of a section.
*Required*: No
*Type*: Array of [BodySectionRepeatDimensionConfiguration](aws-properties-quicksight-dashboard-bodysectionrepeatdimensionconfiguration.md)
*Minimum*: `0`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NonRepeatingVisuals`  <a name="cfn-quicksight-dashboard-bodysectionrepeatconfiguration-nonrepeatingvisuals"></a>
List of visuals to exclude from repetition in repeating sections. The visuals will render identically, and ignore the repeating configurations in all repeating instances.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `512 | 20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PageBreakConfiguration`  <a name="cfn-quicksight-dashboard-bodysectionrepeatconfiguration-pagebreakconfiguration"></a>
Page break configuration to apply for each repeating instance.
*Required*: No
*Type*: [BodySectionRepeatPageBreakConfiguration](aws-properties-quicksight-dashboard-bodysectionrepeatpagebreakconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
