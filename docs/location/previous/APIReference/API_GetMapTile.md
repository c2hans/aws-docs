---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapTile.html
---

# GetMapTile
<a name="API_GetMapTile"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend upgrading to [`GetTile`](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetTile.html) unless you require `Grab` data.
 `GetMapTile` is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
The version 2 `GetTile` operation gives a better user experience and is compatible with the remainder of the V2 Maps API.
If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under `geo-maps` or `geo_maps`, not under `location`.
Since `Grab` is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using `Grab`.
Start your version 2 API journey with the [Maps V2 API Reference](https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html) or the [Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/maps.html).

Retrieves a vector data tile from the map resource. Map tiles are used by clients to render a map. they're addressed using a grid arrangement with an X coordinate, Y coordinate, and Z (zoom) level.

The origin (0, 0) is the top left of the map. Increasing the zoom level by 1 doubles both the X and Y dimensions, so a tile containing data for the entire world at (0/0/0) will be split into 4 tiles at zoom 1 (1/0/0, 1/0/1, 1/1/0, 1/1/1).

## Request Syntax
<a name="API_GetMapTile_RequestSyntax"></a>

```
GET /maps/v0/maps/{{MapName}}/tiles/{{Z}}/{{X}}/{{Y}}?key={{Key}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMapTile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Key](#API_GetMapTile_RequestSyntax) **   <a name="location-GetMapTile-request-uri-Key"></a>
The optional [API key](https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html) to authorize the request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [MapName](#API_GetMapTile_RequestSyntax) **   <a name="location-GetMapTile-request-uri-MapName"></a>
The map resource to retrieve the map tiles from.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

 ** [X](#API_GetMapTile_RequestSyntax) **   <a name="location-GetMapTile-request-uri-X"></a>
The X axis value for the map tile.
Pattern: `.*\d+.*`
Required: Yes

 ** [Y](#API_GetMapTile_RequestSyntax) **   <a name="location-GetMapTile-request-uri-Y"></a>
The Y axis value for the map tile.
Pattern: `.*\d+.*`
Required: Yes

 ** [Z](#API_GetMapTile_RequestSyntax) **   <a name="location-GetMapTile-request-uri-Z"></a>
The zoom value for the map tile.
Pattern: `.*\d+.*`
Required: Yes

## Request Body
<a name="API_GetMapTile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMapTile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{ContentType}}
Cache-Control: {{CacheControl}}

{{Blob}}
```

## Response Elements
<a name="API_GetMapTile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [CacheControl](#API_GetMapTile_ResponseSyntax) **   <a name="location-GetMapTile-response-CacheControl"></a>
The HTTP Cache-Control directive for the value.

 ** [ContentType](#API_GetMapTile_ResponseSyntax) **   <a name="location-GetMapTile-response-ContentType"></a>
The map tile's content type. For example, `application/vnd.mapbox-vector-tile`.

The response returns the following as the HTTP body.

 ** [Blob](#API_GetMapTile_ResponseSyntax) **   <a name="location-GetMapTile-response-Blob"></a>
Contains Mapbox Vector Tile (MVT) data.

## Errors
<a name="API_GetMapTile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed to process because of an unknown server error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource that you've entered was not found in your AWS account.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because of request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input failed to meet the constraints specified by the AWS service.
 ** FieldList **
The field where the invalid entry was detected.
 ** Reason **
A message with the reason for the validation exception error.
HTTP Status Code: 400

## See Also
<a name="API_GetMapTile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/GetMapTile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/GetMapTile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/GetMapTile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/GetMapTile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/GetMapTile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/GetMapTile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/GetMapTile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/GetMapTile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/GetMapTile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/GetMapTile)
