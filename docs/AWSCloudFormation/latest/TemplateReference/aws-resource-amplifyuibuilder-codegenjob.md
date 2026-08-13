---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-amplifyuibuilder-codegenjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmplifyUIBuilder::CodegenJob
<a name="aws-resource-amplifyuibuilder-codegenjob"></a>

Describes the configuration for a code generation job that is associated with an Amplify app.

## Syntax
<a name="aws-resource-amplifyuibuilder-codegenjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-amplifyuibuilder-codegenjob-syntax.json"></a>

```
{
  "Type" : "AWS::AmplifyUIBuilder::CodegenJob",
  "Properties" : {
      "[AppId](#cfn-amplifyuibuilder-codegenjob-appid)" : {{String}},
      "[AutoGenerateForms](#cfn-amplifyuibuilder-codegenjob-autogenerateforms)" : {{Boolean}},
      "[EnvironmentName](#cfn-amplifyuibuilder-codegenjob-environmentname)" : {{String}},
      "[Features](#cfn-amplifyuibuilder-codegenjob-features)" : {{CodegenFeatureFlags}},
      "[RenderConfig](#cfn-amplifyuibuilder-codegenjob-renderconfig)" : {{CodegenJobRenderConfig}}
    }
}
```

### YAML
<a name="aws-resource-amplifyuibuilder-codegenjob-syntax.yaml"></a>

```
Type: AWS::AmplifyUIBuilder::CodegenJob
Properties:
  [AppId](#cfn-amplifyuibuilder-codegenjob-appid): {{String}}
  [AutoGenerateForms](#cfn-amplifyuibuilder-codegenjob-autogenerateforms): {{Boolean}}
  [EnvironmentName](#cfn-amplifyuibuilder-codegenjob-environmentname): {{String}}
  [Features](#cfn-amplifyuibuilder-codegenjob-features): {{
    CodegenFeatureFlags}}
  [RenderConfig](#cfn-amplifyuibuilder-codegenjob-renderconfig): {{
    CodegenJobRenderConfig}}
```

## Properties
<a name="aws-resource-amplifyuibuilder-codegenjob-properties"></a>

`AppId`  <a name="cfn-amplifyuibuilder-codegenjob-appid"></a>
The ID of the Amplify app associated with the code generation job.
*Required*: No
*Type*: String
*Pattern*: `^d[a-z0-9]+$`
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AutoGenerateForms`  <a name="cfn-amplifyuibuilder-codegenjob-autogenerateforms"></a>
Specifies whether to autogenerate forms in the code generation job.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EnvironmentName`  <a name="cfn-amplifyuibuilder-codegenjob-environmentname"></a>
The name of the backend environment associated with the code generation job.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Features`  <a name="cfn-amplifyuibuilder-codegenjob-features"></a>
The feature flags for a code generation job.
*Required*: No
*Type*: [CodegenFeatureFlags](aws-properties-amplifyuibuilder-codegenjob-codegenfeatureflags.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RenderConfig`  <a name="cfn-amplifyuibuilder-codegenjob-renderconfig"></a>
The code generation configuration for the codegen job.
*Required*: Yes
*Type*: [CodegenJobRenderConfig](aws-properties-amplifyuibuilder-codegenjob-codegenjobrenderconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-amplifyuibuilder-codegenjob-return-values"></a>

### Ref
<a name="aws-resource-amplifyuibuilder-codegenjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-amplifyuibuilder-codegenjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-amplifyuibuilder-codegenjob-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`Id`  <a name="Id-fn::getatt"></a>
The unique ID for the code generation job.

`Status`  <a name="Status-fn::getatt"></a>
The status of the code generation job.

`Tags`  <a name="Tags-fn::getatt"></a>
One or more key-value pairs to use when tagging the code generation job.
