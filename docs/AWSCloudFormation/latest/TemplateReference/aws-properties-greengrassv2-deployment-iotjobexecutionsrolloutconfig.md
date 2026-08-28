---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrassv2-deployment-iotjobexecutionsrolloutconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GreengrassV2::Deployment IoTJobExecutionsRolloutConfig
<a name="aws-properties-greengrassv2-deployment-iotjobexecutionsrolloutconfig"></a>

Contains information about the rollout configuration for a job. This configuration defines the rate at which the job deploys a configuration to a fleet of target devices.

## Syntax
<a name="aws-properties-greengrassv2-deployment-iotjobexecutionsrolloutconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrassv2-deployment-iotjobexecutionsrolloutconfig-syntax.json"></a>

```
{
  "[ExponentialRate](#cfn-greengrassv2-deployment-iotjobexecutionsrolloutconfig-exponentialrate)" : {{IoTJobExponentialRolloutRate}},
  "[MaximumPerMinute](#cfn-greengrassv2-deployment-iotjobexecutionsrolloutconfig-maximumperminute)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-greengrassv2-deployment-iotjobexecutionsrolloutconfig-syntax.yaml"></a>

```
  [ExponentialRate](#cfn-greengrassv2-deployment-iotjobexecutionsrolloutconfig-exponentialrate): {{
    IoTJobExponentialRolloutRate}}
  [MaximumPerMinute](#cfn-greengrassv2-deployment-iotjobexecutionsrolloutconfig-maximumperminute): {{Integer}}
```

## Properties
<a name="aws-properties-greengrassv2-deployment-iotjobexecutionsrolloutconfig-properties"></a>

`ExponentialRate`  <a name="cfn-greengrassv2-deployment-iotjobexecutionsrolloutconfig-exponentialrate"></a>
The exponential rate to increase the job rollout rate.
*Required*: No
*Type*: [IoTJobExponentialRolloutRate](aws-properties-greengrassv2-deployment-iotjobexponentialrolloutrate.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaximumPerMinute`  <a name="cfn-greengrassv2-deployment-iotjobexecutionsrolloutconfig-maximumperminute"></a>
The maximum number of devices that receive a pending job notification, per minute.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1000`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
