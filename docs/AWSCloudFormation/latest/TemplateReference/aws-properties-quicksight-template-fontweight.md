---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-template-fontweight.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Template FontWeight
<a name="aws-properties-quicksight-template-fontweight"></a>

The option that determines the text display weight, or boldness.

## Syntax
<a name="aws-properties-quicksight-template-fontweight-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-template-fontweight-syntax.json"></a>

```
{
  "[Name](#cfn-quicksight-template-fontweight-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-template-fontweight-syntax.yaml"></a>

```
  [Name](#cfn-quicksight-template-fontweight-name): {{String}}
```

## Properties
<a name="aws-properties-quicksight-template-fontweight-properties"></a>

`Name`  <a name="cfn-quicksight-template-fontweight-name"></a>
The lexical name for the level of boldness of the text display.
*Required*: No
*Type*: String
*Allowed values*: `NORMAL | BOLD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
