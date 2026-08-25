---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appsync-type.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppSync::Type
<a name="aws-resource-appsync-type"></a>

Describes a type.

## Syntax
<a name="aws-resource-appsync-type-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appsync-type-syntax.json"></a>

```
{
  "Type" : "AWS::AppSync::Type",
  "Properties" : {
      "[ApiId](#cfn-appsync-type-apiid)" : {{String}},
      "[Definition](#cfn-appsync-type-definition)" : {{String}},
      "[Format](#cfn-appsync-type-format)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-appsync-type-syntax.yaml"></a>

```
Type: AWS::AppSync::Type
Properties:
  [ApiId](#cfn-appsync-type-apiid): {{String}}
  [Definition](#cfn-appsync-type-definition): {{String}}
  [Format](#cfn-appsync-type-format): {{String}}
```

## Properties
<a name="aws-resource-appsync-type-properties"></a>

`ApiId`  <a name="cfn-appsync-type-apiid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Definition`  <a name="cfn-appsync-type-definition"></a>
The type definition.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Format`  <a name="cfn-appsync-type-format"></a>
The type format: SDL or JSON.
*Required*: Yes
*Type*: String
*Allowed values*: `SDL | JSON`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-appsync-type-return-values"></a>

### Ref
<a name="aws-resource-appsync-type-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-appsync-type-return-values-fn--getatt"></a>

####
<a name="aws-resource-appsync-type-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The type Amazon Resource Name (ARN).

`Name`  <a name="Name-fn::getatt"></a>
The type name.
