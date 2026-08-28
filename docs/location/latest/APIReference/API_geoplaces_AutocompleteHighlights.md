---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AutocompleteHighlights.html
---

# AutocompleteHighlights
<a name="API_geoplaces_AutocompleteHighlights"></a>

Describes how the parts of the response element matched the input query by returning the sections of the response which matched to input query terms.

## Contents
<a name="API_geoplaces_AutocompleteHighlights_Contents"></a>

 ** Address **   <a name="location-Type-geoplaces_AutocompleteHighlights-Address"></a>
Describes how part of the result address match the input query.
Type: [AutocompleteAddressHighlights](API_geoplaces_AutocompleteAddressHighlights.md) object
Required: No

 ** Title **   <a name="location-Type-geoplaces_AutocompleteHighlights-Title"></a>
Indicates where the title field in the result matches the input query.
Type: Array of [Highlight](API_geoplaces_Highlight.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## See Also
<a name="API_geoplaces_AutocompleteHighlights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/AutocompleteHighlights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/AutocompleteHighlights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/AutocompleteHighlights)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
