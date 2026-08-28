---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_SearchPlaceIndexForPositionSummary.html
---

# SearchPlaceIndexForPositionSummary
<a name="API_SearchPlaceIndexForPositionSummary"></a>

A summary of the request sent by using `SearchPlaceIndexForPosition`.

## Contents
<a name="API_SearchPlaceIndexForPositionSummary_Contents"></a>

 ** DataSource **   <a name="location-Type-SearchPlaceIndexForPositionSummary-DataSource"></a>
The geospatial data provider attached to the place index resource specified in the request. Values can be one of the following:
+ Esri
+ Grab
+ Here
For more information about data providers, see [Amazon Location Service data providers](https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html).
Type: String
Required: Yes

 ** Position **   <a name="location-Type-SearchPlaceIndexForPositionSummary-Position"></a>
The position specified in the request.
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** Language **   <a name="location-Type-SearchPlaceIndexForPositionSummary-Language"></a>
The preferred language used to return results. Matches the language in the request. The value is a valid [BCP 47](https://tools.ietf.org/search/bcp47) language tag, for example, `en` for English.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Required: No

 ** MaxResults **   <a name="location-Type-SearchPlaceIndexForPositionSummary-MaxResults"></a>
Contains the optional result count limit that is specified in the request.
Default value: `50`
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

## See Also
<a name="API_SearchPlaceIndexForPositionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/SearchPlaceIndexForPositionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/SearchPlaceIndexForPositionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/SearchPlaceIndexForPositionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
