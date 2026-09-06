---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-job-recipe.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Job Recipe
<a name="aws-properties-databrew-job-recipe"></a>

Represents one or more actions to be performed on a DataBrew dataset.

## Syntax
<a name="aws-properties-databrew-job-recipe-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-job-recipe-syntax.json"></a>

```
{
  "[Name](#cfn-databrew-job-recipe-name)" : {{String}},
  "[Version](#cfn-databrew-job-recipe-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-databrew-job-recipe-syntax.yaml"></a>

```
  [Name](#cfn-databrew-job-recipe-name): {{String}}
  [Version](#cfn-databrew-job-recipe-version): {{String}}
```

## Properties
<a name="aws-properties-databrew-job-recipe-properties"></a>

`Name`  <a name="cfn-databrew-job-recipe-name"></a>
The unique name for the recipe.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-databrew-job-recipe-version"></a>
The identifier for the version for the recipe.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
