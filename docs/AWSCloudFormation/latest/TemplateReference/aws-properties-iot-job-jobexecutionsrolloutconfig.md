---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-job-jobexecutionsrolloutconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Job JobExecutionsRolloutConfig
<a name="aws-properties-iot-job-jobexecutionsrolloutconfig"></a>

Allows you to create a staged rollout of a job.

## Syntax
<a name="aws-properties-iot-job-jobexecutionsrolloutconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-job-jobexecutionsrolloutconfig-syntax.json"></a>

```
{
  "[ExponentialRate](#cfn-iot-job-jobexecutionsrolloutconfig-exponentialrate)" : {{ExponentialRolloutRate}},
  "[MaximumPerMinute](#cfn-iot-job-jobexecutionsrolloutconfig-maximumperminute)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-iot-job-jobexecutionsrolloutconfig-syntax.yaml"></a>

```
  [ExponentialRate](#cfn-iot-job-jobexecutionsrolloutconfig-exponentialrate): {{
    ExponentialRolloutRate}}
  [MaximumPerMinute](#cfn-iot-job-jobexecutionsrolloutconfig-maximumperminute): {{Integer}}
```

## Properties
<a name="aws-properties-iot-job-jobexecutionsrolloutconfig-properties"></a>

`ExponentialRate`  <a name="cfn-iot-job-jobexecutionsrolloutconfig-exponentialrate"></a>
The rate of increase for a job rollout. This parameter allows you to define an exponential rate for a job rollout.
*Required*: No
*Type*: [ExponentialRolloutRate](aws-properties-iot-job-exponentialrolloutrate.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumPerMinute`  <a name="cfn-iot-job-jobexecutionsrolloutconfig-maximumperminute"></a>
The maximum number of things that will be notified of a pending job, per minute. This parameter allows you to create a staged rollout.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
