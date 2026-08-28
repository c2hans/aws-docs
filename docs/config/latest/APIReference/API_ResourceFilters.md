---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ResourceFilters.html
---

# ResourceFilters
<a name="API_ResourceFilters"></a>

Filters the results by resource account ID, region, resource ID, and resource name.

## Contents
<a name="API_ResourceFilters_Contents"></a>

 ** AccountId **   <a name="config-Type-ResourceFilters-AccountId"></a>
The 12-digit source account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** Region **   <a name="config-Type-ResourceFilters-Region"></a>
The source region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ResourceId **   <a name="config-Type-ResourceFilters-ResourceId"></a>
The ID of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 768.
Required: No

 ** ResourceName **   <a name="config-Type-ResourceFilters-ResourceName"></a>
The name of the resource.
Type: String
Required: No

## See Also
<a name="API_ResourceFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ResourceFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ResourceFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ResourceFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
