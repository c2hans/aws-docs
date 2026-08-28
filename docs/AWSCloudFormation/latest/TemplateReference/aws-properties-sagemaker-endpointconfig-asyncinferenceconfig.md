---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpointconfig-asyncinferenceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::EndpointConfig AsyncInferenceConfig
<a name="aws-properties-sagemaker-endpointconfig-asyncinferenceconfig"></a>

Specifies configuration for how an endpoint performs asynchronous inference.

## Syntax
<a name="aws-properties-sagemaker-endpointconfig-asyncinferenceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpointconfig-asyncinferenceconfig-syntax.json"></a>

```
{
  "[ClientConfig](#cfn-sagemaker-endpointconfig-asyncinferenceconfig-clientconfig)" : {{AsyncInferenceClientConfig}},
  "[OutputConfig](#cfn-sagemaker-endpointconfig-asyncinferenceconfig-outputconfig)" : {{AsyncInferenceOutputConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpointconfig-asyncinferenceconfig-syntax.yaml"></a>

```
  [ClientConfig](#cfn-sagemaker-endpointconfig-asyncinferenceconfig-clientconfig): {{
    AsyncInferenceClientConfig}}
  [OutputConfig](#cfn-sagemaker-endpointconfig-asyncinferenceconfig-outputconfig): {{
    AsyncInferenceOutputConfig}}
```

## Properties
<a name="aws-properties-sagemaker-endpointconfig-asyncinferenceconfig-properties"></a>

`ClientConfig`  <a name="cfn-sagemaker-endpointconfig-asyncinferenceconfig-clientconfig"></a>
Configures the behavior of the client used by SageMaker to interact with the model container during asynchronous inference.
*Required*: No
*Type*: [AsyncInferenceClientConfig](aws-properties-sagemaker-endpointconfig-asyncinferenceclientconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputConfig`  <a name="cfn-sagemaker-endpointconfig-asyncinferenceconfig-outputconfig"></a>
Specifies the configuration for asynchronous inference invocation outputs.
*Required*: Yes
*Type*: [AsyncInferenceOutputConfig](aws-properties-sagemaker-endpointconfig-asyncinferenceoutputconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
