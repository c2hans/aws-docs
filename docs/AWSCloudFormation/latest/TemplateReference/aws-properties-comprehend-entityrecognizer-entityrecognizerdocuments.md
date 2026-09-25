---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-comprehend-entityrecognizer-entityrecognizerdocuments.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::EntityRecognizer EntityRecognizerDocuments
<a name="aws-properties-comprehend-entityrecognizer-entityrecognizerdocuments"></a>

Describes the training documents submitted with an entity recognizer.

## Syntax
<a name="aws-properties-comprehend-entityrecognizer-entityrecognizerdocuments-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-comprehend-entityrecognizer-entityrecognizerdocuments-syntax.json"></a>

```
{
  "[InputFormat](#cfn-comprehend-entityrecognizer-entityrecognizerdocuments-inputformat)" : {{String}},
  "[S3Uri](#cfn-comprehend-entityrecognizer-entityrecognizerdocuments-s3uri)" : {{String}},
  "[TestS3Uri](#cfn-comprehend-entityrecognizer-entityrecognizerdocuments-tests3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-comprehend-entityrecognizer-entityrecognizerdocuments-syntax.yaml"></a>

```
  [InputFormat](#cfn-comprehend-entityrecognizer-entityrecognizerdocuments-inputformat): {{String}}
  [S3Uri](#cfn-comprehend-entityrecognizer-entityrecognizerdocuments-s3uri): {{String}}
  [TestS3Uri](#cfn-comprehend-entityrecognizer-entityrecognizerdocuments-tests3uri): {{String}}
```

## Properties
<a name="aws-properties-comprehend-entityrecognizer-entityrecognizerdocuments-properties"></a>

`InputFormat`  <a name="cfn-comprehend-entityrecognizer-entityrecognizerdocuments-inputformat"></a>
 Specifies how the text in an input file should be processed. This is optional, and the default is ONE\_DOC\_PER\_LINE. ONE\_DOC\_PER\_FILE - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers. ONE\_DOC\_PER\_LINE - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
*Required*: No
*Type*: String
*Allowed values*: `ONE_DOC_PER_FILE | ONE_DOC_PER_LINE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Uri`  <a name="cfn-comprehend-entityrecognizer-entityrecognizerdocuments-s3uri"></a>
 Specifies the Amazon S3 location where the training documents for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.
*Required*: Yes
*Type*: String
*Pattern*: `^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TestS3Uri`  <a name="cfn-comprehend-entityrecognizer-entityrecognizerdocuments-tests3uri"></a>
 Specifies the Amazon S3 location where the test documents for an entity recognizer are located. The URI must be in the same AWS Region as the API endpoint that you are calling.
*Required*: No
*Type*: String
*Pattern*: `^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
