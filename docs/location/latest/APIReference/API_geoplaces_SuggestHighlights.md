---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SuggestHighlights.html
---

# SuggestHighlights
<a name="API_geoplaces_SuggestHighlights"></a>

Describes how the parts of the textQuery matched the input query by returning the sections of the response which matched to textQuery terms.

## Contents
<a name="API_geoplaces_SuggestHighlights_Contents"></a>

 ** Address **   <a name="location-Type-geoplaces_SuggestHighlights-Address"></a>
The place's address.
Type: [SuggestAddressHighlights](API_geoplaces_SuggestAddressHighlights.md) object
Required: No

 ** Title **   <a name="location-Type-geoplaces_SuggestHighlights-Title"></a>
Indicates the starting and ending index of the title in the text query that match the found title.
Type: Array of [Highlight](API_geoplaces_Highlight.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## See Also
<a name="API_geoplaces_SuggestHighlights_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/SuggestHighlights)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/SuggestHighlights)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/SuggestHighlights)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
