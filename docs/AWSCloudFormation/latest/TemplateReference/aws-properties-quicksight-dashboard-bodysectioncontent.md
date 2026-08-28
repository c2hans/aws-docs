---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-bodysectioncontent.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard BodySectionContent
<a name="aws-properties-quicksight-dashboard-bodysectioncontent"></a>

The configuration of content in a body section.

## Syntax
<a name="aws-properties-quicksight-dashboard-bodysectioncontent-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-bodysectioncontent-syntax.json"></a>

```
{
  "[Layout](#cfn-quicksight-dashboard-bodysectioncontent-layout)" : {{SectionLayoutConfiguration}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-bodysectioncontent-syntax.yaml"></a>

```
  [Layout](#cfn-quicksight-dashboard-bodysectioncontent-layout): {{
    SectionLayoutConfiguration}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-bodysectioncontent-properties"></a>

`Layout`  <a name="cfn-quicksight-dashboard-bodysectioncontent-layout"></a>
The layout configuration of a body section.
*Required*: No
*Type*: [SectionLayoutConfiguration](aws-properties-quicksight-dashboard-sectionlayoutconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
