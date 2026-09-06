---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-model-hubaccessconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Model HubAccessConfig
<a name="aws-properties-sagemaker-model-hubaccessconfig"></a>

The configuration for a private hub model reference that points to a public SageMaker JumpStart model.

For more information about private hubs, see [Private curated hubs for foundation model access control in JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-curated-hubs.html).

## Syntax
<a name="aws-properties-sagemaker-model-hubaccessconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-model-hubaccessconfig-syntax.json"></a>

```
{
  "[HubContentArn](#cfn-sagemaker-model-hubaccessconfig-hubcontentarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-model-hubaccessconfig-syntax.yaml"></a>

```
  [HubContentArn](#cfn-sagemaker-model-hubaccessconfig-hubcontentarn): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-model-hubaccessconfig-properties"></a>

`HubContentArn`  <a name="cfn-sagemaker-model-hubaccessconfig-hubcontentarn"></a>
The ARN of your private model hub content. This should be a `ModelReference` resource type that points to a SageMaker JumpStart public hub model.
*Required*: Yes
*Type*: String
*Pattern*: `.*`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
