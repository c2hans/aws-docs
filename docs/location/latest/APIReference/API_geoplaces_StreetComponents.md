---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_StreetComponents.html
---

# StreetComponents
<a name="API_geoplaces_StreetComponents"></a>

Components of a street.

## Contents
<a name="API_geoplaces_StreetComponents_Contents"></a>

 ** BaseName **   <a name="location-Type-geoplaces_StreetComponents-BaseName"></a>
Base name part of the street name.
Example: Younge from the "Younge street".
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Required: No

 ** Direction **   <a name="location-Type-geoplaces_StreetComponents-Direction"></a>
Indicates the official directional identifiers assigned to highways.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

 ** Language **   <a name="location-Type-geoplaces_StreetComponents-Language"></a>
A [BCP 47](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Required: No

 ** Prefix **   <a name="location-Type-geoplaces_StreetComponents-Prefix"></a>
A prefix is a directional identifier that precedes, but is not included in, the base name of a road.
Example: E for East.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

 ** Suffix **   <a name="location-Type-geoplaces_StreetComponents-Suffix"></a>
A suffix is a directional identifier that follows, but is not included in, the base name of a road.
Example W for West.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

 ** Type **   <a name="location-Type-geoplaces_StreetComponents-Type"></a>
Street type part of the street name.
Example: `"avenue"`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

 ** TypePlacement **   <a name="location-Type-geoplaces_StreetComponents-TypePlacement"></a>
Defines if the street type is before or after the base name.
Type: String
Valid Values: `BeforeBaseName | AfterBaseName`
Required: No

 ** TypeSeparator **   <a name="location-Type-geoplaces_StreetComponents-TypeSeparator"></a>
Defines a separator character such as `""` or `" "` between the base name and type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1.
Pattern: `$|^ `
Required: No

## See Also
<a name="API_geoplaces_StreetComponents_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/StreetComponents)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/StreetComponents)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/StreetComponents)
