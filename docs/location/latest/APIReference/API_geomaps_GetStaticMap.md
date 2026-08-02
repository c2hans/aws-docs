---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetStaticMap.html
---

# GetStaticMap
<a name="API_geomaps_GetStaticMap"></a>

**Note**
This operation is not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.

 `GetStaticMap` provides high-quality static map images with customizable options. You can modify the map's appearance and overlay additional information. It's an ideal solution for applications requiring tailored static map snapshots.

For more information, see the following topics in the *Amazon Location Service Developer Guide*:
+  [Static maps](https://docs.aws.amazon.com/location/latest/developerguide/static-maps.html)
+  [Customize static maps](https://docs.aws.amazon.com/location/latest/developerguide/customizing-static-maps.html)
+  [Overlay on the static map](https://docs.aws.amazon.com/location/latest/developerguide/overlaying-static-map.html)

## Request Syntax
<a name="API_geomaps_GetStaticMap_RequestSyntax"></a>

```
GET /v2/static/{{FileName}}?bounded-positions={{BoundedPositions}}&bounding-box={{BoundingBox}}&center={{Center}}&color-scheme={{ColorScheme}}&compact-overlay={{CompactOverlay}}&crop-labels={{CropLabels}}&geojson-overlay={{GeoJsonOverlay}}&height={{Height}}&key={{Key}}&label-size={{LabelSize}}&lang={{Language}}&padding={{Padding}}&pois={{PointsOfInterests}}&political-view={{PoliticalView}}&radius={{Radius}}&scale-unit={{ScaleBarUnit}}&style={{Style}}&width={{Width}}&zoom={{Zoom}} HTTP/1.1
```

## URI Request Parameters
<a name="API_geomaps_GetStaticMap_RequestParameters"></a>

The request uses the following URI parameters.

 ** [BoundedPositions](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-BoundedPositions"></a>
Takes in two or more pair of coordinates in World Geodetic System (WGS 84) format: [longitude, latitude], with each coordinate separated by a comma. The API will generate an image to encompass all of the provided coordinates.
Cannot be used with `Zoom` and or `Radius`
Example: 97.170451,78.039098,99.045536,27.176178
Length Constraints: Minimum length of 0. Maximum length of 5000.
Pattern: `(-?\d{1,3}(\.\d{1,14})?,-?\d{1,2}(\.\d{1,14})?)(,(-?\d{1,3}(\.\d{1,14})?,-?\d{1,2}(\.\d{1,14})?))*`

 ** [BoundingBox](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-BoundingBox"></a>
Takes in two pairs of coordinates in World Geodetic System (WGS 84) format: [longitude, latitude], denoting south-westerly and north-easterly edges of the image. The underlying area becomes the view of the image.
Example: -123.17075,49.26959,-123.08125,49.31429
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `(-?\d{1,3}(\.\d{1,14})?,-?\d{1,2}(\.\d{1,14})?)(,(-?\d{1,3}(\.\d{1,14})?,-?\d{1,2}(\.\d{1,14})?))*`

 ** [Center](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-Center"></a>
Takes in a pair of coordinates in World Geodetic System (WGS 84) format: [longitude, latitude], which becomes the center point of the image. This parameter requires that either zoom or radius is set.
Cannot be used with `Zoom` and or `Radius`
Example: 49.295,-123.108
Length Constraints: Minimum length of 3. Maximum length of 36.
Pattern: `-?\d{1,3}(\.\d{1,14})?,-?\d{1,2}(\.\d{1,14})?`

 ** [ColorScheme](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-ColorScheme"></a>
Sets the color tone for the map, such as dark and light.
Example: `Light`
Default value: `Light`
Valid values for `ColorScheme` are case sensitive.
Valid Values: `Light | Dark`

 ** [CompactOverlay](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-CompactOverlay"></a>
Takes in a string to draw geometries on the image. The input is a comma separated format as follows format: `[Lon, Lat]`
Example: `line:-122.407653,37.798557,-122.413291,37.802443;color=%23DD0000;width=7;outline-color=#00DD00;outline-width=5yd|point:-122.40572,37.80004;label=Fog Hill Market;size=large;text-color=%23DD0000;color=#EE4B2B`
Currently it supports the following geometry types: point, line and polygon. It does not support multiPoint , multiLine and multiPolgyon.
Length Constraints: Minimum length of 1. Maximum length of 5000.

 ** [CropLabels](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-CropLabels"></a>
It is a flag that takes in true or false. It prevents the labels that are on the edge of the image from being cut or obscured.

 ** [FileName](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-FileName"></a>
The map scaling parameter to size the image, icons, and labels. It follows the pattern of `^map(@2x)?$`.
Example: `map, map@2x`
Pattern: `map(@2x)?`
Required: Yes

 ** [GeoJsonOverlay](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-GeoJsonOverlay"></a>
Takes in a string to draw geometries on the image. The input is a valid GeoJSON collection object.
Example: `{"type":"FeatureCollection","features": [{"type":"Feature","geometry":{"type":"MultiPoint","coordinates": [[-90.076345,51.504107],[-0.074451,51.506892]]},"properties": {"color":"#00DD00"}}]}`
Length Constraints: Minimum length of 1. Maximum length of 4200.

 ** [Height](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-Height"></a>
Specifies the height of the map image.
Valid Range: Minimum value of 64. Maximum value of 1400.
Required: Yes

 ** [Key](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-Key"></a>
Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [LabelSize](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-LabelSize"></a>
Overrides the label size auto-calculated by `FileName`. Takes in one of the values - `Small` or `Large`.
Valid Values: `Small | Large`

 ** [Language](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-Language"></a>
Specifies the language on the map labels using the BCP 47 language tag, limited to ISO 639-1 two-letter language codes. If the specified language data isn't available for the map image, the labels will default to the regional primary language.
Supported codes:
+  `ar`
+  `as`
+  `az`
+  `be`
+  `bg`
+  `bn`
+  `bs`
+  `ca`
+  `cs`
+  `cy`
+  `da`
+  `de`
+  `el`
+  `en`
+  `es`
+  `et`
+  `eu`
+  `fi`
+  `fo`
+  `fr`
+  `ga`
+  `gl`
+  `gn`
+  `gu`
+  `he`
+  `hi`
+  `hr`
+  `hu`
+  `hy`
+  `id`
+  `is`
+  `it`
+  `ja`
+  `ka`
+  `kk`
+  `km`
+  `kn`
+  `ko`
+  `ky`
+  `lt`
+  `lv`
+  `mk`
+  `ml`
+  `mr`
+  `ms`
+  `mt`
+  `my`
+  `nl`
+  `no`
+  `or`
+  `pa`
+  `pl`
+  `pt`
+  `ro`
+  `ru`
+  `sk`
+  `sl`
+  `sq`
+  `sr`
+  `sv`
+  `ta`
+  `te`
+  `th`
+  `tr`
+  `uk`
+  `uz`
+  `vi`
+  `zh`
Length Constraints: Minimum length of 2. Maximum length of 35.

 ** [Padding](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-Padding"></a>
Applies additional space (in pixels) around overlay feature to prevent them from being cut or obscured.
Value for max and min is determined by:
Min: `1`
Max: `min(height, width)/4`
Example: `100`
Valid Range: Minimum value of 0. Maximum value of 350.

 ** [PointsOfInterests](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-PointsOfInterests"></a>
Determines if the result image will display icons representing points of interest on the map.
Valid Values: `Enabled | Disabled`

 ** [PoliticalView](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-PoliticalView"></a>
Specifies the political view, using ISO 3166-2 or ISO 3166-3 country code format.
The following political views are currently supported:
+  `ARG`: Argentina's view on the Southern Patagonian Ice Field and Tierra Del Fuego, including the Falkland Islands, South Georgia, and South Sandwich Islands
+  `EGY`: Egypt's view on Bir Tawil
+  `IND`: India's view on Gilgit-Baltistan
+  `KEN`: Kenya's view on the Ilemi Triangle
+  `MAR`: Morocco's view on Western Sahara
+  `RUS`: Russia's view on Crimea
+  `SDN`: Sudan's view on the Halaib Triangle
+  `SRB`: Serbia's view on Kosovo, Vukovar, and Sarengrad Islands
+  `SUR`: Suriname's view on the Courantyne Headwaters and Lawa Headwaters
+  `SYR`: Syria's view on the Golan Heights
+  `TUR`: Turkey's view on Cyprus and Northern Cyprus
+  `TZA`: Tanzania's view on Lake Malawi
+  `URY`: Uruguay's view on Rincon de Artigas
+  `VNM`: Vietnam's view on the Paracel Islands and Spratly Islands
Length Constraints: Minimum length of 2. Maximum length of 3.
Pattern: `([A-Z]{2}|[A-Z]{3})`

 ** [Radius](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-Radius"></a>
Used with center parameter, it specifies the zoom of the image where you can control it on a granular level. Takes in any value `>= 1`.
Example: `1500`
Cannot be used with `Zoom`.
 **Unit**: `Meters`

Valid Range: Minimum value of 0. Maximum value of 4294967295.

 ** [ScaleBarUnit](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-ScaleBarUnit"></a>
Displays a scale on the bottom right of the map image with the unit specified in the input.
Example: `KilometersMiles, Miles, Kilometers, MilesKilometers`
Valid Values: `Kilometers | KilometersMiles | Miles | MilesKilometers`

 ** [Style](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-Style"></a>
 `Style` specifies the desired map style.
Valid Values: `Satellite | Standard`

 ** [Width](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-Width"></a>
Specifies the width of the map image.
Valid Range: Minimum value of 64. Maximum value of 1400.
Required: Yes

 ** [Zoom](#API_geomaps_GetStaticMap_RequestSyntax) **   <a name="location-geomaps_GetStaticMap-request-uri-Zoom"></a>
Specifies the zoom level of the map image.
Cannot be used with `Radius`.
Valid Range: Minimum value of 0. Maximum value of 20.

## Request Body
<a name="API_geomaps_GetStaticMap_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_geomaps_GetStaticMap_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{ContentType}}
Cache-Control: {{CacheControl}}
ETag: {{ETag}}
x-amz-geo-pricing-bucket: {{PricingBucket}}

{{Blob}}
```

## Response Elements
<a name="API_geomaps_GetStaticMap_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [CacheControl](#API_geomaps_GetStaticMap_ResponseSyntax) **   <a name="location-geomaps_GetStaticMap-response-CacheControl"></a>
Header that instructs caching configuration for the client.

 ** [ContentType](#API_geomaps_GetStaticMap_ResponseSyntax) **   <a name="location-geomaps_GetStaticMap-response-ContentType"></a>
Header that represents the format of the response. The response returns the following as the HTTP body.

 ** [ETag](#API_geomaps_GetStaticMap_ResponseSyntax) **   <a name="location-geomaps_GetStaticMap-response-ETag"></a>
The static map's Etag.

 ** [PricingBucket](#API_geomaps_GetStaticMap_ResponseSyntax) **   <a name="location-geomaps_GetStaticMap-response-PricingBucket"></a>
The pricing bucket for which the request is charged at.

The response returns the following as the HTTP body.

 ** [Blob](#API_geomaps_GetStaticMap_ResponseSyntax) **   <a name="location-geomaps_GetStaticMap-response-Blob"></a>
The blob represents a map image as a `jpeg` for the `GetStaticMap` API.

## Errors
<a name="API_geomaps_GetStaticMap_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
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
A message with the reason for the validation exception error.
 ** Reason **
The field where the invalid entry was detected.
HTTP Status Code: 400

## See Also
<a name="API_geomaps_GetStaticMap_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-maps-2020-11-19/GetStaticMap)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-maps-2020-11-19/GetStaticMap)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-maps-2020-11-19/GetStaticMap)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-maps-2020-11-19/GetStaticMap)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-maps-2020-11-19/GetStaticMap)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-maps-2020-11-19/GetStaticMap)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-maps-2020-11-19/GetStaticMap)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-maps-2020-11-19/GetStaticMap)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/geo-maps-2020-11-19/GetStaticMap)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-maps-2020-11-19/GetStaticMap)
