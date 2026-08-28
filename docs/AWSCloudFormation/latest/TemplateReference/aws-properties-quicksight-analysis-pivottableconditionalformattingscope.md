---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-pivottableconditionalformattingscope.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis PivotTableConditionalFormattingScope
<a name="aws-properties-quicksight-analysis-pivottableconditionalformattingscope"></a>

The scope of the cell for conditional formatting.

## Syntax
<a name="aws-properties-quicksight-analysis-pivottableconditionalformattingscope-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-pivottableconditionalformattingscope-syntax.json"></a>

```
{
  "[Role](#cfn-quicksight-analysis-pivottableconditionalformattingscope-role)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-pivottableconditionalformattingscope-syntax.yaml"></a>

```
  [Role](#cfn-quicksight-analysis-pivottableconditionalformattingscope-role): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-pivottableconditionalformattingscope-properties"></a>

`Role`  <a name="cfn-quicksight-analysis-pivottableconditionalformattingscope-role"></a>
The role (field, field total, grand total) of the cell for conditional formatting.
*Required*: No
*Type*: String
*Allowed values*: `FIELD | FIELD_TOTAL | GRAND_TOTAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
