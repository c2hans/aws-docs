---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_BatchGetStreamKey.html
---

# BatchGetStreamKey
<a name="API_BatchGetStreamKey"></a>

Performs [GetStreamKey](API_GetStreamKey.md) on multiple ARNs simultaneously.

## Request Syntax
<a name="API_BatchGetStreamKey_RequestSyntax"></a>

```
POST /BatchGetStreamKey HTTP/1.1
Content-type: application/json

{
   "arns": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetStreamKey_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetStreamKey_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arns](#API_BatchGetStreamKey_RequestSyntax) **   <a name="ivs-BatchGetStreamKey-request-arns"></a>
Array of ARNs, one per stream key.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:stream-key/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_BatchGetStreamKey_ResponseSyntax"></a>

```
HTTP/1.1 200
Access-Control-Allow-Origin: {{accessControlAllowOrigin}}
Access-Control-Expose-Headers: {{accessControlExposeHeaders}}
Cache-Control: {{cacheControl}}
Content-Security-Policy: {{contentSecurityPolicy}}
Strict-Transport-Security: {{strictTransportSecurity}}
X-Content-Type-Options: {{xContentTypeOptions}}
X-Frame-Options: {{xFrameOptions}}
Content-type: application/json

{
   "errors": [
      {
         "arn": "string",
         "code": "string",
         "message": "string"
      }
   ],
   "streamKeys": [
      {
         "arn": "string",
         "channelArn": "string",
         "tags": {
            "string" : "string"
         },
         "value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetStreamKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [accessControlAllowOrigin](#API_BatchGetStreamKey_ResponseSyntax) **   <a name="ivs-BatchGetStreamKey-response-accessControlAllowOrigin"></a>
See [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin) in the MDN Web Docs.

 ** [accessControlExposeHeaders](#API_BatchGetStreamKey_ResponseSyntax) **   <a name="ivs-BatchGetStreamKey-response-accessControlExposeHeaders"></a>
See [Access-Control-Expose-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Expose-Headers) in the MDN Web Docs.

 ** [cacheControl](#API_BatchGetStreamKey_ResponseSyntax) **   <a name="ivs-BatchGetStreamKey-response-cacheControl"></a>
See [Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) in the MDN Web Docs.

 ** [contentSecurityPolicy](#API_BatchGetStreamKey_ResponseSyntax) **   <a name="ivs-BatchGetStreamKey-response-contentSecurityPolicy"></a>
See [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy) in the MDN Web Docs.

 ** [strictTransportSecurity](#API_BatchGetStreamKey_ResponseSyntax) **   <a name="ivs-BatchGetStreamKey-response-strictTransportSecurity"></a>
See [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security) in the MDN Web Docs.

 ** [xContentTypeOptions](#API_BatchGetStreamKey_ResponseSyntax) **   <a name="ivs-BatchGetStreamKey-response-xContentTypeOptions"></a>
See [X-Content-Type-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options) in the MDN Web Docs.

 ** [xFrameOptions](#API_BatchGetStreamKey_ResponseSyntax) **   <a name="ivs-BatchGetStreamKey-response-xFrameOptions"></a>
See [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options) in the MDN Web Docs.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchGetStreamKey_ResponseSyntax) **   <a name="ivs-BatchGetStreamKey-response-errors"></a>

Type: Array of [BatchError](API_BatchError.md) objects

 ** [streamKeys](#API_BatchGetStreamKey_ResponseSyntax) **   <a name="ivs-BatchGetStreamKey-response-streamKeys"></a>

Type: Array of [StreamKey](API_StreamKey.md) objects

## Errors
<a name="API_BatchGetStreamKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ServiceUnavailable **
The service is temporarily unavailable.
HTTP Status Code: 503

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_BatchGetStreamKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/BatchGetStreamKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/BatchGetStreamKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/BatchGetStreamKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/BatchGetStreamKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/BatchGetStreamKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/BatchGetStreamKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/BatchGetStreamKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/BatchGetStreamKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/BatchGetStreamKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/BatchGetStreamKey)
