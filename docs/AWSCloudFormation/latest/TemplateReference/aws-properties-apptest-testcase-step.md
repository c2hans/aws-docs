---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-step.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase Step
<a name="aws-properties-apptest-testcase-step"></a>

Defines a step.

## Syntax
<a name="aws-properties-apptest-testcase-step-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-step-syntax.json"></a>

```
{
  "[Action](#cfn-apptest-testcase-step-action)" : {{StepAction}},
  "[Description](#cfn-apptest-testcase-step-description)" : {{String}},
  "[Name](#cfn-apptest-testcase-step-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-step-syntax.yaml"></a>

```
  [Action](#cfn-apptest-testcase-step-action): {{
    StepAction}}
  [Description](#cfn-apptest-testcase-step-description): {{String}}
  [Name](#cfn-apptest-testcase-step-name): {{String}}
```

## Properties
<a name="aws-properties-apptest-testcase-step-properties"></a>

`Action`  <a name="cfn-apptest-testcase-step-action"></a>
The action of the step.
*Required*: Yes
*Type*: [StepAction](aws-properties-apptest-testcase-stepaction.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-apptest-testcase-step-description"></a>
The description of the step.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-apptest-testcase-step-name"></a>
The name of the step.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][A-Za-z0-9_\-]{1,59}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
