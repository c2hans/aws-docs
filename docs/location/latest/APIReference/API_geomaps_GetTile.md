---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetTile.html
---

# GetTile
<a name="API_geomaps_GetTile"></a>

 `GetTile` returns a tile. Map tiles are used by clients to render a map. They're addressed using a grid arrangement with an X coordinate, Y coordinate, and Z (zoom) level.

For more information, see [Tiles](https://docs.aws.amazon.com/location/latest/developerguide/tiles.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_geomaps_GetTile_RequestSyntax"></a>

```
GET /v2/tiles/{{Tileset}}/{{Z}}/{{X}}/{{Y}}?additional-features={{AdditionalFeatures}}&key={{Key}} HTTP/1.1
```

## URI Request Parameters
<a name="API_geomaps_GetTile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AdditionalFeatures](#API_geomaps_GetTile_RequestSyntax) **   <a name="location-geomaps_GetTile-request-uri-AdditionalFeatures"></a>
A list of optional additional parameters such as map styles that can be requested for each result. Not supported in `ap-southeast-1` and `ap-southeast-5` regions for [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers.
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Valid Values: `ContourLines | Hillshade | Logistics | Transit`

 ** [Key](#API_geomaps_GetTile_RequestSyntax) **   <a name="location-geomaps_GetTile-request-uri-Key"></a>
Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [Tileset](#API_geomaps_GetTile_RequestSyntax) **   <a name="location-geomaps_GetTile-request-uri-Tileset"></a>
Specifies the desired tile set. For [GrabMaps](https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html) customers, `ap-southeast-1` and `ap-southeast-5` regions support only the `vector.basemap` value.
Valid Values: `raster.satellite | vector.basemap | vector.traffic | raster.dem`
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-.\w]+`
Required: Yes

 ** [X](#API_geomaps_GetTile_RequestSyntax) **   <a name="location-geomaps_GetTile-request-uri-X"></a>
The X axis value for the map tile.
Length Constraints: Minimum length of 0. Maximum length of 7.
Pattern: `.*\d+.*`
Required: Yes

 ** [Y](#API_geomaps_GetTile_RequestSyntax) **   <a name="location-geomaps_GetTile-request-uri-Y"></a>
The Y axis value for the map tile.
Length Constraints: Minimum length of 0. Maximum length of 7.
Pattern: `.*\d+.*`
Required: Yes

 ** [Z](#API_geomaps_GetTile_RequestSyntax) **   <a name="location-geomaps_GetTile-request-uri-Z"></a>
The zoom value for the map tile.
Length Constraints: Minimum length of 0. Maximum length of 2.
Pattern: `.*\d+.*`
Required: Yes

## Request Body
<a name="API_geomaps_GetTile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_geomaps_GetTile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{ContentType}}
Cache-Control: {{CacheControl}}
ETag: {{ETag}}
x-amz-geo-pricing-bucket: {{PricingBucket}}

{{Blob}}
```

## Response Elements
<a name="API_geomaps_GetTile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [CacheControl](#API_geomaps_GetTile_ResponseSyntax) **   <a name="location-geomaps_GetTile-response-CacheControl"></a>
Header that instructs caching configuration for the client.

 ** [ContentType](#API_geomaps_GetTile_ResponseSyntax) **   <a name="location-geomaps_GetTile-response-ContentType"></a>
Header that represents the format of the response. The response returns the following as the HTTP body.

 ** [ETag](#API_geomaps_GetTile_ResponseSyntax) **   <a name="location-geomaps_GetTile-response-ETag"></a>
The pricing bucket for which the request is charged at.

 ** [PricingBucket](#API_geomaps_GetTile_ResponseSyntax) **   <a name="location-geomaps_GetTile-response-PricingBucket"></a>
The pricing bucket for which the request is charged at.

The response returns the following as the HTTP body.

 ** [Blob](#API_geomaps_GetTile_ResponseSyntax) **   <a name="location-geomaps_GetTile-response-Blob"></a>
The blob represents a vector tile in `mvt` or a raster tile in an image format.

## Errors
<a name="API_geomaps_GetTile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Exception thrown when the associated resource could not be found.
HTTP Status Code: 404

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
<a name="API_geomaps_GetTile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-maps-2020-11-19/GetTile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-maps-2020-11-19/GetTile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-maps-2020-11-19/GetTile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-maps-2020-11-19/GetTile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-maps-2020-11-19/GetTile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-maps-2020-11-19/GetTile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-maps-2020-11-19/GetTile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-maps-2020-11-19/GetTile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/geo-maps-2020-11-19/GetTile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-maps-2020-11-19/GetTile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
