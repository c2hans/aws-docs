---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_TranslationDetails.html
---

# TranslationDetails
<a name="API_geoplaces_TranslationDetails"></a>

Translation details for the address, including alternative names and translations in available languages.

## Contents
<a name="API_geoplaces_TranslationDetails_Contents"></a>

 ** District **   <a name="location-Type-geoplaces_TranslationDetails-District"></a>
A list of administrative names and translations for the district address component.
Type: Array of [AdminNames](API_geoplaces_AdminNames.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** Locality **   <a name="location-Type-geoplaces_TranslationDetails-Locality"></a>
A list of administrative names and translations for the locality address component.
Type: Array of [AdminNames](API_geoplaces_AdminNames.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** Region **   <a name="location-Type-geoplaces_TranslationDetails-Region"></a>
A list of administrative names and translations for the region address component.
Type: Array of [AdminNames](API_geoplaces_AdminNames.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

 ** SubRegion **   <a name="location-Type-geoplaces_TranslationDetails-SubRegion"></a>
A list of administrative names and translations for the sub-region address component.
Type: Array of [AdminNames](API_geoplaces_AdminNames.md) objects
Array Members: Minimum number of 1 item. Maximum number of 2 items.
Required: No

## See Also
<a name="API_geoplaces_TranslationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/TranslationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/TranslationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/TranslationDetails)
