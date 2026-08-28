---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-image-workflowparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::Image WorkflowParameter
<a name="aws-properties-imagebuilder-image-workflowparameter"></a>

Contains a key/value pair that sets the named workflow parameter.

## Syntax
<a name="aws-properties-imagebuilder-image-workflowparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-image-workflowparameter-syntax.json"></a>

```
{
  "[Name](#cfn-imagebuilder-image-workflowparameter-name)" : {{String}},
  "[Value](#cfn-imagebuilder-image-workflowparameter-value)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-imagebuilder-image-workflowparameter-syntax.yaml"></a>

```
  [Name](#cfn-imagebuilder-image-workflowparameter-name): {{String}}
  [Value](#cfn-imagebuilder-image-workflowparameter-value): {{
    - String}}
```

## Properties
<a name="aws-properties-imagebuilder-image-workflowparameter-properties"></a>

`Name`  <a name="cfn-imagebuilder-image-workflowparameter-name"></a>
The name of the workflow parameter to set.
*Required*: No
*Type*: String
*Pattern*: `[^\x00]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-imagebuilder-image-workflowparameter-value"></a>
Sets the value for the named workflow parameter.
*Required*: No
*Type*: Array of String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
