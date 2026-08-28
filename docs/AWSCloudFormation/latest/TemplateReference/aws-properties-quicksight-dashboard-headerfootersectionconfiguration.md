---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-headerfootersectionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard HeaderFooterSectionConfiguration
<a name="aws-properties-quicksight-dashboard-headerfootersectionconfiguration"></a>

The configuration of a header or footer section.

## Syntax
<a name="aws-properties-quicksight-dashboard-headerfootersectionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-headerfootersectionconfiguration-syntax.json"></a>

```
{
  "[Layout](#cfn-quicksight-dashboard-headerfootersectionconfiguration-layout)" : {{SectionLayoutConfiguration}},
  "[SectionId](#cfn-quicksight-dashboard-headerfootersectionconfiguration-sectionid)" : {{String}},
  "[Style](#cfn-quicksight-dashboard-headerfootersectionconfiguration-style)" : {{SectionStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-headerfootersectionconfiguration-syntax.yaml"></a>

```
  [Layout](#cfn-quicksight-dashboard-headerfootersectionconfiguration-layout): {{
    SectionLayoutConfiguration}}
  [SectionId](#cfn-quicksight-dashboard-headerfootersectionconfiguration-sectionid): {{String}}
  [Style](#cfn-quicksight-dashboard-headerfootersectionconfiguration-style): {{
    SectionStyle}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-headerfootersectionconfiguration-properties"></a>

`Layout`  <a name="cfn-quicksight-dashboard-headerfootersectionconfiguration-layout"></a>
The layout configuration of the header or footer section.
*Required*: Yes
*Type*: [SectionLayoutConfiguration](aws-properties-quicksight-dashboard-sectionlayoutconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SectionId`  <a name="cfn-quicksight-dashboard-headerfootersectionconfiguration-sectionid"></a>
The unique identifier of the header or footer section.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Style`  <a name="cfn-quicksight-dashboard-headerfootersectionconfiguration-style"></a>
The style options of a header or footer section.
*Required*: No
*Type*: [SectionStyle](aws-properties-quicksight-dashboard-sectionstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
