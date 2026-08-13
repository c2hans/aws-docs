---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-remotedebugconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob RemoteDebugConfig
<a name="aws-properties-sagemaker-trainingjob-remotedebugconfig"></a>

Configuration for remote debugging for the [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) API. To learn more about the remote debugging functionality of SageMaker, see [Access a training container through AWS Systems Manager (SSM) for remote debugging](https://docs.aws.amazon.com/sagemaker/latest/dg/train-remote-debugging.html).

## Syntax
<a name="aws-properties-sagemaker-trainingjob-remotedebugconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-remotedebugconfig-syntax.json"></a>

```
{
  "[EnableRemoteDebug](#cfn-sagemaker-trainingjob-remotedebugconfig-enableremotedebug)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-remotedebugconfig-syntax.yaml"></a>

```
  [EnableRemoteDebug](#cfn-sagemaker-trainingjob-remotedebugconfig-enableremotedebug): {{Boolean}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-remotedebugconfig-properties"></a>

`EnableRemoteDebug`  <a name="cfn-sagemaker-trainingjob-remotedebugconfig-enableremotedebug"></a>
If set to True, enables remote debugging.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
