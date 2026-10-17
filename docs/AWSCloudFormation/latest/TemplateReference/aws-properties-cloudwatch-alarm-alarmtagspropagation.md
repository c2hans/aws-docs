---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alarm-alarmtagspropagation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alarm AlarmTagsPropagation
<a name="aws-properties-cloudwatch-alarm-alarmtagspropagation"></a>

Includes the alarm's tags in the notifications that the alarm sends to Amazon SNS topics and AWS Lambda functions. The tags are also included in the alarm's state-change events in Amazon EventBridge. Other types of alarm actions don't receive the tags.

By default, the alarm's tags aren't included.

Use this to route or filter notifications and events by tag, such as by team or environment. You can also use it to read the alarm's tags without looking them up separately.

To limit which tags are included, specify either `IncludedTagKeys` or `ExcludedTagKeys`. You can't specify both. If you specify neither, all of the alarm's tags are included. This includes tags that you add to the alarm later.

## Syntax
<a name="aws-properties-cloudwatch-alarm-alarmtagspropagation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alarm-alarmtagspropagation-syntax.json"></a>

```
{
  "[Enabled](#cfn-cloudwatch-alarm-alarmtagspropagation-enabled)" : {{Boolean}},
  "[ExcludedTagKeys](#cfn-cloudwatch-alarm-alarmtagspropagation-excludedtagkeys)" : {{[ String, ... ]}},
  "[IncludedTagKeys](#cfn-cloudwatch-alarm-alarmtagspropagation-includedtagkeys)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alarm-alarmtagspropagation-syntax.yaml"></a>

```
  [Enabled](#cfn-cloudwatch-alarm-alarmtagspropagation-enabled): {{Boolean}}
  [ExcludedTagKeys](#cfn-cloudwatch-alarm-alarmtagspropagation-excludedtagkeys): {{
    - String}}
  [IncludedTagKeys](#cfn-cloudwatch-alarm-alarmtagspropagation-includedtagkeys): {{
    - String}}
```

## Properties
<a name="aws-properties-cloudwatch-alarm-alarmtagspropagation-properties"></a>

`Enabled`  <a name="cfn-cloudwatch-alarm-alarmtagspropagation-enabled"></a>
Set to `true` to include the alarm's tags. Set to `false` to stop including them.
When this is `true`, you must have the `cloudwatch:ListTagsForResource` permission on the alarm to create or update it.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludedTagKeys`  <a name="cfn-cloudwatch-alarm-alarmtagspropagation-excludedtagkeys"></a>
The tag keys to exclude. All of the alarm's tags except those with these keys are included.
You can specify 1 to 50 tag keys. Each tag key must be 1 to 128 characters long.
You can't specify both `IncludedTagKeys` and `ExcludedTagKeys`.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `128 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludedTagKeys`  <a name="cfn-cloudwatch-alarm-alarmtagspropagation-includedtagkeys"></a>
The tag keys to include. Only the alarm's tags with these keys are included.
You can specify 1 to 50 tag keys. Each tag key must be 1 to 128 characters long.
You can't specify both `IncludedTagKeys` and `ExcludedTagKeys`.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `128 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
