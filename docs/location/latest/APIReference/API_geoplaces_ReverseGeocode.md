---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_ReverseGeocode.html
---

# ReverseGeocode
<a name="API_geoplaces_ReverseGeocode"></a>

 `ReverseGeocode` converts geographic coordinates into a human-readable address or place. You can obtain address component, and other related information such as place type, category, street information. The Reverse Geocode API supports filtering to on place type so that you can refine result based on your need. Also, The Reverse Geocode API can also provide additional features such as time zone information and the inclusion of political views.

For more information, see [Reverse Geocode](https://docs.aws.amazon.com/location/latest/developerguide/reverse-geocode.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_geoplaces_ReverseGeocode_RequestSyntax"></a>

```
POST /v2/reverse-geocode?key={{Key}} HTTP/1.1
Content-type: application/json

{
   "AdditionalFeatures": [ "{{string}}" ],
   "AddressNamesMode": "{{string}}",
   "Filter": {
      "IncludePlaceTypes": [ "{{string}}" ]
   },
   "Heading": {{number}},
   "IntendedUse": "{{string}}",
   "Language": "{{string}}",
   "MaxResults": {{number}},
   "PoliticalView": "{{string}}",
   "QueryPosition": [ {{number}} ],
   "QueryRadius": {{number}}
}
```

## URI Request Parameters
<a name="API_geoplaces_ReverseGeocode_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Key](#API_geoplaces_ReverseGeocode_RequestSyntax) **   <a name="location-geoplaces_ReverseGeocode-request-uri-Key"></a>
Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

## Request Body
<a name="API_geoplaces_ReverseGeocode_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AdditionalFeatures](#API_geoplaces_ReverseGeocode_RequestSyntax) **   <a name="location-geoplaces_ReverseGeocode-request-AdditionalFeatures"></a>
 A list of optional additional parameters, such as time zone that can be requested for each result. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions support only the `TimeZone` value.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 3 items.
Valid Values: `TimeZone | Access | Intersections`
Required: No

 ** [AddressNamesMode](#API_geoplaces_ReverseGeocode_RequestSyntax) **   <a name="location-geoplaces_ReverseGeocode-request-AddressNamesMode"></a>
Specifies how address names are returned. When set to `Administrative`, the service returns the official administrative names for address components. `Administrative` currently applies only to addresses in the United States.
Type: String
Valid Values: `Administrative`
Required: No

 ** [Filter](#API_geoplaces_ReverseGeocode_RequestSyntax) **   <a name="location-geoplaces_ReverseGeocode-request-Filter"></a>
A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.
Type: [ReverseGeocodeFilter](API_geoplaces_ReverseGeocodeFilter.md) object
Required: No

 ** [Heading](#API_geoplaces_ReverseGeocode_RequestSyntax) **   <a name="location-geoplaces_ReverseGeocode-request-Heading"></a>
The heading in degrees from true north in a navigation context. The heading is measured as the angle clockwise from the North direction.
Example: North is `0` degrees, East is `90` degrees, South is `180` degrees, and West is `270` degrees.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 360.0.
Required: No

 ** [IntendedUse](#API_geoplaces_ReverseGeocode_RequestSyntax) **   <a name="location-geoplaces_ReverseGeocode-request-IntendedUse"></a>
 Indicates if the query results will be persisted in customer infrastructure. Defaults to `SingleUse` (not stored).
When storing `ReverseGeocode` responses, you *must* set this field to `Storage` to comply with the terms of service. These requests will be charged at a higher rate. Please review the [user agreement](https://aws.amazon.com/location/sla/) and [service pricing structure](https://aws.amazon.com/location/pricing/) to determine the correct setting for your use case.
Type: String
Valid Values: `SingleUse | Storage`
Required: No

 ** [Language](#API_geoplaces_ReverseGeocode_RequestSyntax) **   <a name="location-geoplaces_ReverseGeocode-request-Language"></a>
 A list of [BCP 47](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions support only the following codes: `en, id, km, lo, ms, my, pt, th, tl, vi, zh`
Type: String
Length Constraints: Minimum length of 2. Maximum length of 35.
Required: No

 ** [MaxResults](#API_geoplaces_ReverseGeocode_RequestSyntax) **   <a name="location-geoplaces_ReverseGeocode-request-MaxResults"></a>
 An optional limit for the number of results returned in a single call.
Default value: 1
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [PoliticalView](#API_geoplaces_ReverseGeocode_RequestSyntax) **   <a name="location-geoplaces_ReverseGeocode-request-PoliticalView"></a>
 The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `([A-Z]{2}|[A-Z]{3})`
Required: No

 ** [QueryPosition](#API_geoplaces_ReverseGeocode_RequestSyntax) **   <a name="location-geoplaces_ReverseGeocode-request-QueryPosition"></a>
The position in World Geodetic System (WGS 84) format: [longitude, latitude] for which you are querying nearby results for. Results closer to the position will be ranked higher then results further away from the position
Type: Array of doubles
Array Members: Fixed number of 2 items.
Required: Yes

 ** [QueryRadius](#API_geoplaces_ReverseGeocode_RequestSyntax) **   <a name="location-geoplaces_ReverseGeocode-request-QueryRadius"></a>
 The maximum distance in meters from the QueryPosition from which a result will be returned. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions support only up to a maximum value of 100,000.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 21000000.
Required: No

## Response Syntax
<a name="API_geoplaces_ReverseGeocode_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-geo-pricing-bucket: {{PricingBucket}}
Content-type: application/json

{
   "ResultItems": [
      {
         "AccessPoints": [
            {
               "Label": "string",
               "Position": [ number ],
               "Primary": boolean,
               "Type": "string"
            }
         ],
         "Address": {
            "AddressNumber": "string",
            "Block": "string",
            "Building": "string",
            "Country": {
               "Code2": "string",
               "Code3": "string",
               "Name": "string"
            },
            "District": "string",
            "Intersection": [ "string" ],
            "Label": "string",
            "Locality": "string",
            "PostalCode": "string",
            "Region": {
               "Code": "string",
               "Name": "string"
            },
            "SecondaryAddressComponents": [
               {
                  "Designator": "string",
                  "Number": "string"
               }
            ],
            "Street": "string",
            "StreetComponents": [
               {
                  "BaseName": "string",
                  "Direction": "string",
                  "Language": "string",
                  "Prefix": "string",
                  "Suffix": "string",
                  "Type": "string",
                  "TypePlacement": "string",
                  "TypeSeparator": "string"
               }
            ],
            "SubBlock": "string",
            "SubDistrict": "string",
            "SubRegion": {
               "Code": "string",
               "Name": "string"
            }
         },
         "AddressNumberCorrected": boolean,
         "Categories": [
            {
               "Id": "string",
               "LocalizedName": "string",
               "Name": "string",
               "Primary": boolean
            }
         ],
         "Distance": number,
         "EstimatedPointAddress": boolean,
         "FoodTypes": [
            {
               "Id": "string",
               "LocalizedName": "string",
               "Primary": boolean
            }
         ],
         "Intersections": [
            {
               "AccessPoints": [
                  {
                     "Label": "string",
                     "Position": [ number ],
                     "Primary": boolean,
                     "Type": "string"
                  }
               ],
               "Address": {
                  "AddressNumber": "string",
                  "Block": "string",
                  "Building": "string",
                  "Country": {
                     "Code2": "string",
                     "Code3": "string",
                     "Name": "string"
                  },
                  "District": "string",
                  "Intersection": [ "string" ],
                  "Label": "string",
                  "Locality": "string",
                  "PostalCode": "string",
                  "Region": {
                     "Code": "string",
                     "Name": "string"
                  },
                  "SecondaryAddressComponents": [
                     {
                        "Designator": "string",
                        "Number": "string"
                     }
                  ],
                  "Street": "string",
                  "StreetComponents": [
                     {
                        "BaseName": "string",
                        "Direction": "string",
                        "Language": "string",
                        "Prefix": "string",
                        "Suffix": "string",
                        "Type": "string",
                        "TypePlacement": "string",
                        "TypeSeparator": "string"
                     }
                  ],
                  "SubBlock": "string",
                  "SubDistrict": "string",
                  "SubRegion": {
                     "Code": "string",
                     "Name": "string"
                  }
               },
               "Distance": number,
               "MapView": [ number ],
               "PlaceId": "string",
               "Position": [ number ],
               "RouteDistance": number,
               "Title": "string"
            }
         ],
         "MainAddress": {
            "AccessPoints": [
               {
                  "Label": "string",
                  "Position": [ number ],
                  "Primary": boolean,
                  "Type": "string"
               }
            ],
            "Address": {
               "AddressNumber": "string",
               "Block": "string",
               "Building": "string",
               "Country": {
                  "Code2": "string",
                  "Code3": "string",
                  "Name": "string"
               },
               "District": "string",
               "Intersection": [ "string" ],
               "Label": "string",
               "Locality": "string",
               "PostalCode": "string",
               "Region": {
                  "Code": "string",
                  "Name": "string"
               },
               "SecondaryAddressComponents": [
                  {
                     "Designator": "string",
                     "Number": "string"
                  }
               ],
               "Street": "string",
               "StreetComponents": [
                  {
                     "BaseName": "string",
                     "Direction": "string",
                     "Language": "string",
                     "Prefix": "string",
                     "Suffix": "string",
                     "Type": "string",
                     "TypePlacement": "string",
                     "TypeSeparator": "string"
                  }
               ],
               "SubBlock": "string",
               "SubDistrict": "string",
               "SubRegion": {
                  "Code": "string",
                  "Name": "string"
               }
            },
            "PlaceId": "string",
            "PlaceType": "string",
            "Position": [ number ],
            "Title": "string"
         },
         "MapView": [ number ],
         "PlaceId": "string",
         "PlaceType": "string",
         "PoliticalView": "string",
         "Position": [ number ],
         "PostalCodeDetails": [
            {
               "PostalAuthority": "string",
               "PostalCode": "string",
               "PostalCodeType": "string",
               "UspsZip": {
                  "ZipClassificationCode": "string"
               },
               "UspsZipPlus4": {
                  "RecordTypeCode": "string"
               }
            }
         ],
         "TimeZone": {
            "Name": "string",
            "Offset": "string",
            "OffsetSeconds": number
         },
         "Title": "string"
      }
   ]
}
```

## Response Elements
<a name="API_geoplaces_ReverseGeocode_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [PricingBucket](#API_geoplaces_ReverseGeocode_ResponseSyntax) **   <a name="location-geoplaces_ReverseGeocode-response-PricingBucket"></a>
The pricing bucket for which the query is charged at.
For more information on pricing, please visit [Amazon Location Service Pricing](https://aws.amazon.com/location/pricing/).

The following data is returned in JSON format by the service.

 ** [ResultItems](#API_geoplaces_ReverseGeocode_ResponseSyntax) **   <a name="location-geoplaces_ReverseGeocode-response-ResultItems"></a>
List of places or results returned for a query.
Type: Array of [ReverseGeocodeResultItem](API_geoplaces_ReverseGeocodeResultItem.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

## Errors
<a name="API_geoplaces_ReverseGeocode_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** FieldList **
Test stub for FieldList.
 ** Reason **
Test stub for reason
HTTP Status Code: 400

## See Also
<a name="API_geoplaces_ReverseGeocode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-places-2020-11-19/ReverseGeocode)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-places-2020-11-19/ReverseGeocode)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/ReverseGeocode)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-places-2020-11-19/ReverseGeocode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/ReverseGeocode)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-places-2020-11-19/ReverseGeocode)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-places-2020-11-19/ReverseGeocode)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-places-2020-11-19/ReverseGeocode)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/geo-places-2020-11-19/ReverseGeocode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/ReverseGeocode)
