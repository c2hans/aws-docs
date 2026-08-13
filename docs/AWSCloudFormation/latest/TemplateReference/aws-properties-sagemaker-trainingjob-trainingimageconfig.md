---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-trainingimageconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob TrainingImageConfig
<a name="aws-properties-sagemaker-trainingjob-trainingimageconfig"></a>

The configuration to use an image from a private Docker registry for a training job.

## Syntax
<a name="aws-properties-sagemaker-trainingjob-trainingimageconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-trainingimageconfig-syntax.json"></a>

```
{
  "[TrainingRepositoryAccessMode](#cfn-sagemaker-trainingjob-trainingimageconfig-trainingrepositoryaccessmode)" : {{String}},
  "[TrainingRepositoryAuthConfig](#cfn-sagemaker-trainingjob-trainingimageconfig-trainingrepositoryauthconfig)" : {{TrainingRepositoryAuthConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-trainingimageconfig-syntax.yaml"></a>

```
  [TrainingRepositoryAccessMode](#cfn-sagemaker-trainingjob-trainingimageconfig-trainingrepositoryaccessmode): {{String}}
  [TrainingRepositoryAuthConfig](#cfn-sagemaker-trainingjob-trainingimageconfig-trainingrepositoryauthconfig): {{
    TrainingRepositoryAuthConfig}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-trainingimageconfig-properties"></a>

`TrainingRepositoryAccessMode`  <a name="cfn-sagemaker-trainingjob-trainingimageconfig-trainingrepositoryaccessmode"></a>
The method that your training job will use to gain access to the images in your private Docker registry. For access to an image in a private Docker registry, set to `Vpc`.
*Required*: Yes
*Type*: String
*Allowed values*: `Platform | Vpc`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TrainingRepositoryAuthConfig`  <a name="cfn-sagemaker-trainingjob-trainingimageconfig-trainingrepositoryauthconfig"></a>
An object containing authentication information for a private Docker registry containing your training images.
*Required*: No
*Type*: [TrainingRepositoryAuthConfig](aws-properties-sagemaker-trainingjob-trainingrepositoryauthconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
