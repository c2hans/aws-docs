---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-runtimeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Function RuntimeConfig
<a name="aws-properties-lambda-function-runtimeconfig"></a>

<a name="aws-properties-lambda-function-runtimeconfig-description"></a>The `RuntimeConfig` property type specifies Property description not available. for an [AWS::Lambda::Function](aws-resource-lambda-function.md).

## Syntax
<a name="aws-properties-lambda-function-runtimeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-function-runtimeconfig-syntax.json"></a>

```
{
  "[RuntimeAlias](#cfn-lambda-function-runtimeconfig-runtimealias)" : {{String}},
  "[RuntimeArn](#cfn-lambda-function-runtimeconfig-runtimearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-function-runtimeconfig-syntax.yaml"></a>

```
  [RuntimeAlias](#cfn-lambda-function-runtimeconfig-runtimealias): {{String}}
  [RuntimeArn](#cfn-lambda-function-runtimeconfig-runtimearn): {{String}}
```

## Properties
<a name="aws-properties-lambda-function-runtimeconfig-properties"></a>

`RuntimeAlias`  <a name="cfn-lambda-function-runtimeconfig-runtimealias"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?$`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeArn`  <a name="cfn-lambda-function-runtimeconfig-runtimearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z-]+:lambda:[a-z0-9-]+:\d{12}:runtime/.+$`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
