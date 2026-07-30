---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-promptversion-promptvariant.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::PromptVersion PromptVariant
<a name="aws-properties-bedrock-promptversion-promptvariant"></a>

Contains details about a variant of the prompt.

## Syntax
<a name="aws-properties-bedrock-promptversion-promptvariant-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-promptversion-promptvariant-syntax.json"></a>

```
{
  "[AdditionalModelRequestFields](#cfn-bedrock-promptversion-promptvariant-additionalmodelrequestfields)" : {{Json}},
  "[GenAiResource](#cfn-bedrock-promptversion-promptvariant-genairesource)" : {{PromptGenAiResource}},
  "[InferenceConfiguration](#cfn-bedrock-promptversion-promptvariant-inferenceconfiguration)" : {{PromptInferenceConfiguration}},
  "[Metadata](#cfn-bedrock-promptversion-promptvariant-metadata)" : {{[ PromptMetadataEntry, ... ]}},
  "[ModelId](#cfn-bedrock-promptversion-promptvariant-modelid)" : {{String}},
  "[Name](#cfn-bedrock-promptversion-promptvariant-name)" : {{String}},
  "[TemplateConfiguration](#cfn-bedrock-promptversion-promptvariant-templateconfiguration)" : {{PromptTemplateConfiguration}},
  "[TemplateType](#cfn-bedrock-promptversion-promptvariant-templatetype)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-promptversion-promptvariant-syntax.yaml"></a>

```
  [AdditionalModelRequestFields](#cfn-bedrock-promptversion-promptvariant-additionalmodelrequestfields): {{Json}}
  [GenAiResource](#cfn-bedrock-promptversion-promptvariant-genairesource): {{
    PromptGenAiResource}}
  [InferenceConfiguration](#cfn-bedrock-promptversion-promptvariant-inferenceconfiguration): {{
    PromptInferenceConfiguration}}
  [Metadata](#cfn-bedrock-promptversion-promptvariant-metadata): {{
    - PromptMetadataEntry}}
  [ModelId](#cfn-bedrock-promptversion-promptvariant-modelid): {{String}}
  [Name](#cfn-bedrock-promptversion-promptvariant-name): {{String}}
  [TemplateConfiguration](#cfn-bedrock-promptversion-promptvariant-templateconfiguration): {{
    PromptTemplateConfiguration}}
  [TemplateType](#cfn-bedrock-promptversion-promptvariant-templatetype): {{String}}
```

## Properties
<a name="aws-properties-bedrock-promptversion-promptvariant-properties"></a>

`AdditionalModelRequestFields`  <a name="cfn-bedrock-promptversion-promptvariant-additionalmodelrequestfields"></a>
Contains model-specific inference configurations that aren't in the `inferenceConfiguration` field. To see model-specific inference parameters, see [Inference request parameters and response fields for foundation models](https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters.html).
*Required*: No
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GenAiResource`  <a name="cfn-bedrock-promptversion-promptvariant-genairesource"></a>
Specifies a generative AI resource with which to use the prompt.
*Required*: No
*Type*: [PromptGenAiResource](aws-properties-bedrock-promptversion-promptgenairesource.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InferenceConfiguration`  <a name="cfn-bedrock-promptversion-promptvariant-inferenceconfiguration"></a>
Contains inference configurations for the prompt variant.
*Required*: No
*Type*: [PromptInferenceConfiguration](aws-properties-bedrock-promptversion-promptinferenceconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Metadata`  <a name="cfn-bedrock-promptversion-promptvariant-metadata"></a>
An array of objects, each containing a key-value pair that defines a metadata tag and value to attach to a prompt variant.
*Required*: No
*Type*: Array of [PromptMetadataEntry](aws-properties-bedrock-promptversion-promptmetadataentry.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelId`  <a name="cfn-bedrock-promptversion-promptvariant-modelid"></a>
The unique identifier of the model or [inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) with which to run inference on the prompt.
*Required*: No
*Type*: String
*Pattern*: `^(arn:aws(-[^:]{1,12})?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-promptversion-promptvariant-name"></a>
The name of the prompt variant.
*Required*: Yes
*Type*: String
*Pattern*: `^([0-9a-zA-Z][_-]?){1,100}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateConfiguration`  <a name="cfn-bedrock-promptversion-promptvariant-templateconfiguration"></a>
Contains configurations for the prompt template.
*Required*: Yes
*Type*: [PromptTemplateConfiguration](aws-properties-bedrock-promptversion-prompttemplateconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateType`  <a name="cfn-bedrock-promptversion-promptvariant-templatetype"></a>
The type of prompt template to use.
*Required*: Yes
*Type*: String
*Allowed values*: `TEXT | CHAT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
