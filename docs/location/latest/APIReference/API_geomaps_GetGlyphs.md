---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetGlyphs.html
---

# GetGlyphs
<a name="API_geomaps_GetGlyphs"></a>

 `GetGlyphs` returns the map's glyphs.

For more information, see [Style labels with glyphs](https://docs.aws.amazon.com/location/latest/developerguide/styling-labels-with-glyphs.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_geomaps_GetGlyphs_RequestSyntax"></a>

```
GET /v2/glyphs/{{FontStack}}/{{FontUnicodeRange}} HTTP/1.1
```

## URI Request Parameters
<a name="API_geomaps_GetGlyphs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FontStack](#API_geomaps_GetGlyphs_RequestSyntax) **   <a name="location-geomaps_GetGlyphs-request-uri-FontStack"></a>
Name of the `FontStack` to retrieve.
Example: `Amazon Ember Bold,Noto Sans Bold`.
The supported font stacks are as follows:
+ Amazon Ember Bold
+ Amazon Ember Bold Italic
+ Amazon Ember Bold,Noto Sans Bold
+ Amazon Ember Bold,Noto Sans Bold,Noto Sans Arabic Bold
+ Amazon Ember Condensed RC BdItalic
+ Amazon Ember Condensed RC Bold
+ Amazon Ember Condensed RC Bold Italic
+ Amazon Ember Condensed RC Bold,Noto Sans Bold
+ Amazon Ember Condensed RC Bold,Noto Sans Bold,Noto Sans Arabic Condensed Bold
+ Amazon Ember Condensed RC Light
+ Amazon Ember Condensed RC Light Italic
+ Amazon Ember Condensed RC LtItalic
+ Amazon Ember Condensed RC Regular
+ Amazon Ember Condensed RC Regular Italic
+ Amazon Ember Condensed RC Regular,Noto Sans Regular
+ Amazon Ember Condensed RC Regular,Noto Sans Regular,Noto Sans Arabic Condensed Regular
+ Amazon Ember Condensed RC RgItalic
+ Amazon Ember Condensed RC ThItalic
+ Amazon Ember Condensed RC Thin
+ Amazon Ember Condensed RC Thin Italic
+ Amazon Ember Heavy
+ Amazon Ember Heavy Italic
+ Amazon Ember Light
+ Amazon Ember Light Italic
+ Amazon Ember Medium
+ Amazon Ember Medium Italic
+ Amazon Ember Medium,Noto Sans Medium
+ Amazon Ember Medium,Noto Sans Medium,Noto Sans Arabic Medium
+ Amazon Ember Regular
+ Amazon Ember Regular Italic
+ Amazon Ember Regular Italic,Noto Sans Italic
+ Amazon Ember Regular Italic,Noto Sans Italic,Noto Sans Arabic Regular
+ Amazon Ember Regular,Noto Sans Regular
+ Amazon Ember Regular,Noto Sans Regular,Noto Sans Arabic Regular
+ Amazon Ember Thin
+ Amazon Ember Thin Italic
+ AmazonEmberCdRC\_Bd
+ AmazonEmberCdRC\_BdIt
+ AmazonEmberCdRC\_Lt
+ AmazonEmberCdRC\_LtIt
+ AmazonEmberCdRC\_Rg
+ AmazonEmberCdRC\_RgIt
+ AmazonEmberCdRC\_Th
+ AmazonEmberCdRC\_ThIt
+ AmazonEmber\_Bd
+ AmazonEmber\_BdIt
+ AmazonEmber\_He
+ AmazonEmber\_HeIt
+ AmazonEmber\_Lt
+ AmazonEmber\_LtIt
+ AmazonEmber\_Md
+ AmazonEmber\_MdIt
+ AmazonEmber\_Rg
+ AmazonEmber\_RgIt
+ AmazonEmber\_Th
+ AmazonEmber\_ThIt
+ Noto Sans Black
+ Noto Sans Black Italic
+ Noto Sans Bold
+ Noto Sans Bold Italic
+ Noto Sans Extra Bold
+ Noto Sans Extra Bold Italic
+ Noto Sans Extra Light
+ Noto Sans Extra Light Italic
+ Noto Sans Italic
+ Noto Sans Light
+ Noto Sans Light Italic
+ Noto Sans Medium
+ Noto Sans Medium Italic
+ Noto Sans Regular
+ Noto Sans Semi Bold
+ Noto Sans Semi Bold Italic
+ Noto Sans Thin
+ Noto Sans Thin Italic
+ NotoSans-Bold
+ NotoSans-Italic
+ NotoSans-Medium
+ NotoSans-Regular
+ Open Sans Regular,Arial Unicode MS Regular
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** [FontUnicodeRange](#API_geomaps_GetGlyphs_RequestSyntax) **   <a name="location-geomaps_GetGlyphs-request-uri-FontUnicodeRange"></a>
A Unicode range of characters to download glyphs for. This must be aligned to multiples of 256.
Example: `0-255.pbf`
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[0-9]+-[0-9]+\.pbf`
Required: Yes

## Request Body
<a name="API_geomaps_GetGlyphs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_geomaps_GetGlyphs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{ContentType}}
Cache-Control: {{CacheControl}}
ETag: {{ETag}}

{{Blob}}
```

## Response Elements
<a name="API_geomaps_GetGlyphs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [CacheControl](#API_geomaps_GetGlyphs_ResponseSyntax) **   <a name="location-geomaps_GetGlyphs-response-CacheControl"></a>
Header that instructs caching configuration for the client.

 ** [ContentType](#API_geomaps_GetGlyphs_ResponseSyntax) **   <a name="location-geomaps_GetGlyphs-response-ContentType"></a>
Header that represents the format of the response. The response returns the following as the HTTP body.

 ** [ETag](#API_geomaps_GetGlyphs_ResponseSyntax) **   <a name="location-geomaps_GetGlyphs-response-ETag"></a>
The glyph's Etag.

The response returns the following as the HTTP body.

 ** [Blob](#API_geomaps_GetGlyphs_ResponseSyntax) **   <a name="location-geomaps_GetGlyphs-response-Blob"></a>
The Glyph, as a binary blob.

## Errors
<a name="API_geomaps_GetGlyphs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_geomaps_GetGlyphs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-maps-2020-11-19/GetGlyphs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-maps-2020-11-19/GetGlyphs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-maps-2020-11-19/GetGlyphs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-maps-2020-11-19/GetGlyphs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-maps-2020-11-19/GetGlyphs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-maps-2020-11-19/GetGlyphs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-maps-2020-11-19/GetGlyphs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-maps-2020-11-19/GetGlyphs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/geo-maps-2020-11-19/GetGlyphs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-maps-2020-11-19/GetGlyphs)
