---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-theme-tilelayoutstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Theme TileLayoutStyle
<a name="aws-properties-quicksight-theme-tilelayoutstyle"></a>

The display options for the layout of tiles on a sheet.

## Syntax
<a name="aws-properties-quicksight-theme-tilelayoutstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-theme-tilelayoutstyle-syntax.json"></a>

```
{
  "[Gutter](#cfn-quicksight-theme-tilelayoutstyle-gutter)" : {{GutterStyle}},
  "[Margin](#cfn-quicksight-theme-tilelayoutstyle-margin)" : {{MarginStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-theme-tilelayoutstyle-syntax.yaml"></a>

```
  [Gutter](#cfn-quicksight-theme-tilelayoutstyle-gutter): {{
    GutterStyle}}
  [Margin](#cfn-quicksight-theme-tilelayoutstyle-margin): {{
    MarginStyle}}
```

## Properties
<a name="aws-properties-quicksight-theme-tilelayoutstyle-properties"></a>

`Gutter`  <a name="cfn-quicksight-theme-tilelayoutstyle-gutter"></a>
The gutter settings that apply between tiles.
*Required*: No
*Type*: [GutterStyle](aws-properties-quicksight-theme-gutterstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Margin`  <a name="cfn-quicksight-theme-tilelayoutstyle-margin"></a>
The margin settings that apply around the outside edge of sheets.
*Required*: No
*Type*: [MarginStyle](aws-properties-quicksight-theme-marginstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
