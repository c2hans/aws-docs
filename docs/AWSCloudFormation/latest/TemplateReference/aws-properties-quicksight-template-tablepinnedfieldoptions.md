---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-tablepinnedfieldoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template TablePinnedFieldOptions
<a name="aws-properties-quicksight-template-tablepinnedfieldoptions"></a>

The settings for the pinned columns of a table visual.

## Syntax
<a name="aws-properties-quicksight-template-tablepinnedfieldoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-tablepinnedfieldoptions-syntax.json"></a>

```
{
  "[PinnedLeftFields](#cfn-quicksight-template-tablepinnedfieldoptions-pinnedleftfields)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-quicksight-template-tablepinnedfieldoptions-syntax.yaml"></a>

```
  [PinnedLeftFields](#cfn-quicksight-template-tablepinnedfieldoptions-pinnedleftfields): {{
    - String}}
```

## Properties
<a name="aws-properties-quicksight-template-tablepinnedfieldoptions-properties"></a>

`PinnedLeftFields`  <a name="cfn-quicksight-template-tablepinnedfieldoptions-pinnedleftfields"></a>
A list of columns to be pinned to the left of a table visual.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `512 | 201`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
