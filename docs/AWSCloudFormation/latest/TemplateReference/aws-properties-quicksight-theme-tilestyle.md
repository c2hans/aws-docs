---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-theme-tilestyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Theme TileStyle
<a name="aws-properties-quicksight-theme-tilestyle"></a>

Display options related to tiles on a sheet.

## Syntax
<a name="aws-properties-quicksight-theme-tilestyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-theme-tilestyle-syntax.json"></a>

```
{
  "[Border](#cfn-quicksight-theme-tilestyle-border)" : {{BorderStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-theme-tilestyle-syntax.yaml"></a>

```
  [Border](#cfn-quicksight-theme-tilestyle-border): {{
    BorderStyle}}
```

## Properties
<a name="aws-properties-quicksight-theme-tilestyle-properties"></a>

`Border`  <a name="cfn-quicksight-theme-tilestyle-border"></a>
The border around a tile.
*Required*: No
*Type*: [BorderStyle](aws-properties-quicksight-theme-borderstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
