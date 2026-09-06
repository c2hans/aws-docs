---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LiveTailSessionMetadata.html
---

# LiveTailSessionMetadata
<a name="API_LiveTailSessionMetadata"></a>

This object contains the metadata for one `LiveTailSessionUpdate` structure. It indicates whether that update includes only a sample of 500 log events out of a larger number of ingested log events, or if it contains all of the matching log events ingested during that second of time.

## Contents
<a name="API_LiveTailSessionMetadata_Contents"></a>

 ** sampled **   <a name="CWL-Type-LiveTailSessionMetadata-sampled"></a>
If this is `true`, then more than 500 log events matched the request for this update, and the `sessionResults` includes a sample of 500 of those events.
If this is `false`, then 500 or fewer log events matched the request for this update, so no sampling was necessary. In this case, the `sessionResults` array includes all log events that matched your request during this time.
Type: Boolean
Required: No

## See Also
<a name="API_LiveTailSessionMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/LiveTailSessionMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/LiveTailSessionMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/LiveTailSessionMetadata)
