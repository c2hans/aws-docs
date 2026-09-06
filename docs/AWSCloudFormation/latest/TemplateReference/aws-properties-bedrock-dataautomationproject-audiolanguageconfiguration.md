---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-dataautomationproject-audiolanguageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataAutomationProject AudioLanguageConfiguration
<a name="aws-properties-bedrock-dataautomationproject-audiolanguageconfiguration"></a>

This allows you to set the input and output language of your audio. The input language can be set to any of the languages supported by Bedrock Data Automation. The output can either be set to english or whatever the dominant language is of the audio, determined by the language spoken for the most seconds.

## Syntax
<a name="aws-properties-bedrock-dataautomationproject-audiolanguageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-dataautomationproject-audiolanguageconfiguration-syntax.json"></a>

```
{
  "[GenerativeOutputLanguage](#cfn-bedrock-dataautomationproject-audiolanguageconfiguration-generativeoutputlanguage)" : {{String}},
  "[IdentifyMultipleLanguages](#cfn-bedrock-dataautomationproject-audiolanguageconfiguration-identifymultiplelanguages)" : {{Boolean}},
  "[InputLanguages](#cfn-bedrock-dataautomationproject-audiolanguageconfiguration-inputlanguages)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-bedrock-dataautomationproject-audiolanguageconfiguration-syntax.yaml"></a>

```
  [GenerativeOutputLanguage](#cfn-bedrock-dataautomationproject-audiolanguageconfiguration-generativeoutputlanguage): {{String}}
  [IdentifyMultipleLanguages](#cfn-bedrock-dataautomationproject-audiolanguageconfiguration-identifymultiplelanguages): {{Boolean}}
  [InputLanguages](#cfn-bedrock-dataautomationproject-audiolanguageconfiguration-inputlanguages): {{
    - String}}
```

## Properties
<a name="aws-properties-bedrock-dataautomationproject-audiolanguageconfiguration-properties"></a>

`GenerativeOutputLanguage`  <a name="cfn-bedrock-dataautomationproject-audiolanguageconfiguration-generativeoutputlanguage"></a>
The output language of your processing results. This can either be set to `EN` (English) or `DEFAULT` which will output the results in the dominant language of the audio. The dominant language is determined as the language in the audio, spoken the longest in the input audio.
*Required*: No
*Type*: String
*Allowed values*: `DEFAULT | EN`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentifyMultipleLanguages`  <a name="cfn-bedrock-dataautomationproject-audiolanguageconfiguration-identifymultiplelanguages"></a>
The toggle determining if you want to detect multiple languages from your audio.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InputLanguages`  <a name="cfn-bedrock-dataautomationproject-audiolanguageconfiguration-inputlanguages"></a>
The input language of your audio. This can be set to any of the currently supported languages via the language codes.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
