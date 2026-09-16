---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-aiworkloadconfig-workloadspec.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AIWorkloadConfig WorkloadSpec
<a name="aws-properties-sagemaker-aiworkloadconfig-workloadspec"></a>

The workload specification for benchmark tool configuration. Provide an inline YAML or JSON string.

## Syntax
<a name="aws-properties-sagemaker-aiworkloadconfig-workloadspec-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-aiworkloadconfig-workloadspec-syntax.json"></a>

```
{
  "[Inline](#cfn-sagemaker-aiworkloadconfig-workloadspec-inline)" : {{String}}
}
```

### YAML
<a name="aws-properties-sagemaker-aiworkloadconfig-workloadspec-syntax.yaml"></a>

```
  [Inline](#cfn-sagemaker-aiworkloadconfig-workloadspec-inline): {{String}}
```

## Properties
<a name="aws-properties-sagemaker-aiworkloadconfig-workloadspec-properties"></a>

`Inline`  <a name="cfn-sagemaker-aiworkloadconfig-workloadspec-inline"></a>
An inline YAML or JSON string that defines benchmark parameters.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
