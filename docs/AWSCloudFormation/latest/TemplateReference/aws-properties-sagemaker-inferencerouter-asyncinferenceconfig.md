---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencerouter-asyncinferenceconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceRouter AsyncInferenceConfig

Specifies configuration for how an endpoint performs asynchronous inference.

## Syntax
<a name="aws-properties-sagemaker-inferencerouter-asyncinferenceconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencerouter-asyncinferenceconfig-syntax.json"></a>

```json
{
  "[ClientConfig](#cfn-sagemaker-inferencerouter-asyncinferenceconfig-clientconfig)" : {{AsyncInferenceClientConfig}},
  "[OutputConfig](#cfn-sagemaker-inferencerouter-asyncinferenceconfig-outputconfig)" : {{AsyncInferenceOutputConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencerouter-asyncinferenceconfig-syntax.yaml"></a>

```yaml
  [ClientConfig](#cfn-sagemaker-inferencerouter-asyncinferenceconfig-clientconfig): {{
    AsyncInferenceClientConfig}}
  [OutputConfig](#cfn-sagemaker-inferencerouter-asyncinferenceconfig-outputconfig): {{
    AsyncInferenceOutputConfig}}
```

## Properties
<a name="aws-properties-sagemaker-inferencerouter-asyncinferenceconfig-properties"></a>

`ClientConfig`  <a name="cfn-sagemaker-inferencerouter-asyncinferenceconfig-clientconfig"></a>
Configures the behavior of the client used by SageMaker to interact with the model container during asynchronous inference.
*Required*: No
*Type*: [AsyncInferenceClientConfig](aws-properties-sagemaker-inferencerouter-asyncinferenceclientconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputConfig`  <a name="cfn-sagemaker-inferencerouter-asyncinferenceconfig-outputconfig"></a>
Specifies the configuration for asynchronous inference invocation outputs.
*Required*: Yes
*Type*: [AsyncInferenceOutputConfig](aws-properties-sagemaker-inferencerouter-asyncinferenceoutputconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
