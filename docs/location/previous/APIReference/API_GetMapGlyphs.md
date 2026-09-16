---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapGlyphs.html
---

# GetMapGlyphs
<a name="API_GetMapGlyphs"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend upgrading to [`GetGlyphs`](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetGlyphs.html) unless you require `Grab` data.
 `GetMapGlyphs` is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
The version 2 `GetGlyphs` operation gives a better user experience and is compatible with the remainder of the V2 Maps API.
If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under `geo-maps` or `geo_maps`, not under `location`.
Since `Grab` is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using `Grab`.
Start your version 2 API journey with the [Maps V2 API Reference](https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html) or the [Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/maps.html).

Retrieves glyphs used to display labels on a map.

## Request Syntax
<a name="API_GetMapGlyphs_RequestSyntax"></a>

```
GET /maps/v0/maps/{{MapName}}/glyphs/{{FontStack}}/{{FontUnicodeRange}}?key={{Key}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMapGlyphs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FontStack](#API_GetMapGlyphs_RequestSyntax) **   <a name="location-GetMapGlyphs-request-uri-FontStack"></a>
A comma-separated list of fonts to load glyphs from in order of preference. For example, `Noto Sans Regular, Arial Unicode`.
Valid font stacks for [Esri](https://docs.aws.amazon.com/location/previous/developerguide/esri.html) styles:
+ VectorEsriDarkGrayCanvas – `Ubuntu Medium Italic` \| `Ubuntu Medium` \| `Ubuntu Italic` \| `Ubuntu Regular` \| `Ubuntu Bold`
+ VectorEsriLightGrayCanvas – `Ubuntu Italic` \| `Ubuntu Regular` \| `Ubuntu Light` \| `Ubuntu Bold`
+ VectorEsriTopographic – `Noto Sans Italic` \| `Noto Sans Regular` \| `Noto Sans Bold` \| `Noto Serif Regular` \| `Roboto Condensed Light Italic`
+ VectorEsriStreets – `Arial Regular` \| `Arial Italic` \| `Arial Bold`
+ VectorEsriNavigation – `Arial Regular` \| `Arial Italic` \| `Arial Bold`
Valid font stacks for [HERE Technologies](https://docs.aws.amazon.com/location/previous/developerguide/HERE.html) styles:
+ VectorHereContrast – `Fira GO Regular` \| `Fira GO Bold`
+ VectorHereExplore, VectorHereExploreTruck, HybridHereExploreSatellite – `Fira GO Italic` \| `Fira GO Map` \| `Fira GO Map Bold` \| `Noto Sans CJK JP Bold` \| `Noto Sans CJK JP Light` \| `Noto Sans CJK JP Regular`
Valid font stacks for [GrabMaps](https://docs.aws.amazon.com/location/previous/developerguide/grab.html) styles:
+ VectorGrabStandardLight, VectorGrabStandardDark – `Noto Sans Regular` \| `Noto Sans Medium` \| `Noto Sans Bold`
Valid font stacks for [Open Data](https://docs.aws.amazon.com/location/previous/developerguide/open-data.html) styles:
+ VectorOpenDataStandardLight, VectorOpenDataStandardDark, VectorOpenDataVisualizationLight, VectorOpenDataVisualizationDark – `Amazon Ember Regular,Noto Sans Regular` \| `Amazon Ember Bold,Noto Sans Bold` \| `Amazon Ember Medium,Noto Sans Medium` \| `Amazon Ember Regular Italic,Noto Sans Italic` \| `Amazon Ember Condensed RC Regular,Noto Sans Regular` \| `Amazon Ember Condensed RC Bold,Noto Sans Bold` \| `Amazon Ember Regular,Noto Sans Regular,Noto Sans Arabic Regular` \| `Amazon Ember Condensed RC Bold,Noto Sans Bold,Noto Sans Arabic Condensed Bold` \| `Amazon Ember Bold,Noto Sans Bold,Noto Sans Arabic Bold` \| `Amazon Ember Regular Italic,Noto Sans Italic,Noto Sans Arabic Regular` \| `Amazon Ember Condensed RC Regular,Noto Sans Regular,Noto Sans Arabic Condensed Regular` \| `Amazon Ember Medium,Noto Sans Medium,Noto Sans Arabic Medium`
The fonts used by the Open Data map styles are combined fonts that use `Amazon Ember` for most glyphs but `Noto Sans` for glyphs unsupported by `Amazon Ember`.
Required: Yes

 ** [FontUnicodeRange](#API_GetMapGlyphs_RequestSyntax) **   <a name="location-GetMapGlyphs-request-uri-FontUnicodeRange"></a>
A Unicode range of characters to download glyphs for. Each response will contain 256 characters. For example, 0–255 includes all characters from range `U+0000` to `00FF`. Must be aligned to multiples of 256.
Pattern: `[0-9]+-[0-9]+\.pbf`
Required: Yes

 ** [Key](#API_GetMapGlyphs_RequestSyntax) **   <a name="location-GetMapGlyphs-request-uri-Key"></a>
The optional [API key](https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html) to authorize the request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [MapName](#API_GetMapGlyphs_RequestSyntax) **   <a name="location-GetMapGlyphs-request-uri-MapName"></a>
The map resource associated with the glyph ﬁle.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_GetMapGlyphs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMapGlyphs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{ContentType}}
Cache-Control: {{CacheControl}}

{{Blob}}
```

## Response Elements
<a name="API_GetMapGlyphs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [CacheControl](#API_GetMapGlyphs_ResponseSyntax) **   <a name="location-GetMapGlyphs-response-CacheControl"></a>
The HTTP Cache-Control directive for the value.

 ** [ContentType](#API_GetMapGlyphs_ResponseSyntax) **   <a name="location-GetMapGlyphs-response-ContentType"></a>
The map glyph content type. For example, `application/octet-stream`.

The response returns the following as the HTTP body.

 ** [Blob](#API_GetMapGlyphs_ResponseSyntax) **   <a name="location-GetMapGlyphs-response-Blob"></a>
The glyph, as binary blob.

## Errors
<a name="API_GetMapGlyphs_Errors"></a>

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
<a name="API_GetMapGlyphs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/GetMapGlyphs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/GetMapGlyphs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/GetMapGlyphs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/GetMapGlyphs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/GetMapGlyphs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/GetMapGlyphs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/GetMapGlyphs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/GetMapGlyphs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/GetMapGlyphs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/GetMapGlyphs)
