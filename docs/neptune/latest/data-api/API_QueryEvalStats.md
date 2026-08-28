---
source_url: https://docs.aws.amazon.com/neptune/latest/data-api/API_QueryEvalStats.html
---

# QueryEvalStats
<a name="API_QueryEvalStats"></a>

Structure to capture query statistics such as how many queries are running, accepted or waiting and their details.

## Contents
<a name="API_QueryEvalStats_Contents"></a>

 ** cancelled **   <a name="neptunedata-Type-QueryEvalStats-cancelled"></a>
Set to `TRUE` if the query was cancelled, or FALSE otherwise.
Type: Boolean
Required: No

 ** elapsed **   <a name="neptunedata-Type-QueryEvalStats-elapsed"></a>
The number of milliseconds the query has been running so far.
Type: Integer
Required: No

 ** subqueries **   <a name="neptunedata-Type-QueryEvalStats-subqueries"></a>
The number of subqueries in this query.
Type: JSON value
Required: No

 ** waited **   <a name="neptunedata-Type-QueryEvalStats-waited"></a>
Indicates how long the query waited, in milliseconds.
Type: Integer
Required: No

## See Also
<a name="API_QueryEvalStats_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptunedata-2023-08-01/QueryEvalStats)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptunedata-2023-08-01/QueryEvalStats)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptunedata-2023-08-01/QueryEvalStats)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Neptune Data API. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
