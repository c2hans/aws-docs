---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-sheettextbox.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis SheetTextBox
<a name="aws-properties-quicksight-analysis-sheettextbox"></a>

A text box.

## Syntax
<a name="aws-properties-quicksight-analysis-sheettextbox-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-sheettextbox-syntax.json"></a>

```
{
  "[Content](#cfn-quicksight-analysis-sheettextbox-content)" : {{String}},
  "[SheetTextBoxId](#cfn-quicksight-analysis-sheettextbox-sheettextboxid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-sheettextbox-syntax.yaml"></a>

```
  [Content](#cfn-quicksight-analysis-sheettextbox-content): {{String}}
  [SheetTextBoxId](#cfn-quicksight-analysis-sheettextbox-sheettextboxid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-sheettextbox-properties"></a>

`Content`  <a name="cfn-quicksight-analysis-sheettextbox-content"></a>
The content that is displayed in the text box.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `150000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SheetTextBoxId`  <a name="cfn-quicksight-analysis-sheettextbox-sheettextboxid"></a>
The unique identifier for a text box. This identifier must be unique within the context of a dashboard, template, or analysis. Two dashboards, analyses, or templates can have text boxes that share identifiers.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
