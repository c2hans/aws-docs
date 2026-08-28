---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_SearchedLogStream.html
---

# SearchedLogStream
<a name="API_SearchedLogStream"></a>

Represents the search status of a log stream.

## Contents
<a name="API_SearchedLogStream_Contents"></a>

 ** logStreamName **   <a name="CWL-Type-SearchedLogStream-logStreamName"></a>
The name of the log stream.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[^:*]*`
Required: No

 ** searchedCompletely **   <a name="CWL-Type-SearchedLogStream-searchedCompletely"></a>
Indicates whether all the events in this log stream were searched.
Type: Boolean
Required: No

## See Also
<a name="API_SearchedLogStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/SearchedLogStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/SearchedLogStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/SearchedLogStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
