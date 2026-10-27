---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-ec2deploymentoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentGroup Ec2DeploymentOptions
<a name="aws-properties-codedeploy-deploymentgroup-ec2deploymentoptions"></a>

Options that control how AWS CodeDeploy manages Amazon EC2 resources during a deployment.

## Syntax
<a name="aws-properties-codedeploy-deploymentgroup-ec2deploymentoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentgroup-ec2deploymentoptions-syntax.json"></a>

```
{
  "[AutoScalingGroupProcessesToSuspend](#cfn-codedeploy-deploymentgroup-ec2deploymentoptions-autoscalinggroupprocessestosuspend)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentgroup-ec2deploymentoptions-syntax.yaml"></a>

```
  [AutoScalingGroupProcessesToSuspend](#cfn-codedeploy-deploymentgroup-ec2deploymentoptions-autoscalinggroupprocessestosuspend): {{
    - String}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentgroup-ec2deploymentoptions-properties"></a>

`AutoScalingGroupProcessesToSuspend`  <a name="cfn-codedeploy-deploymentgroup-ec2deploymentoptions-autoscalinggroupprocessestosuspend"></a>
The Amazon EC2 Auto Scaling processes to suspend during the deployment. AWS CodeDeploy suspends these processes before it deploys to instances in an Auto Scaling group, and resumes them when the deployment succeeds, fails, or is stopped. Valid values are `Terminate`, `AZRebalance`, `InstanceRefresh`, and `ScheduledActions`.
This parameter applies only to in-place deployments to Amazon EC2 instances in Auto Scaling groups. If the list is empty, no processes are suspended. If the list isn't empty and the deployment group doesn't use in-place deployments or doesn't include an Auto Scaling group, the request fails with `InvalidAutoScalingGroupProcessToSuspendException`.
The service role for the deployment group must have permission to call `autoscaling:SuspendProcesses` and `autoscaling:ResumeProcesses` on the target Auto Scaling groups. If the processes cannot be suspended, the deployment fails before any instance is updated.
If you suspend `ScheduledActions`, scheduled actions with a start time during the deployment are skipped and do not run after the process resumes.
If CodeDeploy cannot resume the processes, the deployment fails and the processes stay suspended until you resume them with the Auto Scaling `ResumeProcesses` action. While `Terminate` is suspended, Auto Scaling does not replace unhealthy instances. If you suspend `Terminate`, configure a trigger that notifies you when a deployment fails.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
