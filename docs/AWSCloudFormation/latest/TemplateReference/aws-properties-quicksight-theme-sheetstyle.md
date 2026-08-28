---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-theme-sheetstyle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Theme SheetStyle
<a name="aws-properties-quicksight-theme-sheetstyle"></a>

The theme display options for sheets.

## Syntax
<a name="aws-properties-quicksight-theme-sheetstyle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-theme-sheetstyle-syntax.json"></a>

```
{
  "[Tile](#cfn-quicksight-theme-sheetstyle-tile)" : {{TileStyle}},
  "[TileLayout](#cfn-quicksight-theme-sheetstyle-tilelayout)" : {{TileLayoutStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-theme-sheetstyle-syntax.yaml"></a>

```
  [Tile](#cfn-quicksight-theme-sheetstyle-tile): {{
    TileStyle}}
  [TileLayout](#cfn-quicksight-theme-sheetstyle-tilelayout): {{
    TileLayoutStyle}}
```

## Properties
<a name="aws-properties-quicksight-theme-sheetstyle-properties"></a>

`Tile`  <a name="cfn-quicksight-theme-sheetstyle-tile"></a>
The display options for tiles.
*Required*: No
*Type*: [TileStyle](aws-properties-quicksight-theme-tilestyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TileLayout`  <a name="cfn-quicksight-theme-sheetstyle-tilelayout"></a>
The layout options for tiles.
*Required*: No
*Type*: [TileLayoutStyle](aws-properties-quicksight-theme-tilelayoutstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
