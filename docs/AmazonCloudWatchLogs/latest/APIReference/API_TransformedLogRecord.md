---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TransformedLogRecord.html
---

# TransformedLogRecord
<a name="API_TransformedLogRecord"></a>

This structure contains information for one log event that has been processed by a log transformer.

## Contents
<a name="API_TransformedLogRecord_Contents"></a>

 ** eventMessage **   <a name="CWL-Type-TransformedLogRecord-eventMessage"></a>
The original log event message before it was transformed.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** eventNumber **   <a name="CWL-Type-TransformedLogRecord-eventNumber"></a>
The event number.
Type: Long
Required: No

 ** transformedEventMessage **   <a name="CWL-Type-TransformedLogRecord-transformedEventMessage"></a>
The log event message after being transformed.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_TransformedLogRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/TransformedLogRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/TransformedLogRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/TransformedLogRecord)
