---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-runtimealias.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::RuntimeAlias
<a name="aws-resource-lambda-runtimealias"></a>

<a name="aws-resource-lambda-runtimealias-description"></a>The `AWS::Lambda::RuntimeAlias` resource Property description not available. for Lambda.

## Syntax
<a name="aws-resource-lambda-runtimealias-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-runtimealias-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::RuntimeAlias",
  "Properties" : {
      "[Description](#cfn-lambda-runtimealias-description)" : {{String}},
      "[Name](#cfn-lambda-runtimealias-name)" : {{String}},
      "[ReleaseLifecycle](#cfn-lambda-runtimealias-releaselifecycle)" : {{ReleaseLifecycle}},
      "[RuntimeName](#cfn-lambda-runtimealias-runtimename)" : {{String}},
      "[RuntimeVersion](#cfn-lambda-runtimealias-runtimeversion)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-lambda-runtimealias-syntax.yaml"></a>

```
Type: AWS::Lambda::RuntimeAlias
Properties:
  [Description](#cfn-lambda-runtimealias-description): {{String}}
  [Name](#cfn-lambda-runtimealias-name): {{String}}
  [ReleaseLifecycle](#cfn-lambda-runtimealias-releaselifecycle): {{
    ReleaseLifecycle}}
  [RuntimeName](#cfn-lambda-runtimealias-runtimename): {{String}}
  [RuntimeVersion](#cfn-lambda-runtimealias-runtimeversion): {{String}}
```

## Properties
<a name="aws-resource-lambda-runtimealias-properties"></a>

`Description`  <a name="cfn-lambda-runtimealias-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-lambda-runtimealias-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReleaseLifecycle`  <a name="cfn-lambda-runtimealias-releaselifecycle"></a>
Property description not available.
*Required*: No
*Type*: [ReleaseLifecycle](aws-properties-lambda-runtimealias-releaselifecycle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeName`  <a name="cfn-lambda-runtimealias-runtimename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]$`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RuntimeVersion`  <a name="cfn-lambda-runtimealias-runtimeversion"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lambda-runtimealias-return-values"></a>

### Ref
<a name="aws-resource-lambda-runtimealias-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-lambda-runtimealias-return-values-fn--getatt"></a>

####
<a name="aws-resource-lambda-runtimealias-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Created`  <a name="Created-fn::getatt"></a>
Property description not available.

`LastModified`  <a name="LastModified-fn::getatt"></a>
Property description not available.

`RuntimeVersionArn`  <a name="RuntimeVersionArn-fn::getatt"></a>
Property description not available.

`State`  <a name="State-fn::getatt"></a>
Property description not available.
