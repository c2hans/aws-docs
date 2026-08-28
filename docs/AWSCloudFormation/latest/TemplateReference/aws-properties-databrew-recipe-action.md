---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-recipe-action.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Recipe Action
<a name="aws-properties-databrew-recipe-action"></a>

Represents a transformation and associated parameters that are used to apply a change to an AWS Glue DataBrew dataset.

## Syntax
<a name="aws-properties-databrew-recipe-action-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-recipe-action-syntax.json"></a>

```
{
  "[Operation](#cfn-databrew-recipe-action-operation)" : {{String}},
  "[Parameters](#cfn-databrew-recipe-action-parameters)" : {{RecipeParameters}}
}
```

### YAML
<a name="aws-properties-databrew-recipe-action-syntax.yaml"></a>

```
  [Operation](#cfn-databrew-recipe-action-operation): {{String}}
  [Parameters](#cfn-databrew-recipe-action-parameters): {{
    RecipeParameters}}
```

## Properties
<a name="aws-properties-databrew-recipe-action-properties"></a>

`Operation`  <a name="cfn-databrew-recipe-action-operation"></a>
The name of a valid DataBrew transformation to be performed on the data.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Parameters`  <a name="cfn-databrew-recipe-action-parameters"></a>
Contextual parameters for the transformation.
*Required*: No
*Type*: [RecipeParameters](aws-properties-databrew-recipe-recipeparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
