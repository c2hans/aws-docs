---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-evaluator-categoricalscaledefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::Evaluator CategoricalScaleDefinition
<a name="aws-properties-bedrockagentcore-evaluator-categoricalscaledefinition"></a>

 The definition of a categorical rating scale option that provides a named category with its description for evaluation scoring.

## Syntax
<a name="aws-properties-bedrockagentcore-evaluator-categoricalscaledefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-evaluator-categoricalscaledefinition-syntax.json"></a>

```
{
  "[Definition](#cfn-bedrockagentcore-evaluator-categoricalscaledefinition-definition)" : {{String}},
  "[Label](#cfn-bedrockagentcore-evaluator-categoricalscaledefinition-label)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-evaluator-categoricalscaledefinition-syntax.yaml"></a>

```
  [Definition](#cfn-bedrockagentcore-evaluator-categoricalscaledefinition-definition): {{String}}
  [Label](#cfn-bedrockagentcore-evaluator-categoricalscaledefinition-label): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-evaluator-categoricalscaledefinition-properties"></a>

`Definition`  <a name="cfn-bedrockagentcore-evaluator-categoricalscaledefinition-definition"></a>
 The description that explains what this categorical rating represents and when it should be used.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Label`  <a name="cfn-bedrockagentcore-evaluator-categoricalscaledefinition-label"></a>
 The label or name of this categorical rating option.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
