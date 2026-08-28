---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-sectionbasedlayoutpapercanvassizeoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SectionBasedLayoutPaperCanvasSizeOptions
<a name="aws-properties-quicksight-analysis-sectionbasedlayoutpapercanvassizeoptions"></a>

The options for a paper canvas of a section-based layout.

## Syntax
<a name="aws-properties-quicksight-analysis-sectionbasedlayoutpapercanvassizeoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-sectionbasedlayoutpapercanvassizeoptions-syntax.json"></a>

```
{
  "[PaperMargin](#cfn-quicksight-analysis-sectionbasedlayoutpapercanvassizeoptions-papermargin)" : {{Spacing}},
  "[PaperOrientation](#cfn-quicksight-analysis-sectionbasedlayoutpapercanvassizeoptions-paperorientation)" : {{String}},
  "[PaperSize](#cfn-quicksight-analysis-sectionbasedlayoutpapercanvassizeoptions-papersize)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-sectionbasedlayoutpapercanvassizeoptions-syntax.yaml"></a>

```
  [PaperMargin](#cfn-quicksight-analysis-sectionbasedlayoutpapercanvassizeoptions-papermargin): {{
    Spacing}}
  [PaperOrientation](#cfn-quicksight-analysis-sectionbasedlayoutpapercanvassizeoptions-paperorientation): {{String}}
  [PaperSize](#cfn-quicksight-analysis-sectionbasedlayoutpapercanvassizeoptions-papersize): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-sectionbasedlayoutpapercanvassizeoptions-properties"></a>

`PaperMargin`  <a name="cfn-quicksight-analysis-sectionbasedlayoutpapercanvassizeoptions-papermargin"></a>
Defines the spacing between the canvas content and the top, bottom, left, and right edges.
*Required*: No
*Type*: [Spacing](aws-properties-quicksight-analysis-spacing.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PaperOrientation`  <a name="cfn-quicksight-analysis-sectionbasedlayoutpapercanvassizeoptions-paperorientation"></a>
The paper orientation that is used to define canvas dimensions. Choose one of the following options:
+ PORTRAIT
+ LANDSCAPE
*Required*: No
*Type*: String
*Allowed values*: `PORTRAIT | LANDSCAPE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PaperSize`  <a name="cfn-quicksight-analysis-sectionbasedlayoutpapercanvassizeoptions-papersize"></a>
The paper size that is used to define canvas dimensions.
*Required*: No
*Type*: String
*Allowed values*: `US_LETTER | US_LEGAL | US_TABLOID_LEDGER | A0 | A1 | A2 | A3 | A4 | A5 | JIS_B4 | JIS_B5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
