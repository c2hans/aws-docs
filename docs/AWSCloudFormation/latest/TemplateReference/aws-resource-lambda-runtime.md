---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-runtime.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Runtime
<a name="aws-resource-lambda-runtime"></a>

Sets the runtime management configuration for a function's version. For more information, see [Runtime updates](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html).

## Syntax
<a name="aws-resource-lambda-runtime-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-runtime-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::Runtime",
  "Properties" : {
      "[Description](#cfn-lambda-runtime-description)" : {{String}},
      "[LicenseInfo](#cfn-lambda-runtime-licenseinfo)" : {{String}},
      "[Name](#cfn-lambda-runtime-name)" : {{String}},
      "[ReleaseLifecycle](#cfn-lambda-runtime-releaselifecycle)" : {{ReleaseLifecycle}},
      "[Tags](#cfn-lambda-runtime-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-lambda-runtime-syntax.yaml"></a>

```
Type: AWS::Lambda::Runtime
Properties:
  [Description](#cfn-lambda-runtime-description): {{String}}
  [LicenseInfo](#cfn-lambda-runtime-licenseinfo): {{String}}
  [Name](#cfn-lambda-runtime-name): {{String}}
  [ReleaseLifecycle](#cfn-lambda-runtime-releaselifecycle): {{
    ReleaseLifecycle}}
  [Tags](#cfn-lambda-runtime-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-lambda-runtime-properties"></a>

`Description`  <a name="cfn-lambda-runtime-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LicenseInfo`  <a name="cfn-lambda-runtime-licenseinfo"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-lambda-runtime-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]$`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReleaseLifecycle`  <a name="cfn-lambda-runtime-releaselifecycle"></a>
Property description not available.
*Required*: No
*Type*: [ReleaseLifecycle](aws-properties-lambda-runtime-releaselifecycle.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-lambda-runtime-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-lambda-runtime-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lambda-runtime-return-values"></a>

### Ref
<a name="aws-resource-lambda-runtime-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-lambda-runtime-return-values-fn--getatt"></a>

####
<a name="aws-resource-lambda-runtime-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Created`  <a name="Created-fn::getatt"></a>
Property description not available.

`LastModified`  <a name="LastModified-fn::getatt"></a>
Property description not available.

`State`  <a name="State-fn::getatt"></a>
Property description not available.
