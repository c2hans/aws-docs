---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-view.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::View
<a name="aws-resource-cloudwatch-view"></a>

<a name="aws-resource-cloudwatch-view-description"></a>The `AWS::CloudWatch::View` resource Property description not available. for CloudWatch.

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
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-cloudwatch-view-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-cloudwatch-view-name"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^view\.[a-z0-9][a-z0-9_-]{0,250}$`
*Minimum*: `6`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudwatch-view-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-view-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-view-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-view-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudwatch-view-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudwatch-view-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`Type`  <a name="Type-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.
