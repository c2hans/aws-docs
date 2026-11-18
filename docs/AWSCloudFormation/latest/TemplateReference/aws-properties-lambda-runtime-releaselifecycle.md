---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-runtime-releaselifecycle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Runtime ReleaseLifecycle
<a name="aws-properties-lambda-runtime-releaselifecycle"></a>

<a name="aws-properties-lambda-runtime-releaselifecycle-description"></a>The `ReleaseLifecycle` property type specifies Property description not available. for an [AWS::Lambda::Runtime](aws-resource-lambda-runtime.md).

## Syntax
<a name="aws-properties-lambda-runtime-releaselifecycle-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-runtime-releaselifecycle-syntax.json"></a>

```
{
  "[DeprecationDate](#cfn-lambda-runtime-releaselifecycle-deprecationdate)" : {{String}},
  "[FunctionCreateBlockDate](#cfn-lambda-runtime-releaselifecycle-functioncreateblockdate)" : {{String}},
  "[FunctionUpdateBlockDate](#cfn-lambda-runtime-releaselifecycle-functionupdateblockdate)" : {{String}},
  "[ReleaseState](#cfn-lambda-runtime-releaselifecycle-releasestate)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-runtime-releaselifecycle-syntax.yaml"></a>

```
  [DeprecationDate](#cfn-lambda-runtime-releaselifecycle-deprecationdate): {{String}}
  [FunctionCreateBlockDate](#cfn-lambda-runtime-releaselifecycle-functioncreateblockdate): {{String}}
  [FunctionUpdateBlockDate](#cfn-lambda-runtime-releaselifecycle-functionupdateblockdate): {{String}}
  [ReleaseState](#cfn-lambda-runtime-releaselifecycle-releasestate): {{String}}
```

## Properties
<a name="aws-properties-lambda-runtime-releaselifecycle-properties"></a>

`DeprecationDate`  <a name="cfn-lambda-runtime-releaselifecycle-deprecationdate"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^\d{4}-\d{2}-\d{2}$`
*Minimum*: `10`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionCreateBlockDate`  <a name="cfn-lambda-runtime-releaselifecycle-functioncreateblockdate"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^\d{4}-\d{2}-\d{2}$`
*Minimum*: `10`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionUpdateBlockDate`  <a name="cfn-lambda-runtime-releaselifecycle-functionupdateblockdate"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^\d{4}-\d{2}-\d{2}$`
*Minimum*: `10`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReleaseState`  <a name="cfn-lambda-runtime-releaselifecycle-releasestate"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `PREVIEW | GA | DEPRECATED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
