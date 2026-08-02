---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lex-bot-sampleutterancegenerationspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lex::Bot SampleUtteranceGenerationSpecification
<a name="aws-properties-lex-bot-sampleutterancegenerationspecification"></a>

Contains specifications for the sample utterance generation feature.

## Syntax
<a name="aws-properties-lex-bot-sampleutterancegenerationspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lex-bot-sampleutterancegenerationspecification-syntax.json"></a>

```
{
  "[BedrockModelSpecification](#cfn-lex-bot-sampleutterancegenerationspecification-bedrockmodelspecification)" : {{BedrockModelSpecification}},
  "[Enabled](#cfn-lex-bot-sampleutterancegenerationspecification-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-lex-bot-sampleutterancegenerationspecification-syntax.yaml"></a>

```
  [BedrockModelSpecification](#cfn-lex-bot-sampleutterancegenerationspecification-bedrockmodelspecification): {{
    BedrockModelSpecification}}
  [Enabled](#cfn-lex-bot-sampleutterancegenerationspecification-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-lex-bot-sampleutterancegenerationspecification-properties"></a>

`BedrockModelSpecification`  <a name="cfn-lex-bot-sampleutterancegenerationspecification-bedrockmodelspecification"></a>
Property description not available.
*Required*: No
*Type*: [BedrockModelSpecification](aws-properties-lex-bot-bedrockmodelspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-lex-bot-sampleutterancegenerationspecification-enabled"></a>
Specifies whether to enable sample utterance generation or not.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
