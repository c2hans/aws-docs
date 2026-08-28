---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_RejectedLogEventsInfo.html
---

# RejectedLogEventsInfo
<a name="API_RejectedLogEventsInfo"></a>

Represents the rejected events.

## Contents
<a name="API_RejectedLogEventsInfo_Contents"></a>

 ** expiredLogEventEndIndex **   <a name="CWL-Type-RejectedLogEventsInfo-expiredLogEventEndIndex"></a>
The expired log events.
Type: Integer
Required: No

 ** tooNewLogEventStartIndex **   <a name="CWL-Type-RejectedLogEventsInfo-tooNewLogEventStartIndex"></a>
The index of the first log event that is too new. This field is inclusive.
Type: Integer
Required: No

 ** tooOldLogEventEndIndex **   <a name="CWL-Type-RejectedLogEventsInfo-tooOldLogEventEndIndex"></a>
The index of the last log event that is too old. This field is exclusive.
Type: Integer
Required: No

## See Also
<a name="API_RejectedLogEventsInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/RejectedLogEventsInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/RejectedLogEventsInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/RejectedLogEventsInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
