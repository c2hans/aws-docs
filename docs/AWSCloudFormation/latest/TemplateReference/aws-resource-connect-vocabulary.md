---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-vocabulary.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::Vocabulary
<a name="aws-resource-connect-vocabulary"></a>

Creates a custom vocabulary associated with your Connect Customer instance. You can set a custom vocabulary to be your default vocabulary for a given language. Contact Lens for Connect Customer uses the default vocabulary in post-call and real-time contact analysis sessions for that language.

## Syntax
<a name="aws-resource-connect-vocabulary-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-vocabulary-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::Vocabulary",
  "Properties" : {
      "[Content](#cfn-connect-vocabulary-content)" : {{String}},
      "[InstanceId](#cfn-connect-vocabulary-instanceid)" : {{String}},
      "[LanguageCode](#cfn-connect-vocabulary-languagecode)" : {{String}},
      "[Tags](#cfn-connect-vocabulary-tags)" : {{[ Tag, ... ]}},
      "[VocabularyName](#cfn-connect-vocabulary-vocabularyname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-vocabulary-syntax.yaml"></a>

```
Type: AWS::Connect::Vocabulary
Properties:
  [Content](#cfn-connect-vocabulary-content): {{String}}
  [InstanceId](#cfn-connect-vocabulary-instanceid): {{String}}
  [LanguageCode](#cfn-connect-vocabulary-languagecode): {{String}}
  [Tags](#cfn-connect-vocabulary-tags): {{
    - Tag}}
  [VocabularyName](#cfn-connect-vocabulary-vocabularyname): {{String}}
```

## Properties
<a name="aws-resource-connect-vocabulary-properties"></a>

`Content`  <a name="cfn-connect-vocabulary-content"></a>
The content of the custom vocabulary in plain-text format with a table of values. Each row in the table represents a word or a phrase, described with `Phrase`, `IPA`, `SoundsLike`, and `DisplayAs` fields. Separate the fields with TAB characters. For more information, see [Create a custom vocabulary using a table](https://docs.aws.amazon.com/transcribe/latest/dg/custom-vocabulary.html#create-vocabulary-table).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `60000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceId`  <a name="cfn-connect-vocabulary-instanceid"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LanguageCode`  <a name="cfn-connect-vocabulary-languagecode"></a>
The language code of the vocabulary entries. For a list of languages and their corresponding language codes, see [What is Amazon Transcribe?](https://docs.aws.amazon.com/transcribe/latest/dg/transcribe-whatis.html)
*Required*: Yes
*Type*: String
*Allowed values*: `ar-AE | de-CH | de-DE | en-AB | en-AU | en-GB | en-IE | en-IN | en-US | en-WL | es-ES | es-US | fr-CA | fr-FR | hi-IN | it-IT | ja-JP | ko-KR | pt-BR | pt-PT | zh-CN | en-NZ | en-ZA | ca-ES | da-DK | fi-FI | id-ID | ms-MY | nl-NL | no-NO | pl-PL | sv-SE | tl-PH`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-connect-vocabulary-tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-vocabulary-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VocabularyName`  <a name="cfn-connect-vocabulary-vocabularyname"></a>
A unique name of the custom vocabulary.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-zA-Z._-]+$`
*Minimum*: `1`
*Maximum*: `140`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-connect-vocabulary-return-values"></a>

### Ref
<a name="aws-resource-connect-vocabulary-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-connect-vocabulary-return-values-fn--getatt"></a>

####
<a name="aws-resource-connect-vocabulary-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the custom vocabulary.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The timestamp when the custom vocabulary was last modified.

`State`  <a name="State-fn::getatt"></a>
The current state of the custom vocabulary.

`VocabularyId`  <a name="VocabularyId-fn::getatt"></a>
The identifier of the custom vocabulary.
