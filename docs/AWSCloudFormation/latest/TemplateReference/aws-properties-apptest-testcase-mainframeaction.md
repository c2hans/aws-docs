---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-apptest-testcase-mainframeaction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppTest::TestCase MainframeAction
<a name="aws-properties-apptest-testcase-mainframeaction"></a>

Specifies the mainframe action.

## Syntax
<a name="aws-properties-apptest-testcase-mainframeaction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-apptest-testcase-mainframeaction-syntax.json"></a>

```
{
  "[ActionType](#cfn-apptest-testcase-mainframeaction-actiontype)" : {{MainframeActionType}},
  "[Properties](#cfn-apptest-testcase-mainframeaction-properties)" : {{MainframeActionProperties}},
  "[Resource](#cfn-apptest-testcase-mainframeaction-resource)" : {{String}}
}
```

### YAML
<a name="aws-properties-apptest-testcase-mainframeaction-syntax.yaml"></a>

```
  [ActionType](#cfn-apptest-testcase-mainframeaction-actiontype): {{
    MainframeActionType}}
  [Properties](#cfn-apptest-testcase-mainframeaction-properties): {{
    MainframeActionProperties}}
  [Resource](#cfn-apptest-testcase-mainframeaction-resource): {{String}}
```

## Properties
<a name="aws-properties-apptest-testcase-mainframeaction-properties"></a>

`ActionType`  <a name="cfn-apptest-testcase-mainframeaction-actiontype"></a>
The action type of the mainframe action.
*Required*: Yes
*Type*: [MainframeActionType](aws-properties-apptest-testcase-mainframeactiontype.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Properties`  <a name="cfn-apptest-testcase-mainframeaction-properties"></a>
The properties of the mainframe action.
*Required*: No
*Type*: [MainframeActionProperties](aws-properties-apptest-testcase-mainframeactionproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Resource`  <a name="cfn-apptest-testcase-mainframeaction-resource"></a>
The resource of the mainframe action.
*Required*: Yes
*Type*: String
*Pattern*: `^\S{1,1000}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
