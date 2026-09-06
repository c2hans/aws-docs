---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_EventDestination.html
---

# EventDestination
<a name="API_EventDestination"></a>

Contains information about an event destination.

Event destinations are associated with configuration sets, which enable you to publish message sending events to CloudWatch, Firehose, or Amazon SNS.

## Contents
<a name="API_EventDestination_Contents"></a>

 ** Enabled **   <a name="pinpoint-Type-EventDestination-Enabled"></a>
When set to true events will be logged.
Type: Boolean
Required: Yes

 ** EventDestinationName **   <a name="pinpoint-Type-EventDestination-EventDestinationName"></a>
The name of the EventDestination.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** MatchingEventTypes **   <a name="pinpoint-Type-EventDestination-MatchingEventTypes"></a>
An array of event types that determine which events to log.
The `TEXT_SENT` event type is not supported.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 52 items.
Valid Values: `ALL | TEXT_ALL | TEXT_SENT | TEXT_PENDING | TEXT_QUEUED | TEXT_SUCCESSFUL | TEXT_DELIVERED | TEXT_INVALID | TEXT_INVALID_MESSAGE | TEXT_UNREACHABLE | TEXT_CARRIER_UNREACHABLE | TEXT_BLOCKED | TEXT_CARRIER_BLOCKED | TEXT_SPAM | TEXT_UNKNOWN | TEXT_TTL_EXPIRED | TEXT_PROTECT_BLOCKED | VOICE_ALL | VOICE_INITIATED | VOICE_RINGING | VOICE_ANSWERED | VOICE_COMPLETED | VOICE_BUSY | VOICE_NO_ANSWER | VOICE_FAILED | VOICE_TTL_EXPIRED | MEDIA_ALL | MEDIA_PENDING | MEDIA_QUEUED | MEDIA_SUCCESSFUL | MEDIA_DELIVERED | MEDIA_INVALID | MEDIA_INVALID_MESSAGE | MEDIA_UNREACHABLE | MEDIA_CARRIER_UNREACHABLE | MEDIA_BLOCKED | MEDIA_CARRIER_BLOCKED | MEDIA_SPAM | MEDIA_UNKNOWN | MEDIA_TTL_EXPIRED | MEDIA_FILE_INACCESSIBLE | MEDIA_FILE_TYPE_UNSUPPORTED | MEDIA_FILE_SIZE_EXCEEDED | RCS_ALL | RCS_QUEUED | RCS_SENT | RCS_DELIVERED | RCS_READ | RCS_FAILED | RCS_TTL_EXPIRED | RCS_PROTECT_BLOCKED | RCS_FALLEN_BACK_TO_SMS`
Required: Yes

 ** CloudWatchLogsDestination **   <a name="pinpoint-Type-EventDestination-CloudWatchLogsDestination"></a>
An object that contains information about an event destination that sends logging events to Amazon CloudWatch logs.
Type: [CloudWatchLogsDestination](API_CloudWatchLogsDestination.md) object
Required: No

 ** KinesisFirehoseDestination **   <a name="pinpoint-Type-EventDestination-KinesisFirehoseDestination"></a>
An object that contains information about an event destination for logging to Amazon Data Firehose.
Type: [KinesisFirehoseDestination](API_KinesisFirehoseDestination.md) object
Required: No

 ** SnsDestination **   <a name="pinpoint-Type-EventDestination-SnsDestination"></a>
An object that contains information about an event destination that sends logging events to Amazon SNS.
Type: [SnsDestination](API_SnsDestination.md) object
Required: No

## See Also
<a name="API_EventDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/EventDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/EventDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/EventDestination)
