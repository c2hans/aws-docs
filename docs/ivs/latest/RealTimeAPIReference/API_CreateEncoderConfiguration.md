---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_CreateEncoderConfiguration.html
---

# CreateEncoderConfiguration
<a name="API_CreateEncoderConfiguration"></a>

Creates an EncoderConfiguration object.

## Request Syntax
<a name="API_CreateEncoderConfiguration_RequestSyntax"></a>

```
POST /CreateEncoderConfiguration HTTP/1.1
Content-type: application/json

{
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "video": {
      "bitrate": {{number}},
      "framerate": {{number}},
      "height": {{number}},
      "width": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_CreateEncoderConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateEncoderConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_CreateEncoderConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateEncoderConfiguration-request-name"></a>
Optional name to identify the resource.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

 ** [tags](#API_CreateEncoderConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateEncoderConfiguration-request-tags"></a>
Tags attached to the resource. Array of maps, each of the form `string:string (key:value)`. See [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in *Tagging AWS Resources and Tag Editor* for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS has no constraints on tags beyond what is documented there.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [video](#API_CreateEncoderConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-CreateEncoderConfiguration-request-video"></a>
Video configuration. Default: video resolution 1280x720, bitrate 2500 kbps, 30 fps.
Type: [Video](API_Video.md) object
Required: No

## Response Syntax
<a name="API_CreateEncoderConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "encoderConfiguration": {
      "arn": "string",
      "name": "string",
      "tags": {
         "string" : "string"
      },
      "video": {
         "bitrate": number,
         "framerate": number,
         "height": number,
         "width": number
      }
   }
}
```

## Response Elements
<a name="API_CreateEncoderConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [encoderConfiguration](#API_CreateEncoderConfiguration_ResponseSyntax) **   <a name="ivsrealtimeeapireference-CreateEncoderConfiguration-response-encoderConfiguration"></a>
The EncoderConfiguration that was created.
Type: [EncoderConfiguration](API_EncoderConfiguration.md) object

## Errors
<a name="API_CreateEncoderConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **

 ** exceptionMessage **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **

 ** exceptionMessage **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **

 ** exceptionMessage **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** PendingVerification **

 ** exceptionMessage **
 Your account is pending verification.
HTTP Status Code: 403

 ** ResourceNotFoundException **

 ** exceptionMessage **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **

 ** exceptionMessage **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ValidationException **

 ** exceptionMessage **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateEncoderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/CreateEncoderConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/CreateEncoderConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/CreateEncoderConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/CreateEncoderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/CreateEncoderConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/CreateEncoderConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/CreateEncoderConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/CreateEncoderConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/CreateEncoderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/CreateEncoderConfiguration)
