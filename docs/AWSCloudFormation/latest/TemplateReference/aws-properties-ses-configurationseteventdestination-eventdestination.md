---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-configurationseteventdestination-eventdestination.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ConfigurationSetEventDestination EventDestination
<a name="aws-properties-ses-configurationseteventdestination-eventdestination"></a>

In the Amazon SES API v2, *events* include message sends, deliveries, opens, clicks, bounces, complaints and delivery delays. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.

## Syntax
<a name="aws-properties-ses-configurationseteventdestination-eventdestination-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-configurationseteventdestination-eventdestination-syntax.json"></a>

```
{
  "[CloudWatchDestination](#cfn-ses-configurationseteventdestination-eventdestination-cloudwatchdestination)" : {{CloudWatchDestination}},
  "[Enabled](#cfn-ses-configurationseteventdestination-eventdestination-enabled)" : {{Boolean}},
  "[EventBridgeDestination](#cfn-ses-configurationseteventdestination-eventdestination-eventbridgedestination)" : {{EventBridgeDestination}},
  "[KinesisFirehoseDestination](#cfn-ses-configurationseteventdestination-eventdestination-kinesisfirehosedestination)" : {{KinesisFirehoseDestination}},
  "[MatchingEventTypes](#cfn-ses-configurationseteventdestination-eventdestination-matchingeventtypes)" : {{[ String, ... ]}},
  "[Name](#cfn-ses-configurationseteventdestination-eventdestination-name)" : {{String}},
  "[SnsDestination](#cfn-ses-configurationseteventdestination-eventdestination-snsdestination)" : {{SnsDestination}}
}
```

### YAML
<a name="aws-properties-ses-configurationseteventdestination-eventdestination-syntax.yaml"></a>

```
  [CloudWatchDestination](#cfn-ses-configurationseteventdestination-eventdestination-cloudwatchdestination): {{
    CloudWatchDestination}}
  [Enabled](#cfn-ses-configurationseteventdestination-eventdestination-enabled): {{Boolean}}
  [EventBridgeDestination](#cfn-ses-configurationseteventdestination-eventdestination-eventbridgedestination): {{
    EventBridgeDestination}}
  [KinesisFirehoseDestination](#cfn-ses-configurationseteventdestination-eventdestination-kinesisfirehosedestination): {{
    KinesisFirehoseDestination}}
  [MatchingEventTypes](#cfn-ses-configurationseteventdestination-eventdestination-matchingeventtypes): {{
    - String}}
  [Name](#cfn-ses-configurationseteventdestination-eventdestination-name): {{String}}
  [SnsDestination](#cfn-ses-configurationseteventdestination-eventdestination-snsdestination): {{
    SnsDestination}}
```

## Properties
<a name="aws-properties-ses-configurationseteventdestination-eventdestination-properties"></a>

`CloudWatchDestination`  <a name="cfn-ses-configurationseteventdestination-eventdestination-cloudwatchdestination"></a>
An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.
*Required*: No
*Type*: [CloudWatchDestination](aws-properties-ses-configurationseteventdestination-cloudwatchdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-ses-configurationseteventdestination-eventdestination-enabled"></a>
If `true`, the event destination is enabled. When the event destination is enabled, the specified event types are sent to the destinations in this `EventDestinationDefinition`.
If `false`, the event destination is disabled. When the event destination is disabled, events aren't sent to the specified destinations.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EventBridgeDestination`  <a name="cfn-ses-configurationseteventdestination-eventdestination-eventbridgedestination"></a>
An object that defines an Amazon EventBridge destination for email events. You can use Amazon EventBridge to send notifications when certain email events occur.
*Required*: No
*Type*: [EventBridgeDestination](aws-properties-ses-configurationseteventdestination-eventbridgedestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KinesisFirehoseDestination`  <a name="cfn-ses-configurationseteventdestination-eventdestination-kinesisfirehosedestination"></a>
An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.
*Required*: No
*Type*: [KinesisFirehoseDestination](aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MatchingEventTypes`  <a name="cfn-ses-configurationseteventdestination-eventdestination-matchingeventtypes"></a>
The types of events that Amazon SES sends to the specified event destinations.
+ `SEND` - The send request was successful and SES will attempt to deliver the message to the recipient’s mail server. (If account-level or global suppression is being used, SES will still count it as a send, but delivery is suppressed.)
+ `REJECT` - SES accepted the email, but determined that it contained a virus and didn’t attempt to deliver it to the recipient’s mail server.
+ `BOUNCE` - (*Hard bounce*) The recipient's mail server permanently rejected the email. (*Soft bounces* are only included when SES fails to deliver the email after retrying for a period of time.)
+ `COMPLAINT` - The email was successfully delivered to the recipient’s mail server, but the recipient marked it as spam.
+ `DELIVERY` - SES successfully delivered the email to the recipient's mail server.
+ `OPEN` - The recipient received the message and opened it in their email client.
+ `CLICK` - The recipient clicked one or more links in the email.
+ `RENDERING_FAILURE` - The email wasn't sent because of a template rendering issue. This event type can occur when template data is missing, or when there is a mismatch between template parameters and data. (This event type only occurs when you send email using the [`SendEmail`](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendEmail.html) or [`SendBulkEmail`](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_SendBulkEmail.html) API operations.)
+ `DELIVERY_DELAY` - The email couldn't be delivered to the recipient’s mail server because a temporary issue occurred. Delivery delays can occur, for example, when the recipient's inbox is full, or when the receiving email server experiences a transient issue.
+ `SUBSCRIPTION` - The email was successfully delivered, but the recipient updated their subscription preferences by clicking on an *unsubscribe* link as part of your [subscription management](https://docs.aws.amazon.com/ses/latest/dg/sending-email-subscription-management.html).
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ses-configurationseteventdestination-eventdestination-name"></a>
The name of the event destination. The name must meet the following requirements:
+ Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (\_), or dashes (-).
+ Contain 64 characters or fewer.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{0,64}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SnsDestination`  <a name="cfn-ses-configurationseteventdestination-eventdestination-snsdestination"></a>
An object that contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event destination.
*Required*: No
*Type*: [SnsDestination](aws-properties-ses-configurationseteventdestination-snsdestination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
