---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-deepgramspeechmodelconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot DeepgramSpeechModelConfig
<a name="aws-properties-lex-bot-deepgramspeechmodelconfig"></a>

Configuration settings for integrating Deepgram speech-to-text models with Amazon Lex.

## Syntax
<a name="aws-properties-lex-bot-deepgramspeechmodelconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-deepgramspeechmodelconfig-syntax.json"></a>

```
{
  "[ApiTokenSecretArn](#cfn-lex-bot-deepgramspeechmodelconfig-apitokensecretarn)" : {{String}},
  "[ModelId](#cfn-lex-bot-deepgramspeechmodelconfig-modelid)" : {{String}}
}
```

### YAML
<a name="aws-properties-lex-bot-deepgramspeechmodelconfig-syntax.yaml"></a>

```
  [ApiTokenSecretArn](#cfn-lex-bot-deepgramspeechmodelconfig-apitokensecretarn): {{String}}
  [ModelId](#cfn-lex-bot-deepgramspeechmodelconfig-modelid): {{String}}
```

## Properties
<a name="aws-properties-lex-bot-deepgramspeechmodelconfig-properties"></a>

`ApiTokenSecretArn`  <a name="cfn-lex-bot-deepgramspeechmodelconfig-apitokensecretarn"></a>
The Amazon Resource Name (ARN) of the Secrets Manager secret that contains the Deepgram API token.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[A-Za-z-]*:secretsmanager:[a-z0-9-]{1,20}:[0-9]{12}:secret:[A-Za-z0-9/_+=.@-]{1,512}-[A-Za-z0-9]{6}$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ModelId`  <a name="cfn-lex-bot-deepgramspeechmodelconfig-modelid"></a>
The identifier of the Deepgram speech-to-text model to use for processing speech input.
*Required*: No
*Type*: String
*Pattern*: `[A-Za-z0-9-_]+`
*Minimum*: `4`
*Maximum*: `32`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
