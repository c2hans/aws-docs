---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LiveTailSessionUpdate.html
---

# LiveTailSessionUpdate
<a name="API_LiveTailSessionUpdate"></a>

This object contains the log events and metadata for a Live Tail session.

## Contents
<a name="API_LiveTailSessionUpdate_Contents"></a>

 ** sessionMetadata **   <a name="CWL-Type-LiveTailSessionUpdate-sessionMetadata"></a>
This object contains the session metadata for a Live Tail session.
Type: [LiveTailSessionMetadata](API_LiveTailSessionMetadata.md) object
Required: No

 ** sessionResults **   <a name="CWL-Type-LiveTailSessionUpdate-sessionResults"></a>
An array, where each member of the array includes the information for one log event in the Live Tail session.
A `sessionResults` array can include as many as 500 log events. If the number of log events matching the request exceeds 500 per second, the log events are sampled down to 500 log events to be included in each `sessionUpdate` structure.
Type: Array of [LiveTailSessionLogEvent](API_LiveTailSessionLogEvent.md) objects
Required: No

## See Also
<a name="API_LiveTailSessionUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/LiveTailSessionUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/LiveTailSessionUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/LiveTailSessionUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
