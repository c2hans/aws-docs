---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-imagerecipe-componentconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::ImageRecipe ComponentConfiguration
<a name="aws-properties-imagebuilder-imagerecipe-componentconfiguration"></a>

Configuration details of the component. You can specify each component only once in a recipe, regardless of version. Components with a status of `DEPRECATED` or `DISABLED` can't be added to new recipes.

## Syntax
<a name="aws-properties-imagebuilder-imagerecipe-componentconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-imagerecipe-componentconfiguration-syntax.json"></a>

```
{
  "[ComponentArn](#cfn-imagebuilder-imagerecipe-componentconfiguration-componentarn)" : {{String}},
  "[Parameters](#cfn-imagebuilder-imagerecipe-componentconfiguration-parameters)" : {{[ ComponentParameter, ... ]}}
}
```

### YAML
<a name="aws-properties-imagebuilder-imagerecipe-componentconfiguration-syntax.yaml"></a>

```
  [ComponentArn](#cfn-imagebuilder-imagerecipe-componentconfiguration-componentarn): {{String}}
  [Parameters](#cfn-imagebuilder-imagerecipe-componentconfiguration-parameters): {{
    - ComponentParameter}}
```

## Properties
<a name="aws-properties-imagebuilder-imagerecipe-componentconfiguration-properties"></a>

`ComponentArn`  <a name="cfn-imagebuilder-imagerecipe-componentconfiguration-componentarn"></a>
The Amazon Resource Name (ARN) of the component. You can specify a build version ARN, or a component version ARN whose version segments can use `x` wildcards, for example `1.x.x`.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[^:]*:imagebuilder:[^:]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?|third-party):component/[a-z0-9-_]+/(?:(?:([0-9]+|x)\.([0-9]+|x)\.([0-9]+|x))|(?:[0-9]+\.[0-9]+\.[0-9]+/[0-9]+))$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Parameters`  <a name="cfn-imagebuilder-imagerecipe-componentconfiguration-parameters"></a>
A group of parameter settings that Image Builder uses to configure the component for a specific recipe. You must supply a value for every component parameter that has no default value, and you can only supply parameters that the component defines.
*Required*: No
*Type*: Array of [ComponentParameter](aws-properties-imagebuilder-imagerecipe-componentparameter.md)
*Minimum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
