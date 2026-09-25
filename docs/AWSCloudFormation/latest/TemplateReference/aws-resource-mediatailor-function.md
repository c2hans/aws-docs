---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-mediatailor-function.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Function
<a name="aws-resource-mediatailor-function"></a>

Defines reusable logic that MediaTailor executes at lifecycle hooks during ad insertion. The `FunctionType` determines the function's runtime behavior. For more information about functions, see [Working with functions](https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html) in the *MediaTailor User Guide*.

## Syntax
<a name="aws-resource-mediatailor-function-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-mediatailor-function-syntax.json"></a>

```
{
  "Type" : "AWS::MediaTailor::Function",
  "Properties" : {
      "[ConcurrentExecutorConfiguration](#cfn-mediatailor-function-concurrentexecutorconfiguration)" : {{ConcurrentExecutorConfiguration}},
      "[CustomOutputConfiguration](#cfn-mediatailor-function-customoutputconfiguration)" : {{CustomOutputConfiguration}},
      "[Description](#cfn-mediatailor-function-description)" : {{String}},
      "[FunctionId](#cfn-mediatailor-function-functionid)" : {{String}},
      "[FunctionType](#cfn-mediatailor-function-functiontype)" : {{String}},
      "[HttpRequestConfiguration](#cfn-mediatailor-function-httprequestconfiguration)" : {{HttpRequestConfiguration}},
      "[SequentialExecutorConfiguration](#cfn-mediatailor-function-sequentialexecutorconfiguration)" : {{SequentialExecutorConfiguration}},
      "[Tags](#cfn-mediatailor-function-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-mediatailor-function-syntax.yaml"></a>

```
Type: AWS::MediaTailor::Function
Properties:
  [ConcurrentExecutorConfiguration](#cfn-mediatailor-function-concurrentexecutorconfiguration): {{
    ConcurrentExecutorConfiguration}}
  [CustomOutputConfiguration](#cfn-mediatailor-function-customoutputconfiguration): {{
    CustomOutputConfiguration}}
  [Description](#cfn-mediatailor-function-description): {{String}}
  [FunctionId](#cfn-mediatailor-function-functionid): {{String}}
  [FunctionType](#cfn-mediatailor-function-functiontype): {{String}}
  [HttpRequestConfiguration](#cfn-mediatailor-function-httprequestconfiguration): {{
    HttpRequestConfiguration}}
  [SequentialExecutorConfiguration](#cfn-mediatailor-function-sequentialexecutorconfiguration): {{
    SequentialExecutorConfiguration}}
  [Tags](#cfn-mediatailor-function-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-mediatailor-function-properties"></a>

`ConcurrentExecutorConfiguration`  <a name="cfn-mediatailor-function-concurrentexecutorconfiguration"></a>
The configuration for a `CONCURRENT_EXECUTOR` function.
*Required*: No
*Type*: [ConcurrentExecutorConfiguration](aws-properties-mediatailor-function-concurrentexecutorconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomOutputConfiguration`  <a name="cfn-mediatailor-function-customoutputconfiguration"></a>
The configuration for a `CUSTOM_OUTPUT` function.
*Required*: No
*Type*: [CustomOutputConfiguration](aws-properties-mediatailor-function-customoutputconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-mediatailor-function-description"></a>
A description of the function.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FunctionId`  <a name="cfn-mediatailor-function-functionid"></a>
The identifier of the function.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FunctionType`  <a name="cfn-mediatailor-function-functiontype"></a>
The type of the function.
*Required*: Yes
*Type*: String
*Allowed values*: `HTTP_REQUEST | CUSTOM_OUTPUT | CONCURRENT_EXECUTOR | SEQUENTIAL_EXECUTOR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HttpRequestConfiguration`  <a name="cfn-mediatailor-function-httprequestconfiguration"></a>
The configuration for an `HTTP_REQUEST` function.
*Required*: No
*Type*: [HttpRequestConfiguration](aws-properties-mediatailor-function-httprequestconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SequentialExecutorConfiguration`  <a name="cfn-mediatailor-function-sequentialexecutorconfiguration"></a>
The configuration for a `SEQUENTIAL_EXECUTOR` function.
*Required*: No
*Type*: [SequentialExecutorConfiguration](aws-properties-mediatailor-function-sequentialexecutorconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-mediatailor-function-tags"></a>
The tags assigned to the function. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see [Tagging AWS Elemental MediaTailor Resources](https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-mediatailor-function-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-mediatailor-function-return-values"></a>

### Ref
<a name="aws-resource-mediatailor-function-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-mediatailor-function-return-values-fn--getatt"></a>

####
<a name="aws-resource-mediatailor-function-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the function.
