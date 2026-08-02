---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-lifecyclepolicy-recipeselection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::LifecyclePolicy RecipeSelection
<a name="aws-properties-imagebuilder-lifecyclepolicy-recipeselection"></a>

Specifies an Image Builder recipe that the lifecycle policy uses for resource selection.

## Syntax
<a name="aws-properties-imagebuilder-lifecyclepolicy-recipeselection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-lifecyclepolicy-recipeselection-syntax.json"></a>

```
{
  "[Name](#cfn-imagebuilder-lifecyclepolicy-recipeselection-name)" : {{String}},
  "[SemanticVersion](#cfn-imagebuilder-lifecyclepolicy-recipeselection-semanticversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-imagebuilder-lifecyclepolicy-recipeselection-syntax.yaml"></a>

```
  [Name](#cfn-imagebuilder-lifecyclepolicy-recipeselection-name): {{String}}
  [SemanticVersion](#cfn-imagebuilder-lifecyclepolicy-recipeselection-semanticversion): {{String}}
```

## Properties
<a name="aws-properties-imagebuilder-lifecyclepolicy-recipeselection-properties"></a>

`Name`  <a name="cfn-imagebuilder-lifecyclepolicy-recipeselection-name"></a>
The name of an Image Builder recipe that the lifecycle policy uses for resource selection.
*Required*: Yes
*Type*: String
*Pattern*: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SemanticVersion`  <a name="cfn-imagebuilder-lifecyclepolicy-recipeselection-semanticversion"></a>
The version of the Image Builder recipe specified by the `name` field.
*Required*: Yes
*Type*: String
*Pattern*: `^(?:[0-9]+|x)\.(?:[0-9]+|x)\.(?:[0-9]+|x)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
