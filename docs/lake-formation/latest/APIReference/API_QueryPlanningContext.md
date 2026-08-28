---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_QueryPlanningContext.html
---

# QueryPlanningContext
<a name="API_QueryPlanningContext"></a>

A structure containing information about the query plan.

## Contents
<a name="API_QueryPlanningContext_Contents"></a>

 ** DatabaseName **   <a name="lakeformation-Type-QueryPlanningContext-DatabaseName"></a>
The database containing the table.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** CatalogId **   <a name="lakeformation-Type-QueryPlanningContext-CatalogId"></a>
The ID of the Data Catalog where the partition in question resides. If none is provided, the AWS account ID is used by default.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** QueryAsOfTime **   <a name="lakeformation-Type-QueryPlanningContext-QueryAsOfTime"></a>
The time as of when to read the table contents. If not set, the most recent transaction commit time will be used. Cannot be specified along with `TransactionId`.
Type: Timestamp
Required: No

 ** QueryParameters **   <a name="lakeformation-Type-QueryPlanningContext-QueryParameters"></a>
A map consisting of key-value pairs.
Type: String to string map
Required: No

 ** TransactionId **   <a name="lakeformation-Type-QueryPlanningContext-TransactionId"></a>
The transaction ID at which to read the table contents. If this transaction is not committed, the read will be treated as part of that transaction and will see its writes. If this transaction has aborted, an error will be returned. If not set, defaults to the most recent committed transaction. Cannot be specified along with `QueryAsOfTime`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}\p{N}\p{P}]*`
Required: No

## See Also
<a name="API_QueryPlanningContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/QueryPlanningContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/QueryPlanningContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/QueryPlanningContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
