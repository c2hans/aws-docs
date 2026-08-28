---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_InputLogEvent.html
---

# InputLogEvent
<a name="API_InputLogEvent"></a>

Represents a log event, which is a record of activity that was recorded by the application or resource being monitored.

## Contents
<a name="API_InputLogEvent_Contents"></a>

 ** message **   <a name="CWL-Type-InputLogEvent-message"></a>
The raw event message. Each log event can be no larger than 1 MB.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** timestamp **   <a name="CWL-Type-InputLogEvent-timestamp"></a>
The time the event occurred, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_InputLogEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/InputLogEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/InputLogEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/InputLogEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
