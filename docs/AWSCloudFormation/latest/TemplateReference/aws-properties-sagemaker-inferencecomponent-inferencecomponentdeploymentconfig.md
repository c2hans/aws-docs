---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-inferencecomponent-inferencecomponentdeploymentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::InferenceComponent InferenceComponentDeploymentConfig
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentdeploymentconfig"></a>

The deployment configuration for an endpoint that hosts inference components. The configuration includes the desired deployment strategy and rollback settings.

## Syntax
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentdeploymentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentdeploymentconfig-syntax.json"></a>

```
{
  "[AutoRollbackConfiguration](#cfn-sagemaker-inferencecomponent-inferencecomponentdeploymentconfig-autorollbackconfiguration)" : {{AutoRollbackConfiguration}},
  "[RollingUpdatePolicy](#cfn-sagemaker-inferencecomponent-inferencecomponentdeploymentconfig-rollingupdatepolicy)" : {{InferenceComponentRollingUpdatePolicy}}
}
```

### YAML
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentdeploymentconfig-syntax.yaml"></a>

```
  [AutoRollbackConfiguration](#cfn-sagemaker-inferencecomponent-inferencecomponentdeploymentconfig-autorollbackconfiguration): {{
    AutoRollbackConfiguration}}
  [RollingUpdatePolicy](#cfn-sagemaker-inferencecomponent-inferencecomponentdeploymentconfig-rollingupdatepolicy): {{
    InferenceComponentRollingUpdatePolicy}}
```

## Properties
<a name="aws-properties-sagemaker-inferencecomponent-inferencecomponentdeploymentconfig-properties"></a>

`AutoRollbackConfiguration`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentdeploymentconfig-autorollbackconfiguration"></a>
Configuration for automatic rollback during inference component deployment.
*Required*: No
*Type*: [AutoRollbackConfiguration](aws-properties-sagemaker-inferencecomponent-autorollbackconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RollingUpdatePolicy`  <a name="cfn-sagemaker-inferencecomponent-inferencecomponentdeploymentconfig-rollingupdatepolicy"></a>
Specifies a rolling deployment strategy for updating a SageMaker AI endpoint.
*Required*: No
*Type*: [InferenceComponentRollingUpdatePolicy](aws-properties-sagemaker-inferencecomponent-inferencecomponentrollingupdatepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
