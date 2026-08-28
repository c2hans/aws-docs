---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-captureoption.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig CaptureOption
<a name="aws-properties-sagemaker-endpointconfig-captureoption"></a>

Specifies whether the endpoint captures input data or output data.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-captureoption-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-captureoption-syntax.json"></a>

```
{
  "[CaptureMode](#cfn-sagemaker-endpointconfig-captureoption-capturemode)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-captureoption-syntax.yaml"></a>

```
  [CaptureMode](#cfn-sagemaker-endpointconfig-captureoption-capturemode): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-captureoption-properties"></a>

`CaptureMode`  <a name="cfn-sagemaker-endpointconfig-captureoption-capturemode"></a>
Specifies whether the endpoint captures input data or output data.
*Required*: Yes
*Type*: String
*Allowed values*: `Input | Output | InputAndOutput`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
