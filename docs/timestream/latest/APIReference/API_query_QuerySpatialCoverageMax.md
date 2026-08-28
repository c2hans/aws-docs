---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_query_QuerySpatialCoverageMax.html
---

# QuerySpatialCoverageMax
<a name="API_query_QuerySpatialCoverageMax"></a>

Provides insights into the table with the most sub-optimal spatial range scanned by your query.

## Contents
<a name="API_query_QuerySpatialCoverageMax_Contents"></a>

 ** PartitionKey **   <a name="timestream-Type-query_QuerySpatialCoverageMax-PartitionKey"></a>
The partition key used for partitioning, which can be a default `measure_name` or a [customer defined partition key](https://docs.aws.amazon.com/timestream/latest/developerguide/customer-defined-partition-keys.html).
Type: Array of strings
Required: No

 ** TableArn **   <a name="timestream-Type-query_QuerySpatialCoverageMax-TableArn"></a>
The Amazon Resource Name (ARN) of the table with the most sub-optimal spatial pruning.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Value **   <a name="timestream-Type-query_QuerySpatialCoverageMax-Value"></a>
The maximum ratio of spatial coverage.
Type: Double
Required: No

## See Also
<a name="API_query_QuerySpatialCoverageMax_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-query-2018-11-01/QuerySpatialCoverageMax)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-query-2018-11-01/QuerySpatialCoverageMax)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-query-2018-11-01/QuerySpatialCoverageMax)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
