---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dashboard-customactionurloperation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::Dashboard CustomActionURLOperation
<a name="aws-properties-quicksight-dashboard-customactionurloperation"></a>

The URL operation that opens a link to another webpage.

## Syntax
<a name="aws-properties-quicksight-dashboard-customactionurloperation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dashboard-customactionurloperation-syntax.json"></a>

```
{
  "[URLTarget](#cfn-quicksight-dashboard-customactionurloperation-urltarget)" : {{String}},
  "[URLTemplate](#cfn-quicksight-dashboard-customactionurloperation-urltemplate)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dashboard-customactionurloperation-syntax.yaml"></a>

```
  [URLTarget](#cfn-quicksight-dashboard-customactionurloperation-urltarget): {{String}}
  [URLTemplate](#cfn-quicksight-dashboard-customactionurloperation-urltemplate): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dashboard-customactionurloperation-properties"></a>

`URLTarget`  <a name="cfn-quicksight-dashboard-customactionurloperation-urltarget"></a>
The target of the `CustomActionURLOperation`.
Valid values are defined as follows:
+ `NEW_TAB`: Opens the target URL in a new browser tab.
+ `NEW_WINDOW`: Opens the target URL in a new browser window.
+ `SAME_TAB`: Opens the target URL in the same browser tab.
*Required*: Yes
*Type*: String
*Allowed values*: `NEW_TAB | NEW_WINDOW | SAME_TAB`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`URLTemplate`  <a name="cfn-quicksight-dashboard-customactionurloperation-urltemplate"></a>
THe URL link of the `CustomActionURLOperation`.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
