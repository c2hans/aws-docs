---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_PostalCodeDetails.html
---

# PostalCodeDetails
<a name="API_geoplaces_PostalCodeDetails"></a>

Contains details about the postal code of the place or result.

## Contents
<a name="API_geoplaces_PostalCodeDetails_Contents"></a>

 ** PostalAuthority **   <a name="location-Type-geoplaces_PostalCodeDetails-PostalAuthority"></a>
The postal authority or entity. This could be a governmental authority, a regulatory authority, or a designated postal operator.
Type: String
Valid Values: `Usps`
Required: No

 ** PostalCode **   <a name="location-Type-geoplaces_PostalCodeDetails-PostalCode"></a>
An alphanumeric string included in a postal address to facilitate mail sorting, such as post code, postcode, or ZIP code for which the result should possess.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Required: No

 ** PostalCodeType **   <a name="location-Type-geoplaces_PostalCodeDetails-PostalCodeType"></a>
The postal code type.
Type: String
Valid Values: `UspsZip | UspsZipPlus4`
Required: No

 ** UspsZip **   <a name="location-Type-geoplaces_PostalCodeDetails-UspsZip"></a>
The ZIP Classification Code, or in other words what type of postal code is it.
Type: [UspsZip](API_geoplaces_UspsZip.md) object
Required: No

 ** UspsZipPlus4 **   <a name="location-Type-geoplaces_PostalCodeDetails-UspsZipPlus4"></a>
The USPS ZIP\+4 Record Type Code.
Type: [UspsZipPlus4](API_geoplaces_UspsZipPlus4.md) object
Required: No

## See Also
<a name="API_geoplaces_PostalCodeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/PostalCodeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/PostalCodeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/PostalCodeDetails)
