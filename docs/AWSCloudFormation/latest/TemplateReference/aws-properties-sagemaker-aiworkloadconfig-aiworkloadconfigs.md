---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-aiworkloadconfig-aiworkloadconfigs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::AIWorkloadConfig AIWorkloadConfigs
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloadconfigs"></a>

The benchmark tool configuration for an AI workload.

## Syntax
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloadconfigs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloadconfigs-syntax.json"></a>

```
{
  "[WorkloadSpec](#cfn-sagemaker-aiworkloadconfig-aiworkloadconfigs-workloadspec)" : {{WorkloadSpec}}
}
```

### YAML
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloadconfigs-syntax.yaml"></a>

```
  [WorkloadSpec](#cfn-sagemaker-aiworkloadconfig-aiworkloadconfigs-workloadspec): {{
    WorkloadSpec}}
```

## Properties
<a name="aws-properties-sagemaker-aiworkloadconfig-aiworkloadconfigs-properties"></a>

`WorkloadSpec`  <a name="cfn-sagemaker-aiworkloadconfig-aiworkloadconfigs-workloadspec"></a>
The workload specification that defines benchmark parameters.
*Required*: Yes
*Type*: [WorkloadSpec](aws-properties-sagemaker-aiworkloadconfig-workloadspec.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
