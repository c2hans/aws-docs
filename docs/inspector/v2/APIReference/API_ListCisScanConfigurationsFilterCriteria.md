---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCisScanConfigurationsFilterCriteria.html
---

# ListCisScanConfigurationsFilterCriteria
<a name="API_ListCisScanConfigurationsFilterCriteria"></a>

A list of CIS scan configurations filter criteria.

## Contents
<a name="API_ListCisScanConfigurationsFilterCriteria_Contents"></a>

 ** scanConfigurationArnFilters **   <a name="inspector2-Type-ListCisScanConfigurationsFilterCriteria-scanConfigurationArnFilters"></a>
The list of scan configuration ARN filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** scanNameFilters **   <a name="inspector2-Type-ListCisScanConfigurationsFilterCriteria-scanNameFilters"></a>
The list of scan name filters.
Type: Array of [CisStringFilter](API_CisStringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** targetResourceTagFilters **   <a name="inspector2-Type-ListCisScanConfigurationsFilterCriteria-targetResourceTagFilters"></a>
The list of target resource tag filters.
Type: Array of [TagFilter](API_TagFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_ListCisScanConfigurationsFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListCisScanConfigurationsFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListCisScanConfigurationsFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListCisScanConfigurationsFilterCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
