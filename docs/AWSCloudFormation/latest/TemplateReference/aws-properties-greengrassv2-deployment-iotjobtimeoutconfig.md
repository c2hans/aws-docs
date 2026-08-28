---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrassv2-deployment-iotjobtimeoutconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GreengrassV2::Deployment IoTJobTimeoutConfig
<a name="aws-properties-greengrassv2-deployment-iotjobtimeoutconfig"></a>

Contains information about the timeout configuration for a job.

## Syntax
<a name="aws-properties-greengrassv2-deployment-iotjobtimeoutconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrassv2-deployment-iotjobtimeoutconfig-syntax.json"></a>

```
{
  "[InProgressTimeoutInMinutes](#cfn-greengrassv2-deployment-iotjobtimeoutconfig-inprogresstimeoutinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-greengrassv2-deployment-iotjobtimeoutconfig-syntax.yaml"></a>

```
  [InProgressTimeoutInMinutes](#cfn-greengrassv2-deployment-iotjobtimeoutconfig-inprogresstimeoutinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-greengrassv2-deployment-iotjobtimeoutconfig-properties"></a>

`InProgressTimeoutInMinutes`  <a name="cfn-greengrassv2-deployment-iotjobtimeoutconfig-inprogresstimeoutinminutes"></a>
The amount of time, in minutes, that devices have to complete the job. The timer starts when the job status is set to `IN_PROGRESS`. If the job status doesn't change to a terminal state before the time expires, then the job status is set to `TIMED_OUT`.
The timeout interval must be between 1 minute and 7 days (10080 minutes).
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `2147483647`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
