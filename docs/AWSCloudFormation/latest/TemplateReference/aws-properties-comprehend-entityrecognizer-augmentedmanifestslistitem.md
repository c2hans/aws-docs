---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-comprehend-entityrecognizer-augmentedmanifestslistitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::EntityRecognizer AugmentedManifestsListItem
<a name="aws-properties-comprehend-entityrecognizer-augmentedmanifestslistitem"></a>

An augmented manifest file that provides training data for your custom model. An augmented manifest file is a labeled dataset that is produced by Amazon SageMaker Ground Truth.

## Syntax
<a name="aws-properties-comprehend-entityrecognizer-augmentedmanifestslistitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-comprehend-entityrecognizer-augmentedmanifestslistitem-syntax.json"></a>

```
{
  "[AnnotationDataS3Uri](#cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-annotationdatas3uri)" : {{String}},
  "[AttributeNames](#cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-attributenames)" : {{[ String, ... ]}},
  "[DocumentType](#cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-documenttype)" : {{String}},
  "[S3Uri](#cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-s3uri)" : {{String}},
  "[SourceDocumentsS3Uri](#cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-sourcedocumentss3uri)" : {{String}},
  "[Split](#cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-split)" : {{String}}
}
```

### YAML
<a name="aws-properties-comprehend-entityrecognizer-augmentedmanifestslistitem-syntax.yaml"></a>

```
  [AnnotationDataS3Uri](#cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-annotationdatas3uri): {{String}}
  [AttributeNames](#cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-attributenames): {{
    - String}}
  [DocumentType](#cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-documenttype): {{String}}
  [S3Uri](#cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-s3uri): {{String}}
  [SourceDocumentsS3Uri](#cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-sourcedocumentss3uri): {{String}}
  [Split](#cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-split): {{String}}
```

## Properties
<a name="aws-properties-comprehend-entityrecognizer-augmentedmanifestslistitem-properties"></a>

`AnnotationDataS3Uri`  <a name="cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-annotationdatas3uri"></a>
The S3 prefix to the annotation files that are referred in the augmented manifest file.
*Required*: No
*Type*: String
*Pattern*: `^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AttributeNames`  <a name="cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-attributenames"></a>
The JSON attribute that contains the annotations for your training documents. The number of attribute names that you specify depends on whether your augmented manifest file is the output of a single labeling job or a chained labeling job.
If your file is the output of a single labeling job, specify the LabelAttributeName key that was used when the job was created in Ground Truth.
If your file is the output of a chained labeling job, specify the LabelAttributeName key for one or more jobs in the chain. Each LabelAttributeName key provides the annotations from an individual job.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DocumentType`  <a name="cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-documenttype"></a>
The type of augmented manifest. PlainTextDocument or SemiStructuredDocument. If you don't specify, the default is PlainTextDocument.
+ `PLAIN_TEXT_DOCUMENT` A document type that represents any unicode text that is encoded in UTF-8.
+ `SEMI_STRUCTURED_DOCUMENT` A document type with positional and structural context, like a PDF. For training with Amazon Comprehend, only PDFs are supported. For inference, Amazon Comprehend support PDFs, DOCX and TXT.
*Required*: No
*Type*: String
*Allowed values*: `PLAIN_TEXT_DOCUMENT | SEMI_STRUCTURED_DOCUMENT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Uri`  <a name="cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-s3uri"></a>
The Amazon S3 location of the augmented manifest file.
*Required*: Yes
*Type*: String
*Pattern*: `^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceDocumentsS3Uri`  <a name="cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-sourcedocumentss3uri"></a>
The S3 prefix to the source files (PDFs) that are referred to in the augmented manifest file.
*Required*: No
*Type*: String
*Pattern*: `^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Split`  <a name="cfn-comprehend-entityrecognizer-augmentedmanifestslistitem-split"></a>
The purpose of the data you've provided in the augmented manifest. You can either train or test this data. If you don't specify, the default is train.
TRAIN - all of the documents in the manifest will be used for training. If no test documents are provided, Amazon Comprehend will automatically reserve a portion of the training documents for testing.
 TEST - all of the documents in the manifest will be used for testing.
*Required*: No
*Type*: String
*Allowed values*: `TRAIN | TEST`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
