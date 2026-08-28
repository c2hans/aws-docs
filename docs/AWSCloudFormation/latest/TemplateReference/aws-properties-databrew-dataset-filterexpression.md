---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-dataset-filterexpression.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Dataset FilterExpression
<a name="aws-properties-databrew-dataset-filterexpression"></a>

Represents a structure for defining parameter conditions.

## Syntax
<a name="aws-properties-databrew-dataset-filterexpression-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-dataset-filterexpression-syntax.json"></a>

```
{
  "[Expression](#cfn-databrew-dataset-filterexpression-expression)" : {{String}},
  "[ValuesMap](#cfn-databrew-dataset-filterexpression-valuesmap)" : {{[ FilterValue, ... ]}}
}
```

### YAML
<a name="aws-properties-databrew-dataset-filterexpression-syntax.yaml"></a>

```
  [Expression](#cfn-databrew-dataset-filterexpression-expression): {{String}}
  [ValuesMap](#cfn-databrew-dataset-filterexpression-valuesmap): {{
    - FilterValue}}
```

## Properties
<a name="aws-properties-databrew-dataset-filterexpression-properties"></a>

`Expression`  <a name="cfn-databrew-dataset-filterexpression-expression"></a>
The expression which includes condition names followed by substitution variables, possibly grouped and combined with other conditions. For example, "(starts\_with :prefix1 or starts\_with :prefix2) and (ends\_with :suffix1 or ends\_with :suffix2)". Substitution variables should start with ':' symbol.
*Required*: Yes
*Type*: String
*Pattern*: `^[><0-9A-Za-z_.,:)(!= ]+$`
*Minimum*: `4`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ValuesMap`  <a name="cfn-databrew-dataset-filterexpression-valuesmap"></a>
The map of substitution variable names to their values used in this filter expression.
*Required*: Yes
*Type*: Array of [FilterValue](aws-properties-databrew-dataset-filtervalue.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
