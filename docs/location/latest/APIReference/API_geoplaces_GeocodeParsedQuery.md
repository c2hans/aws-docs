---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GeocodeParsedQuery.html
---

# GeocodeParsedQuery
<a name="API_geoplaces_GeocodeParsedQuery"></a>

Parsed components in the provided QueryText.

## Contents
<a name="API_geoplaces_GeocodeParsedQuery_Contents"></a>

 ** Address **   <a name="location-Type-geoplaces_GeocodeParsedQuery-Address"></a>
The place address.
Type: [GeocodeParsedQueryAddressComponents](API_geoplaces_GeocodeParsedQueryAddressComponents.md) object
Required: No

 ** Title **   <a name="location-Type-geoplaces_GeocodeParsedQuery-Title"></a>
The localized display name of this result item based on request parameter `language`.
Type: Array of [ParsedQueryComponent](API_geoplaces_ParsedQueryComponent.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## See Also
<a name="API_geoplaces_GeocodeParsedQuery_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/GeocodeParsedQuery)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/GeocodeParsedQuery)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/GeocodeParsedQuery)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
