---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-pipelineexecution-usercontext.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::PipelineExecution UserContext
<a name="aws-properties-sagemaker-pipelineexecution-usercontext"></a>

Information about the user who created or modified a SageMaker resource.

## Syntax
<a name="aws-properties-sagemaker-pipelineexecution-usercontext-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-pipelineexecution-usercontext-syntax.json"></a>

```
{
  "[IamIdentity](#cfn-sagemaker-pipelineexecution-usercontext-iamidentity)" : {{IamIdentity}}
}
```

### YAML
<a name="aws-properties-sagemaker-pipelineexecution-usercontext-syntax.yaml"></a>

```
  [IamIdentity](#cfn-sagemaker-pipelineexecution-usercontext-iamidentity): {{
    IamIdentity}}
```

## Properties
<a name="aws-properties-sagemaker-pipelineexecution-usercontext-properties"></a>

`IamIdentity`  <a name="cfn-sagemaker-pipelineexecution-usercontext-iamidentity"></a>
The IAM Identity details associated with the user. These details are associated with model package groups, model packages, and project entities only.
*Required*: No
*Type*: [IamIdentity](aws-properties-sagemaker-pipelineexecution-iamidentity.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
