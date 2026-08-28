---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchTextFilter.html
---

# SearchTextFilter
<a name="API_geoplaces_SearchTextFilter"></a>

SearchText structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.

## Contents
<a name="API_geoplaces_SearchTextFilter_Contents"></a>

 ** BoundingBox **   <a name="location-Type-geoplaces_SearchTextFilter-BoundingBox"></a>
The bounding box enclosing the geometric shape (area or line) that an individual result covers.
The bounding box formed is defined as a set 4 coordinates: `[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]`
Type: Array of doubles
Array Members: Fixed number of 4 items.
Required: No

 ** Circle **   <a name="location-Type-geoplaces_SearchTextFilter-Circle"></a>
The `Circle` that all results must be in.
Type: [FilterCircle](API_geoplaces_FilterCircle.md) object
Required: No

 ** IncludeCountries **   <a name="location-Type-geoplaces_SearchTextFilter-IncludeCountries"></a>
 A list of countries that all results must be in. Countries are represented by either their alpha-2 or alpha-3 character codes.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `([A-Z]{2}|[A-Z]{3})`
Required: No

## See Also
<a name="API_geoplaces_SearchTextFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/SearchTextFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/SearchTextFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/SearchTextFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
