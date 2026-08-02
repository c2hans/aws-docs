---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-project-cfnstackparameter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Project CfnStackParameter
<a name="aws-properties-sagemaker-project-cfnstackparameter"></a>

 A key-value pair representing a parameter used in the CloudFormation stack.

## Syntax
<a name="aws-properties-sagemaker-project-cfnstackparameter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-project-cfnstackparameter-syntax.json"></a>

```
{
  "[Key](#cfn-sagemaker-project-cfnstackparameter-key)" : {{String}},
  "[Value](#cfn-sagemaker-project-cfnstackparameter-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-project-cfnstackparameter-syntax.yaml"></a>

```
  [Key](#cfn-sagemaker-project-cfnstackparameter-key): {{String}}
  [Value](#cfn-sagemaker-project-cfnstackparameter-value): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-project-cfnstackparameter-properties"></a>

`Key`  <a name="cfn-sagemaker-project-cfnstackparameter-key"></a>
 The name of the CloudFormation parameter.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Value`  <a name="cfn-sagemaker-project-cfnstackparameter-value"></a>
 The value of the CloudFormation parameter.
*Required*: Yes
*Type*: String
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
