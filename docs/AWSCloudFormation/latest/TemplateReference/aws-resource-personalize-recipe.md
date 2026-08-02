---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-personalize-recipe.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Personalize::Recipe
<a name="aws-resource-personalize-recipe"></a>

Provides information about a recipe. Each recipe provides an algorithm that Amazon Personalize uses in model training when you use the [CreateSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolution.html) operation.

## Syntax
<a name="aws-resource-personalize-recipe-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-personalize-recipe-syntax.json"></a>

```
{
  "Type" : "AWS::Personalize::Recipe",
  "Properties" : {
      "[Name](#cfn-personalize-recipe-name)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-personalize-recipe-syntax.yaml"></a>

```
Type: AWS::Personalize::Recipe
Properties:
  [Name](#cfn-personalize-recipe-name): {{String}}
```

## Properties
<a name="aws-resource-personalize-recipe-properties"></a>

`Name`  <a name="cfn-personalize-recipe-name"></a>
The name of the recipe.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-personalize-recipe-return-values"></a>

### Ref
<a name="aws-resource-personalize-recipe-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-personalize-recipe-return-values-fn--getatt"></a>

####
<a name="aws-resource-personalize-recipe-return-values-fn--getatt-fn--getatt"></a>

`AlgorithmArn`  <a name="AlgorithmArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the algorithm that Amazon Personalize uses to train the model.

`CreationDateTime`  <a name="CreationDateTime-fn::getatt"></a>
The date and time (in Unix format) that the recipe was created.

`Description`  <a name="Description-fn::getatt"></a>
The description of the recipe.

`FeatureTransformationArn`  <a name="FeatureTransformationArn-fn::getatt"></a>
The ARN of the FeatureTransformation object.

`LastUpdatedDateTime`  <a name="LastUpdatedDateTime-fn::getatt"></a>
The date and time (in Unix format) that the recipe was last updated.

`RecipeArn`  <a name="RecipeArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the recipe.

`RecipeType`  <a name="RecipeType-fn::getatt"></a>
One of the following values:
+ PERSONALIZED\_RANKING
+ RELATED\_ITEMS
+ USER\_PERSONALIZATION

`Status`  <a name="Status-fn::getatt"></a>
The status of the recipe.
