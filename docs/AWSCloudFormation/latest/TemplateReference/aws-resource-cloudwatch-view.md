---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-view.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::View
<a name="aws-resource-cloudwatch-view"></a>

Resource Type definition for `AWS::CloudWatch::View`. A view is a named, reusable SQL query that can be referenced from CloudWatch telemetry queries. View names must be unique within the account and region.

## Syntax
<a name="aws-resource-cloudwatch-view-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-view-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::View",
  "Properties" : {
      "[Definition](#cfn-cloudwatch-view-definition)" : {{String}},
      "[Description](#cfn-cloudwatch-view-description)" : {{String}},
      "[Name](#cfn-cloudwatch-view-name)" : {{String}},
      "[Tags](#cfn-cloudwatch-view-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-view-syntax.yaml"></a>

```
Type: AWS::CloudWatch::View
Properties:
  [Definition](#cfn-cloudwatch-view-definition): {{String}}
  [Description](#cfn-cloudwatch-view-description): {{String}}
  [Name](#cfn-cloudwatch-view-name): {{String}}
  [Tags](#cfn-cloudwatch-view-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudwatch-view-properties"></a>

`Definition`  <a name="cfn-cloudwatch-view-definition"></a>
The SQL query that defines the view.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-cloudwatch-view-description"></a>
A description of the view.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudwatch-view-name"></a>
The name of the view. Must begin with the "view." prefix followed by lowercase alphanumeric characters, hyphens, and underscores. View names must be unique within the account and region. If not specified, a name is generated.
*Required*: No
*Type*: String
*Pattern*: `^view\.[a-z0-9][a-z0-9_-]{0,250}$`
*Minimum*: `6`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudwatch-view-tags"></a>
An array of key-value pairs to apply to the view.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-view-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-view-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-view-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the value of the `Name` property.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudwatch-view-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudwatch-view-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the view.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the view was created.

`Type`  <a name="Type-fn::getatt"></a>
The ownership category of the view. Views created through CloudFormation are always USER views; MANAGED views are provisioned by AWS.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the view was last updated.
