---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartLiveTailResponseStream.html
---

# StartLiveTailResponseStream
<a name="API_StartLiveTailResponseStream"></a>

This object includes the stream returned by your [StartLiveTail](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartLiveTail.html) request.

## Contents
<a name="API_StartLiveTailResponseStream_Contents"></a>

 ** sessionStart **   <a name="CWL-Type-StartLiveTailResponseStream-sessionStart"></a>
This object contains information about this Live Tail session, including the log groups included and the log stream filters, if any.
Type: [LiveTailSessionStart](API_LiveTailSessionStart.md) object
Required: No

 ** SessionStreamingException **   <a name="CWL-Type-StartLiveTailResponseStream-SessionStreamingException"></a>
This exception is returned if an unknown error occurs.
Type: Exception
HTTP Status Code:
Required: No

 ** SessionTimeoutException **   <a name="CWL-Type-StartLiveTailResponseStream-SessionTimeoutException"></a>
This exception is returned in the stream when the Live Tail session times out. Live Tail sessions time out after three hours.
Type: Exception
HTTP Status Code:
Required: No

 ** sessionUpdate **   <a name="CWL-Type-StartLiveTailResponseStream-sessionUpdate"></a>
This object contains the log events and session metadata.
Type: [LiveTailSessionUpdate](API_LiveTailSessionUpdate.md) object
Required: No

## See Also
<a name="API_StartLiveTailResponseStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/StartLiveTailResponseStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/StartLiveTailResponseStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/StartLiveTailResponseStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
