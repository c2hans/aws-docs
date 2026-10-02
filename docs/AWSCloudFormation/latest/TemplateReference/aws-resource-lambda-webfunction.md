---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-webfunction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunction
<a name="aws-resource-lambda-webfunction"></a>

<a name="aws-resource-lambda-webfunction-description"></a>The `AWS::Lambda::WebFunction` resource Property description not available. for Lambda.

## Syntax
<a name="aws-resource-lambda-webfunction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-webfunction-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::WebFunction",
  "Properties" : {
      "[FunctionName](#cfn-lambda-webfunction-functionname)" : {{String}},
      "[Tags](#cfn-lambda-webfunction-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-lambda-webfunction-syntax.yaml"></a>

```
Type: AWS::Lambda::WebFunction
Properties:
  [FunctionName](#cfn-lambda-webfunction-functionname): {{String}}
  [Tags](#cfn-lambda-webfunction-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-lambda-webfunction-properties"></a>

`FunctionName`  <a name="cfn-lambda-webfunction-functionname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-lambda-webfunction-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-lambda-webfunction-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lambda-webfunction-return-values"></a>

### Ref
<a name="aws-resource-lambda-webfunction-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-lambda-webfunction-return-values-fn--getatt"></a>

####
<a name="aws-resource-lambda-webfunction-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`FunctionArn`  <a name="FunctionArn-fn::getatt"></a>
Property description not available.

`State`  <a name="State-fn::getatt"></a>
Property description not available.

`StateReason`  <a name="StateReason-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.
