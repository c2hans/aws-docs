---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetStyleDescriptor.html
---

# GetStyleDescriptor
<a name="API_geomaps_GetStyleDescriptor"></a>

 `GetStyleDescriptor` returns information about the style.

For more information, see [Style dynamic maps](https://docs.aws.amazon.com/location/latest/developerguide/styling-dynamic-maps.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_geomaps_GetStyleDescriptor_RequestSyntax"></a>

```
GET /v2/styles/{{Style}}/descriptor?buildings={{Buildings}}&color-scheme={{ColorScheme}}&contour-density={{ContourDensity}}&key={{Key}}&poi-categories={{PoiCategories}}&poi-density={{PoiDensity}}&political-view={{PoliticalView}}&terrain={{Terrain}}&traffic={{Traffic}}&travel-modes={{TravelModes}} HTTP/1.1
```

## URI Request Parameters
<a name="API_geomaps_GetStyleDescriptor_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Buildings](#API_geomaps_GetStyleDescriptor_RequestSyntax) **   <a name="location-geomaps_GetStyleDescriptor-request-uri-Buildings"></a>
Adjusts how building details are rendered on the map.
The following building styles are currently supported:
+  `Buildings3D`: Displays buildings as three-dimensional extrusions on the map.
 `Buildings3D` is valid only for the `Standard` and `Monochrome` map styles.
Valid Values: `Buildings3D`

 ** [ColorScheme](#API_geomaps_GetStyleDescriptor_RequestSyntax) **   <a name="location-geomaps_GetStyleDescriptor-request-uri-ColorScheme"></a>
Sets the color tone for the map, such as dark and light.
Example: `Light`
Default value: `Light`
Valid values for ColorScheme are case sensitive.
Valid Values: `Light | Dark`

 ** [ContourDensity](#API_geomaps_GetStyleDescriptor_RequestSyntax) **   <a name="location-geomaps_GetStyleDescriptor-request-uri-ContourDensity"></a>
Displays the shape and steepness of terrain features using elevation lines. The density value controls how densely the available contour line information is rendered on the map. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
This parameter is valid for all map styles except `Satellite`.
Valid Values: `Low | Medium | High`

 ** [Key](#API_geomaps_GetStyleDescriptor_RequestSyntax) **   <a name="location-geomaps_GetStyleDescriptor-request-uri-Key"></a>
Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [PoiCategories](#API_geomaps_GetStyleDescriptor_RequestSyntax) **   <a name="location-geomaps_GetStyleDescriptor-request-uri-PoiCategories"></a>
Renders only the specified categories of points of interest. When you omit this parameter, the map renders all categories.
The following categories are currently supported:
+  `FoodAndDrink`
+  `Entertainment`
+  `SightsAndMuseums`
+  `Transportation`
+  `Accommodations`
+  `LeisureAndOutdoor`
+  `Shopping`
+  `BusinessAndServices`
+  `FacilitiesAndBuildings`
Specify each category as a separate `poi-categories` query parameter. Duplicate values are rejected.
This parameter has no effect when `poi-density` is set to `Off`, which hides all points of interest regardless of category.
This parameter is valid only for the `Standard` and `Hybrid` map styles. In `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers, this parameter is valid only for the `Standard` map style.
Array Members: Minimum number of 0 items. Maximum number of 9 items.
Valid Values: `FoodAndDrink | Entertainment | SightsAndMuseums | Transportation | Accommodations | LeisureAndOutdoor | Shopping | BusinessAndServices | FacilitiesAndBuildings`

 ** [PoiDensity](#API_geomaps_GetStyleDescriptor_RequestSyntax) **   <a name="location-geomaps_GetStyleDescriptor-request-uri-PoiDensity"></a>
Controls how densely points of interest are rendered on the map. The density value controls the zoom level at which each category of points of interest appears, and how quickly less prominent points of interest are revealed as you zoom in. Denser values display more points of interest at lower zoom levels.
Use `Off` to hide all points of interest. When you omit this parameter, the map renders at `Default` density.
The difference between density values is most noticeable at mid-range zoom levels. At high zoom levels, all density values converge on displaying every available point of interest.
This parameter is valid only for the `Standard` and `Hybrid` map styles. In `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers, this parameter is valid only for the `Standard` map style.
Valid Values: `Off | VerySparse | Sparse | Default | Dense | VeryDense`

 ** [PoliticalView](#API_geomaps_GetStyleDescriptor_RequestSyntax) **   <a name="location-geomaps_GetStyleDescriptor-request-uri-PoliticalView"></a>
Specifies the political view using ISO 3166-2 or ISO 3166-3 country code format. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
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

 ** [Style](#API_geomaps_GetStyleDescriptor_RequestSyntax) **   <a name="location-geomaps_GetStyleDescriptor-request-uri-Style"></a>
Style specifies the desired map style. For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers, `ap-southeast-1` and `ap-southeast-5` regions support only the `Standard` and `Monochrome` values.
Valid Values: `Standard | Monochrome | Hybrid | Satellite`
Required: Yes

 ** [Terrain](#API_geomaps_GetStyleDescriptor_RequestSyntax) **   <a name="location-geomaps_GetStyleDescriptor-request-uri-Terrain"></a>
Adjusts how physical terrain details are rendered on the map. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
The following terrain styles are currently supported:
+  `Hillshade`: Displays the physical terrain details through shading and highlighting of elevation change and geographic features.
+  `Terrain3D`: Displays physical terrain details and elevations as a three-dimensional model.
 `Hillshade` is valid only for the `Standard` and `Monochrome` map styles.
Valid Values: `Hillshade | Terrain3D`

 ** [Traffic](#API_geomaps_GetStyleDescriptor_RequestSyntax) **   <a name="location-geomaps_GetStyleDescriptor-request-uri-Traffic"></a>
Displays real-time traffic information overlay on map, such as incident events and flow events. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
This parameter is valid for all map styles except `Satellite`.
Valid Values: `All | Congestion`

 ** [TravelModes](#API_geomaps_GetStyleDescriptor_RequestSyntax) **   <a name="location-geomaps_GetStyleDescriptor-request-uri-TravelModes"></a>
Renders additional map information relevant to selected travel modes. Information for multiple travel modes can be displayed simultaneously, although this increases the overall information density rendered on the map. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
This parameter is valid for all map styles except `Satellite`.
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Valid Values: `Transit | Truck`

## Request Body
<a name="API_geomaps_GetStyleDescriptor_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_geomaps_GetStyleDescriptor_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{ContentType}}
Cache-Control: {{CacheControl}}
ETag: {{ETag}}

{{Blob}}
```

## Response Elements
<a name="API_geomaps_GetStyleDescriptor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [CacheControl](#API_geomaps_GetStyleDescriptor_ResponseSyntax) **   <a name="location-geomaps_GetStyleDescriptor-response-CacheControl"></a>
Header that instructs caching configuration for the client.

 ** [ContentType](#API_geomaps_GetStyleDescriptor_ResponseSyntax) **   <a name="location-geomaps_GetStyleDescriptor-response-ContentType"></a>
Header that represents the format of the response. The response returns the following as the HTTP body.

 ** [ETag](#API_geomaps_GetStyleDescriptor_ResponseSyntax) **   <a name="location-geomaps_GetStyleDescriptor-response-ETag"></a>
The style descriptor's Etag.

The response returns the following as the HTTP body.

 ** [Blob](#API_geomaps_GetStyleDescriptor_ResponseSyntax) **   <a name="location-geomaps_GetStyleDescriptor-response-Blob"></a>
This Blob contains the body of the style descriptor which is in application/json format.

## Errors
<a name="API_geomaps_GetStyleDescriptor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_geomaps_GetStyleDescriptor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-maps-2020-11-19/GetStyleDescriptor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-maps-2020-11-19/GetStyleDescriptor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-maps-2020-11-19/GetStyleDescriptor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-maps-2020-11-19/GetStyleDescriptor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-maps-2020-11-19/GetStyleDescriptor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-maps-2020-11-19/GetStyleDescriptor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-maps-2020-11-19/GetStyleDescriptor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-maps-2020-11-19/GetStyleDescriptor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/geo-maps-2020-11-19/GetStyleDescriptor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-maps-2020-11-19/GetStyleDescriptor)
