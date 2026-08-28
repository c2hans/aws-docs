---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_MessageInsightsDataSource.html
---

# MessageInsightsDataSource
<a name="API_MessageInsightsDataSource"></a>

An object that contains filters applied when performing the Message Insights export.

## Contents
<a name="API_MessageInsightsDataSource_Contents"></a>

 ** EndDate **   <a name="SES-Type-MessageInsightsDataSource-EndDate"></a>
Represents the end date for the export interval as a timestamp. The end date is inclusive.
Type: Timestamp
Required: Yes

 ** StartDate **   <a name="SES-Type-MessageInsightsDataSource-StartDate"></a>
Represents the start date for the export interval as a timestamp. The start date is inclusive.
Type: Timestamp
Required: Yes

 ** Exclude **   <a name="SES-Type-MessageInsightsDataSource-Exclude"></a>
Filters for results to be excluded from the export file.
Type: [MessageInsightsFilters](API_MessageInsightsFilters.md) object
Required: No

 ** Include **   <a name="SES-Type-MessageInsightsDataSource-Include"></a>
Filters for results to be included in the export file.
Type: [MessageInsightsFilters](API_MessageInsightsFilters.md) object
Required: No

 ** MaxResults **   <a name="SES-Type-MessageInsightsDataSource-MaxResults"></a>
The maximum number of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10000.
Required: No

## See Also
<a name="API_MessageInsightsDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sesv2-2019-09-27/MessageInsightsDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sesv2-2019-09-27/MessageInsightsDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sesv2-2019-09-27/MessageInsightsDataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
