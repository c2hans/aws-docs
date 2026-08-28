---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-stepaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase StepAction
<a name="aws-properties-apptest-testcase-stepaction"></a>

Specifies a step action.

## Syntax
<a name="aws-properties-apptest-testcase-stepaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-stepaction-syntax.json"></a>

```
{
  "[CompareAction](#cfn-apptest-testcase-stepaction-compareaction)" : {{CompareAction}},
  "[MainframeAction](#cfn-apptest-testcase-stepaction-mainframeaction)" : {{MainframeAction}},
  "[ResourceAction](#cfn-apptest-testcase-stepaction-resourceaction)" : {{ResourceAction}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-stepaction-syntax.yaml"></a>

```
  [CompareAction](#cfn-apptest-testcase-stepaction-compareaction): {{
    CompareAction}}
  [MainframeAction](#cfn-apptest-testcase-stepaction-mainframeaction): {{
    MainframeAction}}
  [ResourceAction](#cfn-apptest-testcase-stepaction-resourceaction): {{
    ResourceAction}}
```

## Properties
<a name="aws-properties-apptest-testcase-stepaction-properties"></a>

`CompareAction`  <a name="cfn-apptest-testcase-stepaction-compareaction"></a>
The compare action of the step action.
*Required*: No
*Type*: [CompareAction](aws-properties-apptest-testcase-compareaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MainframeAction`  <a name="cfn-apptest-testcase-stepaction-mainframeaction"></a>
The mainframe action of the step action.
*Required*: No
*Type*: [MainframeAction](aws-properties-apptest-testcase-mainframeaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceAction`  <a name="cfn-apptest-testcase-stepaction-resourceaction"></a>
The resource action of the step action.
*Required*: No
*Type*: [ResourceAction](aws-properties-apptest-testcase-resourceaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
