---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-guardrail-topicconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Guardrail TopicConfig
<a name="aws-properties-bedrock-guardrail-topicconfig"></a>

Details about topics for the guardrail to identify and deny.

## Syntax
<a name="aws-properties-bedrock-guardrail-topicconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-guardrail-topicconfig-syntax.json"></a>

```
{
  "[Definition](#cfn-bedrock-guardrail-topicconfig-definition)" : {{String}},
  "[Examples](#cfn-bedrock-guardrail-topicconfig-examples)" : {{[ String, ... ]}},
  "[InputAction](#cfn-bedrock-guardrail-topicconfig-inputaction)" : {{String}},
  "[InputEnabled](#cfn-bedrock-guardrail-topicconfig-inputenabled)" : {{Boolean}},
  "[Name](#cfn-bedrock-guardrail-topicconfig-name)" : {{String}},
  "[OutputAction](#cfn-bedrock-guardrail-topicconfig-outputaction)" : {{String}},
  "[OutputEnabled](#cfn-bedrock-guardrail-topicconfig-outputenabled)" : {{Boolean}},
  "[Type](#cfn-bedrock-guardrail-topicconfig-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-guardrail-topicconfig-syntax.yaml"></a>

```
  [Definition](#cfn-bedrock-guardrail-topicconfig-definition): {{String}}
  [Examples](#cfn-bedrock-guardrail-topicconfig-examples): {{
    - String}}
  [InputAction](#cfn-bedrock-guardrail-topicconfig-inputaction): {{String}}
  [InputEnabled](#cfn-bedrock-guardrail-topicconfig-inputenabled): {{Boolean}}
  [Name](#cfn-bedrock-guardrail-topicconfig-name): {{String}}
  [OutputAction](#cfn-bedrock-guardrail-topicconfig-outputaction): {{String}}
  [OutputEnabled](#cfn-bedrock-guardrail-topicconfig-outputenabled): {{Boolean}}
  [Type](#cfn-bedrock-guardrail-topicconfig-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-guardrail-topicconfig-properties"></a>

`Definition`  <a name="cfn-bedrock-guardrail-topicconfig-definition"></a>
A definition of the topic to deny.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Examples`  <a name="cfn-bedrock-guardrail-topicconfig-examples"></a>
A list of prompts, each of which is an example of a prompt that can be categorized as belonging to the topic.
*Required*: No
*Type*: Array of String
*Maximum*: `100`
*Minimum*: `1 | 0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputAction`  <a name="cfn-bedrock-guardrail-topicconfig-inputaction"></a>
Specifies the action to take when harmful content is detected in the input. Supported values include:
+ `BLOCK` – Block the content and replace it with blocked messaging.
+ `NONE` – Take no action but return detection information in the trace response.
*Required*: No
*Type*: String
*Allowed values*: `BLOCK | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputEnabled`  <a name="cfn-bedrock-guardrail-topicconfig-inputenabled"></a>
Specifies whether to enable guardrail evaluation on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-guardrail-topicconfig-name"></a>
The name of the topic to deny.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z-_ !?.]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputAction`  <a name="cfn-bedrock-guardrail-topicconfig-outputaction"></a>
Specifies the action to take when harmful content is detected in the output. Supported values include:
+ `BLOCK` – Block the content and replace it with blocked messaging.
+ `NONE` – Take no action but return detection information in the trace response.
*Required*: No
*Type*: String
*Allowed values*: `BLOCK | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputEnabled`  <a name="cfn-bedrock-guardrail-topicconfig-outputenabled"></a>
Specifies whether to enable guardrail evaluation on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-guardrail-topicconfig-type"></a>
Specifies to deny the topic.
*Required*: Yes
*Type*: String
*Allowed values*: `DENY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
