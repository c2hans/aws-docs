---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-guardrail-contentfilterconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Guardrail ContentFilterConfig
<a name="aws-properties-bedrock-guardrail-contentfilterconfig"></a>

Contains filter strengths for harmful content. Guardrails support the following content filters to detect and filter harmful user inputs and FM-generated outputs.
+ **Hate** – Describes language or a statement that discriminates, criticizes, insults, denounces, or dehumanizes a person or group on the basis of an identity (such as race, ethnicity, gender, religion, sexual orientation, ability, and national origin).
+ **Insults** – Describes language or a statement that includes demeaning, humiliating, mocking, insulting, or belittling language. This type of language is also labeled as bullying.
+ **Sexual** – Describes language or a statement that indicates sexual interest, activity, or arousal using direct or indirect references to body parts, physical traits, or sex.
+ **Violence** – Describes language or a statement that includes glorification of or threats to inflict physical pain, hurt, or injury toward a person, group or thing.

Content filtering depends on the confidence classification of user inputs and FM responses across each of the four harmful categories. All input and output statements are classified into one of four confidence levels (NONE, LOW, MEDIUM, HIGH) for each harmful category. For example, if a statement is classified as *Hate* with HIGH confidence, the likelihood of the statement representing hateful content is high. A single statement can be classified across multiple categories with varying confidence levels. For example, a single statement can be classified as *Hate* with HIGH confidence, *Insults* with LOW confidence, *Sexual* with NONE confidence, and *Violence* with MEDIUM confidence.

For more information, see [Guardrails content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-filters.html).

## Syntax
<a name="aws-properties-bedrock-guardrail-contentfilterconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-guardrail-contentfilterconfig-syntax.json"></a>

```
{
  "[InputAction](#cfn-bedrock-guardrail-contentfilterconfig-inputaction)" : {{String}},
  "[InputEnabled](#cfn-bedrock-guardrail-contentfilterconfig-inputenabled)" : {{Boolean}},
  "[InputModalities](#cfn-bedrock-guardrail-contentfilterconfig-inputmodalities)" : {{[ String, ... ]}},
  "[InputStrength](#cfn-bedrock-guardrail-contentfilterconfig-inputstrength)" : {{String}},
  "[OutputAction](#cfn-bedrock-guardrail-contentfilterconfig-outputaction)" : {{String}},
  "[OutputEnabled](#cfn-bedrock-guardrail-contentfilterconfig-outputenabled)" : {{Boolean}},
  "[OutputModalities](#cfn-bedrock-guardrail-contentfilterconfig-outputmodalities)" : {{[ String, ... ]}},
  "[OutputStrength](#cfn-bedrock-guardrail-contentfilterconfig-outputstrength)" : {{String}},
  "[Type](#cfn-bedrock-guardrail-contentfilterconfig-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-guardrail-contentfilterconfig-syntax.yaml"></a>

```
  [InputAction](#cfn-bedrock-guardrail-contentfilterconfig-inputaction): {{String}}
  [InputEnabled](#cfn-bedrock-guardrail-contentfilterconfig-inputenabled): {{Boolean}}
  [InputModalities](#cfn-bedrock-guardrail-contentfilterconfig-inputmodalities): {{
    - String}}
  [InputStrength](#cfn-bedrock-guardrail-contentfilterconfig-inputstrength): {{String}}
  [OutputAction](#cfn-bedrock-guardrail-contentfilterconfig-outputaction): {{String}}
  [OutputEnabled](#cfn-bedrock-guardrail-contentfilterconfig-outputenabled): {{Boolean}}
  [OutputModalities](#cfn-bedrock-guardrail-contentfilterconfig-outputmodalities): {{
    - String}}
  [OutputStrength](#cfn-bedrock-guardrail-contentfilterconfig-outputstrength): {{String}}
  [Type](#cfn-bedrock-guardrail-contentfilterconfig-type): {{String}}
```

## Properties
<a name="aws-properties-bedrock-guardrail-contentfilterconfig-properties"></a>

`InputAction`  <a name="cfn-bedrock-guardrail-contentfilterconfig-inputaction"></a>
Specifies the action to take when harmful content is detected. Supported values include:
+ `BLOCK` – Block the content and replace it with blocked messaging.
+ `NONE` – Take no action but return detection information in the trace response.
*Required*: No
*Type*: String
*Allowed values*: `BLOCK | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputEnabled`  <a name="cfn-bedrock-guardrail-contentfilterconfig-inputenabled"></a>
Specifies whether to enable guardrail evaluation on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputModalities`  <a name="cfn-bedrock-guardrail-contentfilterconfig-inputmodalities"></a>
The input modalities selected for the guardrail content filter configuration.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputStrength`  <a name="cfn-bedrock-guardrail-contentfilterconfig-inputstrength"></a>
The strength of the content filter to apply to prompts. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | LOW | MEDIUM | HIGH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputAction`  <a name="cfn-bedrock-guardrail-contentfilterconfig-outputaction"></a>
Specifies the action to take when harmful content is detected in the output. Supported values include:
+ `BLOCK` – Block the content and replace it with blocked messaging.
+ `NONE` – Take no action but return detection information in the trace response.
*Required*: No
*Type*: String
*Allowed values*: `BLOCK | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputEnabled`  <a name="cfn-bedrock-guardrail-contentfilterconfig-outputenabled"></a>
Specifies whether to enable guardrail evaluation on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputModalities`  <a name="cfn-bedrock-guardrail-contentfilterconfig-outputmodalities"></a>
The output modalities selected for the guardrail content filter configuration.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputStrength`  <a name="cfn-bedrock-guardrail-contentfilterconfig-outputstrength"></a>
The strength of the content filter to apply to model responses. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your application reduces.
*Required*: Yes
*Type*: String
*Allowed values*: `NONE | LOW | MEDIUM | HIGH`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-bedrock-guardrail-contentfilterconfig-type"></a>
The harmful category that the content filter is applied to.
*Required*: Yes
*Type*: String
*Allowed values*: `SEXUAL | VIOLENCE | HATE | INSULTS | MISCONDUCT | PROMPT_ATTACK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
