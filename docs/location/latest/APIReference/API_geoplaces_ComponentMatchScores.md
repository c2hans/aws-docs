---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ComponentMatchScores.html
---

# ComponentMatchScores
<a name="API_geoplaces_ComponentMatchScores"></a>

Indicates how well the returned title and address components matches the input TextQuery. For each component a score is provied with 1 indicating all tokens were matched and 0 indicating no tokens were matched.

## Contents
<a name="API_geoplaces_ComponentMatchScores_Contents"></a>

 ** Address **   <a name="location-Type-geoplaces_ComponentMatchScores-Address"></a>
The place's address.
Type: [AddressComponentMatchScores](API_geoplaces_AddressComponentMatchScores.md) object
Required: No

 ** Title **   <a name="location-Type-geoplaces_ComponentMatchScores-Title"></a>
Indicates the match score of the title in the text query that match the found title.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: No

## See Also
<a name="API_geoplaces_ComponentMatchScores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/ComponentMatchScores)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/ComponentMatchScores)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/ComponentMatchScores)
