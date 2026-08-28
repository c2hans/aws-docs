---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-job-timeoutconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::Job TimeoutConfig
<a name="aws-properties-iot-job-timeoutconfig"></a>

Specifies the amount of time each device has to finish its execution of the job. A timer is started when the job execution status is set to `IN_PROGRESS`. If the job execution status is not set to another terminal state before the timer expires, it will be automatically set to `TIMED_OUT`.

## Syntax
<a name="aws-properties-iot-job-timeoutconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-job-timeoutconfig-syntax.json"></a>

```
{
  "[InProgressTimeoutInMinutes](#cfn-iot-job-timeoutconfig-inprogresstimeoutinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-iot-job-timeoutconfig-syntax.yaml"></a>

```
  [InProgressTimeoutInMinutes](#cfn-iot-job-timeoutconfig-inprogresstimeoutinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-iot-job-timeoutconfig-properties"></a>

`InProgressTimeoutInMinutes`  <a name="cfn-iot-job-timeoutconfig-inprogresstimeoutinminutes"></a>
Specifies the amount of time, in minutes, this device has to finish execution of this job. The timeout interval can be anywhere between 1 minute and 7 days (1 to 10080 minutes). The in progress timer can't be updated and will apply to all job executions for the job. Whenever a job execution remains in the IN\_PROGRESS status for longer than this interval, the job execution will fail and switch to the terminal `TIMED_OUT` status.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
