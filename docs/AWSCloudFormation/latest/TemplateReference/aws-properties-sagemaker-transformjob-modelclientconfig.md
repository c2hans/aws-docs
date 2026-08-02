---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-transformjob-modelclientconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TransformJob ModelClientConfig
<a name="aws-properties-sagemaker-transformjob-modelclientconfig"></a>

Configures the timeout and maximum number of retries for processing a transform job invocation.

## Syntax
<a name="aws-properties-sagemaker-transformjob-modelclientconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-transformjob-modelclientconfig-syntax.json"></a>

```
{
  "[InvocationsMaxRetries](#cfn-sagemaker-transformjob-modelclientconfig-invocationsmaxretries)" : {{Integer}},
  "[InvocationsTimeoutInSeconds](#cfn-sagemaker-transformjob-modelclientconfig-invocationstimeoutinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-transformjob-modelclientconfig-syntax.yaml"></a>

```
  [InvocationsMaxRetries](#cfn-sagemaker-transformjob-modelclientconfig-invocationsmaxretries): {{Integer}}
  [InvocationsTimeoutInSeconds](#cfn-sagemaker-transformjob-modelclientconfig-invocationstimeoutinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-transformjob-modelclientconfig-properties"></a>

`InvocationsMaxRetries`  <a name="cfn-sagemaker-transformjob-modelclientconfig-invocationsmaxretries"></a>
The maximum number of retries when invocation requests are failing. The default value is 3.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InvocationsTimeoutInSeconds`  <a name="cfn-sagemaker-transformjob-modelclientconfig-invocationstimeoutinseconds"></a>
The timeout value in seconds for an invocation request. The default value is 600.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `3600`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
