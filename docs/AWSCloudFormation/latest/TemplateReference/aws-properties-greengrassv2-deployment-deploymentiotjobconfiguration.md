---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrassv2-deployment-deploymentiotjobconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GreengrassV2::Deployment DeploymentIoTJobConfiguration
<a name="aws-properties-greengrassv2-deployment-deploymentiotjobconfiguration"></a>

Contains information about an AWS IoT job configuration.

## Syntax
<a name="aws-properties-greengrassv2-deployment-deploymentiotjobconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrassv2-deployment-deploymentiotjobconfiguration-syntax.json"></a>

```
{
  "[AbortConfig](#cfn-greengrassv2-deployment-deploymentiotjobconfiguration-abortconfig)" : {{IoTJobAbortConfig}},
  "[JobExecutionsRolloutConfig](#cfn-greengrassv2-deployment-deploymentiotjobconfiguration-jobexecutionsrolloutconfig)" : {{IoTJobExecutionsRolloutConfig}},
  "[TimeoutConfig](#cfn-greengrassv2-deployment-deploymentiotjobconfiguration-timeoutconfig)" : {{IoTJobTimeoutConfig}}
}
```

### YAML
<a name="aws-properties-greengrassv2-deployment-deploymentiotjobconfiguration-syntax.yaml"></a>

```
  [AbortConfig](#cfn-greengrassv2-deployment-deploymentiotjobconfiguration-abortconfig): {{
    IoTJobAbortConfig}}
  [JobExecutionsRolloutConfig](#cfn-greengrassv2-deployment-deploymentiotjobconfiguration-jobexecutionsrolloutconfig): {{
    IoTJobExecutionsRolloutConfig}}
  [TimeoutConfig](#cfn-greengrassv2-deployment-deploymentiotjobconfiguration-timeoutconfig): {{
    IoTJobTimeoutConfig}}
```

## Properties
<a name="aws-properties-greengrassv2-deployment-deploymentiotjobconfiguration-properties"></a>

`AbortConfig`  <a name="cfn-greengrassv2-deployment-deploymentiotjobconfiguration-abortconfig"></a>
The stop configuration for the job. This configuration defines when and how to stop a job rollout.
*Required*: No
*Type*: [IoTJobAbortConfig](aws-properties-greengrassv2-deployment-iotjobabortconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobExecutionsRolloutConfig`  <a name="cfn-greengrassv2-deployment-deploymentiotjobconfiguration-jobexecutionsrolloutconfig"></a>
The rollout configuration for the job. This configuration defines the rate at which the job rolls out to the fleet of target devices.
*Required*: No
*Type*: [IoTJobExecutionsRolloutConfig](aws-properties-greengrassv2-deployment-iotjobexecutionsrolloutconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TimeoutConfig`  <a name="cfn-greengrassv2-deployment-deploymentiotjobconfiguration-timeoutconfig"></a>
The timeout configuration for the job. This configuration defines the amount of time each device has to complete the job.
*Required*: No
*Type*: [IoTJobTimeoutConfig](aws-properties-greengrassv2-deployment-iotjobtimeoutconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
