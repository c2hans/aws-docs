---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_PhonemeTranscription.html
---

# PhonemeTranscription
<a name="API_geoplaces_PhonemeTranscription"></a>

How to pronounce the various components of the address or place.

## Contents
<a name="API_geoplaces_PhonemeTranscription_Contents"></a>

 ** Language **   <a name="location-Type-geoplaces_PhonemeTranscription-Language"></a>
A list of [BCP 47](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Required: No

 ** Preferred **   <a name="location-Type-geoplaces_PhonemeTranscription-Preferred"></a>
Boolean which indicates if it the preferred pronunciation.
Type: Boolean
Required: No

 ** Value **   <a name="location-Type-geoplaces_PhonemeTranscription-Value"></a>
Value which indicates how to pronounce the value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

## See Also
<a name="API_geoplaces_PhonemeTranscription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/PhonemeTranscription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/PhonemeTranscription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/PhonemeTranscription)
