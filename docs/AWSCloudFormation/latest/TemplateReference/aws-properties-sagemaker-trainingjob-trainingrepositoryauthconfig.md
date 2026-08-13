---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-trainingjob-trainingrepositoryauthconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::TrainingJob TrainingRepositoryAuthConfig
<a name="aws-properties-sagemaker-trainingjob-trainingrepositoryauthconfig"></a>

An object containing authentication information for a private Docker registry.

## Syntax
<a name="aws-properties-sagemaker-trainingjob-trainingrepositoryauthconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-trainingjob-trainingrepositoryauthconfig-syntax.json"></a>

```
{
  "[TrainingRepositoryCredentialsProviderArn](#cfn-sagemaker-trainingjob-trainingrepositoryauthconfig-trainingrepositorycredentialsproviderarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-trainingjob-trainingrepositoryauthconfig-syntax.yaml"></a>

```
  [TrainingRepositoryCredentialsProviderArn](#cfn-sagemaker-trainingjob-trainingrepositoryauthconfig-trainingrepositorycredentialsproviderarn): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-trainingjob-trainingrepositoryauthconfig-properties"></a>

`TrainingRepositoryCredentialsProviderArn`  <a name="cfn-sagemaker-trainingjob-trainingrepositoryauthconfig-trainingrepositorycredentialsproviderarn"></a>
The Amazon Resource Name (ARN) of an AWS Lambda function used to give SageMaker access credentials to your private Docker registry.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
