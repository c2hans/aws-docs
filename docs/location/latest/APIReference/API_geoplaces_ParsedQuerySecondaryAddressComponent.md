---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ParsedQuerySecondaryAddressComponent.html
---

# ParsedQuerySecondaryAddressComponent
<a name="API_geoplaces_ParsedQuerySecondaryAddressComponent"></a>

Information about a secondary address component parsed from the query text.

## Contents
<a name="API_geoplaces_ParsedQuerySecondaryAddressComponent_Contents"></a>

 ** Designator **   <a name="location-Type-geoplaces_ParsedQuerySecondaryAddressComponent-Designator"></a>
Secondary address designator provided in the query.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4.
Required: Yes

 ** EndIndex **   <a name="location-Type-geoplaces_ParsedQuerySecondaryAddressComponent-EndIndex"></a>
End index of the parsed secondary address component in the query text.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** Number **   <a name="location-Type-geoplaces_ParsedQuerySecondaryAddressComponent-Number"></a>
Secondary address number provided in the query.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10.
Required: Yes

 ** StartIndex **   <a name="location-Type-geoplaces_ParsedQuerySecondaryAddressComponent-StartIndex"></a>
Start index of the parsed secondary address component in the query text.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** Value **   <a name="location-Type-geoplaces_ParsedQuerySecondaryAddressComponent-Value"></a>
Value of the parsed secondary address component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: Yes

## See Also
<a name="API_geoplaces_ParsedQuerySecondaryAddressComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/ParsedQuerySecondaryAddressComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/ParsedQuerySecondaryAddressComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/ParsedQuerySecondaryAddressComponent)
