---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-guardrail-wordconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Guardrail WordConfig
<a name="aws-properties-bedrock-guardrail-wordconfig"></a>

A word to configure for the guardrail.

## Syntax
<a name="aws-properties-bedrock-guardrail-wordconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-guardrail-wordconfig-syntax.json"></a>

```
{
  "[InputAction](#cfn-bedrock-guardrail-wordconfig-inputaction)" : {{String}},
  "[InputEnabled](#cfn-bedrock-guardrail-wordconfig-inputenabled)" : {{Boolean}},
  "[OutputAction](#cfn-bedrock-guardrail-wordconfig-outputaction)" : {{String}},
  "[OutputEnabled](#cfn-bedrock-guardrail-wordconfig-outputenabled)" : {{Boolean}},
  "[Text](#cfn-bedrock-guardrail-wordconfig-text)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-guardrail-wordconfig-syntax.yaml"></a>

```
  [InputAction](#cfn-bedrock-guardrail-wordconfig-inputaction): {{String}}
  [InputEnabled](#cfn-bedrock-guardrail-wordconfig-inputenabled): {{Boolean}}
  [OutputAction](#cfn-bedrock-guardrail-wordconfig-outputaction): {{String}}
  [OutputEnabled](#cfn-bedrock-guardrail-wordconfig-outputenabled): {{Boolean}}
  [Text](#cfn-bedrock-guardrail-wordconfig-text): {{String}}
```

## Properties
<a name="aws-properties-bedrock-guardrail-wordconfig-properties"></a>

`InputAction`  <a name="cfn-bedrock-guardrail-wordconfig-inputaction"></a>
Specifies the action to take when harmful content is detected in the input. Supported values include:
+ `BLOCK` – Block the content and replace it with blocked messaging.
+ `NONE` – Take no action but return detection information in the trace response.
*Required*: No
*Type*: String
*Allowed values*: `BLOCK | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputEnabled`  <a name="cfn-bedrock-guardrail-wordconfig-inputenabled"></a>
Specifies whether to enable guardrail evaluation on the intput. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputAction`  <a name="cfn-bedrock-guardrail-wordconfig-outputaction"></a>
Specifies the action to take when harmful content is detected in the output. Supported values include:
+ `BLOCK` – Block the content and replace it with blocked messaging.
+ `NONE` – Take no action but return detection information in the trace response.
*Required*: No
*Type*: String
*Allowed values*: `BLOCK | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputEnabled`  <a name="cfn-bedrock-guardrail-wordconfig-outputenabled"></a>
Specifies whether to enable guardrail evaluation on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Text`  <a name="cfn-bedrock-guardrail-wordconfig-text"></a>
Text of the word configured for the guardrail to block.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
