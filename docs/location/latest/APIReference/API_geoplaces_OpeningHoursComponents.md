---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_OpeningHoursComponents.html
---

# OpeningHoursComponents
<a name="API_geoplaces_OpeningHoursComponents"></a>

Components of the opening hours object.

## Contents
<a name="API_geoplaces_OpeningHoursComponents_Contents"></a>

 ** OpenDuration **   <a name="location-Type-geoplaces_OpeningHoursComponents-OpenDuration"></a>
String which represents the duration of the opening period, such as `"PT12H00M"`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** OpenTime **   <a name="location-Type-geoplaces_OpeningHoursComponents-OpenTime"></a>
String which represents the opening hours, such as `"T070000"`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 21.
Required: No

 ** Recurrence **   <a name="location-Type-geoplaces_OpeningHoursComponents-Recurrence"></a>
Days or periods when the provided opening hours are in affect.
Example: `FREQ:DAILY;BYDAY:MO,TU,WE,TH,SU`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

## See Also
<a name="API_geoplaces_OpeningHoursComponents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/OpeningHoursComponents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/OpeningHoursComponents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/OpeningHoursComponents)
