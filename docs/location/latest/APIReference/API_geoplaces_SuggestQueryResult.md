---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SuggestQueryResult.html
---

# SuggestQueryResult
<a name="API_geoplaces_SuggestQueryResult"></a>

The suggested query results.

## Contents
<a name="API_geoplaces_SuggestQueryResult_Contents"></a>

 ** QueryId **   <a name="location-Type-geoplaces_SuggestQueryResult-QueryId"></a>
QueryId can be used to complete a follow up query through the SearchText API. The QueryId retains context from the original Suggest request such as filters, political view and language. See the SearchText API documentation for more details [SearchText API docs](https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_SearchText.html). If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
The fields `QueryText`, and `QueryID` are mutually exclusive.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** QueryType **   <a name="location-Type-geoplaces_SuggestQueryResult-QueryType"></a>
 The query type. Category queries will search for places which have an entry matching the given category, for example "doctor office". BusinessChain queries will search for instances of a given business. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: String
Valid Values: `Category | BusinessChain`
Required: No

## See Also
<a name="API_geoplaces_SuggestQueryResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/SuggestQueryResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/SuggestQueryResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/SuggestQueryResult)
