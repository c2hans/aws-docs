---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-guardrail-regexconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Guardrail RegexConfig
<a name="aws-properties-bedrock-guardrail-regexconfig"></a>

The regular expression to configure for the guardrail.

## Syntax
<a name="aws-properties-bedrock-guardrail-regexconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-guardrail-regexconfig-syntax.json"></a>

```
{
  "[Action](#cfn-bedrock-guardrail-regexconfig-action)" : {{String}},
  "[Description](#cfn-bedrock-guardrail-regexconfig-description)" : {{String}},
  "[InputAction](#cfn-bedrock-guardrail-regexconfig-inputaction)" : {{String}},
  "[InputEnabled](#cfn-bedrock-guardrail-regexconfig-inputenabled)" : {{Boolean}},
  "[Name](#cfn-bedrock-guardrail-regexconfig-name)" : {{String}},
  "[OutputAction](#cfn-bedrock-guardrail-regexconfig-outputaction)" : {{String}},
  "[OutputEnabled](#cfn-bedrock-guardrail-regexconfig-outputenabled)" : {{Boolean}},
  "[Pattern](#cfn-bedrock-guardrail-regexconfig-pattern)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-guardrail-regexconfig-syntax.yaml"></a>

```
  [Action](#cfn-bedrock-guardrail-regexconfig-action): {{String}}
  [Description](#cfn-bedrock-guardrail-regexconfig-description): {{String}}
  [InputAction](#cfn-bedrock-guardrail-regexconfig-inputaction): {{String}}
  [InputEnabled](#cfn-bedrock-guardrail-regexconfig-inputenabled): {{Boolean}}
  [Name](#cfn-bedrock-guardrail-regexconfig-name): {{String}}
  [OutputAction](#cfn-bedrock-guardrail-regexconfig-outputaction): {{String}}
  [OutputEnabled](#cfn-bedrock-guardrail-regexconfig-outputenabled): {{Boolean}}
  [Pattern](#cfn-bedrock-guardrail-regexconfig-pattern): {{String}}
```

## Properties
<a name="aws-properties-bedrock-guardrail-regexconfig-properties"></a>

`Action`  <a name="cfn-bedrock-guardrail-regexconfig-action"></a>
The guardrail action to configure when matching regular expression is detected.
*Required*: Yes
*Type*: String
*Allowed values*: `BLOCK | ANONYMIZE | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-bedrock-guardrail-regexconfig-description"></a>
The description of the regular expression to configure for the guardrail.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputAction`  <a name="cfn-bedrock-guardrail-regexconfig-inputaction"></a>
Specifies the action to take when harmful content is detected in the input. Supported values include:
+ `BLOCK` – Block the content and replace it with blocked messaging.
+ `NONE` – Take no action but return detection information in the trace response.
*Required*: No
*Type*: String
*Allowed values*: `BLOCK | ANONYMIZE | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputEnabled`  <a name="cfn-bedrock-guardrail-regexconfig-inputenabled"></a>
Specifies whether to enable guardrail evaluation on the input. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrock-guardrail-regexconfig-name"></a>
The name of the regular expression to configure for the guardrail.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputAction`  <a name="cfn-bedrock-guardrail-regexconfig-outputaction"></a>
Specifies the action to take when harmful content is detected in the output. Supported values include:
+ `BLOCK` – Block the content and replace it with blocked messaging.
+ `NONE` – Take no action but return detection information in the trace response.
*Required*: No
*Type*: String
*Allowed values*: `BLOCK | ANONYMIZE | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputEnabled`  <a name="cfn-bedrock-guardrail-regexconfig-outputenabled"></a>
Specifies whether to enable guardrail evaluation on the output. When disabled, you aren't charged for the evaluation. The evaluation doesn't appear in the response.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Pattern`  <a name="cfn-bedrock-guardrail-regexconfig-pattern"></a>
The regular expression pattern to configure for the guardrail.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
