---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-sectionpagebreakconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard SectionPageBreakConfiguration
<a name="aws-properties-quicksight-dashboard-sectionpagebreakconfiguration"></a>

The configuration of a page break for a section.

## Syntax
<a name="aws-properties-quicksight-dashboard-sectionpagebreakconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-sectionpagebreakconfiguration-syntax.json"></a>

```
{
  "[After](#cfn-quicksight-dashboard-sectionpagebreakconfiguration-after)" : {{SectionAfterPageBreak}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-sectionpagebreakconfiguration-syntax.yaml"></a>

```
  [After](#cfn-quicksight-dashboard-sectionpagebreakconfiguration-after): {{
    SectionAfterPageBreak}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-sectionpagebreakconfiguration-properties"></a>

`After`  <a name="cfn-quicksight-dashboard-sectionpagebreakconfiguration-after"></a>
The configuration of a page break after a section.
*Required*: No
*Type*: [SectionAfterPageBreak](aws-properties-quicksight-dashboard-sectionafterpagebreak.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
