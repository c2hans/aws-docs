---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-model-repositoryauthconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Model RepositoryAuthConfig
<a name="aws-properties-sagemaker-model-repositoryauthconfig"></a>

Specifies an authentication configuration for the private docker registry where your model image is hosted. Specify a value for this property only if you specified `Vpc` as the value for the `RepositoryAccessMode` field of the `ImageConfig` object that you passed to a call to `CreateModel` and the private Docker registry where the model image is hosted requires authentication.

## Syntax
<a name="aws-properties-sagemaker-model-repositoryauthconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-model-repositoryauthconfig-syntax.json"></a>

```
{
  "[RepositoryCredentialsProviderArn](#cfn-sagemaker-model-repositoryauthconfig-repositorycredentialsproviderarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-model-repositoryauthconfig-syntax.yaml"></a>

```
  [RepositoryCredentialsProviderArn](#cfn-sagemaker-model-repositoryauthconfig-repositorycredentialsproviderarn): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-model-repositoryauthconfig-properties"></a>

`RepositoryCredentialsProviderArn`  <a name="cfn-sagemaker-model-repositoryauthconfig-repositorycredentialsproviderarn"></a>
The Amazon Resource Name (ARN) of an AWS Lambda function that provides credentials to authenticate to the private Docker registry where your model image is hosted. For information about how to create an AWS Lambda function, see [Create a Lambda function with the console](https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html) in the *AWS Lambda Developer Guide*.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
