---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-imagepipeline-workflowparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ImagePipeline WorkflowParameter
<a name="aws-properties-imagebuilder-imagepipeline-workflowparameter"></a>

Contains a key/value pair that sets the named workflow parameter.

## Syntax
<a name="aws-properties-imagebuilder-imagepipeline-workflowparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-imagepipeline-workflowparameter-syntax.json"></a>

```
{
  "[Name](#cfn-imagebuilder-imagepipeline-workflowparameter-name)" : {{String}},
  "[Value](#cfn-imagebuilder-imagepipeline-workflowparameter-value)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-imagebuilder-imagepipeline-workflowparameter-syntax.yaml"></a>

```
  [Name](#cfn-imagebuilder-imagepipeline-workflowparameter-name): {{String}}
  [Value](#cfn-imagebuilder-imagepipeline-workflowparameter-value): {{
    - String}}
```

## Properties
<a name="aws-properties-imagebuilder-imagepipeline-workflowparameter-properties"></a>

`Name`  <a name="cfn-imagebuilder-imagepipeline-workflowparameter-name"></a>
The name of the workflow parameter to set.
*Required*: No
*Type*: String
*Pattern*: `[^\x00]+`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-imagebuilder-imagepipeline-workflowparameter-value"></a>
Sets the value for the named workflow parameter.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
