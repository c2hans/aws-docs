---
source_url: https://docs.aws.amazon.com/ivs/latest/RealTimeAPIReference/API_GetEncoderConfiguration.html
---

# GetEncoderConfiguration
<a name="API_GetEncoderConfiguration"></a>

Gets information about the specified EncoderConfiguration resource.

## Request Syntax
<a name="API_GetEncoderConfiguration_RequestSyntax"></a>

```
POST /GetEncoderConfiguration HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetEncoderConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetEncoderConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_GetEncoderConfiguration_RequestSyntax) **   <a name="ivsrealtimeeapireference-GetEncoderConfiguration-request-arn"></a>
ARN of the EncoderConfiguration resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:encoder-configuration/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_GetEncoderConfiguration_ResponseSyntax"></a>

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
<a name="API_GetEncoderConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [encoderConfiguration](#API_GetEncoderConfiguration_ResponseSyntax) **   <a name="ivsrealtimeeapireference-GetEncoderConfiguration-response-encoderConfiguration"></a>
The EncoderConfiguration that was returned.
Type: [EncoderConfiguration](API_EncoderConfiguration.md) object

## Errors
<a name="API_GetEncoderConfiguration_Errors"></a>

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
<a name="API_GetEncoderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-realtime-2020-07-14/GetEncoderConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-realtime-2020-07-14/GetEncoderConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-realtime-2020-07-14/GetEncoderConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-realtime-2020-07-14/GetEncoderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-realtime-2020-07-14/GetEncoderConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-realtime-2020-07-14/GetEncoderConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-realtime-2020-07-14/GetEncoderConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-realtime-2020-07-14/GetEncoderConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ivs-realtime-2020-07-14/GetEncoderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-realtime-2020-07-14/GetEncoderConfiguration)
