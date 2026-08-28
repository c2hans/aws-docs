---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferenceexperiment-datastorageconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceExperiment DataStorageConfig
<a name="aws-properties-sagemaker-inferenceexperiment-datastorageconfig"></a>

 The Amazon S3 location and configuration for storing inference request and response data.

 This is an optional parameter that you can use for data capture. For more information, see [Capture data](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html).

## Syntax
<a name="aws-properties-sagemaker-inferenceexperiment-datastorageconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferenceexperiment-datastorageconfig-syntax.json"></a>

```
{
  "[ContentType](#cfn-sagemaker-inferenceexperiment-datastorageconfig-contenttype)" : {{CaptureContentTypeHeader}},
  "[Destination](#cfn-sagemaker-inferenceexperiment-datastorageconfig-destination)" : {{String}},
  "[KmsKey](#cfn-sagemaker-inferenceexperiment-datastorageconfig-kmskey)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferenceexperiment-datastorageconfig-syntax.yaml"></a>

```
  [ContentType](#cfn-sagemaker-inferenceexperiment-datastorageconfig-contenttype): {{
    CaptureContentTypeHeader}}
  [Destination](#cfn-sagemaker-inferenceexperiment-datastorageconfig-destination): {{String}}
  [KmsKey](#cfn-sagemaker-inferenceexperiment-datastorageconfig-kmskey): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-inferenceexperiment-datastorageconfig-properties"></a>

`ContentType`  <a name="cfn-sagemaker-inferenceexperiment-datastorageconfig-contenttype"></a>
Configuration specifying how to treat different headers. If no headers are specified SageMaker will by default base64 encode when capturing the data.
*Required*: No
*Type*: [CaptureContentTypeHeader](aws-properties-sagemaker-inferenceexperiment-capturecontenttypeheader.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Destination`  <a name="cfn-sagemaker-inferenceexperiment-datastorageconfig-destination"></a>
The Amazon S3 bucket where the inference request and response data is stored.
*Required*: Yes
*Type*: String
*Pattern*: `^(https|s3)://([^/])/?(.*)$`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKey`  <a name="cfn-sagemaker-inferenceexperiment-datastorageconfig-kmskey"></a>
 The AWS Key Management Service key that Amazon SageMaker uses to encrypt captured data at rest using Amazon S3 server-side encryption.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
