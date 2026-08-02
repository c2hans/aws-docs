---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-coderepository-gitconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::CodeRepository GitConfig
<a name="aws-properties-sagemaker-coderepository-gitconfig"></a>

Specifies configuration details for a Git repository in your AWS account.

## Syntax
<a name="aws-properties-sagemaker-coderepository-gitconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-coderepository-gitconfig-syntax.json"></a>

```
{
  "[Branch](#cfn-sagemaker-coderepository-gitconfig-branch)" : {{String}},
  "[RepositoryUrl](#cfn-sagemaker-coderepository-gitconfig-repositoryurl)" : {{String}},
  "[SecretArn](#cfn-sagemaker-coderepository-gitconfig-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-coderepository-gitconfig-syntax.yaml"></a>

```
  [Branch](#cfn-sagemaker-coderepository-gitconfig-branch): {{String}}
  [RepositoryUrl](#cfn-sagemaker-coderepository-gitconfig-repositoryurl): {{String}}
  [SecretArn](#cfn-sagemaker-coderepository-gitconfig-secretarn): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-coderepository-gitconfig-properties"></a>

`Branch`  <a name="cfn-sagemaker-coderepository-gitconfig-branch"></a>
The default branch for the Git repository.
*Required*: No
*Type*: String
*Pattern*: `[^ ~^:?*\[]+`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RepositoryUrl`  <a name="cfn-sagemaker-coderepository-gitconfig-repositoryurl"></a>
The URL where the Git repository is located.
*Required*: Yes
*Type*: String
*Pattern*: `https://([^/]+)/?.{3,1016}`
*Minimum*: `11`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecretArn`  <a name="cfn-sagemaker-coderepository-gitconfig-secretarn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the credentials used to access the git repository. The secret must have a staging label of `AWSCURRENT` and must be in the following format:
 `{"username": UserName, "password": Password}`
*Required*: No
*Type*: String
*Pattern*: `arn:aws[a-z\-]*:secretsmanager:[a-z0-9\-]*:[0-9]{12}:secret:.*`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
