---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alert-query.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alert Query
<a name="aws-properties-cloudwatch-alert-query"></a>

The query the alert runs, and the language it is written in.

## Syntax
<a name="aws-properties-cloudwatch-alert-query-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alert-query-syntax.json"></a>

```
{
  "[Expression](#cfn-cloudwatch-alert-query-expression)" : {{String}},
  "[Language](#cfn-cloudwatch-alert-query-language)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alert-query-syntax.yaml"></a>

```
  [Expression](#cfn-cloudwatch-alert-query-expression): {{String}}
  [Language](#cfn-cloudwatch-alert-query-language): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-alert-query-properties"></a>

`Expression`  <a name="cfn-cloudwatch-alert-query-expression"></a>
The query expression. For PromQL, the series value is returned in a field named value.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Language`  <a name="cfn-cloudwatch-alert-query-language"></a>
The query language. Valid values: SQL, PROMQL.
*Required*: Yes
*Type*: String
*Allowed values*: `SQL | PROMQL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
