---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-imagebuilder-lifecyclepolicy-resourceselection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::LifecyclePolicy ResourceSelection
<a name="aws-properties-imagebuilder-lifecyclepolicy-resourceselection"></a>

Resource selection criteria for the lifecycle policy.

## Syntax
<a name="aws-properties-imagebuilder-lifecyclepolicy-resourceselection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-imagebuilder-lifecyclepolicy-resourceselection-syntax.json"></a>

```
{
  "[Recipes](#cfn-imagebuilder-lifecyclepolicy-resourceselection-recipes)" : {{[ RecipeSelection, ... ]}},
  "[TagMap](#cfn-imagebuilder-lifecyclepolicy-resourceselection-tagmap)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-imagebuilder-lifecyclepolicy-resourceselection-syntax.yaml"></a>

```
  [Recipes](#cfn-imagebuilder-lifecyclepolicy-resourceselection-recipes): {{
    - RecipeSelection}}
  [TagMap](#cfn-imagebuilder-lifecyclepolicy-resourceselection-tagmap): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-imagebuilder-lifecyclepolicy-resourceselection-properties"></a>

`Recipes`  <a name="cfn-imagebuilder-lifecyclepolicy-resourceselection-recipes"></a>
A list of recipes that are used as selection criteria for the output images that the lifecycle policy applies to.
*Required*: No
*Type*: Array of [RecipeSelection](aws-properties-imagebuilder-lifecyclepolicy-recipeselection.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TagMap`  <a name="cfn-imagebuilder-lifecyclepolicy-resourceselection-tagmap"></a>
A list of tags that are used as selection criteria for the Image Builder image resources that the lifecycle policy applies to.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
