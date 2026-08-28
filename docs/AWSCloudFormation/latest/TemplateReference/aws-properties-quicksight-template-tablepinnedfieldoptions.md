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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
