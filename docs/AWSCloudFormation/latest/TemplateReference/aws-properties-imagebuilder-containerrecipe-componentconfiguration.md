---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-containerrecipe-componentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ContainerRecipe ComponentConfiguration
<a name="aws-properties-imagebuilder-containerrecipe-componentconfiguration"></a>

Configuration details of the component.

## Syntax
<a name="aws-properties-imagebuilder-containerrecipe-componentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-containerrecipe-componentconfiguration-syntax.json"></a>

```
{
  "[ComponentArn](#cfn-imagebuilder-containerrecipe-componentconfiguration-componentarn)" : {{String}},
  "[Parameters](#cfn-imagebuilder-containerrecipe-componentconfiguration-parameters)" : {{[ ComponentParameter, ... ]}}
}
```

### YAML
<a name="aws-properties-imagebuilder-containerrecipe-componentconfiguration-syntax.yaml"></a>

```
  [ComponentArn](#cfn-imagebuilder-containerrecipe-componentconfiguration-componentarn): {{String}}
  [Parameters](#cfn-imagebuilder-containerrecipe-componentconfiguration-parameters): {{
    - ComponentParameter}}
```

## Properties
<a name="aws-properties-imagebuilder-containerrecipe-componentconfiguration-properties"></a>

`ComponentArn`  <a name="cfn-imagebuilder-containerrecipe-componentconfiguration-componentarn"></a>
The Amazon Resource Name (ARN) of the component.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):component/[a-z0-9-_]+/(?:(?:([0-9]+|x)\.([0-9]+|x)\.([0-9]+|x))|(?:[0-9]+\.[0-9]+\.[0-9]+/[0-9]+))$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Parameters`  <a name="cfn-imagebuilder-containerrecipe-componentconfiguration-parameters"></a>
A group of parameter settings that Image Builder uses to configure the component for a specific recipe.
*Required*: No
*Type*: Array of [ComponentParameter](aws-properties-imagebuilder-containerrecipe-componentparameter.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
