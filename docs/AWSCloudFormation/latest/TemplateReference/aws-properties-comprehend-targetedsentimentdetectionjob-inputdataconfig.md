---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-comprehend-targetedsentimentdetectionjob-inputdataconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::TargetedSentimentDetectionJob InputDataConfig
<a name="aws-properties-comprehend-targetedsentimentdetectionjob-inputdataconfig"></a>

The input properties for an inference job. The document reader config field applies only to non-text inputs for custom analysis.

## Syntax
<a name="aws-properties-comprehend-targetedsentimentdetectionjob-inputdataconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-comprehend-targetedsentimentdetectionjob-inputdataconfig-syntax.json"></a>

```
{
  "[InputFormat](#cfn-comprehend-targetedsentimentdetectionjob-inputdataconfig-inputformat)" : {{String}},
  "[S3Uri](#cfn-comprehend-targetedsentimentdetectionjob-inputdataconfig-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-comprehend-targetedsentimentdetectionjob-inputdataconfig-syntax.yaml"></a>

```
  [InputFormat](#cfn-comprehend-targetedsentimentdetectionjob-inputdataconfig-inputformat): {{String}}
  [S3Uri](#cfn-comprehend-targetedsentimentdetectionjob-inputdataconfig-s3uri): {{String}}
```

## Properties
<a name="aws-properties-comprehend-targetedsentimentdetectionjob-inputdataconfig-properties"></a>

`InputFormat`  <a name="cfn-comprehend-targetedsentimentdetectionjob-inputdataconfig-inputformat"></a>
Specifies how the text in an input file should be processed:
+ `ONE_DOC_PER_FILE` - Each file is considered a separate document. Use this option when you are processing large documents, such as newspaper articles or scientific papers.
+ `ONE_DOC_PER_LINE` - Each line in a file is considered a separate document. Use this option when you are processing many short documents, such as text messages.
*Required*: No
*Type*: String
*Allowed values*: `ONE_DOC_PER_FILE | ONE_DOC_PER_LINE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Uri`  <a name="cfn-comprehend-targetedsentimentdetectionjob-inputdataconfig-s3uri"></a>
The Amazon S3 URI for the input data. The URI must be in same Region as the API endpoint that you are calling. The URI can point to a single input file or it can provide the prefix for a collection of data files.
For example, if you use the URI `S3://bucketName/prefix`, if the prefix is a single file, Amazon Comprehend uses that file as input. If more than one file begins with the prefix, Amazon Comprehend uses all of them as input.
*Required*: Yes
*Type*: String
*Pattern*: `^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
