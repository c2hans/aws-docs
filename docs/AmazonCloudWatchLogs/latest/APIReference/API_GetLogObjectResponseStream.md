---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogObjectResponseStream.html
---

# GetLogObjectResponseStream
<a name="API_GetLogObjectResponseStream"></a>

A stream of structured log data returned by the GetLogObject operation. This stream contains log events with their associated metadata and extracted fields.

## Contents
<a name="API_GetLogObjectResponseStream_Contents"></a>

 ** fields **   <a name="CWL-Type-GetLogObjectResponseStream-fields"></a>
A structure containing the extracted fields from a log event. These fields are extracted based on the log format and can be used for structured querying and analysis.
Type: [FieldsData](API_FieldsData.md) object
Required: No

 ** InternalStreamingException **   <a name="CWL-Type-GetLogObjectResponseStream-InternalStreamingException"></a>
An internal error occurred during the streaming of log data. This exception is thrown when there's an issue with the internal streaming mechanism used by the GetLogObject operation.
Type: Exception
HTTP Status Code:
Required: No

## See Also
<a name="API_GetLogObjectResponseStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/GetLogObjectResponseStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/GetLogObjectResponseStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/GetLogObjectResponseStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
