---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoplaces_GetPlace.html
---

# GetPlace
<a name="API_geoplaces_GetPlace"></a>

 `GetPlace` finds a place by its unique ID. A `PlaceId` is returned by other place operations.

For more information, see [GetPlace](https://docs.aws.amazon.com/location/latest/developerguide/get-place.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_geoplaces_GetPlace_RequestSyntax"></a>

```
GET /v2/place/{{PlaceId}}?additional-features={{AdditionalFeatures}}&address-names-mode={{AddressNamesMode}}&intended-use={{IntendedUse}}&key={{Key}}&language={{Language}}&political-view={{PoliticalView}} HTTP/1.1
```

## URI Request Parameters
<a name="API_geoplaces_GetPlace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AdditionalFeatures](#API_geoplaces_GetPlace_RequestSyntax) **   <a name="location-geoplaces_GetPlace-request-uri-AdditionalFeatures"></a>
 A list of optional additional parameters such as time zone that can be requested for each result. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions support only the `TimeZone` value.
Array Members: Minimum number of 1 item. Maximum number of 6 items.
Valid Values: `TimeZone | Phonemes | Access | Contact | SecondaryAddresses | CrossReferences`

 ** [AddressNamesMode](#API_geoplaces_GetPlace_RequestSyntax) **   <a name="location-geoplaces_GetPlace-request-uri-AddressNamesMode"></a>
Specifies how address names are returned. When set to `Administrative`, the service returns the official administrative names for address components. `Administrative` currently applies only to addresses in the United States.
Valid Values: `Administrative`

 ** [IntendedUse](#API_geoplaces_GetPlace_RequestSyntax) **   <a name="location-geoplaces_GetPlace-request-uri-IntendedUse"></a>
 Indicates if the query results will be persisted in customer infrastructure. Defaults to `SingleUse` (not stored). If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
When storing `GetPlace` responses, you *must* set this field to `Storage` to comply with the terms of service. These requests will be charged at a higher rate. Please review the [user agreement](https://aws.amazon.com/location/sla/) and [service pricing structure](https://aws.amazon.com/location/pricing/) to determine the correct setting for your use case.
Valid Values: `SingleUse | Storage`

 ** [Key](#API_geoplaces_GetPlace_RequestSyntax) **   <a name="location-geoplaces_GetPlace-request-uri-Key"></a>
Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [Language](#API_geoplaces_GetPlace_RequestSyntax) **   <a name="location-geoplaces_GetPlace-request-uri-Language"></a>
 A list of [BCP 47](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions support only the following codes: `en, id, km, lo, ms, my, pt, th, tl, vi, zh`
Length Constraints: Minimum length of 2. Maximum length of 35.

 ** [PlaceId](#API_geoplaces_GetPlace_RequestSyntax) **   <a name="location-geoplaces_GetPlace-request-uri-PlaceId"></a>
The `PlaceId` of the place you wish to receive the information for.
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: Yes

 ** [PoliticalView](#API_geoplaces_GetPlace_RequestSyntax) **   <a name="location-geoplaces_GetPlace-request-uri-PoliticalView"></a>
 The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `([A-Z]{2}|[A-Z]{3})`

## Request Body
<a name="API_geoplaces_GetPlace_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_geoplaces_GetPlace_ResponseSyntax"></a>

```
HTTP/1.1 200
x-amz-geo-pricing-bucket: {{PricingBucket}}
Content-type: application/json

{
   "AccessPoints": [
      {
         "Label": "string",
         "Position": [ number ],
         "Primary": boolean,
         "Type": "string"
      }
   ],
   "AccessRestrictions": [
      {
         "Categories": [
            {
               "Id": "string",
               "LocalizedName": "string",
               "Name": "string",
               "Primary": boolean
            }
         ],
         "Restricted": boolean
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
   "BusinessChains": [
      {
         "Id": "string",
         "Name": "string"
      }
   ],
   "Categories": [
      {
         "Id": "string",
         "LocalizedName": "string",
         "Name": "string",
         "Primary": boolean
      }
   ],
   "Contacts": {
      "Emails": [
         {
            "Categories": [
               {
                  "Id": "string",
                  "LocalizedName": "string",
                  "Name": "string",
                  "Primary": boolean
               }
            ],
            "Label": "string",
            "Value": "string"
         }
      ],
      "Faxes": [
         {
            "Categories": [
               {
                  "Id": "string",
                  "LocalizedName": "string",
                  "Name": "string",
                  "Primary": boolean
               }
            ],
            "Label": "string",
            "Value": "string"
         }
      ],
      "Phones": [
         {
            "Categories": [
               {
                  "Id": "string",
                  "LocalizedName": "string",
                  "Name": "string",
                  "Primary": boolean
               }
            ],
            "Label": "string",
            "Value": "string"
         }
      ],
      "Websites": [
         {
            "Categories": [
               {
                  "Id": "string",
                  "LocalizedName": "string",
                  "Name": "string",
                  "Primary": boolean
               }
            ],
            "Label": "string",
            "Value": "string"
         }
      ]
   },
   "CrossReferences": [
      {
         "Source": "string",
         "SourceCategories": [
            {
               "Id": "string",
               "LocalizedName": "string",
               "Name": "string",
               "Primary": boolean
            }
         ],
         "SourcePlaceId": "string"
      }
   ],
   "EstimatedPointAddress": boolean,
   "FoodTypes": [
      {
         "Id": "string",
         "LocalizedName": "string",
         "Primary": boolean
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
   "OpeningHours": [
      {
         "Categories": [
            {
               "Id": "string",
               "LocalizedName": "string",
               "Name": "string",
               "Primary": boolean
            }
         ],
         "Components": [
            {
               "OpenDuration": "string",
               "OpenTime": "string",
               "Recurrence": "string"
            }
         ],
         "Display": [ "string" ],
         "OpenNow": boolean
      }
   ],
   "Phonemes": {
      "Address": {
         "Block": [
            {
               "Language": "string",
               "Preferred": boolean,
               "Value": "string"
            }
         ],
         "Country": [
            {
               "Language": "string",
               "Preferred": boolean,
               "Value": "string"
            }
         ],
         "District": [
            {
               "Language": "string",
               "Preferred": boolean,
               "Value": "string"
            }
         ],
         "Locality": [
            {
               "Language": "string",
               "Preferred": boolean,
               "Value": "string"
            }
         ],
         "Region": [
            {
               "Language": "string",
               "Preferred": boolean,
               "Value": "string"
            }
         ],
         "Street": [
            {
               "Language": "string",
               "Preferred": boolean,
               "Value": "string"
            }
         ],
         "SubBlock": [
            {
               "Language": "string",
               "Preferred": boolean,
               "Value": "string"
            }
         ],
         "SubDistrict": [
            {
               "Language": "string",
               "Preferred": boolean,
               "Value": "string"
            }
         ],
         "SubRegion": [
            {
               "Language": "string",
               "Preferred": boolean,
               "Value": "string"
            }
         ]
      },
      "Title": [
         {
            "Language": "string",
            "Preferred": boolean,
            "Value": "string"
         }
      ]
   },
   "PlaceAttributes": [ "string" ],
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
   "SecondaryAddresses": [
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
         "PlaceId": "string",
         "PlaceType": "string",
         "Position": [ number ],
         "Title": "string"
      }
   ],
   "TimeZone": {
      "Name": "string",
      "Offset": "string",
      "OffsetSeconds": number
   },
   "Title": "string"
}
```

## Response Elements
<a name="API_geoplaces_GetPlace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [PricingBucket](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-PricingBucket"></a>
The pricing bucket for which the query is charged at.
For more information on pricing, please visit [Amazon Location Service Pricing](https://aws.amazon.com/location/pricing/).

The following data is returned in JSON format by the service.

 ** [AccessPoints](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-AccessPoints"></a>
 Position of the access point in World Geodetic System (WGS 84) format: [longitude, latitude]. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: Array of [AccessPoint](API_geoplaces_AccessPoint.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [AccessRestrictions](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-AccessRestrictions"></a>
 Indicates known access restrictions on a vehicle access point. The index correlates to an access point and indicates if access through this point has some form of restriction. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: Array of [AccessRestriction](API_geoplaces_AccessRestriction.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [Address](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-Address"></a>
The place's address.
Type: [Address](API_geoplaces_Address.md) object

 ** [AddressNumberCorrected](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-AddressNumberCorrected"></a>
 Boolean indicating if the address provided has been corrected. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: Boolean

 ** [BusinessChains](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-BusinessChains"></a>
The Business Chains associated with the place.
Type: Array of [BusinessChain](API_geoplaces_BusinessChain.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [Categories](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-Categories"></a>
Categories of results that results must belong to.
Type: Array of [Category](API_geoplaces_Category.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [Contacts](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-Contacts"></a>
 List of potential contact methods for the place or result. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: [Contacts](API_geoplaces_Contacts.md) object

 ** [CrossReferences](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-CrossReferences"></a>
The list of supplier references available for this place. Requires the `CrossReferences` additional feature to be enabled.
Type: Array of [CrossReference](API_geoplaces_CrossReference.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [EstimatedPointAddress](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-EstimatedPointAddress"></a>
If `true`, indicates that the coordinates of the position and access points of the point address are estimated.
Type: Boolean

 ** [FoodTypes](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-FoodTypes"></a>
 List of food types offered by this result. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: Array of [FoodType](API_geoplaces_FoodType.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [MainAddress](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-MainAddress"></a>
 The main address corresponding to a place of type Secondary Address. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: [RelatedPlace](API_geoplaces_RelatedPlace.md) object

 ** [MapView](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-MapView"></a>
The bounding box enclosing the geometric shape (area or line) that an individual result covers.
The bounding box formed is defined as a set of four coordinates: `[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]`
Type: Array of doubles
Array Members: Fixed number of 4 items.

 ** [OpeningHours](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-OpeningHours"></a>
 List of opening hours objects. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: Array of [OpeningHours](API_geoplaces_OpeningHours.md) objects
Array Members: Minimum number of 1 item. Maximum number of 100 items.

 ** [Phonemes](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-Phonemes"></a>
 How the various components of the result's address are pronounced in various languages. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: [PhonemeDetails](API_geoplaces_PhonemeDetails.md) object

 ** [PlaceAttributes](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-PlaceAttributes"></a>
A list of place attributes for the result, such as whether the business offers drive-through service.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Valid Values: `DriveThrough`

 ** [PlaceId](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-PlaceId"></a>
The `PlaceId` of the place you wish to receive the information for.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [PlaceType](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-PlaceType"></a>
A `PlaceType` is a category that the result place must belong to.
Type: String
Valid Values: `Country | Region | SubRegion | Locality | District | SubDistrict | PostalCode | Block | SubBlock | Intersection | Street | PointOfInterest | PointAddress | InterpolatedAddress | SecondaryAddress | InferredSecondaryAddress`

 ** [PoliticalView](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-PoliticalView"></a>
 The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `[A-Z]{3}`

 ** [Position](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-Position"></a>
The position in World Geodetic System (WGS 84) format: [longitude, latitude].
Type: Array of doubles
Array Members: Fixed number of 2 items.

 ** [PostalCodeDetails](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-PostalCodeDetails"></a>
 Contains details about the postal code of the place or result. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Type: Array of [PostalCodeDetails](API_geoplaces_PostalCodeDetails.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [SecondaryAddresses](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-SecondaryAddresses"></a>
 All secondary addresses that are associated with a main address. A secondary address is one that includes secondary designators, such as a Suite or Unit Number, Building, or Floor information. If you use [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html), the `ap-southeast-1` and `ap-southeast-5` AWS Regions do not support this parameter.
Coverage for this functionality is available in the following countries: AUS, CAN, NZL, USA, PRI.
Type: Array of [RelatedPlace](API_geoplaces_RelatedPlace.md) objects
Array Members: Minimum number of 1 item.

 ** [TimeZone](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-TimeZone"></a>
The time zone in which the place is located.
Type: [TimeZone](API_geoplaces_TimeZone.md) object

 ** [Title](#API_geoplaces_GetPlace_ResponseSyntax) **   <a name="location-geoplaces_GetPlace-response-Title"></a>
The localized display name of this result item based on request parameter `language`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.

## Errors
<a name="API_geoplaces_GetPlace_Errors"></a>

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
<a name="API_geoplaces_GetPlace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-places-2020-11-19/GetPlace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-places-2020-11-19/GetPlace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-places-2020-11-19/GetPlace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-places-2020-11-19/GetPlace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-places-2020-11-19/GetPlace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-places-2020-11-19/GetPlace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-places-2020-11-19/GetPlace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-places-2020-11-19/GetPlace)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/geo-places-2020-11-19/GetPlace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-places-2020-11-19/GetPlace)
