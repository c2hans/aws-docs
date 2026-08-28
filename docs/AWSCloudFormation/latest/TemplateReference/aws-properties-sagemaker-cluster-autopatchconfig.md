---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-autopatchconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster AutoPatchConfig
<a name="aws-properties-sagemaker-cluster-autopatchconfig"></a>

<a name="aws-properties-sagemaker-cluster-autopatchconfig-description"></a>The `AutoPatchConfig` property type specifies Property description not available. for an [AWS::SageMaker::Cluster](aws-resource-sagemaker-cluster.md).

## Syntax
<a name="aws-properties-sagemaker-cluster-autopatchconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-autopatchconfig-syntax.json"></a>

```
{
  "[DeploymentConfig](#cfn-sagemaker-cluster-autopatchconfig-deploymentconfig)" : {{DeploymentConfig}},
  "[PatchingStrategy](#cfn-sagemaker-cluster-autopatchconfig-patchingstrategy)" : {{String}},
  "[PatchSchedule](#cfn-sagemaker-cluster-autopatchconfig-patchschedule)" : {{PatchSchedule}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-autopatchconfig-syntax.yaml"></a>

```
  [DeploymentConfig](#cfn-sagemaker-cluster-autopatchconfig-deploymentconfig): {{
    DeploymentConfig}}
  [PatchingStrategy](#cfn-sagemaker-cluster-autopatchconfig-patchingstrategy): {{String}}
  [PatchSchedule](#cfn-sagemaker-cluster-autopatchconfig-patchschedule): {{
    PatchSchedule}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-autopatchconfig-properties"></a>

`DeploymentConfig`  <a name="cfn-sagemaker-cluster-autopatchconfig-deploymentconfig"></a>
Property description not available.
*Required*: No
*Type*: [DeploymentConfig](aws-properties-sagemaker-cluster-deploymentconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PatchingStrategy`  <a name="cfn-sagemaker-cluster-autopatchconfig-patchingstrategy"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `WhenIdle | WhenAllIdle`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PatchSchedule`  <a name="cfn-sagemaker-cluster-autopatchconfig-patchschedule"></a>
Property description not available.
*Required*: No
*Type*: [PatchSchedule](aws-properties-sagemaker-cluster-patchschedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
