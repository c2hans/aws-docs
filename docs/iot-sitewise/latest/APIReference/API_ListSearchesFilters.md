---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListSearchesFilters.html
---

# ListSearchesFilters
<a name="API_ListSearchesFilters"></a>

Optional filters for ListSearches. When multiple filters are set, a search must match all of them.

## Contents
<a name="API_ListSearchesFilters_Contents"></a>

 ** groupIdFilter **   <a name="iotsitewise-Type-ListSearchesFilters-groupIdFilter"></a>
Returns only searches whose `groupId` is one of the listed values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 2. Maximum length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]*`
Required: No

 ** searchTypeFilter **   <a name="iotsitewise-Type-ListSearchesFilters-searchTypeFilter"></a>
Returns only searches whose `searchType` is one of the listed values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Valid Values: `DEEP | QUICK`
Required: No

 ** startedAfter **   <a name="iotsitewise-Type-ListSearchesFilters-startedAfter"></a>
Returns only searches started at or after this time.
Type: Timestamp
Required: No

 ** startedBefore **   <a name="iotsitewise-Type-ListSearchesFilters-startedBefore"></a>
Returns only searches started at or before this time.
Type: Timestamp
Required: No

 ** statusFilter **   <a name="iotsitewise-Type-ListSearchesFilters-statusFilter"></a>
Returns only searches whose status is one of the listed values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `QUEUED | RUNNING | SUCCEEDED | FAILED`
Required: No

## See Also
<a name="API_ListSearchesFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ListSearchesFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ListSearchesFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ListSearchesFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
