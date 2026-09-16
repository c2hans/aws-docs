---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_BatchGetChannel.html
---

# BatchGetChannel
<a name="API_BatchGetChannel"></a>

Performs [GetChannel](API_GetChannel.md) on multiple ARNs simultaneously.

## Request Syntax
<a name="API_BatchGetChannel_RequestSyntax"></a>

```
POST /BatchGetChannel HTTP/1.1
Content-type: application/json

{
   "arns": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetChannel_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetChannel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arns](#API_BatchGetChannel_RequestSyntax) **   <a name="ivs-BatchGetChannel-request-arns"></a>
Array of ARNs, one per channel.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:channel/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_BatchGetChannel_ResponseSyntax"></a>

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
   "channels": [
      {
         "adConfigurationArn": "string",
         "arn": "string",
         "authorized": boolean,
         "containerFormat": "string",
         "ingestEndpoint": "string",
         "insecureIngest": boolean,
         "latencyMode": "string",
         "multitrackInputConfiguration": {
            "enabled": boolean,
            "maximumResolution": "string",
            "policy": "string"
         },
         "name": "string",
         "playbackRestrictionPolicyArn": "string",
         "playbackUrl": "string",
         "preset": "string",
         "recordingConfigurationArn": "string",
         "srt": {
            "endpoint": "string",
            "passphrase": "string"
         },
         "tags": {
            "string" : "string"
         },
         "type": "string"
      }
   ],
   "errors": [
      {
         "arn": "string",
         "code": "string",
         "message": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetChannel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The response returns the following HTTP headers.

 ** [accessControlAllowOrigin](#API_BatchGetChannel_ResponseSyntax) **   <a name="ivs-BatchGetChannel-response-accessControlAllowOrigin"></a>
See [Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin) in the MDN Web Docs.

 ** [accessControlExposeHeaders](#API_BatchGetChannel_ResponseSyntax) **   <a name="ivs-BatchGetChannel-response-accessControlExposeHeaders"></a>
See [Access-Control-Expose-Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Expose-Headers) in the MDN Web Docs.

 ** [cacheControl](#API_BatchGetChannel_ResponseSyntax) **   <a name="ivs-BatchGetChannel-response-cacheControl"></a>
See [Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) in the MDN Web Docs.

 ** [contentSecurityPolicy](#API_BatchGetChannel_ResponseSyntax) **   <a name="ivs-BatchGetChannel-response-contentSecurityPolicy"></a>
See [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy) in the MDN Web Docs.

 ** [strictTransportSecurity](#API_BatchGetChannel_ResponseSyntax) **   <a name="ivs-BatchGetChannel-response-strictTransportSecurity"></a>
See [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security) in the MDN Web Docs.

 ** [xContentTypeOptions](#API_BatchGetChannel_ResponseSyntax) **   <a name="ivs-BatchGetChannel-response-xContentTypeOptions"></a>
See [X-Content-Type-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options) in the MDN Web Docs.

 ** [xFrameOptions](#API_BatchGetChannel_ResponseSyntax) **   <a name="ivs-BatchGetChannel-response-xFrameOptions"></a>
See [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options) in the MDN Web Docs.

The following data is returned in JSON format by the service.

 ** [channels](#API_BatchGetChannel_ResponseSyntax) **   <a name="ivs-BatchGetChannel-response-channels"></a>

Type: Array of [Channel](API_Channel.md) objects

 ** [errors](#API_BatchGetChannel_ResponseSyntax) **   <a name="ivs-BatchGetChannel-response-errors"></a>
Each error object is related to a specific ARN in the request.
Type: Array of [BatchError](API_BatchError.md) objects

## Errors
<a name="API_BatchGetChannel_Errors"></a>

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
<a name="API_BatchGetChannel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/BatchGetChannel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/BatchGetChannel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/BatchGetChannel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/BatchGetChannel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/BatchGetChannel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/BatchGetChannel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/BatchGetChannel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/BatchGetChannel)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/BatchGetChannel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/BatchGetChannel)
