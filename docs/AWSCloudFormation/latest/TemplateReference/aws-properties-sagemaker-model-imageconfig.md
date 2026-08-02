---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-model-imageconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Model ImageConfig
<a name="aws-properties-sagemaker-model-imageconfig"></a>

Specifies whether the model container is in Amazon ECR or a private Docker registry accessible from your Amazon Virtual Private Cloud (VPC).

## Syntax
<a name="aws-properties-sagemaker-model-imageconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-model-imageconfig-syntax.json"></a>

```
{
  "[RepositoryAccessMode](#cfn-sagemaker-model-imageconfig-repositoryaccessmode)" : {{String}},
  "[RepositoryAuthConfig](#cfn-sagemaker-model-imageconfig-repositoryauthconfig)" : {{RepositoryAuthConfig}}
}
```

### YAML
<a name="aws-properties-sagemaker-model-imageconfig-syntax.yaml"></a>

```
  [RepositoryAccessMode](#cfn-sagemaker-model-imageconfig-repositoryaccessmode): {{String}}
  [RepositoryAuthConfig](#cfn-sagemaker-model-imageconfig-repositoryauthconfig): {{
    RepositoryAuthConfig}}
```

## Properties
<a name="aws-properties-sagemaker-model-imageconfig-properties"></a>

`RepositoryAccessMode`  <a name="cfn-sagemaker-model-imageconfig-repositoryaccessmode"></a>
Set this to one of the following values:
+ `Platform` - The model image is hosted in Amazon ECR.
+ `Vpc` - The model image is hosted in a private Docker registry in your VPC.
*Required*: Yes
*Type*: String
*Allowed values*: `Platform | Vpc`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RepositoryAuthConfig`  <a name="cfn-sagemaker-model-imageconfig-repositoryauthconfig"></a>
(Optional) Specifies an authentication configuration for the private docker registry where your model image is hosted. Specify a value for this property only if you specified `Vpc` as the value for the `RepositoryAccessMode` field, and the private Docker registry where the model image is hosted requires authentication.
*Required*: No
*Type*: [RepositoryAuthConfig](aws-properties-sagemaker-model-repositoryauthconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
