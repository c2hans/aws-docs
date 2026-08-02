---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-space-coderepository.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Space CodeRepository
<a name="aws-properties-sagemaker-space-coderepository"></a>

A Git repository that SageMaker AI automatically displays to users for cloning in the JupyterServer application.

## Syntax
<a name="aws-properties-sagemaker-space-coderepository-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-space-coderepository-syntax.json"></a>

```
{
  "[RepositoryUrl](#cfn-sagemaker-space-coderepository-repositoryurl)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-space-coderepository-syntax.yaml"></a>

```
  [RepositoryUrl](#cfn-sagemaker-space-coderepository-repositoryurl): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-space-coderepository-properties"></a>

`RepositoryUrl`  <a name="cfn-sagemaker-space-coderepository-repositoryurl"></a>
The URL of the Git repository.
*Required*: Yes
*Type*: String
*Pattern*: `^https://([.\-_a-zA-Z0-9]+/?){3,1016}$`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
