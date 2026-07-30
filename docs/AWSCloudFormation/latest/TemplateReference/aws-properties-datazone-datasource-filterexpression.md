---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-datasource-filterexpression.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource FilterExpression
<a name="aws-properties-datazone-datasource-filterexpression"></a>

A filter expression in Amazon DataZone.

## Syntax
<a name="aws-properties-datazone-datasource-filterexpression-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-datasource-filterexpression-syntax.json"></a>

```
{
  "[Expression](#cfn-datazone-datasource-filterexpression-expression)" : {{String}},
  "[Type](#cfn-datazone-datasource-filterexpression-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-datasource-filterexpression-syntax.yaml"></a>

```
  [Expression](#cfn-datazone-datasource-filterexpression-expression): {{String}}
  [Type](#cfn-datazone-datasource-filterexpression-type): {{String}}
```

## Properties
<a name="aws-properties-datazone-datasource-filterexpression-properties"></a>

`Expression`  <a name="cfn-datazone-datasource-filterexpression-expression"></a>
The search filter expression.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-datazone-datasource-filterexpression-type"></a>
The search filter explresison type.
*Required*: Yes
*Type*: String
*Allowed values*: `INCLUDE | EXCLUDE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
