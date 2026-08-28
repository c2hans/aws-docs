---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-function-functionref.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Function FunctionRef
<a name="aws-properties-mediatailor-function-functionref"></a>

A reference to a child function within a `SEQUENTIAL_EXECUTOR` function.

## Syntax
<a name="aws-properties-mediatailor-function-functionref-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-function-functionref-syntax.json"></a>

```
{
  "[FunctionId](#cfn-mediatailor-function-functionref-functionid)" : {{String}},
  "[RunCondition](#cfn-mediatailor-function-functionref-runcondition)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-function-functionref-syntax.yaml"></a>

```
  [FunctionId](#cfn-mediatailor-function-functionref-functionid): {{String}}
  [RunCondition](#cfn-mediatailor-function-functionref-runcondition): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-function-functionref-properties"></a>

`FunctionId`  <a name="cfn-mediatailor-function-functionref-functionid"></a>
The identifier of the child function to execute in this step.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RunCondition`  <a name="cfn-mediatailor-function-functionref-runcondition"></a>
An optional expression that evaluates to a boolean. MediaTailor evaluates this expression immediately before running the step, using the accumulated state at that point in the sequence. If the expression evaluates to `false`, MediaTailor skips the step and moves to the next one. If omitted, the step always runs.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
