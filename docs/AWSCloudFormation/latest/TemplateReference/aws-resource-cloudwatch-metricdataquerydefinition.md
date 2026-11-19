---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-metricdataquerydefinition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::MetricDataQueryDefinition

Creates or updates a metric data query definition.

A metric data query definition saves a metric query so that you can reuse it later. It includes the query expression, the query language, and a path that names the definition and can organize it into folders. When you save a definition, CloudWatch doesn't validate or run its expression.

To create a definition, omit `Id`. CloudWatch generates the ID and returns it. To update a definition, specify its `Id`. An update replaces the path, expression, and type, and keeps the creation time.

The path must be unique in your account and Region. If another definition already uses the path, the request fails with a `ConflictException`.

You can have up to 1,000 metric data query definitions in each Region of your account. A request that would create more fails with a `LimitExceededException`.

 **Permissions**

To create or update a definition, you need the `cloudwatch:PutMetricDataQueryDefinition` permission on the metric data query definition resource. The resource ARN has the format `arn:aws:cloudwatch:Region:account-id:metric-query-definition/Id`.

To add tags when you create a definition, you also need the `cloudwatch:TagResource` permission. You can use the `aws:RequestTag/${TagKey}` and `aws:TagKeys` condition keys to control which tags can be added.

## Syntax
<a name="aws-resource-cloudwatch-metricdataquerydefinition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-metricdataquerydefinition-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::MetricDataQueryDefinition",
  "Properties" : {
      "[Expression](#cfn-cloudwatch-metricdataquerydefinition-expression)" : {{String}},
      "[Path](#cfn-cloudwatch-metricdataquerydefinition-path)" : {{String}},
      "[Tags](#cfn-cloudwatch-metricdataquerydefinition-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-cloudwatch-metricdataquerydefinition-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-metricdataquerydefinition-syntax.yaml"></a>

```
Type: AWS::CloudWatch::MetricDataQueryDefinition
Properties:
  [Expression](#cfn-cloudwatch-metricdataquerydefinition-expression): {{String}}
  [Path](#cfn-cloudwatch-metricdataquerydefinition-path): {{String}}
  [Tags](#cfn-cloudwatch-metricdataquerydefinition-tags): {{
    - Tag}}
  [Type](#cfn-cloudwatch-metricdataquerydefinition-type): {{String}}
```

## Properties
<a name="aws-resource-cloudwatch-metricdataquerydefinition-properties"></a>

`Expression`  <a name="cfn-cloudwatch-metricdataquerydefinition-expression"></a>
The metric query. It is stored as-is and is not validated.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `65536`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Path`  <a name="cfn-cloudwatch-metricdataquerydefinition-path"></a>
The path of the metric data query definition.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudwatch-metricdataquerydefinition-tags"></a>
An array of key-value pairs to apply to the metric data query definition.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-metricdataquerydefinition-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-cloudwatch-metricdataquerydefinition-type"></a>
The language of the expression. Valid values are the following:
+ `PROMQL` – A PromQL query.
+ `SQL` – A CloudWatch Metrics Insights query.
+ `METRIC_MATH` – A metric math expression.
*Required*: Yes
*Type*: String
*Allowed values*: `PROMQL | SQL | METRIC_MATH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-metricdataquerydefinition-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-metricdataquerydefinition-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the value of the `Arn` property.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudwatch-metricdataquerydefinition-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudwatch-metricdataquerydefinition-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the metric data query definition.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the metric data query definition was created.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the metric data query definition.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when you last updated the metric data query definition.
