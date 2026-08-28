---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetSprites.html
---

# GetSprites
<a name="API_geomaps_GetSprites"></a>

 `GetSprites` returns the map's sprites.

For more information, see [Style iconography with sprites](https://docs.aws.amazon.com/location/latest/developerguide/styling-iconography-with-sprites.html) in the *Amazon Location Service Developer Guide*.

## Request Syntax
<a name="API_geomaps_GetSprites_RequestSyntax"></a>

```
GET /v2/styles/{{Style}}/{{ColorScheme}}/{{Variant}}/sprites/{{FileName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_geomaps_GetSprites_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ColorScheme](#API_geomaps_GetSprites_RequestSyntax) **   <a name="location-geomaps_GetSprites-request-uri-ColorScheme"></a>
Sets the color tone for the map sprites, such as dark and light.
Example: `Light`
Default value: `Light`
Valid values for ColorScheme are case sensitive.
Valid Values: `Light | Dark`
Required: Yes

 ** [FileName](#API_geomaps_GetSprites_RequestSyntax) **   <a name="location-geomaps_GetSprites-request-uri-FileName"></a>
 `Sprites` API: The name of the sprite ﬁle to retrieve, following pattern `sprites(@2x)?\.(png|json)`.
Example: `sprites.png`
Pattern: `sprites(@2x)?\.(png|json)`
Required: Yes

 ** [Style](#API_geomaps_GetSprites_RequestSyntax) **   <a name="location-geomaps_GetSprites-request-uri-Style"></a>
Style specifies the desired map style for the `Sprites` APIs.
Valid Values: `Standard | Monochrome | Hybrid | Satellite`
Required: Yes

 ** [Variant](#API_geomaps_GetSprites_RequestSyntax) **   <a name="location-geomaps_GetSprites-request-uri-Variant"></a>
Optimizes map styles for specific use case or industry. You can choose allowed variant only with Standard map style.
Example: `Default`
Valid values for Variant are case sensitive.
Valid Values: `Default`
Required: Yes

## Request Body
<a name="API_geomaps_GetSprites_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_geomaps_GetSprites_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{ContentType}}
Cache-Control: {{CacheControl}}
ETag: {{ETag}}

{{Blob}}
```

## Response Elements
<a name="API_geomaps_GetSprites_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [CacheControl](#API_geomaps_GetSprites_ResponseSyntax) **   <a name="location-geomaps_GetSprites-response-CacheControl"></a>
Header that instructs caching configuration for the client.

 ** [ContentType](#API_geomaps_GetSprites_ResponseSyntax) **   <a name="location-geomaps_GetSprites-response-ContentType"></a>
Header that represents the format of the response. The response returns the following as the HTTP body.

 ** [ETag](#API_geomaps_GetSprites_ResponseSyntax) **   <a name="location-geomaps_GetSprites-response-ETag"></a>
The sprite's Etag.

The response returns the following as the HTTP body.

 ** [Blob](#API_geomaps_GetSprites_ResponseSyntax) **   <a name="location-geomaps_GetSprites-response-Blob"></a>
The body of the sprite sheet or JSON offset file (image/png or application/json, depending on input).

## Errors
<a name="API_geomaps_GetSprites_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_geomaps_GetSprites_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/geo-maps-2020-11-19/GetSprites)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/geo-maps-2020-11-19/GetSprites)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geo-maps-2020-11-19/GetSprites)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/geo-maps-2020-11-19/GetSprites)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geo-maps-2020-11-19/GetSprites)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/geo-maps-2020-11-19/GetSprites)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/geo-maps-2020-11-19/GetSprites)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/geo-maps-2020-11-19/GetSprites)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/geo-maps-2020-11-19/GetSprites)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geo-maps-2020-11-19/GetSprites)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
