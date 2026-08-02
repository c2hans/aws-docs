---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LogEvent.html
---

# LogEvent
<a name="API_LogEvent"></a>

This structure contains the information for one sample log event that is associated with an anomaly found by a log anomaly detector.

## Contents
<a name="API_LogEvent_Contents"></a>

 ** message **   <a name="CWL-Type-LogEvent-message"></a>
The message content of the log event.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** timestamp **   <a name="CWL-Type-LogEvent-timestamp"></a>
The time stamp of the log event.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_LogEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/LogEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/LogEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/LogEvent)
