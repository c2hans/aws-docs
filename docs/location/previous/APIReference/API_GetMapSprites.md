---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_GetMapSprites.html
---

# GetMapSprites
<a name="API_GetMapSprites"></a>

**Important**
This operation is no longer current and may be deprecated in the future. We recommend upgrading to [`GetSprites`](https://docs.aws.amazon.com/location/latest/APIReference/API_geomaps_GetSprites.html) unless you require `Grab` data.
 `GetMapSprites` is part of a previous Amazon Location Service Maps API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).
The version 2 `GetSprites` operation gives a better user experience and is compatible with the remainder of the V2 Maps API.
If you are using an AWS SDK or the AWS CLI, note that the Maps API version 2 is found under `geo-maps` or `geo_maps`, not under `location`.
Since `Grab` is not yet fully supported in Maps API version 2, we recommend you continue using API version 1 when using `Grab`.
Start your version 2 API journey with the [Maps V2 API Reference](https://docs.aws.amazon.com/location/latest/APIReference/API_Operations_Amazon_Location_Service_Maps_V2.html) or the [Developer Guide](https://docs.aws.amazon.com/location/latest/developerguide/maps.html).

Retrieves the sprite sheet corresponding to a map resource. The sprite sheet is a PNG image paired with a JSON document describing the offsets of individual icons that will be displayed on a rendered map.

## Request Syntax
<a name="API_GetMapSprites_RequestSyntax"></a>

```
GET /maps/v0/maps/{{MapName}}/sprites/{{FileName}}?key={{Key}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetMapSprites_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FileName](#API_GetMapSprites_RequestSyntax) **   <a name="location-GetMapSprites-request-uri-FileName"></a>
The name of the sprite ﬁle. Use the following ﬁle names for the sprite sheet:
+  `sprites.png`
+  `sprites@2x.png` for high pixel density displays
For the JSON document containing image offsets. Use the following ﬁle names:
+  `sprites.json`
+  `sprites@2x.json` for high pixel density displays
Pattern: `sprites(@2x)?\.(png|json)`
Required: Yes

 ** [Key](#API_GetMapSprites_RequestSyntax) **   <a name="location-GetMapSprites-request-uri-Key"></a>
The optional [API key](https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html) to authorize the request.
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [MapName](#API_GetMapSprites_RequestSyntax) **   <a name="location-GetMapSprites-request-uri-MapName"></a>
The map resource associated with the sprite ﬁle.
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[-._\w]+`
Required: Yes

## Request Body
<a name="API_GetMapSprites_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetMapSprites_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-Type: {{ContentType}}
Cache-Control: {{CacheControl}}

{{Blob}}
```

## Response Elements
<a name="API_GetMapSprites_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [CacheControl](#API_GetMapSprites_ResponseSyntax) **   <a name="location-GetMapSprites-response-CacheControl"></a>
The HTTP Cache-Control directive for the value.

 ** [ContentType](#API_GetMapSprites_ResponseSyntax) **   <a name="location-GetMapSprites-response-ContentType"></a>
The content type of the sprite sheet and offsets. For example, the sprite sheet content type is `image/png`, and the sprite offset JSON document is `application/json`.

The response returns the following as the HTTP body.

 ** [Blob](#API_GetMapSprites_ResponseSyntax) **   <a name="location-GetMapSprites-response-Blob"></a>
Contains the body of the sprite sheet or JSON offset ﬁle.

## Errors
<a name="API_GetMapSprites_Errors"></a>

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
<a name="API_GetMapSprites_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/location-2020-11-19/GetMapSprites)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/location-2020-11-19/GetMapSprites)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/GetMapSprites)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/location-2020-11-19/GetMapSprites)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/GetMapSprites)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/location-2020-11-19/GetMapSprites)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/location-2020-11-19/GetMapSprites)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/location-2020-11-19/GetMapSprites)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/location-2020-11-19/GetMapSprites)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/GetMapSprites)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
