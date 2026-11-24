---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencerouter-asyncinferenceclientconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceRouter AsyncInferenceClientConfig

Configures the behavior of the client used by SageMaker to interact with the model container during asynchronous inference.

## Syntax
<a name="aws-properties-sagemaker-inferencerouter-asyncinferenceclientconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencerouter-asyncinferenceclientconfig-syntax.json"></a>

```json
{
  "[MaxTimeInBacklogSeconds](#cfn-sagemaker-inferencerouter-asyncinferenceclientconfig-maxtimeinbacklogseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencerouter-asyncinferenceclientconfig-syntax.yaml"></a>

```yaml
  [MaxTimeInBacklogSeconds](#cfn-sagemaker-inferencerouter-asyncinferenceclientconfig-maxtimeinbacklogseconds): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-inferencerouter-asyncinferenceclientconfig-properties"></a>

`MaxTimeInBacklogSeconds`  <a name="cfn-sagemaker-inferencerouter-asyncinferenceclientconfig-maxtimeinbacklogseconds"></a>
Property description not available.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `21600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
