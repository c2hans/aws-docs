---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-scheduler-schedule-retrypolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Scheduler::Schedule RetryPolicy
<a name="aws-properties-scheduler-schedule-retrypolicy"></a>

A `RetryPolicy` object that includes information about the retry policy settings, including the maximum age of an event, and the maximum number of times EventBridge Scheduler will try to deliver the event to a target.

## Syntax
<a name="aws-properties-scheduler-schedule-retrypolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-scheduler-schedule-retrypolicy-syntax.json"></a>

```
{
  "[MaximumEventAgeInSeconds](#cfn-scheduler-schedule-retrypolicy-maximumeventageinseconds)" : {{Number}},
  "[MaximumRetryAttempts](#cfn-scheduler-schedule-retrypolicy-maximumretryattempts)" : {{Number}}
}
```

### YAML
<a name="aws-properties-scheduler-schedule-retrypolicy-syntax.yaml"></a>

```
  [MaximumEventAgeInSeconds](#cfn-scheduler-schedule-retrypolicy-maximumeventageinseconds): {{Number}}
  [MaximumRetryAttempts](#cfn-scheduler-schedule-retrypolicy-maximumretryattempts): {{Number}}
```

## Properties
<a name="aws-properties-scheduler-schedule-retrypolicy-properties"></a>

`MaximumEventAgeInSeconds`  <a name="cfn-scheduler-schedule-retrypolicy-maximumeventageinseconds"></a>
The maximum amount of time, in seconds, to continue to make retry attempts.
*Required*: No
*Type*: Number
*Minimum*: `60`
*Maximum*: `86400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaximumRetryAttempts`  <a name="cfn-scheduler-schedule-retrypolicy-maximumretryattempts"></a>
The maximum number of retry attempts to make before the request fails. Retry attempts with exponential backoff continue until either the maximum number of attempts is made or until the duration of the `MaximumEventAgeInSeconds` is reached.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `185`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
