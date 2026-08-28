---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-bodysectionrepeatdimensionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template BodySectionRepeatDimensionConfiguration
<a name="aws-properties-quicksight-template-bodysectionrepeatdimensionconfiguration"></a>

Describes the dataset column and constraints for the dynamic values used to repeat the contents of a section. The dataset column is either **Category** or **Numeric** column configuration

## Syntax
<a name="aws-properties-quicksight-template-bodysectionrepeatdimensionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-bodysectionrepeatdimensionconfiguration-syntax.json"></a>

```
{
  "[DynamicCategoryDimensionConfiguration](#cfn-quicksight-template-bodysectionrepeatdimensionconfiguration-dynamiccategorydimensionconfiguration)" : {{BodySectionDynamicCategoryDimensionConfiguration}},
  "[DynamicNumericDimensionConfiguration](#cfn-quicksight-template-bodysectionrepeatdimensionconfiguration-dynamicnumericdimensionconfiguration)" : {{BodySectionDynamicNumericDimensionConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-template-bodysectionrepeatdimensionconfiguration-syntax.yaml"></a>

```
  [DynamicCategoryDimensionConfiguration](#cfn-quicksight-template-bodysectionrepeatdimensionconfiguration-dynamiccategorydimensionconfiguration): {{
    BodySectionDynamicCategoryDimensionConfiguration}}
  [DynamicNumericDimensionConfiguration](#cfn-quicksight-template-bodysectionrepeatdimensionconfiguration-dynamicnumericdimensionconfiguration): {{
    BodySectionDynamicNumericDimensionConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-template-bodysectionrepeatdimensionconfiguration-properties"></a>

`DynamicCategoryDimensionConfiguration`  <a name="cfn-quicksight-template-bodysectionrepeatdimensionconfiguration-dynamiccategorydimensionconfiguration"></a>
Describes the **Category** dataset column and constraints around the dynamic values that will be used in repeating the section contents.
*Required*: No
*Type*: [BodySectionDynamicCategoryDimensionConfiguration](aws-properties-quicksight-template-bodysectiondynamiccategorydimensionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DynamicNumericDimensionConfiguration`  <a name="cfn-quicksight-template-bodysectionrepeatdimensionconfiguration-dynamicnumericdimensionconfiguration"></a>
Describes the **Numeric** dataset column and constraints around the dynamic values used to repeat the contents of a section.
*Required*: No
*Type*: [BodySectionDynamicNumericDimensionConfiguration](aws-properties-quicksight-template-bodysectiondynamicnumericdimensionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
