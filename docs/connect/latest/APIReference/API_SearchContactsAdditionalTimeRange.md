---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchContactsAdditionalTimeRange.html
---

# SearchContactsAdditionalTimeRange
<a name="API_SearchContactsAdditionalTimeRange"></a>

Time range that you **additionally** want to filter on.

**Note**
This is different from the [SearchContactsTimeRange](https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchContactsTimeRange.html) data type.

## Contents
<a name="API_SearchContactsAdditionalTimeRange_Contents"></a>

 ** Criteria **   <a name="connect-Type-SearchContactsAdditionalTimeRange-Criteria"></a>
List of criteria of the time range to additionally filter on.
Type: Array of [SearchContactsAdditionalTimeRangeCriteria](API_SearchContactsAdditionalTimeRangeCriteria.md) objects
Required: Yes

 ** MatchType **   <a name="connect-Type-SearchContactsAdditionalTimeRange-MatchType"></a>
The match type combining multiple time range filters.
Type: String
Valid Values: `MATCH_ALL | MATCH_ANY | MATCH_EXACT | MATCH_NONE`
Required: Yes

## See Also
<a name="API_SearchContactsAdditionalTimeRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchContactsAdditionalTimeRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchContactsAdditionalTimeRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchContactsAdditionalTimeRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
