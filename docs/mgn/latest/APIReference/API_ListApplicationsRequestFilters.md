---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ListApplicationsRequestFilters.html
---

# ListApplicationsRequestFilters
<a name="API_ListApplicationsRequestFilters"></a>

Applications list filters.

## Contents
<a name="API_ListApplicationsRequestFilters_Contents"></a>

 ** applicationIDs **   <a name="mgn-Type-ListApplicationsRequestFilters-applicationIDs"></a>
Filter applications list by application ID.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Fixed length of 21.
Pattern: `app-[0-9a-zA-Z]{17}`
Required: No

 ** isArchived **   <a name="mgn-Type-ListApplicationsRequestFilters-isArchived"></a>
Filter applications list by archival status.
Type: Boolean
Required: No

 ** waveIDs **   <a name="mgn-Type-ListApplicationsRequestFilters-waveIDs"></a>
Filter applications list by wave ID.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Length Constraints: Fixed length of 22.
Pattern: `wave-[0-9a-zA-Z]{17}`
Required: No

## See Also
<a name="API_ListApplicationsRequestFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ListApplicationsRequestFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ListApplicationsRequestFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ListApplicationsRequestFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
