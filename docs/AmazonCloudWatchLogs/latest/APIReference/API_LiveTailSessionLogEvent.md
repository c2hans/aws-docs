---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LiveTailSessionLogEvent.html
---

# LiveTailSessionLogEvent
<a name="API_LiveTailSessionLogEvent"></a>

This object contains the information for one log event returned in a Live Tail stream.

## Contents
<a name="API_LiveTailSessionLogEvent_Contents"></a>

 ** ingestionTime **   <a name="CWL-Type-LiveTailSessionLogEvent-ingestionTime"></a>
The timestamp specifying when this log event was ingested into the log group.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** logGroupIdentifier **   <a name="CWL-Type-LiveTailSessionLogEvent-logGroupIdentifier"></a>
The name or ARN of the log group that ingested this log event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w#+=/:,.@-]*`
Required: No

 ** logStreamName **   <a name="CWL-Type-LiveTailSessionLogEvent-logStreamName"></a>
The name of the log stream that ingested this log event.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

 ** message **   <a name="CWL-Type-LiveTailSessionLogEvent-message"></a>
The log event message text.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** timestamp **   <a name="CWL-Type-LiveTailSessionLogEvent-timestamp"></a>
The timestamp specifying when this log event was created.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_LiveTailSessionLogEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/LiveTailSessionLogEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/LiveTailSessionLogEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/LiveTailSessionLogEvent)
