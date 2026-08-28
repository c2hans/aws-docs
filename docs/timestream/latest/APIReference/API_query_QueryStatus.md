---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_QueryStatus.html
---

# QueryStatus
<a name="API_query_QueryStatus"></a>

Information about the status of the query, including progress and bytes scanned.

## Contents
<a name="API_query_QueryStatus_Contents"></a>

 ** CumulativeBytesMetered **   <a name="timestream-Type-query_QueryStatus-CumulativeBytesMetered"></a>
The amount of data scanned by the query in bytes that you will be charged for. This is a cumulative sum and represents the total amount of data that you will be charged for since the query was started. The charge is applied only once and is either applied when the query completes running or when the query is cancelled.
Type: Long
Required: No

 ** CumulativeBytesScanned **   <a name="timestream-Type-query_QueryStatus-CumulativeBytesScanned"></a>
The amount of data scanned by the query in bytes. This is a cumulative sum and represents the total amount of bytes scanned since the query was started.
Type: Long
Required: No

 ** ProgressPercentage **   <a name="timestream-Type-query_QueryStatus-ProgressPercentage"></a>
The progress of the query, expressed as a percentage.
Type: Double
Required: No

## See Also
<a name="API_query_QueryStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/QueryStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/QueryStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/QueryStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
