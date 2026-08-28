---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_FilterClause.html
---

# FilterClause
<a name="API_FilterClause"></a>

A search filter clause in Amazon DataZone.

## Contents
<a name="API_FilterClause_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** and **   <a name="datazone-Type-FilterClause-and"></a>
The 'and' search filter clause in Amazon DataZone.
Type: Array of [FilterClause](#API_FilterClause) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

 ** filter **   <a name="datazone-Type-FilterClause-filter"></a>
A search filter in Amazon DataZone.
Type: [Filter](API_Filter.md) object
Required: No

 ** or **   <a name="datazone-Type-FilterClause-or"></a>
The 'or' search filter clause in Amazon DataZone.
Type: Array of [FilterClause](#API_FilterClause) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: No

## See Also
<a name="API_FilterClause_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/FilterClause)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/FilterClause)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/FilterClause)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
