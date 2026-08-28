---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.

**Note**
Currently, wildcards are not supported in filters.

The following actions can be filtered:
+  `DescribeDBClusterBacktracks`
+  `DescribeDBClusterEndpoints`
+  `DescribeDBClusters`
+  `DescribeDBInstances`
+  `DescribeDBRecommendations`
+  `DescribeDBShardGroups`
+  `DescribePendingMaintenanceActions`

## Contents
<a name="API_Filter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **
The name of the filter. Filter names are case-sensitive.
Type: String
Required: Yes

 ** Values.Value.N **
One or more filter values. Filter values are case-sensitive.
Type: Array of strings
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/Filter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
