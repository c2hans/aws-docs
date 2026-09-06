---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FilteredLogEvent.html
---

# FilteredLogEvent
<a name="API_FilteredLogEvent"></a>

Represents a matched event.

## Contents
<a name="API_FilteredLogEvent_Contents"></a>

 ** eventId **   <a name="CWL-Type-FilteredLogEvent-eventId"></a>
The ID of the event.
Type: String
Required: No

 ** ingestionTime **   <a name="CWL-Type-FilteredLogEvent-ingestionTime"></a>
The time the event was ingested, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** logStreamName **   <a name="CWL-Type-FilteredLogEvent-logStreamName"></a>
The name of the log stream to which this event belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

 ** message **   <a name="CWL-Type-FilteredLogEvent-message"></a>
The data contained in the log event.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** timestamp **   <a name="CWL-Type-FilteredLogEvent-timestamp"></a>
The time the event occurred, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_FilteredLogEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/FilteredLogEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/FilteredLogEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/FilteredLogEvent)
