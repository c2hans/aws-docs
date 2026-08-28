---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_RouteExclusionOptions.html
---

# RouteExclusionOptions
<a name="API_RouteExclusionOptions"></a>

Specifies strict exclusion options for the route calculation. This setting mandates that the router will avoid any routes that include the specified options, rather than merely attempting to minimize them.

## Contents
<a name="API_RouteExclusionOptions_Contents"></a>

 ** Countries **   <a name="location-Type-RouteExclusionOptions-Countries"></a>
List of countries to be avoided defined by two-letter or three-letter country codes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `([A-Z]{2}|[A-Z]{3})`
Required: Yes

## See Also
<a name="API_RouteExclusionOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-routes-2020-11-19/RouteExclusionOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-routes-2020-11-19/RouteExclusionOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-routes-2020-11-19/RouteExclusionOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
