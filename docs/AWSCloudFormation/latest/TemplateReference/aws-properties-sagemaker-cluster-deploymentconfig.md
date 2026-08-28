---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-sagemaker-cluster-deploymentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Cluster DeploymentConfig
<a name="aws-properties-sagemaker-cluster-deploymentconfig"></a>

The deployment configuration for an endpoint, which contains the desired deployment strategy and rollback configurations.

## Syntax
<a name="aws-properties-sagemaker-cluster-deploymentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-sagemaker-cluster-deploymentconfig-syntax.json"></a>

```
{
  "[AutoRollbackConfiguration](#cfn-sagemaker-cluster-deploymentconfig-autorollbackconfiguration)" : {{[ AlarmDetails, ... ]}},
  "[RollingUpdatePolicy](#cfn-sagemaker-cluster-deploymentconfig-rollingupdatepolicy)" : {{RollingUpdatePolicy}},
  "[WaitIntervalInSeconds](#cfn-sagemaker-cluster-deploymentconfig-waitintervalinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-sagemaker-cluster-deploymentconfig-syntax.yaml"></a>

```
  [AutoRollbackConfiguration](#cfn-sagemaker-cluster-deploymentconfig-autorollbackconfiguration): {{
    - AlarmDetails}}
  [RollingUpdatePolicy](#cfn-sagemaker-cluster-deploymentconfig-rollingupdatepolicy): {{
    RollingUpdatePolicy}}
  [WaitIntervalInSeconds](#cfn-sagemaker-cluster-deploymentconfig-waitintervalinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-sagemaker-cluster-deploymentconfig-properties"></a>

`AutoRollbackConfiguration`  <a name="cfn-sagemaker-cluster-deploymentconfig-autorollbackconfiguration"></a>
Automatic rollback configuration for handling endpoint deployment failures and recovery.
*Required*: No
*Type*: Array of [AlarmDetails](aws-properties-sagemaker-cluster-alarmdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RollingUpdatePolicy`  <a name="cfn-sagemaker-cluster-deploymentconfig-rollingupdatepolicy"></a>
Specifies a rolling deployment strategy for updating a SageMaker endpoint.
*Required*: No
*Type*: [RollingUpdatePolicy](aws-properties-sagemaker-cluster-rollingupdatepolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WaitIntervalInSeconds`  <a name="cfn-sagemaker-cluster-deploymentconfig-waitintervalinseconds"></a>
The wait interval in seconds between deployment batches.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `3600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
