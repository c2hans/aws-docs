---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_QueryStatistics.html
---

# QueryStatistics
<a name="API_QueryStatistics"></a>

Metadata about a query, such as the number of results.

## Contents
<a name="API_QueryStatistics_Contents"></a>

 ** BytesScanned **   <a name="awscloudtrail-Type-QueryStatistics-BytesScanned"></a>
The total bytes that the query scanned in the event data store. This value matches the number of bytes for which your account is billed for the query, unless the query is still running.
Type: Long
Required: No

 ** ResultsCount **   <a name="awscloudtrail-Type-QueryStatistics-ResultsCount"></a>
The number of results returned.
Type: Integer
Required: No

 ** TotalResultsCount **   <a name="awscloudtrail-Type-QueryStatistics-TotalResultsCount"></a>
The total number of results returned by a query.
Type: Integer
Required: No

## See Also
<a name="API_QueryStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/QueryStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/QueryStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/QueryStatistics)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
