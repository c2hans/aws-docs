---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferenceexperiment-capturecontenttypeheader.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceExperiment CaptureContentTypeHeader
<a name="aws-properties-sagemaker-inferenceexperiment-capturecontenttypeheader"></a>

Configuration specifying how to treat different headers. If no headers are specified Amazon SageMaker AI will by default base64 encode when capturing the data.

## Syntax
<a name="aws-properties-sagemaker-inferenceexperiment-capturecontenttypeheader-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferenceexperiment-capturecontenttypeheader-syntax.json"></a>

```
{
  "[CsvContentTypes](#cfn-sagemaker-inferenceexperiment-capturecontenttypeheader-csvcontenttypes)" : {{[ String, ... ]}},
  "[JsonContentTypes](#cfn-sagemaker-inferenceexperiment-capturecontenttypeheader-jsoncontenttypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferenceexperiment-capturecontenttypeheader-syntax.yaml"></a>

```
  [CsvContentTypes](#cfn-sagemaker-inferenceexperiment-capturecontenttypeheader-csvcontenttypes): {{
    - String}}
  [JsonContentTypes](#cfn-sagemaker-inferenceexperiment-capturecontenttypeheader-jsoncontenttypes): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-inferenceexperiment-capturecontenttypeheader-properties"></a>

`CsvContentTypes`  <a name="cfn-sagemaker-inferenceexperiment-capturecontenttypeheader-csvcontenttypes"></a>
The list of all content type headers that Amazon SageMaker AI will treat as CSV and capture accordingly.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `256 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JsonContentTypes`  <a name="cfn-sagemaker-inferenceexperiment-capturecontenttypeheader-jsoncontenttypes"></a>
The list of all content type headers that SageMaker AI will treat as JSON and capture accordingly.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `256 | 10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
