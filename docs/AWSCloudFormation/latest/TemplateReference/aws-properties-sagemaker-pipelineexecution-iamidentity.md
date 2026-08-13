---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-pipelineexecution-iamidentity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::PipelineExecution IamIdentity
<a name="aws-properties-sagemaker-pipelineexecution-iamidentity"></a>

The IAM Identity details associated with the user. These details are associated with model package groups, model packages and project entities only.

## Syntax
<a name="aws-properties-sagemaker-pipelineexecution-iamidentity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-pipelineexecution-iamidentity-syntax.json"></a>

```
{
  "[Arn](#cfn-sagemaker-pipelineexecution-iamidentity-arn)" : {{String}},
  "[PrincipalId](#cfn-sagemaker-pipelineexecution-iamidentity-principalid)" : {{String}},
  "[SourceIdentity](#cfn-sagemaker-pipelineexecution-iamidentity-sourceidentity)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-pipelineexecution-iamidentity-syntax.yaml"></a>

```
  [Arn](#cfn-sagemaker-pipelineexecution-iamidentity-arn): {{String}}
  [PrincipalId](#cfn-sagemaker-pipelineexecution-iamidentity-principalid): {{String}}
  [SourceIdentity](#cfn-sagemaker-pipelineexecution-iamidentity-sourceidentity): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-pipelineexecution-iamidentity-properties"></a>

`Arn`  <a name="cfn-sagemaker-pipelineexecution-iamidentity-arn"></a>
The Amazon Resource Name (ARN) of the IAM identity.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrincipalId`  <a name="cfn-sagemaker-pipelineexecution-iamidentity-principalid"></a>
The ID of the principal that assumes the IAM identity.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourceIdentity`  <a name="cfn-sagemaker-pipelineexecution-iamidentity-sourceidentity"></a>
The person or application which assumes the IAM identity.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
