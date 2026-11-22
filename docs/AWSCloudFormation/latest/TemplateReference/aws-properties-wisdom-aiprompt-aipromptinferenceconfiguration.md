---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wisdom-aiprompt-aipromptinferenceconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Wisdom::AIPrompt AIPromptInferenceConfiguration

The configuration for inference parameters when using AI Prompts.

## Syntax
<a name="aws-properties-wisdom-aiprompt-aipromptinferenceconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wisdom-aiprompt-aipromptinferenceconfiguration-syntax.json"></a>

```json
{
  "[MaxTokensToSample](#cfn-wisdom-aiprompt-aipromptinferenceconfiguration-maxtokenstosample)" : {{Integer}},
  "[Temperature](#cfn-wisdom-aiprompt-aipromptinferenceconfiguration-temperature)" : {{Number}},
  "[TopK](#cfn-wisdom-aiprompt-aipromptinferenceconfiguration-topk)" : {{Integer}},
  "[TopP](#cfn-wisdom-aiprompt-aipromptinferenceconfiguration-topp)" : {{Number}}
}
```

### YAML
<a name="aws-properties-wisdom-aiprompt-aipromptinferenceconfiguration-syntax.yaml"></a>

```yaml
  [MaxTokensToSample](#cfn-wisdom-aiprompt-aipromptinferenceconfiguration-maxtokenstosample): {{Integer}}
  [Temperature](#cfn-wisdom-aiprompt-aipromptinferenceconfiguration-temperature): {{Number}}
  [TopK](#cfn-wisdom-aiprompt-aipromptinferenceconfiguration-topk): {{Integer}}
  [TopP](#cfn-wisdom-aiprompt-aipromptinferenceconfiguration-topp): {{Number}}
```

## Properties
<a name="aws-properties-wisdom-aiprompt-aipromptinferenceconfiguration-properties"></a>

`MaxTokensToSample`  <a name="cfn-wisdom-aiprompt-aipromptinferenceconfiguration-maxtokenstosample"></a>
The maximum number of tokens to generate in the response.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Temperature`  <a name="cfn-wisdom-aiprompt-aipromptinferenceconfiguration-temperature"></a>
The temperature setting for controlling randomness in the generated response.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopK`  <a name="cfn-wisdom-aiprompt-aipromptinferenceconfiguration-topk"></a>
The top-K sampling parameter for token selection.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TopP`  <a name="cfn-wisdom-aiprompt-aipromptinferenceconfiguration-topp"></a>
The top-P sampling parameter for nucleus sampling.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
