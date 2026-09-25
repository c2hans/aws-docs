---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-comprehend-entityrecognizer-entityrecognizerinputdataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::EntityRecognizer EntityRecognizerInputDataConfig
<a name="aws-properties-comprehend-entityrecognizer-entityrecognizerinputdataconfig"></a>

Specifies the format and location of the input data.

## Syntax
<a name="aws-properties-comprehend-entityrecognizer-entityrecognizerinputdataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-comprehend-entityrecognizer-entityrecognizerinputdataconfig-syntax.json"></a>

```
{
  "[Annotations](#cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-annotations)" : {{EntityRecognizerAnnotations}},
  "[AugmentedManifests](#cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-augmentedmanifests)" : {{[ AugmentedManifestsListItem, ... ]}},
  "[DataFormat](#cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-dataformat)" : {{String}},
  "[Documents](#cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-documents)" : {{EntityRecognizerDocuments}},
  "[EntityList](#cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-entitylist)" : {{EntityRecognizerEntityList}},
  "[EntityTypes](#cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-entitytypes)" : {{[ EntityTypesListItem, ... ]}}
}
```

### YAML
<a name="aws-properties-comprehend-entityrecognizer-entityrecognizerinputdataconfig-syntax.yaml"></a>

```
  [Annotations](#cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-annotations): {{
    EntityRecognizerAnnotations}}
  [AugmentedManifests](#cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-augmentedmanifests): {{
    - AugmentedManifestsListItem}}
  [DataFormat](#cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-dataformat): {{String}}
  [Documents](#cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-documents): {{
    EntityRecognizerDocuments}}
  [EntityList](#cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-entitylist): {{
    EntityRecognizerEntityList}}
  [EntityTypes](#cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-entitytypes): {{
    - EntityTypesListItem}}
```

## Properties
<a name="aws-properties-comprehend-entityrecognizer-entityrecognizerinputdataconfig-properties"></a>

`Annotations`  <a name="cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-annotations"></a>
The S3 location of the CSV file that annotates your training documents.
*Required*: No
*Type*: [EntityRecognizerAnnotations](aws-properties-comprehend-entityrecognizer-entityrecognizerannotations.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AugmentedManifests`  <a name="cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-augmentedmanifests"></a>
A list of augmented manifest files that provide training data for your custom model. An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth.
This parameter is required if you set `DataFormat` to `AUGMENTED_MANIFEST`.
*Required*: No
*Type*: Array of [AugmentedManifestsListItem](aws-properties-comprehend-entityrecognizer-augmentedmanifestslistitem.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DataFormat`  <a name="cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-dataformat"></a>
The format of your training data:
+ `COMPREHEND_CSV`: A CSV file that supplements your training documents. The CSV file contains information about the custom entities that your trained model will detect. The required format of the file depends on whether you are providing annotations or an entity list.

  If you use this value, you must provide your CSV file by using either the `Annotations` or `EntityList` parameters. You must provide your training documents by using the `Documents` parameter.
+ `AUGMENTED_MANIFEST`: A labeled dataset that is produced by Amazon SageMaker Ground Truth. This file is in JSON lines format. Each line is a complete JSON object that contains a training document and its labels. Each label annotates a named entity in the training document.

  If you use this value, you must provide the `AugmentedManifests` parameter in your request.
If you don't specify a value, Amazon Comprehend uses `COMPREHEND_CSV` as the default.
*Required*: No
*Type*: String
*Allowed values*: `COMPREHEND_CSV | AUGMENTED_MANIFEST`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Documents`  <a name="cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-documents"></a>
The S3 location of the folder that contains the training documents for your custom entity recognizer.
This parameter is required if you set `DataFormat` to `COMPREHEND_CSV`.
*Required*: No
*Type*: [EntityRecognizerDocuments](aws-properties-comprehend-entityrecognizer-entityrecognizerdocuments.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EntityList`  <a name="cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-entitylist"></a>
The S3 location of the CSV file that has the entity list for your custom entity recognizer.
*Required*: No
*Type*: [EntityRecognizerEntityList](aws-properties-comprehend-entityrecognizer-entityrecognizerentitylist.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EntityTypes`  <a name="cfn-comprehend-entityrecognizer-entityrecognizerinputdataconfig-entitytypes"></a>
The entity types in the labeled training data that Amazon Comprehend uses to train the custom entity recognizer. Any entity types that you don't specify are ignored.
A maximum of 25 entity types can be used at one time to train an entity recognizer. Entity types must not contain the following invalid characters: \\n (line break), \\\\n (escaped line break), \\r (carriage return), \\\\r (escaped carriage return), \\t (tab), \\\\t (escaped tab), space, and , (comma).
*Required*: Yes
*Type*: Array of [EntityTypesListItem](aws-properties-comprehend-entityrecognizer-entitytypeslistitem.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
