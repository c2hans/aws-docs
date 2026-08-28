---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_EventDestination.html
---

# EventDestination
<a name="API_EventDestination"></a>

In Amazon Pinpoint, *events* include message sends, deliveries, opens, clicks, bounces, and complaints. *Event destinations* are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.

## Contents
<a name="API_EventDestination_Contents"></a>

 ** MatchingEventTypes **   <a name="pinpoint-Type-EventDestination-MatchingEventTypes"></a>
The types of events that Amazon Pinpoint sends to the specified event destinations.
Type: Array of strings
Valid Values: `SEND | REJECT | BOUNCE | COMPLAINT | DELIVERY | OPEN | CLICK | RENDERING_FAILURE`
Required: Yes

 ** Name **   <a name="pinpoint-Type-EventDestination-Name"></a>
A name that identifies the event destination.
Type: String
Required: Yes

 ** CloudWatchDestination **   <a name="pinpoint-Type-EventDestination-CloudWatchDestination"></a>
An object that defines an Amazon CloudWatch destination for email events. You can use Amazon CloudWatch to monitor and gain insights on your email sending metrics.
Type: [CloudWatchDestination](API_CloudWatchDestination.md) object
Required: No

 ** Enabled **   <a name="pinpoint-Type-EventDestination-Enabled"></a>
If `true`, the event destination is enabled. When the event destination is enabled, the specified event types are sent to the destinations in this `EventDestinationDefinition`.
If `false`, the event destination is disabled. When the event destination is disabled, events aren't sent to the specified destinations.
Type: Boolean
Required: No

 ** KinesisFirehoseDestination **   <a name="pinpoint-Type-EventDestination-KinesisFirehoseDestination"></a>
An object that defines an Amazon Kinesis Data Firehose destination for email events. You can use Amazon Kinesis Data Firehose to stream data to other services, such as Amazon S3 and Amazon Redshift.
Type: [KinesisFirehoseDestination](API_KinesisFirehoseDestination.md) object
Required: No

 ** PinpointDestination **   <a name="pinpoint-Type-EventDestination-PinpointDestination"></a>
An object that defines a Amazon Pinpoint destination for email events. You can use Amazon Pinpoint events to create attributes in Amazon Pinpoint projects. You can use these attributes to create segments for your campaigns.
Type: [PinpointDestination](API_PinpointDestination.md) object
Required: No

 ** SnsDestination **   <a name="pinpoint-Type-EventDestination-SnsDestination"></a>
An object that defines an Amazon SNS destination for email events. You can use Amazon SNS to send notification when certain email events occur.
Type: [SnsDestination](API_SnsDestination.md) object
Required: No

## See Also
<a name="API_EventDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/EventDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/EventDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/EventDestination)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Pinpoint Email. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint-email` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
