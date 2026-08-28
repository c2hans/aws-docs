---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_AddressComponentPhonemes.html
---

# AddressComponentPhonemes
<a name="API_geoplaces_AddressComponentPhonemes"></a>

How to pronounce the various components of the address or place.

## Contents
<a name="API_geoplaces_AddressComponentPhonemes_Contents"></a>

 ** Block **   <a name="location-Type-geoplaces_AddressComponentPhonemes-Block"></a>
How to pronounce the name of the block.
Type: Array of [PhonemeTranscription](API_geoplaces_PhonemeTranscription.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** Country **   <a name="location-Type-geoplaces_AddressComponentPhonemes-Country"></a>
The alpha-2 or alpha-3 character code for the country that the results will be present in.
Type: Array of [PhonemeTranscription](API_geoplaces_PhonemeTranscription.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** District **   <a name="location-Type-geoplaces_AddressComponentPhonemes-District"></a>
How to pronounce the district or division of a city results should be present in.
Type: Array of [PhonemeTranscription](API_geoplaces_PhonemeTranscription.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** Locality **   <a name="location-Type-geoplaces_AddressComponentPhonemes-Locality"></a>
How to pronounce the city or locality results should be present in.
Example: `Vancouver`.
Type: Array of [PhonemeTranscription](API_geoplaces_PhonemeTranscription.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** Region **   <a name="location-Type-geoplaces_AddressComponentPhonemes-Region"></a>
How to pronounce the region or state results should be to be present in.
Type: Array of [PhonemeTranscription](API_geoplaces_PhonemeTranscription.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** Street **   <a name="location-Type-geoplaces_AddressComponentPhonemes-Street"></a>
How to pronounce the name of the street results should be present in.
Type: Array of [PhonemeTranscription](API_geoplaces_PhonemeTranscription.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** SubBlock **   <a name="location-Type-geoplaces_AddressComponentPhonemes-SubBlock"></a>
How to pronounce the name of the sub-block.
Type: Array of [PhonemeTranscription](API_geoplaces_PhonemeTranscription.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** SubDistrict **   <a name="location-Type-geoplaces_AddressComponentPhonemes-SubDistrict"></a>
How to pronounce the sub-district or division of a city results should be present in.
Type: Array of [PhonemeTranscription](API_geoplaces_PhonemeTranscription.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** SubRegion **   <a name="location-Type-geoplaces_AddressComponentPhonemes-SubRegion"></a>
How to pronounce the sub-region or county for which results should be present in.
Type: Array of [PhonemeTranscription](API_geoplaces_PhonemeTranscription.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## See Also
<a name="API_geoplaces_AddressComponentPhonemes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/AddressComponentPhonemes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/AddressComponentPhonemes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/AddressComponentPhonemes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
