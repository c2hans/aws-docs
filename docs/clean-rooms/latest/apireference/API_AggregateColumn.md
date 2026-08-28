---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AggregateColumn.html
---

# AggregateColumn
<a name="API_AggregateColumn"></a>

Column in configured table that can be used in aggregate function in query.

## Contents
<a name="API_AggregateColumn_Contents"></a>

 ** columnNames **   <a name="API-Type-AggregateColumn-columnNames"></a>
Column names in configured table of aggregate columns.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** function **   <a name="API-Type-AggregateColumn-function"></a>
Aggregation function that can be applied to aggregate column in query.
Type: String
Valid Values: `SUM | SUM_DISTINCT | COUNT | COUNT_DISTINCT | AVG`
Required: Yes

## See Also
<a name="API_AggregateColumn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AggregateColumn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AggregateColumn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AggregateColumn)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
