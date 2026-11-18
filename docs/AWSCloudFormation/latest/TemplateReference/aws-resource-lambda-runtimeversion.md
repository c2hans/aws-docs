---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-runtimeversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::RuntimeVersion
<a name="aws-resource-lambda-runtimeversion"></a>

<a name="aws-resource-lambda-runtimeversion-description"></a>The `AWS::Lambda::RuntimeVersion` resource Property description not available. for Lambda.

## Syntax
<a name="aws-resource-lambda-runtimeversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-runtimeversion-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::RuntimeVersion",
  "Properties" : {
      "[ImageUri](#cfn-lambda-runtimeversion-imageuri)" : {{String}},
      "[Name](#cfn-lambda-runtimeversion-name)" : {{String}},
      "[ReleaseNotes](#cfn-lambda-runtimeversion-releasenotes)" : {{String}},
      "[RuntimeName](#cfn-lambda-runtimeversion-runtimename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-lambda-runtimeversion-syntax.yaml"></a>

```
Type: AWS::Lambda::RuntimeVersion
Properties:
  [ImageUri](#cfn-lambda-runtimeversion-imageuri): {{String}}
  [Name](#cfn-lambda-runtimeversion-name): {{String}}
  [ReleaseNotes](#cfn-lambda-runtimeversion-releasenotes): {{String}}
  [RuntimeName](#cfn-lambda-runtimeversion-runtimename): {{String}}
```

## Properties
<a name="aws-resource-lambda-runtimeversion-properties"></a>

`ImageUri`  <a name="cfn-lambda-runtimeversion-imageuri"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-lambda-runtimeversion-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReleaseNotes`  <a name="cfn-lambda-runtimeversion-releasenotes"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeName`  <a name="cfn-lambda-runtimeversion-runtimename"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]$`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-lambda-runtimeversion-return-values"></a>

### Ref
<a name="aws-resource-lambda-runtimeversion-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-lambda-runtimeversion-return-values-fn--getatt"></a>

####
<a name="aws-resource-lambda-runtimeversion-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Created`  <a name="Created-fn::getatt"></a>
Property description not available.

`LastModified`  <a name="LastModified-fn::getatt"></a>
Property description not available.

`Platforms`  <a name="Platforms-fn::getatt"></a>
Property description not available.

`ResolvedUri`  <a name="ResolvedUri-fn::getatt"></a>
Property description not available.

`State`  <a name="State-fn::getatt"></a>
Property description not available.
