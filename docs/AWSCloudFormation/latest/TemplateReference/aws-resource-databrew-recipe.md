---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-databrew-recipe.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Recipe
<a name="aws-resource-databrew-recipe"></a>

Specifies a new AWS Glue DataBrew transformation recipe.

## Syntax
<a name="aws-resource-databrew-recipe-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-databrew-recipe-syntax.json"></a>

```
{
  "Type" : "AWS::DataBrew::Recipe",
  "Properties" : {
      "[Description](#cfn-databrew-recipe-description)" : {{String}},
      "[Name](#cfn-databrew-recipe-name)" : {{String}},
      "[Steps](#cfn-databrew-recipe-steps)" : {{[ RecipeStep, ... ]}},
      "[Tags](#cfn-databrew-recipe-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-databrew-recipe-syntax.yaml"></a>

```
Type: AWS::DataBrew::Recipe
Properties:
  [Description](#cfn-databrew-recipe-description): {{String}}
  [Name](#cfn-databrew-recipe-name): {{String}}
  [Steps](#cfn-databrew-recipe-steps): {{
    - RecipeStep}}
  [Tags](#cfn-databrew-recipe-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-databrew-recipe-properties"></a>

`Description`  <a name="cfn-databrew-recipe-description"></a>
The description of the recipe.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-databrew-recipe-name"></a>
The unique name for the recipe.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Steps`  <a name="cfn-databrew-recipe-steps"></a>
A list of steps that are defined by the recipe.
*Required*: Yes
*Type*: Array of [RecipeStep](aws-properties-databrew-recipe-recipestep.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-databrew-recipe-tags"></a>
Metadata tags that have been applied to the recipe.
*Required*: No
*Type*: Array of [Tag](aws-properties-databrew-recipe-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-databrew-recipe-return-values"></a>

### Ref
<a name="aws-resource-databrew-recipe-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name. For example:

 `{ "Ref": "myRecipe" }`

For an AWS Glue DataBrew recipe named `myRecipe`, `Ref` returns the name of the recipe.

## Examples
<a name="aws-resource-databrew-recipe--examples"></a>

### Creating recipes
<a name="aws-resource-databrew-recipe--examples--Creating_recipes"></a>

The following examples create new DataBrew recipes.

#### YAML
<a name="aws-resource-databrew-recipe--examples--Creating_recipes--yaml"></a>

```
Resources:
  TestDataBrewRecipe:
    Type: AWS::DataBrew::Recipe
    Properties:
      Name: recipe-name
      Description: This is the recipe description.
      Steps:
      - Action:
          Operation: EXTRACT_PATTERN
          Parameters:
            SourceColumn: Consulate
            Pattern: A
            TargetColumn: extract_pattern
        ConditionExpressions:
        - Condition : LESS_THAN_EQUAL
          Value: 5
          TargetColumn: Target
      Tags: [{Key: key00AtCreate, Value: value001AtCreate}]
```

#### JSON
<a name="aws-resource-databrew-recipe--examples--Creating_recipes--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "This CloudFormation template specifies a DataBrew Recipe",
    "Resources": {
        "MyDataBrewRecipe": {
            "Type": "AWS::DataBrew::Recipe",
            "Properties": {
              "Name": "na-recipe-cf-test",
              "Description": "This is the recipe description.",
              "Steps":[
                {
                  "Action":{
                    "Operation":"EXTRACT_PATTERN",
                    "Parameters":{
                      "SourceColumn": "Consulate",
                      "Pattern": "A",
                      "TargetColumn": "extract_pattern"
                  }
                },
                  "ConditionExpressions":[
                    {
                      "Condition": "LESS_THAN",
                      "ConditionValue": "2",
                      "TargetColumn": "target"
                    },
                    {
                      "Condition": "GREATER_THAN",
                      "Value": "0",
                      "TargetColumn": "target"
                    }
                  ]
                }
              ],
              "Tags": [
                    {
                        "Key": "key00AtCreate",
                        "Value": "value001AtCreate"
                    }
                ]
            }
        }
    }
}
```
