---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-sectionafterpagebreak.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SectionAfterPageBreak
<a name="aws-properties-quicksight-analysis-sectionafterpagebreak"></a>

The configuration of a page break after a section.

## Syntax
<a name="aws-properties-quicksight-analysis-sectionafterpagebreak-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-sectionafterpagebreak-syntax.json"></a>

```
{
  "[Status](#cfn-quicksight-analysis-sectionafterpagebreak-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-sectionafterpagebreak-syntax.yaml"></a>

```
  [Status](#cfn-quicksight-analysis-sectionafterpagebreak-status): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-sectionafterpagebreak-properties"></a>

`Status`  <a name="cfn-quicksight-analysis-sectionafterpagebreak-status"></a>
The option that enables or disables a page break at the end of a section.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
