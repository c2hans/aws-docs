---
source_url: https://docs.aws.amazon.com/ivs/latest/LowLatencyAPIReference/API_GetRecordingConfiguration.html
---

# GetRecordingConfiguration
<a name="API_GetRecordingConfiguration"></a>

Gets the recording configuration for the specified ARN.

## Request Syntax
<a name="API_GetRecordingConfiguration_RequestSyntax"></a>

```
POST /GetRecordingConfiguration HTTP/1.1
Content-type: application/json

{
   "arn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetRecordingConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetRecordingConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [arn](#API_GetRecordingConfiguration_RequestSyntax) **   <a name="ivs-GetRecordingConfiguration-request-arn"></a>
ARN of the recording configuration to be retrieved.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `arn:aws:ivs:[a-z0-9-]+:[0-9]+:recording-configuration/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_GetRecordingConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "recordingConfiguration": {
      "arn": "string",
      "destinationConfiguration": {
         "s3": {
            "bucketName": "string"
         }
      },
      "name": "string",
      "recordingReconnectWindowSeconds": number,
      "renditionConfiguration": {
         "renditions": [ "string" ],
         "renditionSelection": "string"
      },
      "state": "string",
      "tags": {
         "string" : "string"
      },
      "thumbnailConfiguration": {
         "recordingMode": "string",
         "resolution": "string",
         "storage": [ "string" ],
         "targetIntervalSeconds": number
      }
   }
}
```

## Response Elements
<a name="API_GetRecordingConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [recordingConfiguration](#API_GetRecordingConfiguration_ResponseSyntax) **   <a name="ivs-GetRecordingConfiguration-response-recordingConfiguration"></a>
An object representing a configuration to record a channel stream.
Type: [RecordingConfiguration](API_RecordingConfiguration.md) object

## Errors
<a name="API_GetRecordingConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetRecordingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ivs-2020-07-14/GetRecordingConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ivs-2020-07-14/GetRecordingConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ivs-2020-07-14/GetRecordingConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ivs-2020-07-14/GetRecordingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ivs-2020-07-14/GetRecordingConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ivs-2020-07-14/GetRecordingConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ivs-2020-07-14/GetRecordingConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ivs-2020-07-14/GetRecordingConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ivs-2020-07-14/GetRecordingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ivs-2020-07-14/GetRecordingConfiguration)
