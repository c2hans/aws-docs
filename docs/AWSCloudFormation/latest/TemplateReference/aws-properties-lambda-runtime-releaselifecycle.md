---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-runtime-releaselifecycle.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::Runtime ReleaseLifecycle

The runtime lifecycle for the runtime or alias. Optional. Used to schedule runtime deprecation. Omitting or providing an empty object removes the existing lifecycle.

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
The date (UTC) on which the runtime or alias becomes deprecated.
*Required*: No
*Type*: String
*Pattern*: `^\d{4}-\d{2}-\d{2}$`
*Minimum*: `10`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionCreateBlockDate`  <a name="cfn-lambda-runtime-releaselifecycle-functioncreateblockdate"></a>
The date (UTC) on which creating new functions that use this runtime or alias is blocked.
*Required*: No
*Type*: String
*Pattern*: `^\d{4}-\d{2}-\d{2}$`
*Minimum*: `10`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionUpdateBlockDate`  <a name="cfn-lambda-runtime-releaselifecycle-functionupdateblockdate"></a>
The date (UTC) on which updating existing functions that use this runtime or alias is blocked.
*Required*: No
*Type*: String
*Pattern*: `^\d{4}-\d{2}-\d{2}$`
*Minimum*: `10`
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReleaseState`  <a name="cfn-lambda-runtime-releaselifecycle-releasestate"></a>
Optional, with no default applied. DEPRECATED requires a DeprecationDate on or before today (UTC); PREVIEW and GA require a later one, or none. Reads report DEPRECATED once DeprecationDate is reached.
*Required*: No
*Type*: String
*Allowed values*: `PREVIEW | GA | DEPRECATED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
