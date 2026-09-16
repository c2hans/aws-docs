---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateStream.html
---

# UpdateStream
<a name="API_UpdateStream"></a>

Updates an existing stream. The stream version will be incremented by one.

Requires permission to access the [UpdateStream](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateStream_RequestSyntax"></a>

```
PUT /streams/{{streamId}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "files": [
      {
         "fileId": {{number}},
         "s3Location": {
            "bucket": "{{string}}",
            "key": "{{string}}",
            "version": "{{string}}"
         }
      }
   ],
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateStream_RequestParameters"></a>

The request uses the following URI parameters.

 ** [streamId](#API_UpdateStream_RequestSyntax) **   <a name="iot-UpdateStream-request-uri-streamId"></a>
The stream ID.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Request Body
<a name="API_UpdateStream_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateStream_RequestSyntax) **   <a name="iot-UpdateStream-request-description"></a>
The description of the stream.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`
Required: No

 ** [files](#API_UpdateStream_RequestSyntax) **   <a name="iot-UpdateStream-request-files"></a>
The files associated with the stream.
Type: Array of [StreamFile](API_StreamFile.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** [roleArn](#API_UpdateStream_RequestSyntax) **   <a name="iot-UpdateStream-request-roleArn"></a>
An IAM role that allows the IoT service principal assumes to access your S3 files.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_UpdateStream_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "description": "string",
   "streamArn": "string",
   "streamId": "string",
   "streamVersion": number
}
```

## Response Elements
<a name="API_UpdateStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [description](#API_UpdateStream_ResponseSyntax) **   <a name="iot-UpdateStream-response-description"></a>
A description of the stream.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`

 ** [streamArn](#API_UpdateStream_ResponseSyntax) **   <a name="iot-UpdateStream-response-streamArn"></a>
The stream ARN.
Type: String

 ** [streamId](#API_UpdateStream_ResponseSyntax) **   <a name="iot-UpdateStream-response-streamId"></a>
The stream ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_-]+`

 ** [streamVersion](#API_UpdateStream_ResponseSyntax) **   <a name="iot-UpdateStream-response-streamVersion"></a>
The stream version.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 65535.

## Errors
<a name="API_UpdateStream_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_UpdateStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateStream)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateStream)
