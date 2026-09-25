---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-eventsv2-subscriber-retrypolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EventsV2::Subscriber RetryPolicy
<a name="aws-properties-eventsv2-subscriber-retrypolicy"></a>

The retry policy for failed deliveries.

## Syntax
<a name="aws-properties-eventsv2-subscriber-retrypolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-eventsv2-subscriber-retrypolicy-syntax.json"></a>

```
{
  "[MaxEventAgeInSeconds](#cfn-eventsv2-subscriber-retrypolicy-maxeventageinseconds)" : {{Integer}},
  "[MaxRetryAttempts](#cfn-eventsv2-subscriber-retrypolicy-maxretryattempts)" : {{Integer}},
  "[RetryStrategy](#cfn-eventsv2-subscriber-retrypolicy-retrystrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-eventsv2-subscriber-retrypolicy-syntax.yaml"></a>

```
  [MaxEventAgeInSeconds](#cfn-eventsv2-subscriber-retrypolicy-maxeventageinseconds): {{Integer}}
  [MaxRetryAttempts](#cfn-eventsv2-subscriber-retrypolicy-maxretryattempts): {{Integer}}
  [RetryStrategy](#cfn-eventsv2-subscriber-retrypolicy-retrystrategy): {{String}}
```

## Properties
<a name="aws-properties-eventsv2-subscriber-retrypolicy-properties"></a>

`MaxEventAgeInSeconds`  <a name="cfn-eventsv2-subscriber-retrypolicy-maxeventageinseconds"></a>
The maximum age of an event in seconds, 60-86400 (24 hours). When an event reaches this age, retries stop; if OnFailureConfiguration is set, the event is delivered to that destination, otherwise it is dropped. The default is 300.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `86400`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxRetryAttempts`  <a name="cfn-eventsv2-subscriber-retrypolicy-maxretryattempts"></a>
The maximum number of retry attempts, 0-185. When the attempts are exhausted, retries stop; if OnFailureConfiguration is set, the event is delivered to that destination, otherwise it is dropped. The default is 5.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `185`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RetryStrategy`  <a name="cfn-eventsv2-subscriber-retrypolicy-retrystrategy"></a>
Which errors are retried. ALL retries all errors. The default is ALL.
*Required*: No
*Type*: String
*Allowed values*: `ALL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
