---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-smsvoice-configurationset-eventdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::ConfigurationSet EventDestination
<a name="aws-properties-smsvoice-configurationset-eventdestination"></a>

Contains information about an event destination.

Event destinations are associated with configuration sets, which enable you to publish message sending events to CloudWatch, Firehose, or Amazon SNS.

## Syntax
<a name="aws-properties-smsvoice-configurationset-eventdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-smsvoice-configurationset-eventdestination-syntax.json"></a>

```
{
  "[CloudWatchLogsDestination](#cfn-smsvoice-configurationset-eventdestination-cloudwatchlogsdestination)" : {{CloudWatchLogsDestination}},
  "[Enabled](#cfn-smsvoice-configurationset-eventdestination-enabled)" : {{Boolean}},
  "[EventDestinationName](#cfn-smsvoice-configurationset-eventdestination-eventdestinationname)" : {{String}},
  "[KinesisFirehoseDestination](#cfn-smsvoice-configurationset-eventdestination-kinesisfirehosedestination)" : {{KinesisFirehoseDestination}},
  "[MatchingEventTypes](#cfn-smsvoice-configurationset-eventdestination-matchingeventtypes)" : {{[ String, ... ]}},
  "[SnsDestination](#cfn-smsvoice-configurationset-eventdestination-snsdestination)" : {{SnsDestination}}
}
```

### YAML
<a name="aws-properties-smsvoice-configurationset-eventdestination-syntax.yaml"></a>

```
  [CloudWatchLogsDestination](#cfn-smsvoice-configurationset-eventdestination-cloudwatchlogsdestination): {{
    CloudWatchLogsDestination}}
  [Enabled](#cfn-smsvoice-configurationset-eventdestination-enabled): {{Boolean}}
  [EventDestinationName](#cfn-smsvoice-configurationset-eventdestination-eventdestinationname): {{String}}
  [KinesisFirehoseDestination](#cfn-smsvoice-configurationset-eventdestination-kinesisfirehosedestination): {{
    KinesisFirehoseDestination}}
  [MatchingEventTypes](#cfn-smsvoice-configurationset-eventdestination-matchingeventtypes): {{
    - String}}
  [SnsDestination](#cfn-smsvoice-configurationset-eventdestination-snsdestination): {{
    SnsDestination}}
```

## Properties
<a name="aws-properties-smsvoice-configurationset-eventdestination-properties"></a>

`CloudWatchLogsDestination`  <a name="cfn-smsvoice-configurationset-eventdestination-cloudwatchlogsdestination"></a>
An object that contains information about an event destination that sends logging events to Amazon CloudWatch logs.
*Required*: No
*Type*: [CloudWatchLogsDestination](aws-properties-smsvoice-configurationset-cloudwatchlogsdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-smsvoice-configurationset-eventdestination-enabled"></a>
When set to true events will be logged.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventDestinationName`  <a name="cfn-smsvoice-configurationset-eventdestination-eventdestinationname"></a>
The name of the EventDestination.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KinesisFirehoseDestination`  <a name="cfn-smsvoice-configurationset-eventdestination-kinesisfirehosedestination"></a>
An object that contains information about an event destination for logging to Amazon Data Firehose.
*Required*: No
*Type*: [KinesisFirehoseDestination](aws-properties-smsvoice-configurationset-kinesisfirehosedestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchingEventTypes`  <a name="cfn-smsvoice-configurationset-eventdestination-matchingeventtypes"></a>
An array of event types that determine which events to log.
The `TEXT_SENT` event type is not supported.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnsDestination`  <a name="cfn-smsvoice-configurationset-eventdestination-snsdestination"></a>
An object that contains information about an event destination that sends logging events to Amazon SNS.
*Required*: No
*Type*: [SnsDestination](aws-properties-smsvoice-configurationset-snsdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
