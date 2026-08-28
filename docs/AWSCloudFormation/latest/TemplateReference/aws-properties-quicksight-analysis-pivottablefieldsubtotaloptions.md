---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-analysis-pivottablefieldsubtotaloptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Analysis PivotTableFieldSubtotalOptions
<a name="aws-properties-quicksight-analysis-pivottablefieldsubtotaloptions"></a>

The optional configuration of subtotals cells.

## Syntax
<a name="aws-properties-quicksight-analysis-pivottablefieldsubtotaloptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-analysis-pivottablefieldsubtotaloptions-syntax.json"></a>

```
{
  "[FieldId](#cfn-quicksight-analysis-pivottablefieldsubtotaloptions-fieldid)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-analysis-pivottablefieldsubtotaloptions-syntax.yaml"></a>

```
  [FieldId](#cfn-quicksight-analysis-pivottablefieldsubtotaloptions-fieldid): {{String}}
```

## Properties
<a name="aws-properties-quicksight-analysis-pivottablefieldsubtotaloptions-properties"></a>

`FieldId`  <a name="cfn-quicksight-analysis-pivottablefieldsubtotaloptions-fieldid"></a>
The field ID of the subtotal options.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
