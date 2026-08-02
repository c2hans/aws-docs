---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-model-modelaccessconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Model ModelAccessConfig
<a name="aws-properties-sagemaker-model-modelaccessconfig"></a>

The access configuration file to control access to the ML model. You can explicitly accept the model end-user license agreement (EULA) within the `ModelAccessConfig`.
+ If you are a Jumpstart user, see the [End-user license agreements](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-choose.html#jumpstart-foundation-models-choose-eula) section for more details on accepting the EULA.
+ If you are an AutoML user, see the *Optional Parameters* section of *Create an AutoML job to fine-tune text generation models using the API* for details on [How to set the EULA acceptance when fine-tuning a model using the AutoML API](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-create-experiment-finetune-llms.html#autopilot-llms-finetuning-api-optional-params).

## Syntax
<a name="aws-properties-sagemaker-model-modelaccessconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-model-modelaccessconfig-syntax.json"></a>

```
{
  "[AcceptEula](#cfn-sagemaker-model-modelaccessconfig-accepteula)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-sagemaker-model-modelaccessconfig-syntax.yaml"></a>

```
  [AcceptEula](#cfn-sagemaker-model-modelaccessconfig-accepteula): {{Boolean}}
```

## Properties
<a name="aws-properties-sagemaker-model-modelaccessconfig-properties"></a>

`AcceptEula`  <a name="cfn-sagemaker-model-modelaccessconfig-accepteula"></a>
Specifies agreement to the model end-user license agreement (EULA). The `AcceptEula` value must be explicitly defined as `True` in order to accept the EULA that this model requires. You are responsible for reviewing and complying with any applicable license terms and making sure they are acceptable for your use case before downloading or using a model.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
