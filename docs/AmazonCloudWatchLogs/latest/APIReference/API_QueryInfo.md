---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_QueryInfo.html
---

# QueryInfo
<a name="API_QueryInfo"></a>

Information about one CloudWatch Logs Insights query that matches the request in a `DescribeQueries` operation.

## Contents
<a name="API_QueryInfo_Contents"></a>

 ** bytesScanned **   <a name="CWL-Type-QueryInfo-bytesScanned"></a>
The total number of bytes scanned by the query. This indicates the cost associated with the query.
Type: Double
Required: No

 ** createTime **   <a name="CWL-Type-QueryInfo-createTime"></a>
The date and time that this query was created.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** logGroupName **   <a name="CWL-Type-QueryInfo-logGroupName"></a>
The name of the log group scanned by this query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** queryDuration **   <a name="CWL-Type-QueryInfo-queryDuration"></a>
The duration in milliseconds that the query took to execute.
Type: Long
Required: No

 ** queryId **   <a name="CWL-Type-QueryInfo-queryId"></a>
The unique ID number of this query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** queryLanguage **   <a name="CWL-Type-QueryInfo-queryLanguage"></a>
The query language used for this query. For more information about the query languages that CloudWatch Logs supports, see [Supported query languages](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html).
Type: String
Valid Values: `CWLI | SQL | PPL`
Required: No

 ** queryString **   <a name="CWL-Type-QueryInfo-queryString"></a>
The query string used in this query.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Required: No

 ** status **   <a name="CWL-Type-QueryInfo-status"></a>
The status of this query. Possible values are `Cancelled`, `Complete`, `Failed`, `Running`, `Scheduled`, and `Unknown`.
Type: String
Valid Values: `Scheduled | Running | Complete | Failed | Cancelled | Timeout | Unknown`
Required: No

 ** userIdentity **   <a name="CWL-Type-QueryInfo-userIdentity"></a>
The ARN of the user who ran the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_QueryInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/QueryInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/QueryInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/QueryInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
