---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-guardrail-managedwordsconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Guardrail ManagedWordsConfig
<a name="aws-properties-bedrock-guardrail-managedwordsconfig"></a>

The managed word list to configure for the guardrail.

## Syntax
<a name="aws-properties-bedrock-guardrail-managedwordsconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-guardrail-managedwordsconfig-syntax.json"></a>

```
{
  "[InputAction](#cfn-bedrock-guardrail-managedwordsconfig-inputaction)" : {{String}},
  "[InputEnabled](#cfn-bedrock-guardrail-managedwordsconfig-inputenabled)" : {{Boolean}},
  "[OutputAction](#cfn-bedrock-guardrail-managedwordsconfig-outputaction)" : {{String}},
  "[OutputEnabled](#cfn-bedrock-guardrail-managedwordsconfig-outputenabled)" : {{Boolean}},
  "[Type](#cfn-bedrock-guardrail-managedwordsconfig-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-guardrail-managedwordsconfig-syntax.yaml"></a>

```
  [InputAction](#cfn-bedrock-guardrail-managedwordsconfig-inputaction): {{String}}
  [InputEnabled](#cfn-bedrock-guardrail-managedwordsconfig-inputenabled): {{Boolean}}
  [OutputAction](#cfn-bedrock-guardrail-managedwordsconfig-outputaction): {{String}}
  [OutputEnabled](#cfn-bedrock-guardrail-managedwordsconfig-outputenabled): {{Boolean}}
  [Type](#cfn-bedrock-guardrail-managedwordsconfig-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-guardrail-managedwordsconfig-properties"></a>

`InputAction`  <a name="cfn-bedrock-guardrail-managedwordsconfig-inputaction"></a>
Specifies the action to take when harmful content is detected in the input. Supported values include:
+ `BLOCK` – Block the content and replace it with blocked messaging.
+ `NONE` – Take no action but return detection information in the trace response.
*Required*: No
*Type*: String
*Allowed values*: `BLOCK | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputEnabled`  <a name="cfn-bedrock-guardrail-managedwordsconfig-inputenabled"></a>
Specifies whether to enable guardrail evaluation on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputAction`  <a name="cfn-bedrock-guardrail-managedwordsconfig-outputaction"></a>
Specifies the action to take when harmful content is detected in the output. Supported values include:
+ `BLOCK` – Block the content and replace it with blocked messaging.
+ `NONE` – Take no action but return detection information in the trace response.
*Required*: No
*Type*: String
*Allowed values*: `BLOCK | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputEnabled`  <a name="cfn-bedrock-guardrail-managedwordsconfig-outputenabled"></a>
Specifies whether to enable guardrail evaluation on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-guardrail-managedwordsconfig-type"></a>
The managed word type to configure for the guardrail.
*Required*: Yes
*Type*: String
*Allowed values*: `PROFANITY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
