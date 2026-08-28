---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-capturecontenttypeheader.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig CaptureContentTypeHeader
<a name="aws-properties-sagemaker-endpointconfig-capturecontenttypeheader"></a>

Specifies the JSON and CSV content types of the data that the endpoint captures.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-capturecontenttypeheader-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-capturecontenttypeheader-syntax.json"></a>

```
{
  "[CsvContentTypes](#cfn-sagemaker-endpointconfig-capturecontenttypeheader-csvcontenttypes)" : {{[ String, ... ]}},
  "[JsonContentTypes](#cfn-sagemaker-endpointconfig-capturecontenttypeheader-jsoncontenttypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-capturecontenttypeheader-syntax.yaml"></a>

```
  [CsvContentTypes](#cfn-sagemaker-endpointconfig-capturecontenttypeheader-csvcontenttypes): {{
    - String}}
  [JsonContentTypes](#cfn-sagemaker-endpointconfig-capturecontenttypeheader-jsoncontenttypes): {{
    - String}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-capturecontenttypeheader-properties"></a>

`CsvContentTypes`  <a name="cfn-sagemaker-endpointconfig-capturecontenttypeheader-csvcontenttypes"></a>
A list of the CSV content types of the data that the endpoint captures. For the endpoint to capture the data, you must also specify the content type when you invoke the endpoint.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JsonContentTypes`  <a name="cfn-sagemaker-endpointconfig-capturecontenttypeheader-jsoncontenttypes"></a>
A list of the JSON content types of the data that the endpoint captures. For the endpoint to capture the data, you must also specify the content type when you invoke the endpoint.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
