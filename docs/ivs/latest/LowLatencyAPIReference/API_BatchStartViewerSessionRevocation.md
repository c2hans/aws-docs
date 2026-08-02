---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_BatchStartViewerSessionRevocation.html
---

# BatchStartViewerSessionRevocation
<a name="API_BatchStartViewerSessionRevocation"></a>

Performs [StartViewerSessionRevocation](API_StartViewerSessionRevocation.md) on multiple channel ARN and viewer ID pairs simultaneously.

## Request Syntax
<a name="API_BatchStartViewerSessionRevocation_RequestSyntax"></a>

```
POST /BatchStartViewerSessionRevocation HTTP/1.1
Content-type: application/json

{
   "viewerSessions": [
      {
         "channelArn": "{{string}}",
         "viewerId": "{{string}}",
         "viewerSessionVersionsLessThanOrEqualTo": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchStartViewerSessionRevocation_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchStartViewerSessionRevocation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [viewerSessions](#API_BatchStartViewerSessionRevocation_RequestSyntax) **   <a name="ivs-BatchStartViewerSessionRevocation-request-viewerSessions"></a>
Array of viewer sessions, one per channel-ARN and viewer-ID pair.
Type: Array of [BatchStartViewerSessionRevocationViewerSession](API_BatchStartViewerSessionRevocationViewerSession.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: Yes

## Response Syntax
<a name="API_BatchStartViewerSessionRevocation_ResponseSyntax"></a>

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
         "channelArn": "string",
         "code": "string",
         "message": "string",
         "viewerId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchStartViewerSessionRevocation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [accessControlAllowOrigin](#API_BatchStartViewerSessionRevocation_ResponseSyntax) **   <a name="ivs-BatchStartViewerSessionRevocation-response-accessControlAllowOrigin"></a>
See [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin) in the MDN Web Docs.

 ** [accessControlExposeHeaders](#API_BatchStartViewerSessionRevocation_ResponseSyntax) **   <a name="ivs-BatchStartViewerSessionRevocation-response-accessControlExposeHeaders"></a>
See [Access-Control-Expose-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Expose-Headers) in the MDN Web Docs.

 ** [cacheControl](#API_BatchStartViewerSessionRevocation_ResponseSyntax) **   <a name="ivs-BatchStartViewerSessionRevocation-response-cacheControl"></a>
See [Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) in the MDN Web Docs.

 ** [contentSecurityPolicy](#API_BatchStartViewerSessionRevocation_ResponseSyntax) **   <a name="ivs-BatchStartViewerSessionRevocation-response-contentSecurityPolicy"></a>
See [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy) in the MDN Web Docs.

 ** [strictTransportSecurity](#API_BatchStartViewerSessionRevocation_ResponseSyntax) **   <a name="ivs-BatchStartViewerSessionRevocation-response-strictTransportSecurity"></a>
See [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security) in the MDN Web Docs.

 ** [xContentTypeOptions](#API_BatchStartViewerSessionRevocation_ResponseSyntax) **   <a name="ivs-BatchStartViewerSessionRevocation-response-xContentTypeOptions"></a>
See [X-Content-Type-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options) in the MDN Web Docs.

 ** [xFrameOptions](#API_BatchStartViewerSessionRevocation_ResponseSyntax) **   <a name="ivs-BatchStartViewerSessionRevocation-response-xFrameOptions"></a>
See [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options) in the MDN Web Docs.

The following data is returned in JSON format by the service.

 ** [errors](#API_BatchStartViewerSessionRevocation_ResponseSyntax) **   <a name="ivs-BatchStartViewerSessionRevocation-response-errors"></a>
Each error object is related to a specific `channelArn` and `viewerId` pair in the request.
Type: Array of [BatchStartViewerSessionRevocationError](API_BatchStartViewerSessionRevocationError.md) objects

## Errors
<a name="API_BatchStartViewerSessionRevocation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** PendingVerification **
Your account is pending verification.
HTTP Status Code: 403

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_BatchStartViewerSessionRevocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/BatchStartViewerSessionRevocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/BatchStartViewerSessionRevocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/BatchStartViewerSessionRevocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/BatchStartViewerSessionRevocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/BatchStartViewerSessionRevocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/BatchStartViewerSessionRevocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/BatchStartViewerSessionRevocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/BatchStartViewerSessionRevocation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/BatchStartViewerSessionRevocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/BatchStartViewerSessionRevocation)
