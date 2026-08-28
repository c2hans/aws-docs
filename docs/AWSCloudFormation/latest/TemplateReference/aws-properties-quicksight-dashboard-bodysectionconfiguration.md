---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-bodysectionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard BodySectionConfiguration
<a name="aws-properties-quicksight-dashboard-bodysectionconfiguration"></a>

The configuration of a body section.

## Syntax
<a name="aws-properties-quicksight-dashboard-bodysectionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-bodysectionconfiguration-syntax.json"></a>

```
{
  "[Content](#cfn-quicksight-dashboard-bodysectionconfiguration-content)" : {{BodySectionContent}},
  "[PageBreakConfiguration](#cfn-quicksight-dashboard-bodysectionconfiguration-pagebreakconfiguration)" : {{SectionPageBreakConfiguration}},
  "[RepeatConfiguration](#cfn-quicksight-dashboard-bodysectionconfiguration-repeatconfiguration)" : {{BodySectionRepeatConfiguration}},
  "[SectionId](#cfn-quicksight-dashboard-bodysectionconfiguration-sectionid)" : {{String}},
  "[Style](#cfn-quicksight-dashboard-bodysectionconfiguration-style)" : {{SectionStyle}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-bodysectionconfiguration-syntax.yaml"></a>

```
  [Content](#cfn-quicksight-dashboard-bodysectionconfiguration-content): {{
    BodySectionContent}}
  [PageBreakConfiguration](#cfn-quicksight-dashboard-bodysectionconfiguration-pagebreakconfiguration): {{
    SectionPageBreakConfiguration}}
  [RepeatConfiguration](#cfn-quicksight-dashboard-bodysectionconfiguration-repeatconfiguration): {{
    BodySectionRepeatConfiguration}}
  [SectionId](#cfn-quicksight-dashboard-bodysectionconfiguration-sectionid): {{String}}
  [Style](#cfn-quicksight-dashboard-bodysectionconfiguration-style): {{
    SectionStyle}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-bodysectionconfiguration-properties"></a>

`Content`  <a name="cfn-quicksight-dashboard-bodysectionconfiguration-content"></a>
The configuration of content in a body section.
*Required*: Yes
*Type*: [BodySectionContent](aws-properties-quicksight-dashboard-bodysectioncontent.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PageBreakConfiguration`  <a name="cfn-quicksight-dashboard-bodysectionconfiguration-pagebreakconfiguration"></a>
The configuration of a page break for a section.
*Required*: No
*Type*: [SectionPageBreakConfiguration](aws-properties-quicksight-dashboard-sectionpagebreakconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RepeatConfiguration`  <a name="cfn-quicksight-dashboard-bodysectionconfiguration-repeatconfiguration"></a>
Describes the configurations that are required to declare a section as repeating.
*Required*: No
*Type*: [BodySectionRepeatConfiguration](aws-properties-quicksight-dashboard-bodysectionrepeatconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SectionId`  <a name="cfn-quicksight-dashboard-bodysectionconfiguration-sectionid"></a>
The unique identifier of a body section.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Style`  <a name="cfn-quicksight-dashboard-bodysectionconfiguration-style"></a>
The style options of a body section.
*Required*: No
*Type*: [SectionStyle](aws-properties-quicksight-dashboard-sectionstyle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
