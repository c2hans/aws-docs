---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-modelcard-securityconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::ModelCard SecurityConfig
<a name="aws-properties-sagemaker-modelcard-securityconfig"></a>

The security configuration used to protect model card data.

## Syntax
<a name="aws-properties-sagemaker-modelcard-securityconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-modelcard-securityconfig-syntax.json"></a>

```
{
  "[KmsKeyId](#cfn-sagemaker-modelcard-securityconfig-kmskeyid)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-modelcard-securityconfig-syntax.yaml"></a>

```
  [KmsKeyId](#cfn-sagemaker-modelcard-securityconfig-kmskeyid): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-modelcard-securityconfig-properties"></a>

`KmsKeyId`  <a name="cfn-sagemaker-modelcard-securityconfig-kmskeyid"></a>
A AWS Key Management Service[key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id) used to encrypt a model card.
*Required*: No
*Type*: String
*Pattern*: `.*`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
