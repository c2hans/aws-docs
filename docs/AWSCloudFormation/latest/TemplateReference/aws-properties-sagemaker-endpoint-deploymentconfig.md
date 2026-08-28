---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-endpoint-deploymentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Endpoint DeploymentConfig
<a name="aws-properties-sagemaker-endpoint-deploymentconfig"></a>

The deployment configuration for an endpoint, which contains the desired deployment strategy and rollback configurations.

## Syntax
<a name="aws-properties-sagemaker-endpoint-deploymentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-endpoint-deploymentconfig-syntax.json"></a>

```
{
  "[AutoRollbackConfiguration](#cfn-sagemaker-endpoint-deploymentconfig-autorollbackconfiguration)" : {{AutoRollbackConfig}},
  "[BlueGreenUpdatePolicy](#cfn-sagemaker-endpoint-deploymentconfig-bluegreenupdatepolicy)" : {{BlueGreenUpdatePolicy}},
  "[RollingUpdatePolicy](#cfn-sagemaker-endpoint-deploymentconfig-rollingupdatepolicy)" : {{RollingUpdatePolicy}}
}
```

### YAML
<a name="aws-properties-sagemaker-endpoint-deploymentconfig-syntax.yaml"></a>

```
  [AutoRollbackConfiguration](#cfn-sagemaker-endpoint-deploymentconfig-autorollbackconfiguration): {{
    AutoRollbackConfig}}
  [BlueGreenUpdatePolicy](#cfn-sagemaker-endpoint-deploymentconfig-bluegreenupdatepolicy): {{
    BlueGreenUpdatePolicy}}
  [RollingUpdatePolicy](#cfn-sagemaker-endpoint-deploymentconfig-rollingupdatepolicy): {{
    RollingUpdatePolicy}}
```

## Properties
<a name="aws-properties-sagemaker-endpoint-deploymentconfig-properties"></a>

`AutoRollbackConfiguration`  <a name="cfn-sagemaker-endpoint-deploymentconfig-autorollbackconfiguration"></a>
Automatic rollback configuration for handling endpoint deployment failures and recovery.
*Required*: No
*Type*: [AutoRollbackConfig](aws-properties-sagemaker-endpoint-autorollbackconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlueGreenUpdatePolicy`  <a name="cfn-sagemaker-endpoint-deploymentconfig-bluegreenupdatepolicy"></a>
Update policy for a blue/green deployment. If this update policy is specified, SageMaker creates a new fleet during the deployment while maintaining the old fleet. SageMaker flips traffic to the new fleet according to the specified traffic routing configuration. Only one update policy should be used in the deployment configuration. If no update policy is specified, SageMaker uses a blue/green deployment strategy with all at once traffic shifting by default.
*Required*: No
*Type*: [BlueGreenUpdatePolicy](aws-properties-sagemaker-endpoint-bluegreenupdatepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RollingUpdatePolicy`  <a name="cfn-sagemaker-endpoint-deploymentconfig-rollingupdatepolicy"></a>
Specifies a rolling deployment strategy for updating a SageMaker endpoint.
*Required*: No
*Type*: [RollingUpdatePolicy](aws-properties-sagemaker-endpoint-rollingupdatepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
