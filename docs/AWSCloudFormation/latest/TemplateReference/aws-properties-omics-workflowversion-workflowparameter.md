---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-omics-workflowversion-workflowparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Omics::WorkflowVersion WorkflowParameter
<a name="aws-properties-omics-workflowversion-workflowparameter"></a>

A workflow parameter.

## Syntax
<a name="aws-properties-omics-workflowversion-workflowparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-omics-workflowversion-workflowparameter-syntax.json"></a>

```
{
  "[Description](#cfn-omics-workflowversion-workflowparameter-description)" : {{String}},
  "[Optional](#cfn-omics-workflowversion-workflowparameter-optional)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-omics-workflowversion-workflowparameter-syntax.yaml"></a>

```
  [Description](#cfn-omics-workflowversion-workflowparameter-description): {{String}}
  [Optional](#cfn-omics-workflowversion-workflowparameter-optional): {{Boolean}}
```

## Properties
<a name="aws-properties-omics-workflowversion-workflowparameter-properties"></a>

`Description`  <a name="cfn-omics-workflowversion-workflowparameter-description"></a>
The parameter's description.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Optional`  <a name="cfn-omics-workflowversion-workflowparameter-optional"></a>
Whether the parameter is optional.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
